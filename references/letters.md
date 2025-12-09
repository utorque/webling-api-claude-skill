# Letters API Reference

**Note**: These endpoints are only available for letters created with the new editor.

## Letter

Letters are used for writing and sending letters. They can be printed or sent by email.
Once a PDF is generated, the letter becomes immutable with state "sent".

**Not all actions available via API**:
- Email sending - not available
- Saving drafts - not available

### List Letters
```
GET /letter?filter=&order=title ASC&format=
```

| Param | Type | Description |
|-------|------|-------------|
| `filter` | string | Filter using Query Language |
| `order` | string | Sort by property and direction |
| `format` | string | Use `full` for complete objects |

**Response 200**: List of letter IDs or full objects

### Get Letter
```
GET /letter/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Letter ID (e.g., `1099`) |

**Response 200**: Letter object

### Delete Letter
```
DELETE /letter/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Letter ID |

**Response 204**: No content

### Create PDFs
```
POST /letter/new/send
```

Creates new PDFs for members or debitors. Returns combined PDF and saves individual PDFs as letterpdf objects.

**Properties**:
- `title` - Title shown in UI
- `state` - Must be `"sent"`
- `data` - Letter template to render PDF (examine letters created via UI for format)
- `lettertype` - `"member"` or `"debitor"`

**Links**: Letter can link to members OR debitors (not both).

**Request Body** (minimal example):
```json
{
  "properties": {
    "title": "Annual Membership Letter",
    "state": "sent",
    "lettertype": "member",
    "data": {
      "content": "<p>Dear {{Vorname}} {{Name}},</p><p>Your membership is confirmed.</p>",
      "format": {
        "pageSize": "A4",
        "margins": {
          "top": 20,
          "bottom": 20,
          "left": 25,
          "right": 25
        }
      }
    }
  },
  "links": {
    "member": [504, 505, 506]
  }
}
```

**Response 200**: PDF binary data

If creating PDFs for multiple members/debitors, individual PDFs are combined into one multi-page PDF.

---

## Letterpdf

Generated PDFs from letters. Immutable - cannot be created or updated manually.

To get the actual PDF file, call the `href` URL returned with the object.

A letterpdf is:
- Linked to either a member or a debitor
- Always a child of a letter

### List Letterpdfs
```
GET /letterpdf?filter=&format=
```

| Param | Type | Description |
|-------|------|-------------|
| `filter` | string | Filter using Query Language |
| `format` | string | Use `full` for complete objects |

**Response 200**: List of letterpdf IDs or full objects

### Get Letterpdf
```
GET /letterpdf/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Letterpdf ID (e.g., `4816`) |

**Response 200**: Letterpdf object with PDF metadata

**Example Response**:
```json
{
  "type": "letterpdf",
  "properties": {
    "pdf": {
      "href": "/api/1/letterpdf/4816/file/letter.pdf",
      "size": 45632,
      "ext": "pdf",
      "mime": "application/pdf",
      "timestamp": "2024-01-15 10:30:00"
    }
  },
  "parents": [1099],
  "links": {
    "member": [504]
  }
}
```

### Get Letterpdf Header Only
```
HEAD /letterpdf/{id}
```

**Response 200**: Headers only (no body)

### Delete Letterpdf
```
DELETE /letterpdf/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Letterpdf ID |

**Response 204**: No content

---

## Letter Workflow

### Creating and Sending Letters

1. **Prepare data**: Build letter template with content and format options
2. **Determine recipients**: Get member or debitor IDs
3. **Generate PDFs**: `POST /letter/new/send` with template and recipient links
4. **Retrieve PDFs later**: Access via letterpdf `href` property

### Accessing Invoice PDFs from Debitors

Debitor PDFs are linked as letterpdfs:
```
/debitor/{id} → links.letterpdf[*] → properties.pdf.href
```

**Query Example**:
```bash
# Get all letter PDFs for a specific debitor
/letterpdf?filter=$links.debitor.$id = 4333

# Get all letter PDFs for a specific member
/letterpdf?filter=$links.member.$id = 504
```

### Letter Data Format

The `data` property contains the letter template. Best practice: create a letter via the Webling UI and examine the resulting data structure to understand all available options.

Common `data` fields:
- `content` - HTML content with merge fields (e.g., `{{Vorname}}`)
- `format` - Page settings (size, margins)
- `header` / `footer` - Optional header/footer content
- `senderAddress` - Sender information
