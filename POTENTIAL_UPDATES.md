# Potential Skill Updates - Nested Data Retrieval Issue

**Investigation Date:** 2025-12-11
**Issue:** Data fields showing placeholders instead of actual values when using `format=full`

## Issue Description

When fetching objects with `format=full`, nested relationship data (via `links` or `children`) shows placeholder values like `[First]`, `[Name]`, `[Account Name]` instead of actual field content.

### Example Observed Data

```
member_id  member_name  member_firstname  member_email  total_amount  remaining_amount
474        Brunner      [First]           email@ex.ch   100           100
472        Baumann      [First]           email@ex.ch   100           100
```

The `member_firstname` column shows `[First]` (likely a field name placeholder) instead of the actual first name.

## Root Cause Analysis

### API Behavior

The Webling API `format=full` parameter has a specific behavior:

1. **First-level objects** are returned with complete data (all properties, metadata, etc.)
2. **Relationship references** (parents, children, links) are returned as:
   - **IDs only** (e.g., `parents: [550]`, `links: { debitor: [1234] }`)
   - **Not fully expanded objects**

3. **Nested queries** using filters like `$links.debitor.state = "open"` can:
   - **Filter based on nested properties** (query language supports deep traversal)
   - **But do NOT return full nested object data** in the response

### Why This Happens

When using queries like:
```bash
GET /member?filter=$links.debitor.state = "open"&format=full
```

The API:
- ✅ Filters members by checking if they have linked debitors with `state = "open"`
- ✅ Returns full member objects with complete properties
- ❌ Does NOT expand the linked debitor objects
- ❌ Does NOT provide debitor details in the response

The member response contains:
```json
{
  "type": "member",
  "properties": {
    "Vorname": "Fritz",
    "Name": "Meier"
  },
  "links": {
    "debitor": [1234, 1235]  // IDs only, not full objects
  }
}
```

### Test Code Issue

The test scripts attempted to access nested data in a single query:

```python
# ❌ INCORRECT APPROACH - Trying to get member data from a filter
# This assumes members are fully populated, but they're not when fetched via relationship filters

members = requests.get(
    f"{BASE_URL}/member",
    params={
        "filter": '$links.debitor.state = "open"',
        "format": "full"
    }
).json()

# This might show placeholders instead of actual data
firstname = member.get("properties", {}).get("Vorname")  # Could be "[First]"
```

## Confirmed Limitations

### What `format=full` Does

✅ Returns complete objects for the **primary endpoint** being queried
✅ Includes all properties, metadata (created, lastmodified)
✅ Includes relationship **IDs** (parents, children, links)
✅ Works with filters on nested properties (for filtering only)

### What `format=full` Does NOT Do

❌ Does NOT expand child objects into full objects
❌ Does NOT expand linked objects into full objects
❌ Does NOT expand parent objects into full objects
❌ Does NOT support `format=full` recursively/nested

## Correct Implementation Pattern

To get complete data with relationships, use the **fetch-and-join** pattern:

### Pattern 1: Fetch Primary + Related Objects Separately

```python
# Step 1: Fetch primary objects (members with filter)
members = requests.get(
    f"{BASE_URL}/member",
    params={
        "apikey": API_KEY,
        "filter": '$links.debitor.state = "open"',
        "format": "full"
    }
).json()

# Step 2: Fetch ALL related objects separately (not by ID list)
debitors = requests.get(
    f"{BASE_URL}/debitor",
    params={
        "apikey": API_KEY,
        "filter": 'state = "open"',
        "format": "full"
    }
).json()

# Step 3: Create lookup dictionaries
debitors_dict = {d["id"]: d for d in debitors}

# Step 4: Join in memory
for member in members:
    member_debitor_ids = member.get("links", {}).get("debitor", [])
    member["debitors_full"] = [
        debitors_dict.get(d_id)
        for d_id in member_debitor_ids
        if d_id in debitors_dict
    ]
```

### Pattern 2: Fetch with Multiple Parallel Queries

For complex scenarios (e.g., entries + accounts + entrygroups):

```python
# Fetch all related entity types in parallel
entries = fetch("/entry?format=full")
accounts = fetch("/account?format=full")
entrygroups = fetch("/entrygroup?format=full")

# Create lookup dictionaries
accounts_dict = {a["id"]: a for a in accounts}
entrygroups_dict = {eg["id"]: eg for eg in entrygroups}

# Join in memory
for entry in entries:
    # Get parent entrygroup
    entrygroup_id = entry.get("parents", [None])[0]
    entry["entrygroup_data"] = entrygroups_dict.get(entrygroup_id)

    # Get linked accounts
    debit_id = entry.get("links", {}).get("debit", [None])[0]
    credit_id = entry.get("links", {}).get("credit", [None])[0]
    entry["debit_account"] = accounts_dict.get(debit_id)
    entry["credit_account"] = accounts_dict.get(credit_id)
```

### Why NOT Use Comma-Separated ID Lists

❌ **Avoid this pattern** for large datasets:
```python
# DON'T DO THIS - URL length limitations
member_ids = [m["id"] for m in members]
url = f"/member/{','.join(map(str, member_ids))}"  # Can exceed URL length limit
```

✅ **Use this instead**:
```python
# Fetch all objects and filter in memory
all_members = fetch("/member?format=full")
members_dict = {m["id"]: m for m in all_members}
filtered_members = [members_dict[id] for id in needed_ids if id in members_dict]
```

## Recommended Skill Updates

### 1. Add Prominent Warning Section

Add a new section early in `SKILL.md` (after "Response Format", around line 105):

```markdown
## ⚠️ Important: Nested Data Retrieval

**The `format=full` parameter only expands the first level of objects.**

When you query an endpoint with `format=full`:
- ✅ Primary objects are fully expanded with all properties
- ❌ Relationship references (parents, children, links) are **IDs only**
- ❌ You **cannot** get nested object data in a single request

### Common Mistake

```bash
# ❌ This does NOT return full debitor data
GET /member?filter=$links.debitor.state = "open"&format=full

# Response includes debitor IDs only:
{
  "type": "member",
  "properties": { "Vorname": "Fritz", "Name": "Meier" },
  "links": { "debitor": [1234] }  // ID only, not full object
}
```

### Correct Approach

To get full related object data, fetch separately and join in memory:

```python
# Step 1: Fetch primary objects
members = fetch("/member?filter=$links.debitor.state='open'&format=full")

# Step 2: Fetch related objects separately
debitors = fetch("/debitor?filter=state='open'&format=full")

# Step 3: Join in memory
debitors_dict = {d["id"]: d for d in debitors}
for member in members:
    debitor_ids = member.get("links", {}).get("debitor", [])
    member["debitors_full"] = [debitors_dict.get(id) for id in debitor_ids]
```

See [Navigating Relationships](#navigating-relationships) for detailed patterns.
```

### 2. Enhance "Navigating Relationships" Section

Update the existing section (around line 140) to emphasize the limitation:

```markdown
## Navigating Relationships

**CRITICAL: Relationships are returned as IDs, not full objects.**

When you fetch a member with `format=full`, you get:
```json
{
  "type": "member",
  "properties": { "Vorname": "Fritz" },
  "parents": [550],           // ← Parent group ID (not full object)
  "links": { "debitor": [1234] }  // ← Linked debitor ID (not full object)
}
```

To get the full parent or linked object, make a separate API call:
```bash
GET /membergroup/550?format=full
GET /debitor/1234?format=full
```

[Rest of existing content...]
```

### 3. Update Common Patterns Section

Replace the existing "⚠️ Batch Fetching Considerations" section (lines 268-294) with a more detailed version:

```markdown
## Common Patterns

### Pattern: Fetch Objects with Related Data

**Problem**: You need members with their unpaid invoices (debitors) and full details of both.

**Solution**: Fetch-and-join pattern (2-3 API calls, join in memory)

```python
import requests

BASE_URL = "https://demo.webling.ch/api/1"
API_KEY = "your_api_key"

def fetch(endpoint, filter=None):
    """Helper to fetch from API"""
    params = {"apikey": API_KEY, "format": "full"}
    if filter:
        params["filter"] = filter
    response = requests.get(f"{BASE_URL}{endpoint}", params=params)
    response.raise_for_status()
    return response.json()

# Step 1: Fetch members filtered by relationship
members = fetch("/member", filter='$links.debitor.state = "open"')

# Step 2: Fetch all related debitors separately
debitors = fetch("/debitor", filter='state = "open"')

# Step 3: Create lookup dictionary for fast access
debitors_by_id = {d["id"]: d for d in debitors}

# Step 4: Enrich members with full debitor data
for member in members:
    debitor_ids = member.get("links", {}).get("debitor", [])
    member["unpaid_invoices"] = [
        debitors_by_id[did]
        for did in debitor_ids
        if did in debitors_by_id
    ]
    member["total_unpaid"] = sum(
        d.get("properties", {}).get("remainingamount", 0)
        for d in member["unpaid_invoices"]
    )

# Now you have complete data
for member in members:
    print(f"{member['properties']['Vorname']} {member['properties']['Name']}")
    print(f"  Total unpaid: {member['total_unpaid']}")
    for invoice in member["unpaid_invoices"]:
        print(f"  - Invoice {invoice['id']}: {invoice['properties']['remainingamount']}")
```

**Why this works**:
- ✅ Avoids URL length limits (no comma-separated ID lists)
- ✅ Efficient: Only 2-3 API calls regardless of result size
- ✅ Complete data: Full objects for both members and debitors
- ✅ Flexible: Easy to add more related entities

**Common mistake to avoid**:
```python
# ❌ DON'T DO THIS - Tries to build URLs with hundreds of IDs
debitor_ids = [d for m in members for d in m["links"].get("debitor", [])]
url = f"/debitor/{','.join(map(str, debitor_ids))}"  # URL too long!
```

### Pattern: Complex Multi-Entity Join

For accounting data (entries + accounts + entrygroups):

```python
# Step 1: Fetch all entity types in parallel
entries = fetch("/entry")
accounts = fetch("/account")
entrygroups = fetch("/entrygroup")

# Step 2: Create lookup dictionaries
accounts_dict = {a["id"]: a for a in accounts}
entrygroups_dict = {eg["id"]: eg for eg in entrygroups}

# Step 3: Enrich entries with related data
for entry in entries:
    # Add parent entrygroup data
    entrygroup_id = entry.get("parents", [None])[0]
    entry["entrygroup"] = entrygroups_dict.get(entrygroup_id)

    # Add linked account data
    debit_id = entry.get("links", {}).get("debit", [None])[0]
    credit_id = entry.get("links", {}).get("credit", [None])[0]
    entry["debit_account"] = accounts_dict.get(debit_id)
    entry["credit_account"] = accounts_dict.get(credit_id)

    # Now you can access nested properties
    entry["date"] = entry["entrygroup"]["properties"]["date"]
    entry["debit_account_name"] = entry["debit_account"]["properties"]["title"]
    entry["credit_account_name"] = entry["credit_account"]["properties"]["title"]
```
```

### 4. Add Troubleshooting Section

Add a new section near the end of `SKILL.md`:

```markdown
## Troubleshooting

### Issue: Getting Placeholder Values Like `[First]`, `[Name]`

**Symptoms**: When accessing object properties, you see placeholder text instead of actual data:
```python
member["properties"]["Vorname"]  # Returns "[First]" instead of "Fritz"
account["properties"]["title"]   # Returns "[Account Name]" instead of "Bank Account"
```

**Cause**: You're trying to access data from a relationship that hasn't been fetched with `format=full`.

**Solution**: Fetch the related objects separately:

```python
# ❌ Wrong - tries to get member data through a filter
members = fetch("/member?filter=$links.debitor.state='open'&format=full")
# This WILL work for member properties, but NOT for debitor properties

# ✅ Correct - fetch both entity types separately
members = fetch("/member?filter=$links.debitor.state='open'&format=full")
debitors = fetch("/debitor?filter=state='open'&format=full")

# Join them
debitors_dict = {d["id"]: d for d in debitors}
for member in members:
    member["debitors"] = [
        debitors_dict[did]
        for did in member.get("links", {}).get("debitor", [])
        if did in debitors_dict
    ]
```

### Issue: URL Too Long Error (HTTP 414)

**Symptoms**: Getting HTTP 414 "Request-URI Too Large" when fetching multiple objects by ID.

**Cause**: Trying to fetch too many objects using comma-separated IDs:
```python
# ❌ This can fail with many IDs
GET /member/536,525,506,535,...,999  # URL too long
```

**Solution**: Use `format=full` and filter in memory:
```python
# ✅ Fetch all objects
all_members = fetch("/member?format=full")

# Filter in Python
needed_ids = [536, 525, 506, 535, ...]
members_dict = {m["id"]: m for m in all_members}
filtered = [members_dict[id] for id in needed_ids if id in members_dict]
```

Or use filters:
```python
# ✅ Use IN filter (query language)
GET /member?filter=$id IN (536, 525, 506)&format=full
```
```

### 5. Update Query Language Examples

In `references/query-language.md`, add a note in the "Linked Objects" section (after line 213):

```markdown
### Linked Objects

**Important**: Filters can query nested properties, but responses only include IDs.

```bash
# ✅ Filter works - finds members with open invoices
/member?filter=$links.debitor.state = "open"

# Response includes member data + debitor IDs:
{
  "type": "member",
  "properties": { "Vorname": "Fritz" },
  "links": { "debitor": [1234] }  // ID only
}

# ❌ To get full debitor data, fetch separately:
/debitor?filter=state = "open"&format=full
```

[Existing examples continue...]
```

## Testing Recommendations

### Test Cases to Add

Create test scripts that demonstrate the correct pattern:

1. **test_correct_member_debitor_join.py**
   - Fetch members with unpaid fees correctly
   - Show full data for both members and debitors
   - Validate no placeholder values

2. **test_correct_entry_account_join.py**
   - Fetch entries with account details correctly
   - Show full account names and entry data
   - Validate proper date handling from entrygroups

3. **test_complex_join.py**
   - Demonstrate multi-entity join pattern
   - Show accounting hierarchy (period > entrygroup > entry > accounts)

### Validation Criteria

Each test should verify:
- ✅ No placeholder values in output (no `[First]`, `[Name]`, etc.)
- ✅ All expected fields populated with actual data
- ✅ Proper data types (numbers, dates, strings)
- ✅ Correct relationships (parent/child, links)

## Summary

### Key Takeaways

1. **`format=full` only expands the primary endpoint** - relationships are IDs only
2. **Filters can query nested properties** - but responses don't include nested full objects
3. **Use fetch-and-join pattern** - separate API calls + in-memory joins
4. **Avoid comma-separated ID lists** - use `format=full` and filter in memory
5. **Always validate data** - check for placeholder values indicating incomplete fetches

### Skill Changes Priority

**High Priority** (addresses user-facing confusion):
1. Add prominent warning about nested data limitation
2. Update "Common Patterns" with correct fetch-and-join examples
3. Add troubleshooting section for placeholder values

**Medium Priority** (improves clarity):
4. Enhance relationship navigation documentation
5. Add query language clarification notes

**Low Priority** (nice-to-have):
6. Add comprehensive test scripts demonstrating correct patterns
7. Add more examples in reference files

## References

- User report: Test scripts showing `[First]` placeholders
- Skill location: `/skill/SKILL.md`
- Test examples: User-provided Python scripts (test_2, test_3, test_4)
- API behavior: Confirmed through documentation analysis
