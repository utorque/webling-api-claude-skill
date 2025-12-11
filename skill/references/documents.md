# Documents API Reference

## Data Model Overview

This document covers document storage and organization in Webling. The document system provides hierarchical file storage with folders (documentgroups) and files (documents).

### Complete Object Hierarchy

```
documentgroup (self-referencing hierarchy)
  ├── document (files)
  └── documentgroup (subfolders)
```

### Object Relationships Summary

| Object | Parent | Children | Links To |
|--------|--------|----------|----------|
| **document** | documentgroup | none | none |
| **documentgroup** | documentgroup (self) | document, documentgroup | usergroup, user, page |

> **Note**: For complex queries involving multiple object relationships, refer to `full-object-relations.md`

## Document

A document is equivalent to a file on the filesystem.

**Object Type**: `document`
**Parent**: `documentgroup`
**Links**: None (standalone files)

**Properties** (from graphviz):
- `title` [text] - Document title
- `description` [longtext] - Description
- `file` [file] - The actual file with metadata (href, size, ext, mime)
- `href` [text] - Download URL
- `size` [int] - File size in bytes
- `lastmodified` [timestamp] - Last modification time
- `isProtected` [bool] - Whether file is password protected
- `protectedBy` [text] - Protection type

**Response Structure**:
```json
{
  "type": "document",
  "id": 1805,
  "meta": {
    "created": "2024-01-15 10:00:00",
    "createuser": { "label": "Admin", "type": "user" }
  },
  "readonly": false,
  "properties": {
    "title": "Annual Report",
    "description": "Financial report for 2024",
    "file": {
      "href": "/document/1805/file/report.pdf",
      "size": 2048576,
      "ext": "pdf",
      "mime": "application/pdf"
    }
  },
  "parents": [1806],
  "children": {},
  "links": {}
}
```

### List Documents
```
GET /document?filter=&order=title ASC&format=
```
| Param | Type | Description |
|-------|------|-------------|
| `filter` | string | Filter using Query Language |
| `order` | string | Sort by property and direction |
| `format` | string | Use `full` for complete objects |

**Response 200**: List of document IDs or full objects

### Create Document
```
POST /document
```

**Request Body**:
```json
{
  "properties": {
    "title": "Annual Report",
    "file": {
      "filename": "report.pdf",
      "content": "<base64 encoded file>"
    }
  },
  "parents": [1806]
}
```

**Response 201**: ID of newly created document

### Get Document
```
GET /document/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Document ID (e.g., `1804`) |

**Response 200**: Document object with metadata

### Get Document Header Only
```
HEAD /document/{id}
```

**Response 200**: Headers only (no body)

### Update Document
```
PUT /document/{id}
```

**Request Body**:
```json
{
  "properties": {
    "title": "Updated Report Title"
  }
}
```

**Response 204**: No content

### Delete Document
```
DELETE /document/{id}
```

**Response 204**: No content

### Get Document Content (File)
```
GET /document/{id}/file/{filename}.{extension}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Document ID (e.g., `1805`) |
| `filename` | string | Name of the file without extension (e.g., `Jahresabschluss`) |
| `extension` | string | File extension (e.g., `xlsx`) |

**Response 200**: Binary file data with appropriate content-type

**Example**:
```
GET /document/1805/file/Jahresabschluss.xlsx
```

---

## Documentgroup

Documentgroups are folders that contain documents and other documentgroups.

### List Documentgroups
```
GET /documentgroup?filter=&order=title ASC&format=
```

**Response 200**: 
```json
{
  "objects": [1806, 1807, 1808],
  "roots": [1806]
}
```
- `objects`: All documentgroup IDs
- `roots`: Root documentgroup IDs (for building folder tree)

### Create Documentgroup
```
POST /documentgroup
```

**Request Body**:
```json
{
  "properties": {
    "title": "Financial Documents"
  },
  "parents": [1806]
}
```

For root folder (no parent):
```json
{
  "properties": {
    "title": "Root Folder"
  },
  "parents": []
}
```

**Response 201**: ID of newly created documentgroup

### Get Documentgroup
```
GET /documentgroup/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Documentgroup ID (e.g., `1806`) |

**Response 200**: Documentgroup object with children info

### Update Documentgroup
```
PUT /documentgroup/{id}
```

**Request Body**:
```json
{
  "properties": {
    "title": "Renamed Folder"
  }
}
```

**Response 204**: No content

### Delete Documentgroup
```
DELETE /documentgroup/{id}
```

**Response 204**: No content

### Download Archive (ZIP)
```
GET /documentgroup/{id}/archive.zip
```

Downloads a ZIP archive containing all documents and subdocumentgroups.

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Documentgroup ID (e.g., `577`) |

**Response 200**: ZIP file binary data

---

## Document Query Examples

```bash
# Find documents by title
/document?filter=`title` FILTER "Report"

# Documents in specific folder
/document?filter=$parents.$id = 1806

# Search in folder and subfolders
/document?filter=$ancestors.$id = 1806

# Recently modified documents
/document?order=$meta.lastmodified DESC

# Documents with specific extension (if stored as property)
/document?filter=`file`.ext = "pdf"
```

## Building Folder Tree

1. Fetch all documentgroups: `GET /documentgroup`
2. Use `roots` array as starting points
3. For each group, get children from the object's `children.documentgroup` array
4. Recursively build tree structure
