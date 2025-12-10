# Track Changes / Replicate API Reference

> **Note**: These endpoints (`/replicate`, `/changes`) provide change tracking for efficient synchronization. They return object IDs that can be fetched using standard endpoints. See `webling_data_graphviz.txt` for object type definitions.

## How It Works

Every change in Webling creates a new revision with an incrementing revision ID. Use `/replicate` or `/changes` to sync only changed data.

**Two approaches**:
1. **Time-based** (`/changes/{timestamp}`) - Get changes since Unix timestamp
2. **Revision-based** (`/replicate/{id}`) - Get changes since specific revision

## Changes by Time

### Get Changes Since Timestamp
```
GET /changes/{timestamp}
```

Returns all changed objects since the Unix timestamp.

| Param | Type | Description |
|-------|------|-------------|
| `timestamp` | number | Unix timestamp (e.g., `1631167410`) |

**Response 200**:
```json
{
  "objects": {
    "member": [504, 505],
    "membergroup": [550],
    "debitor": [4333]
  },
  "deleted": {
    "member": [506]
  },
  "context": {},
  "definitions": [],
  "quota": false,
  "subscription": false,
  "revision": 1529,
  "version": "2024.1"
}
```

**Response fields**:
- `objects` - Changed object IDs grouped by type
- `deleted` - Deleted object IDs (also in `objects`)
- `context` - Reserved for future use
- `definitions` - Types with changed field definitions
- `quota` - `true` if `/quota` data changed
- `subscription` - `true` if `/subscription` data changed
- `revision` - Latest revision number
- `version` - Current Webling version

**Best for**: Scheduled syncs (cron jobs) at regular intervals.

---

## Changes by Revision

### Get Current Revision
```
GET /replicate
```

Returns current revision number and Webling version.

**Response 200**:
```json
{
  "revision": 1529,
  "version": "2024.1"
}
```

### Get Changes Since Revision
```
GET /replicate/{id}
```

Returns all changes since the specified revision.

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Revision ID (e.g., `1529`) |

**Response 200**: Same format as `/changes/{timestamp}`

**Special case**: Returns `-1` revision if API key permissions changed. Clear cache and resync completely.

---

## Sync Workflow

### Initial Sync
1. Call `GET /replicate` to get current revision (e.g., `100`)
2. Fetch all data you need
3. Store revision `100` as "last synced"

### Incremental Sync
1. Call `GET /replicate/100` (your last synced revision)
2. If `revision` in response equals `100`: no changes
3. If `revision` is higher (e.g., `105`):
   - Fetch changed objects from `objects` lists
   - Handle deleted objects from `deleted` lists
   - Store new revision `105` as "last synced"
4. Next sync: call `GET /replicate/105`

### Example Flow

```
Current revision: 100

Call: GET /replicate/97
Returns: Changes in revisions 98, 99, 100

Call: GET /replicate/98
Returns: Changes in revisions 99, 100

Call: GET /replicate/99
Returns: Changes in revision 100

Call: GET /replicate/100
Returns: No changes (current revision)

--- Someone makes changes ---

Call: GET /replicate/100
Returns: Changes in revisions 101+ up to current
```

---

## Permission Changes

If API key permissions are modified:
- `/replicate/{id}` returns `revision: -1`
- You may now see different data than before
- **Action required**: Clear cache and perform full resync

---

## Caching Best Practices

1. **Store last revision**: Keep track of successfully synced revision
2. **Incremental updates**: Only fetch changed objects
3. **Handle deletions**: Remove cached objects listed in `deleted`
4. **Full resync on -1**: Clear cache if revision returns `-1`
5. **Check definitions**: Resync object types if they appear in `definitions`

### Rate Limit Optimization

Design for <50 requests/minute:
- Use `/replicate` to detect changes before fetching
- Batch fetch with multi-get: `/member/504,505,506`
- Use `format=full` to get all data in one request
- Cache aggressively, update only changed objects

---

## Code Example (Python)

```python
import requests

API_URL = "https://<yourdomain>.webling.ch/api/1"
API_KEY = "your_api_key"

def get_headers():
    return {"apikey": API_KEY}

def get_current_revision():
    r = requests.get(f"{API_URL}/replicate", headers=get_headers())
    return r.json()["revision"]

def get_changes_since(revision):
    r = requests.get(f"{API_URL}/replicate/{revision}", headers=get_headers())
    return r.json()

def sync(last_revision):
    changes = get_changes_since(last_revision)
    
    if changes["revision"] == -1:
        print("Permissions changed - full resync required")
        return None
    
    if changes["revision"] == last_revision:
        print("No changes")
        return last_revision
    
    # Process changed objects
    for obj_type, ids in changes["objects"].items():
        print(f"Changed {obj_type}: {ids}")
        # Fetch and update cache...
    
    # Process deletions
    for obj_type, ids in changes.get("deleted", {}).items():
        print(f"Deleted {obj_type}: {ids}")
        # Remove from cache...
    
    return changes["revision"]

# Usage
last_rev = 0  # Load from persistent storage
new_rev = sync(last_rev)
if new_rev:
    # Save new_rev to persistent storage
    pass
```
