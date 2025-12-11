# Members API Reference

> **Data Model Reference**: See `webling_data_graphviz.txt` for complete member object definitions including member, membergroup, memberform, presencelist, attendee, participant, and calendar.

## Member Object Hierarchy

```
membergroup (hierarchy)
  ├── member
  ├── memberform (signup forms)
  └── presencelist
        └── attendee → links to member

calendar → links to membergroup
  └── calendarevent
        ├── participant → links to member
        └── presencelist
```

## Member

**Object Type**: `member`
**Parent**: `membergroup`
**Links**: comment, email, debitor, emailsent, letter, letterpdf, attendee, participant, postcomment, emotion

**Note**: Property names are customizable per Webling instance. Common German names shown below (from graphviz example).

**Common Properties** (example - varies by instance):
- `Mitglieder-ID` [autoincrement] - Unique member number
- `Vorname` [text] - First name
- `Name` [text] - Last name
- `Strasse` [text] - Street
- `PLZ` [text] - Postal code
- `Ort` [text] - City
- `Telefon` [text] - Phone
- `Mobile` [text] - Mobile
- `E-Mail` [text] - Email
- `Geburtstag` [date] - Birthday
- `Mitgliederbild` [image] - Profile picture
- `Status` [enum] - Member status
- `Funktion` [multienum] - Roles/functions
- `IBAN` [text] - Bank account
- `Bemerkungen` [longtext] - Notes
- `Geschlecht` [enum] - Gender
- `Lizenz` [enum] - License type

**Response Structure**:
```json
{
  "type": "member",
  "id": 504,
  "meta": {
    "created": "2020-01-15 10:00:00",
    "createuser": { "label": "Admin", "type": "user" },
    "lastmodified": "2024-12-01 14:30:00",
    "lastmodifieduser": { "label": "John Doe", "type": "user" }
  },
  "readonly": false,
  "properties": {
    "Mitglieder-ID": 504,
    "Vorname": "Fritz",
    "Name": "Meier",
    "E-Mail": "fritz.meier@example.ch",
    "Telefon": "+41 44 123 45 67",
    "Status": "Aktiv"
  },
  "parents": [550],
  "children": {},
  "links": {
    "debitor": [1234],
    "attendee": [8001, 8002]
  }
}
```

### List Members
```
GET /member?filter=&order=`Name` ASC&format=
GET /member?filter=$parents.$id = 550  # Members in specific group
```
| Param | Type | Description |
|-------|------|-------------|
| `filter` | string | Filter using Query Language |
| `order` | string | Sort by property and direction (e.g., `Name ASC`) |
| `format` | string | Use `full` for complete objects instead of IDs |

**Response 200**: List of member IDs or full objects

### Create Member
```
POST /member
```
Only `properties`, `parents`, and `links` can be set. Member needs at least one parent.
Image/file `content` must be base64 encoded.

**Request Body**:
```json
{
  "properties": {
    "Vorname": "Fritz",
    "Name": "Meier",
    "E-Mail": "fritz.meier@example.ch",
    "Mitgliederbild": {
      "filename": "portrait.png",
      "content": "<base64 encoded image>"
    }
  },
  "parents": [550],
  "links": {}
}
```

**Response 201**: ID of newly created member

### Get Member
```
GET /member/{id}
```
| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Member ID |

**Response 200**: Member object

### Update Member
```
PUT /member/{id}
```
Only `properties`, `parents`, and `links` may be changed. Pass `null` to empty a field.
Omitted fields are not changed.

**Request Body**:
```json
{
  "properties": {
    "E-Mail": "new.email@example.ch"
  }
}
```

**Response 204**: No content

### Delete Member
```
DELETE /member/{id}
```

**Response 204**: No content

### Get Member Image
```
GET /member/{id}/image/{fieldname}.{extension}?size=
HEAD /member/{id}/image/{fieldname}.{extension}?size=
```
| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Member ID |
| `fieldname` | string | Name of the datafield (e.g., `Mitgliederbild`) |
| `extension` | string | File extension (e.g., `png`) |
| `size` | string | `original` (default), `thumb`, or `mini` |

**Response 200**: Image binary data

### Get Member File
```
GET /member/{id}/file/{fieldname}.{extension}
HEAD /member/{id}/file/{fieldname}.{extension}
```
| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Member ID |
| `fieldname` | string | Name of the datafield (e.g., `Datei`) |
| `extension` | string | File extension (e.g., `pdf`) |

**Response 200**: File binary data

---

## Membergroup

Membergroups contain members and other membergroups (hierarchical).

**Object Type**: `membergroup`
**Parent**: `membergroup` (can be nested)
**Children**: member, memberform, presencelist, membergroup (subgroups)
**Links**: presencelist, calendar, page

**Properties** (from graphviz):
- `title` [text] - Group name
- `position` [int] - Display order

**Response Structure**:
```json
{
  "type": "membergroup",
  "id": 550,
  "meta": {
    "created": "2018-01-01 00:00:00",
    "createuser": { "label": "Admin", "type": "user" }
  },
  "readonly": false,
  "properties": {
    "title": "Main Group",
    "position": 1
  },
  "parents": [],
  "children": {
    "member": [504, 505, 506],
    "membergroup": [551, 552]
  },
  "links": {
    "calendar": [100]
  }
}
```

### List Membergroups
```
GET /membergroup?filter=&order=title ASC&format=
```
Returns object with `objects` (all IDs) and `roots` (root group IDs for building tree).

| Param | Type | Description |
|-------|------|-------------|
| `filter` | string | Filter using Query Language |
| `order` | string | Sort by property and direction |
| `format` | string | Use `full` for complete objects |

**Response 200** (simple format):
```json
{
  "objects": [550, 551, 552],
  "roots": [550]
}
```

**Response 200** (format=full):
```json
[
  { "type": "membergroup", "id": 550, "properties": {...}, "children": {...} },
  { "type": "membergroup", "id": 551, "properties": {...}, "children": {...} }
]
```

### Create Membergroup
```
POST /membergroup
```

**Request Body**:
```json
{
  "properties": {
    "title": "New Group"
  },
  "parents": [550]
}
```

**Response 201**: ID of newly created membergroup

### Get Membergroup
```
GET /membergroup/{id}
```

**Response 200**: Membergroup object

### Update Membergroup
```
PUT /membergroup/{id}
```

**Request Body**:
```json
{
  "properties": {
    "title": "Updated Group Name"
  }
}
```

**Response 204**: No content

### Delete Membergroup
```
DELETE /membergroup/{id}
```

**Response 204**: No content

---

## Common Member Queries

```bash
# Get all members in group 555
/member?filter=$parents.$id = 555

# Search in group and all subgroups
/member?filter=`Vorname` = "Tim" AND $ancestors.$id = 550

# Members with empty email
/member?filter=`E-Mail` IS EMPTY

# Members by age
/member?filter=AGE(`Geburtstag`) >= 18

# Members with birthday in August, sorted
/member?filter=MONTH(`Geburtstag`) = 8&order=DAY(`Geburtstag`) ASC

# Case-insensitive search
/member?filter=UPPER(`Name`) = "MEIER"

# Members with open invoices
/member?filter=$links.debitor.state = "open"

# Members you can edit
/member?filter=$writable = true

# Search all fields
/member?filter=* = "Müller"
```
