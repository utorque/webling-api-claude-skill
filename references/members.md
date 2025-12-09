# Members API Reference

## Member

### List Members
```
GET /member?filter=&order=Name ASC&format=
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

**Response 200**: 
```json
{
  "objects": [550, 551, 552],
  "roots": [550]
}
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
