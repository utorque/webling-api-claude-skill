---
name: webling-api
description: Complete Webling API integration skill for interacting with Webling databases. Use when working with Webling member management, accounting/finance, documents, articles, or any Webling API operations. Covers authentication, all endpoints (members, membergroups, debitors, accounts, entries, documents, periods, users, etc.), query language, pagination, change tracking/replication, and the complete data model with relationships.
---

# Webling API Skill

This skill provides comprehensive guidance for interacting with the Webling API, including the complete data model and relationship navigation.

## Base URL & Authentication

```
Base URL: https://<yourdomain>.webling.ch/api/1/
```

**Authentication**: Pass API key via:
- Query param: `?apikey=<your_api_key>`
- Header: `apikey: <your_api_key>`

Generate API keys in Administration > API.

## Data Model Overview

Webling uses a graph-based data model with hierarchical relationships (parents/children) and cross-references (links).

**Data Model Resources**:
- **[full-object-relations.md](references/full-object-relations.md)** - Complete reference guide for ALL object relationships, navigation patterns, and complex queries
- `webling_data_graphviz.txt` - Complete technical data model (all properties and relationships)

**Key Concepts**:
- **Parents**: Hierarchical containment (e.g., member belongs to membergroup)
- **Children**: Objects contained within (inverse of parents)
- **Links**: Cross-references between objects (e.g., debitor links to member)
- All objects have metadata (created, lastmodified, createuser, lastmodifieduser)
- Many objects can be readonly (system-managed or template-based)

> **For Complex Queries**: When working with queries that involve multiple related objects (e.g., members with invoices and payments, events with participants, accounting entries with accounts), consult [full-object-relations.md](references/full-object-relations.md) for navigation patterns and best practices.

## Quick Reference

| Category | Reference File | Key Endpoints |
|----------|----------------|---------------|
| **Object Relations** | **[full-object-relations.md](references/full-object-relations.md)** | **All objects with complete parent/child/link mappings** |
| Members | [members.md](references/members.md) | `/member`, `/membergroup` |
| Finance | [finance.md](references/finance.md) | `/debitor`, `/entry`, `/account`, `/period` |
| Documents | [documents.md](references/documents.md) | `/document`, `/documentgroup` |
| Articles | [articles.md](references/articles.md) | `/article`, `/articlegroup` |
| Users/Admin | [admin.md](references/admin.md) | `/user`, `/usergroup`, `/apikey` |
| Core | [core.md](references/core.md) | `/config`, `/definition`, `/quota`, `/setting` |
| Letters | [letters.md](references/letters.md) | `/letter`, `/letterpdf` |
| Replication | [replication.md](references/replication.md) | `/replicate`, `/changes` |

## Response Format

### Single Object Structure
Every Webling object follows this structure:

```json
{
  "type": "periodgroup",
  "meta": {
    "created": "2025-01-03 17:14:07",
    "createuser": { "label": "Demo Benutzer", "type": "user" },
    "lastmodified": "2025-01-03 17:14:15",
    "lastmodifieduser": { "label": "Demo Benutzer", "type": "user" }
  },
  "readonly": true,
  "properties": {
    "title": "KMU-Kontenplan"
  },
  "parents": [],
  "children": {
    "period": [10864],
    "periodchain": [10863]
  },
  "links": {},
  "id": 10862
}
```

**Key Fields**:
- `type`: Object type (member, period, account, etc.)
- `meta`: Creation and modification tracking
- `readonly`: Boolean - if true, object cannot be modified
- `properties`: Object's data fields (varies by type)
- `parents`: Array of parent object IDs (hierarchical containment)
- `children`: Object with arrays of child IDs grouped by type
- `links`: Object with arrays of linked object IDs grouped by type
- `id`: Unique object identifier

### Property Datatypes
- `text` (max 255 chars), `longtext` (max 2GB), `bool`, `int`, `numeric` (2 decimal places)
- `enum`, `multienum` (array), `date` (YYYY-MM-DD), `timestamp` (YYYY-MM-DD hh:mm:ss)
- `file`, `image`, `binary` - contain metadata with `href`, `size`, `ext`, `mime`
- `autoincrement` - immutable unique integer
- `json` - arbitrary JSON data
- `permissions` - permission configuration objects

### List Responses
Simple lists return just IDs:
```json
{ "objects": [12, 23, 34, 45] }
```

Full lists return array of complete objects:
```json
[
  { "type": "periodgroup", "id": 10862, "properties": {...}, ... },
  { "type": "periodgroup", "id": 800, "properties": {...}, ... }
]
```

### Errors
```json
{ "error": "Error message" }
```

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

See [Common Patterns](#common-patterns) below for detailed examples.

## HTTP Status Codes
- `200` OK, `201` Created, `204` No Content, `304` Not Modified
- `400` Bad Request, `401` Unauthorized, `403` Forbidden, `404` Not Found
- `413` Request Entity Too Large, `425` Quota Exceeded, `429` Too Many Requests
- `500` Server Error, `501` Not Implemented, `503` Service Unavailable

## Rate Limit
500 requests/minute. Design for <50 requests/minute. Use caching and `/replicate` for change detection.

## Fetching Multiple Objects

**Recommended**: Full format parameter (for bulk operations)
```
/api/1/member?format=full
/api/1/member?format=full&filter=$parents.$id=552
```
Best for fetching large numbers of objects. Returns complete objects for all matching records.

**Alternative**: Comma-separated IDs (for small batches only)
```
/api/1/member/536,525,506,535
```
⚠️ **Warning**: Limited by URL length (~2000 chars). Use only for small batches (<50 IDs). For larger datasets, use `format=full` with filters instead to avoid HTTP 414 "Request-URI Too Large" errors.

## Pagination
```
/api/1/member?page=1&per_page=100
```

## Navigating Relationships

**CRITICAL: Relationships are returned as IDs, not full objects.**

> **Comprehensive Guide**: For complete object relationship mappings, navigation patterns, and complex query examples, see [full-object-relations.md](references/full-object-relations.md)

When you fetch a member with `format=full`, you get:
```json
{
  "type": "member",
  "properties": { "Vorname": "Fritz" },
  "parents": [550],              // ← Parent group ID (not full object)
  "links": { "debitor": [1234] } // ← Linked debitor ID (not full object)
}
```

To get the full parent or linked object, make a separate API call:
```bash
GET /membergroup/550?format=full
GET /debitor/1234?format=full
```

Webling's data model uses two types of relationships:

### Parent-Child Relationships (Hierarchical)
Objects are organized in hierarchies. For example:
- `member` → parent: `membergroup`
- `period` → parent: `periodgroup`
- `account` → parent: `accountgroup` → parent: `period`

**Example**: Get a periodgroup with all its children
```bash
# Step 1: Get periodgroup list
GET /periodgroup?format=full
# Returns array with children listed by type

# Step 2: Navigate to specific child (e.g., periodchain)
GET /periodchain/7131?format=full
```

**Response showing relationships**:
```json
{
  "type": "periodchain",
  "properties": { "title": "Kontenrahmen" },
  "parents": [800],
  "children": {
    "accountgrouptemplate": [7132, 7138, 7140, 7144, 7147, 7152, 7155, 7157]
  },
  "links": {
    "period": [3269, 3943, 5712, 6337, 7180, 7943, 8580, 9234, 9653, 10312]
  }
}
```

**To navigate**:
1. `children.accountgrouptemplate` contains child object IDs → fetch with `/accountgrouptemplate/7132`
2. `links.period` contains linked period IDs → fetch with `/period/3269`

### Link Relationships (Cross-References)
Links connect objects across different hierarchies:
- `debitor` links to `member` (invoice to person)
- `account` links to `accounttemplate` (period-specific account to template)
- `entry` links to `debit` and `credit` accounts

**Example**: Working with accounting data
```bash
# Get all periods in a periodgroup
GET /periodgroup/800?format=full
# Returns children.period: [10312, 9653, ...]

# Get specific period
GET /period/10312?format=full
# Returns children with accountgroups, entrygroups, etc.

# Get accounts in a specific accountgroup
GET /accountgroup/2243?format=full
# Returns children.account: [account IDs]

# Get entries that reference a specific account
GET /entry?filter=$links.debit.$id = 2001 OR $links.credit.$id = 2001
```

### Common Navigation Patterns

**Pattern 1: Get all members in a group**
```bash
GET /membergroup/550?format=full
# Check children.member array for IDs
# Then fetch: GET /member/536,525,506
```

**Pattern 2: Get invoices for a member**
```bash
GET /debitor?filter=$links.member.$id = 504
```

**Pattern 3: Get full accounting structure**
```bash
# 1. Get periodgroups
GET /periodgroup?format=full

# 2. Get periodchain from children
GET /periodchain/7131?format=full

# 3. Get accountgrouptemplates from children
GET /accountgrouptemplate/7132?format=full

# 4. Get specific period from links
GET /period/10312?format=full

# 5. Get accountgroups in that period
GET /accountgroup?filter=$parents.$id = 10312
```

## Query Language

Filter results with `filter=` parameter. See [query-language.md](references/query-language.md) for complete reference.

### Basic Syntax
```
`Name` = "Meier"
`Betrag` > 100
* = "Müller"                    # Search all properties
`Name` IS EMPTY
NOT `Email` IS EMPTY
`Status` IN ("Aktiv", "Passiv")
(`Name` = "Meier" OR `Name` = "Müller") AND `Vorname` = "Hans"
```

### Special Properties
- `$parents.<property>`, `$ancestors.<property>`, `$children.<type>.<property>`
- `$links.<category>.<property>`, `$readonly`, `$writable`, `$label`, `$id`

### Operators
`<`, `<=`, `>`, `>=`, `=`, `!=`, `FILTER` (starts with), `CONTAINS`, `IS EMPTY`, `IN`, `WITH`

### Functions
`LOWER()`, `UPPER()`, `TRIM()`, `DAY()`, `MONTH()`, `YEAR()`, `AGE()`, `AGETHISYEAR()`, `BIRTHDAY()`, `TODAY()`, `COUNT()`

### Sorting
```
?order=`Vorname` ASC
?order=`Vorname` DESC, `Nachname` ASC
```

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
    if entry["entrygroup"]:
        entry["date"] = entry["entrygroup"]["properties"]["date"]
    if entry["debit_account"]:
        entry["debit_account_name"] = entry["debit_account"]["properties"]["title"]
    if entry["credit_account"]:
        entry["credit_account_name"] = entry["credit_account"]["properties"]["title"]
```

### Create Member
```bash
curl -X POST "https://<yourdomain>.webling.ch/api/1/member?apikey=KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "properties": { "Vorname": "Fritz", "Name": "Meier", "E-Mail": "fritz@example.ch" },
    "parents": [550]
  }'
```

### Filter Members
```
/member?filter=`Vorname` = "Hans"
/member?filter=$parents.$id = 555&order=`Vorname` ASC
/member?filter=AGE(`Geburtstag`) > 18
/member?filter=$links.debitor.state = "open"
```

### Track Changes
```
GET /replicate          # Get current revision
GET /replicate/{id}     # Get changes since revision
GET /changes/{timestamp} # Get changes since Unix timestamp
```

## Endpoint Overview

All endpoints support: `GET` (list/single), `POST` (create), `PUT` (update), `DELETE`

| Endpoint | Description |
|----------|-------------|
| `/member` | Members |
| `/membergroup` | Member groups (hierarchy) |
| `/debitor` | Invoices |
| `/debitorcategory` | Invoice categories |
| `/entry` | Financial postings |
| `/entrygroup` | Collective postings |
| `/account` | Finance accounts |
| `/accountgroup` | Account groups |
| `/period` | Accounting periods |
| `/periodgroup` | Period containers |
| `/periodchain` | Period sequences |
| `/costcenter` | Cost centers |
| `/document` | Files |
| `/documentgroup` | Folders |
| `/article` | Material items |
| `/articlegroup` | Article categories |
| `/letter` | Letters (new editor) |
| `/letterpdf` | Generated PDFs |
| `/user` | Users (admin only) |
| `/usergroup` | Roles (admin only) |
| `/apikey` | API keys (admin only) |
| `/object` | Generic endpoint |
| `/config` | Store config |
| `/definition` | Field definitions |
| `/quota` | Usage limits |
| `/setting` | Store settings |
| `/replicate` | Change tracking |
| `/changes` | Time-based changes |
| `/currentuser` | Current session info |

For detailed endpoint documentation, see the reference files listed in Quick Reference above.

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
# ❌ Wrong - assumes linked objects are expanded
members = fetch("/member?filter=$links.debitor.state='open'&format=full")
# member["links"]["debitor"] only contains IDs, not full objects

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

## Complete Data Model Reference

The file `webling_data_graphviz.txt` contains the complete Webling data model in Graphviz format, showing:

### All Object Types (50+ types)
Including: account, accountgroup, accountgrouptemplate, accounttemplate, apikey, article, articlegroup, attendee, bankaccount, calendar, calendarevent, comment, costcenter, debitor, debitorcategory, document, documentgroup, domain, email, entry, entrygroup, file, letter, member, memberform, membergroup, page, participant, payment, period, periodchain, periodgroup, post, user, usergroup, vat, and more.

### For Each Object Type
- **Properties**: Field names and data types (text, numeric, bool, date, enum, etc.)
- **Links**: Cross-reference relationships (e.g., debitor ↔ member)
- **Parents**: Hierarchical containment (e.g., account → accountgroup)

### Key Hierarchies

**Member Management**:
```
membergroup (hierarchy)
  └── member
  └── memberform
  └── presencelist
        └── attendee → member
```

**Finance/Accounting**:
```
periodgroup
  ├── period
  │     ├── accountgroup
  │     │     └── account → accounttemplate
  │     ├── entrygroup
  │     │     └── entry → account (debit/credit)
  │     ├── debitor → member
  │     └── costcenter
  ├── periodchain
  │     ├── accountgrouptemplate
  │     │     └── accounttemplate
  │     ├── bankaccount → accounttemplate
  │     └── saltedgeconnection
  └── debitorcategory
```

**Documents**:
```
documentgroup (hierarchy)
  └── document
```

**Articles**:
```
articlegroup (hierarchy)
  └── article
```

**Calendars**:
```
calendar → membergroup
  └── calendarevent
        ├── participant → member
        └── presencelist

```

### Understanding the Model

**Parent Relationships** (solid arrows in graphviz):
- Define containment hierarchy
- When you fetch an object, `parents` array shows parent IDs
- When you fetch a parent, `children` object shows child IDs grouped by type

**Link Relationships** (dashed arrows in graphviz):
- Cross-reference between hierarchies
- Shown in `links` object grouped by link type
- Often bidirectional (both objects reference each other)

**Example from graphviz**:
```
account has:
  + Properties: title [text], amount [numeric], budget [numeric], openingentry [numeric]
  + Links: comment, accounttemplate, entrygroup, entry, vat
  + Parents: accountgroup
```

This means:
- GET `/account/123` returns an object with these properties
- The response includes `links.accounttemplate` array with template IDs
- The response includes `parents` array with accountgroup ID
- You can query: `/entry?filter=$links.account.$id = 123`

### Using the Data Model

1. **Find object type** in graphviz (search for `datatype_<typename>`)
2. **Check properties** to know what fields are available
3. **Check parents** to understand hierarchy requirements
4. **Check links** to understand what can be connected
5. **Use references** for field-specific documentation (members.md, finance.md, etc.)
