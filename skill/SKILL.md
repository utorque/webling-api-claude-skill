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

Webling uses a graph-based data model with hierarchical relationships (parents/children) and cross-references (links). The complete data model with all object types, properties, and relationships is available in `webling_data_graphviz.txt`.

**Key Concepts**:
- **Parents**: Hierarchical containment (e.g., member belongs to membergroup)
- **Children**: Objects contained within (inverse of parents)
- **Links**: Cross-references between objects (e.g., debitor links to member)
- All objects have metadata (created, lastmodified, createuser, lastmodifieduser)
- Many objects can be readonly (system-managed or template-based)

## Quick Reference

| Category | Reference File | Key Endpoints |
|----------|----------------|---------------|
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

### ⚠️ Batch Fetching Considerations

When working with related objects (e.g., entries + entrygroups + accounts):
- **Don't** build URLs with hundreds of comma-separated IDs
- **Do** use `format=full` and filter in memory

**Example - Fetching all accounting entries with details:**
```python
# Step 1: Fetch all entries
entries = fetch("/entry?format=full")

# Step 2: Fetch all related objects (NOT by ID list)
entrygroups = fetch("/entrygroup?format=full")
accounts = fetch("/account?format=full")

# Step 3: Join in memory
entrygroups_dict = {eg["id"]: eg for eg in entrygroups}
accounts_dict = {acc["id"]: acc for acc in accounts}

# Step 4: Enrich entries with related data
for entry in entries:
    entry["entrygroup_data"] = entrygroups_dict.get(entry["parents"][0])
    entry["debit_account"] = accounts_dict.get(entry["links"]["debit"][0])
    entry["credit_account"] = accounts_dict.get(entry["links"]["credit"][0])
```

This approach avoids URL length limitations and is more efficient than multiple individual requests.

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
