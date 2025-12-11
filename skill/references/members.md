# Members API Reference

## Data Model Overview

This document covers all member-related objects in Webling. The member system includes hierarchical groups, members themselves, signup forms, attendance tracking, and calendar integration.

### Complete Object Hierarchy

```
membergroup (self-referencing hierarchy)
  ├── member
  ├── memberform (signup forms)
  ├── membergroup (subgroups)
  └── presencelist (attendance lists, optional parent)

calendar (root object)
  └── calendarevent
        ├── participant → links to member
        └── presencelist (linked)

presencelist (can exist independently or be linked)
  └── attendee → links to member
```

### Object Relationships Summary

| Object | Parent | Children | Links To |
|--------|--------|----------|----------|
| **member** | membergroup | none | comment, email, debitor, emailsent, letter, letterpdf, attendee, participant, postcomment, emotion |
| **membergroup** | membergroup (self) | member, memberform, membergroup, presencelist | presencelist, calendar, page |
| **memberform** | membergroup | none | file |
| **presencelist** | membergroup (optional) | attendee | membergroup, calendarevent |
| **attendee** | presencelist | none | member |
| **calendar** | none (root) | calendarevent | membergroup |
| **calendarevent** | calendar | participant | presencelist, file |
| **participant** | calendarevent | none | member |

> **Note**: For complex queries involving multiple object relationships, refer to `full-object-relations.md`

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

## Memberform

Signup forms for collecting new member information.

**Object Type**: `memberform`
**Parent**: `membergroup`
**Children**: none
**Links**: file

**Properties** (from data model):
- `title` [text] - Form name
- `hash` [text] - Public access hash
- `fields` [json] - Form field configuration
- `notificationEmail` [text] - Email for notifications
- `confirmationHtml` [longtext] - Confirmation page HTML
- `submitButtonText` [text] - Submit button text
- `maxSignups` [int] - Maximum number of signups
- `maxSignupsText` [longtext] - Text shown when max reached
- `confirmationEmailEnabled` [bool] - Whether to send confirmation emails
- `confirmationEmailField` [int] - Field ID for email address
- `confirmationEmailReplyto` [text] - Reply-to address
- `confirmationEmailSubject` [text] - Email subject
- `confirmationEmailText` [longtext] - Email body text
- `descriptionHtml` [longtext] - Form description
- `privacyCheckboxEnabled` [bool] - Require privacy checkbox
- `privacyCheckboxHtml` [longtext] - Privacy checkbox text
- `color` [text] - Form theme color

---

## Presencelist

Attendance tracking for events or groups.

**Object Type**: `presencelist`
**Parent**: `membergroup` (optional - can also be created independently)
**Children**: attendee
**Links**: membergroup, calendarevent

**Properties** (from data model):
- `title` [text] - List name
- `from` [timestamp] - Start date/time
- `archived` [bool] - Whether list is archived

**Relationship Notes**:
- Can be child of membergroup OR linked to membergroup
- Can be linked to calendarevent for event attendance
- Contains attendee objects that link to members

---

## Attendee

Individual attendance record linking members to presence lists.

**Object Type**: `attendee`
**Parent**: `presencelist`
**Children**: none
**Links**: member

**Properties** (from data model):
- `state` [enum] - Attendance state (e.g., present, absent, excused)

**Usage Pattern**:
```python
# Get attendance for a specific presence list
attendees = fetch("/attendee", filter=f'$parents.$id = {presencelist_id}')

# Get member details for attendees
member_ids = [a["links"]["member"][0] for a in attendees if a.get("links", {}).get("member")]
members = fetch("/member", filter=f'$id IN ({",".join(map(str, member_ids))})')
```

---

## Calendar

Calendar container for events.

**Object Type**: `calendar`
**Parent**: none (root object)
**Children**: calendarevent
**Links**: membergroup

**Properties** (from data model):
- `title` [text] - Calendar name
- `color` [text] - Calendar color (hex code)
- `isPublic` [bool] - Whether calendar is public
- `publicHash` [text] - Public access hash
- `icsHash` [text] - ICS feed hash

**Relationship Notes**:
- Links to membergroup to associate calendar with a group
- Contains calendar events as children

---

## Calendarevent

Individual calendar event with participant management.

**Object Type**: `calendarevent`
**Parent**: `calendar`
**Children**: participant
**Links**: presencelist, file

**Properties** (from data model):
- `title` [text] - Event name
- `description` [longtext] - Event description
- `place` [text] - Event location
- `begin` [timestamp] - Start date/time
- `end` [timestamp] - End date/time
- `duration` [int] - Duration in minutes
- `isAllDay` [bool] - All-day event flag
- `isRecurring` [bool] - Recurring event flag
- `status` [enum] - Event status (confirmed, tentative, cancelled)
- `recurrencePattern` [text] - Recurrence rule (RFC 5545 format)
- `enableParticipantSignup` [bool] - Allow signups
- `enableParticipantMaybeState` [bool] - Allow "maybe" responses
- `isSignupBinding` [bool] - Whether signup is binding
- `maxParticipants` [int] - Maximum participants
- `signedupParticipants` [int] - Current signup count (computed)
- `signupAllowedUntil` [timestamp] - Signup deadline
- `doAutoAcceptParticipants` [bool] - Auto-accept signups
- `questionSchema` [json] - Additional signup questions
- `showParticipationsInPortal` [bool] - Show in member portal
- `showAllAnswersInPortal` [bool] - Show all answers publicly

**Relationship Notes**:
- Can link to presencelist for attendance tracking
- Contains participant objects for signup management
- Can link to file for attachments

---

## Participant

Event participant (signup) linking members to calendar events.

**Object Type**: `participant`
**Parent**: `calendarevent`
**Children**: none
**Links**: member

**Properties** (from data model):
- `state` [enum] - Participation state (accepted, declined, maybe)
- `accepted` [bool] - Whether participation is accepted
- `acceptedAt` [timestamp] - Acceptance timestamp
- `invitedAt` [timestamp] - Invitation timestamp
- `questions` [json] - Answers to signup questions
- `memberlabel` [text] - Cached member name
- `memberimage` [image] - Cached member image

**Usage Pattern**:
```python
# Get participants for an event
participants = fetch("/participant", filter=f'$parents.$id = {event_id}')

# Get member details
member_ids = [p["links"]["member"][0] for p in participants if p.get("links", {}).get("member")]
members = fetch("/member", filter=f'$id IN ({",".join(map(str, member_ids))})')

# Filter accepted participants
accepted = [p for p in participants if p["properties"].get("state") == "accepted"]
```

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

---

## Practical Pattern: Members with Complete Contact Details

**Problem**: Get all members with their full contact information and group membership.

**⚠️ Important**: When fetching members with `format=full`, you get complete member data but parent group references are IDs only.

**Correct Approach**:

```python
import requests

BASE_URL = "https://yourdomain.webling.ch/api/1"
API_KEY = "your_api_key"

def fetch(endpoint, filter=None):
    params = {"apikey": API_KEY, "format": "full"}
    if filter:
        params["filter"] = filter
    response = requests.get(f"{BASE_URL}{endpoint}", params=params)
    response.raise_for_status()
    return response.json()

# Step 1: Fetch all members
members = fetch("/member")

# Step 2: Fetch all membergroups to get group names
membergroups = fetch("/membergroup")

# Step 3: Create lookup dictionary for groups
groups_dict = {g["id"]: g for g in membergroups}

# Step 4: Enrich members with group information
for member in members:
    props = member.get("properties", {})
    parent_ids = member.get("parents", [])

    # Add group information
    member["groups"] = [
        {
            "id": gid,
            "title": groups_dict.get(gid, {}).get("properties", {}).get("title", "Unknown")
        }
        for gid in parent_ids
        if gid in groups_dict
    ]

    # Format contact info
    member["full_name"] = f"{props.get('Vorname', '')} {props.get('Name', '')}".strip()
    member["address"] = f"{props.get('Strasse', '')}, {props.get('PLZ', '')} {props.get('Ort', '')}".strip(", ")

# Now you have complete member data with group names
for member in members:
    print(f"{member['full_name']}")
    print(f"  Email: {member['properties'].get('E-Mail', 'N/A')}")
    print(f"  Phone: {member['properties'].get('Telefon', 'N/A')}")
    print(f"  Groups: {', '.join(g['title'] for g in member['groups'])}")
```

## Practical Pattern: Members in Specific Group with Unpaid Fees

**Problem**: Get members from a specific membergroup who have unpaid membership fees.

**Correct Approach**:

```python
# Step 1: Fetch members in specific group with open debitors
members = fetch("/member", filter='$parents.$id = 555 AND $links.debitor.state = "open"')

# Step 2: Fetch open debitors
debitors = fetch("/debitor", filter='state = "open"')

# Step 3: Create lookup dictionary
debitors_dict = {d["id"]: d for d in debitors}

# Step 4: Enrich members with unpaid invoice details
for member in members:
    debitor_ids = member.get("links", {}).get("debitor", [])
    member["unpaid_invoices"] = [
        debitors_dict[did]
        for did in debitor_ids
        if did in debitors_dict
    ]
    member["total_unpaid"] = sum(
        d.get("properties", {}).get("remainingamount", 0)
        for d in member["unpaid_invoices"]
    )

# Display members with unpaid fees
for member in members:
    props = member["properties"]
    print(f"{props.get('Vorname')} {props.get('Name')}")
    print(f"  Email: {props.get('E-Mail')}")
    print(f"  Total unpaid: CHF {member['total_unpaid']:.2f}")
    for invoice in member["unpaid_invoices"]:
        inv_props = invoice["properties"]
        print(f"    - {inv_props.get('title')}: CHF {inv_props.get('remainingamount', 0):.2f}")
```

## Practical Pattern: Member Hierarchy Navigation

**Problem**: Get all members across a membergroup hierarchy (including subgroups).

**Correct Approach**:

```python
# Step 1: Fetch all membergroups to understand hierarchy
membergroups = fetch("/membergroup")

# Step 2: Find all subgroups under target group (e.g., group 550)
def get_all_subgroup_ids(group_id, groups_dict):
    """Recursively find all subgroup IDs"""
    subgroup_ids = [group_id]
    group = groups_dict.get(group_id)
    if group:
        child_group_ids = group.get("children", {}).get("membergroup", [])
        for child_id in child_group_ids:
            subgroup_ids.extend(get_all_subgroup_ids(child_id, groups_dict))
    return subgroup_ids

groups_dict = {g["id"]: g for g in membergroups}
target_group_id = 550
all_group_ids = get_all_subgroup_ids(target_group_id, groups_dict)

print(f"Found {len(all_group_ids)} groups in hierarchy")

# Step 3: Fetch members in any of these groups
# Using $ancestors is easier for this use case:
members = fetch("/member", filter=f'$ancestors.$id = {target_group_id}')

print(f"Found {len(members)} members across all subgroups")

# Step 4: Organize members by their direct parent group
members_by_group = {}
for member in members:
    parent_id = member.get("parents", [None])[0]
    if parent_id not in members_by_group:
        members_by_group[parent_id] = []
    members_by_group[parent_id].append(member)

# Display by group
for group_id, group_members in members_by_group.items():
    group_name = groups_dict.get(group_id, {}).get("properties", {}).get("title", "Unknown")
    print(f"\n{group_name} ({len(group_members)} members):")
    for member in group_members:
        props = member["properties"]
        print(f"  - {props.get('Vorname')} {props.get('Name')}")
```
