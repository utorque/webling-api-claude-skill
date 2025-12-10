# Core API Reference

> **Data Model Reference**: Core endpoints (`/config`, `/definition`, `/quota`, `/setting`) provide system-level information and configuration. See also `settings` object type in `webling_data_graphviz.txt`.

## Config

### Get Config Values
```
GET /config
```

Returns configuration values for the current Webling store. These are the same for every user.

**Response 200**: Config object with store-wide settings

---

## Definition

### Get Field Definitions
```
GET /definition?format=
```

Returns the field configuration of all objects.

| Param | Type | Description |
|-------|------|-------------|
| `format` | string | `simple` (human-readable) or `full` (complete details) |

**Response 200**: Definition object with all field configurations

**Example Response** (simplified):
```json
{
  "member": {
    "properties": {
      "Vorname": { "type": "text", "maxlength": 255 },
      "Name": { "type": "text", "maxlength": 255 },
      "E-Mail": { "type": "text", "maxlength": 255 },
      "Geburtstag": { "type": "date" },
      "Aktiv": { "type": "bool" }
    }
  },
  "membergroup": {
    "properties": {
      "title": { "type": "text" }
    }
  }
}
```

The `full` format includes internal property IDs useful for the `/object` endpoint.

---

## Quota

### Get Quota
```
GET /quota
```

Returns current and available quota for the Webling store.
- Storage values are in bytes
- Value of `-1` means unlimited
- Store cannot exceed max values; upgrade plan to increase

**Response 200**:
```json
{
  "members": {
    "current": 150,
    "max": 500
  },
  "storage": {
    "current": 52428800,
    "max": 1073741824
  }
}
```

### Get Storage Details
```
GET /quota/storage
```

Returns detailed storage usage breakdown by category.

**Response 200**:
```json
{
  "members": 10485760,
  "documents": 41943040,
  "total": 52428800
}
```

---

## Settings

### Get Settings
```
GET /setting
```

Returns setting values for the current Webling store.

**Response 200**: Settings object

### Update Settings
```
PUT /setting
```

Omit settings you don't want to change.

**Request Body**:
```json
{
  "property_name": "new_value"
}
```

**Response 204**: No content

---

## Object (Generic Endpoint)

The `/object` endpoint is a generic endpoint to get any Webling object by ID when you don't know the datatype.

**Key Difference**: Properties are indexed by internal ID, not name.
- Example: `title` property might be `"85"` (internal ID) not `"title"`
- Get internal IDs from `/definition` endpoint
- IDs may differ between Webling accounts

**Note**: `/object` does not support object listing, only single object operations.

### Create Object
```
POST /object
```

Omit fields to leave them empty.

**Request Body**:
```json
{
  "type": "member",
  "properties": {
    "123": "Fritz",
    "124": "Meier"
  },
  "parents": [550]
}
```

**Response 201**: ID of newly created object

### Get Object
```
GET /object/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Object ID (e.g., `557`) |

**Response 200**: Object with properties indexed by internal ID

### Update Object
```
PUT /object/{id}
```

Omit fields to leave them unchanged.

**Request Body**:
```json
{
  "properties": {
    "123": "Updated Value"
  }
}
```

**Response 204**: No content

### Delete Object
```
DELETE /object/{id}
```

**Response 204**: No content

---

## Object vs Typed Endpoints

| Feature | `/object` | `/member`, etc. |
|---------|-----------|-----------------|
| Property keys | Internal IDs (`"123"`) | Field names (`"Vorname"`) |
| Listing | Not supported | Supported |
| Use case | Unknown type | Known type |
| Definition lookup | Required | Not required |

### Example: Same Member via Both Endpoints

**Via `/member/504`**:
```json
{
  "properties": {
    "Vorname": "Fritz",
    "Name": "Meier"
  }
}
```

**Via `/object/504`**:
```json
{
  "properties": {
    "123": "Fritz",
    "124": "Meier"
  }
}
```
