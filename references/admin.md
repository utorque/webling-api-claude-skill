# Admin API Reference

**Note**: Only administrators have access to `/user`, `/usergroup`, and `/apikey` endpoints.

## User

### Access Levels

For `financeaccess` and `memberaccess`:
- `none` - No access
- `read` - Read access
- `read+write` - Read & Write access

For `articleaccess`:
- `none` - No access
- `read+write` - Read & Write access

### List Users
```
GET /user?filter=&order=title ASC&format=
```

| Param | Type | Description |
|-------|------|-------------|
| `filter` | string | Filter using Query Language |
| `order` | string | Sort by property and direction |
| `format` | string | Use `full` for complete objects |

**Response 200**: List of user IDs or full objects

### Create User
```
POST /user
```

Omit `password` field or send `null` if not setting a password.

**Request Body**:
```json
{
  "properties": {
    "email": "user@example.ch",
    "name": "John Doe",
    "password": "securepassword123",
    "isadmin": false
  },
  "parents": [2224]
}
```

**Response 201**: ID of newly created user

### Get User
```
GET /user/{id}
```

The `password` field is always `null` when fetching data.

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | User ID (e.g., `29`) |

**Response 200**: User object

### Update User
```
PUT /user/{id}
```

Omit `password` field or send `null` if not updating password.

**Request Body**:
```json
{
  "properties": {
    "name": "John Updated",
    "password": null
  }
}
```

**Response 204**: No content

### Delete User
```
DELETE /user/{id}
```

**Response 204**: No content

### Send Onboarding Email
```
POST /user/{id}/onboarding
```

Sends email to user with account info. Use `{{invite-link}}` placeholder for password reset link.

**Request Body**:
```json
{
  "subject": "Welcome to Our Organization",
  "body": "Hello! Your account has been created. Click here to set your password: {{invite-link}}"
}
```

**Response 204**: No content

---

## Usergroup (Roles)

Usergroups define access permissions. Also known as "Rollen" (Roles).

### Access Rules

Access rules are combinations of:
- `+r` - Add read access
- `-r` - Remove read access
- `+w` - Add write access
- `-w` - Remove write access

Rules are hierarchical and inherited by subgroups.

**Examples**:
- `+r` - Allow read
- `+r+w` - Allow read and write
- `-r` - Remove read (from inherited)

### List Usergroups
```
GET /usergroup?filter=&order=title ASC&format=
```

**Response 200**: List of usergroup IDs or full objects

### Create Usergroup
```
POST /usergroup
```

**Request Body**:
```json
{
  "properties": {
    "title": "Editors",
    "memberaccess": "read+write",
    "financeaccess": "read",
    "articleaccess": "none",
    "custommemberaccess": {
      "550": "+r",
      "551": "+r+w"
    },
    "customfinanceaccess": {
      "1814": "+r"
    }
  }
}
```

**Response 201**: ID of newly created usergroup

### Get Usergroup
```
GET /usergroup/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Usergroup ID (e.g., `2224`) |

**Response 200**: Usergroup object

### Update Usergroup
```
PUT /usergroup/{id}
```

**Request Body**:
```json
{
  "properties": {
    "title": "Senior Editors",
    "custommemberaccess": {
      "550": "+r+w"
    }
  }
}
```

**Response 204**: No content

### Delete Usergroup
```
DELETE /usergroup/{id}
```

**Response 204**: No content

---

## Apikey

### List API Keys
```
GET /apikey?filter=&order=title ASC&format=
```

| Param | Type | Description |
|-------|------|-------------|
| `filter` | string | Filter using Query Language |
| `order` | string | Sort by property and direction |
| `format` | string | Use `full` for complete objects |

**Response 200**: List of apikey IDs or full objects

### Create API Key
```
POST /apikey
```

**Request Body**:
```json
{
  "properties": {
    "title": "Integration Key",
    "memberaccess": "read+write",
    "financeaccess": "read",
    "articleaccess": "none"
  }
}
```

**Response 201**: ID and key value of newly created apikey

### Get API Key
```
GET /apikey/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Apikey ID (e.g., `1793`) |

**Response 200**: Apikey object

### Update API Key
```
PUT /apikey/{id}
```

**Request Body**:
```json
{
  "properties": {
    "title": "Updated Key Name"
  }
}
```

**Response 204**: No content

### Delete API Key
```
DELETE /apikey/{id}
```

**Response 204**: No content

### Get API Key Last Used
```
GET /apikey/{id}/lastused
```

Returns information about when the API key was last used.

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Apikey ID (e.g., `1791`) |

**Response 200**: Last used information

---

## Current User

### Get Current User/Apikey Info
```
GET /currentuser
```

Returns id and name of the currently logged-in user or apikey.

**Response 200**:
```json
{
  "id": 29,
  "name": "John Doe",
  "type": "user"
}
```

Or for API key:
```json
{
  "id": 1793,
  "name": "Integration Key",
  "type": "apikey"
}
```
