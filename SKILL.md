---
name: webling-api
description: Complete Webling API integration skill for interacting with Webling databases. Use when working with Webling member management, accounting/finance, documents, articles, or any Webling API operations. Covers authentication, all endpoints (members, membergroups, debitors, accounts, entries, documents, periods, users, etc.), query language, pagination, and change tracking/replication.
---

# Webling API Skill

This skill provides comprehensive guidance for interacting with the Webling API.

## Base URL & Authentication

```
Base URL: https://<yourdomain>.webling.ch/api/1/
```

**Authentication**: Pass API key via:
- Query param: `?apikey=<your_api_key>`
- Header: `apikey: <your_api_key>`

Generate API keys in Administration > API.

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

### Object Structure
```json
{
  "type": "objecttype",
  "meta": { "created": "2018-04-06 01:20:04", "lastmodified": "2017-05-23 11:43:54" },
  "readonly": false,
  "properties": {},
  "children": {},
  "parents": [],
  "links": {}
}
```

### Property Datatypes
- `text` (max 255 chars), `longtext` (max 2GB), `bool`, `int`, `numeric` (2 decimal places)
- `enum`, `multienum` (array), `date` (YYYY-MM-DD), `timestamp` (YYYY-MM-DD hh:mm:ss)
- `file`, `image`, `binary` - contain metadata with `href`, `size`, `ext`, `mime`
- `autoincrement` - immutable unique integer

### Lists
```json
{ "objects": [12, 23, 34, 45] }
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

**Option 1**: Comma-separated IDs
```
/api/1/member/536,525,506,535
```

**Option 2**: Full format parameter
```
/api/1/member?format=full
/api/1/member?format=full&filter=$parents.$id=552
```

## Pagination
```
/api/1/member?page=1&per_page=100
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
