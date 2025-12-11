# Complete Webling Object Relationships Reference

This document provides a comprehensive overview of ALL object types in Webling, their parent-child relationships, and link connections. Use this reference when working with complex API queries that involve multiple related objects.

> **Quick Navigation**: Jump to [Members](#members) | [Finance](#finance) | [Documents](#documents) | [Articles](#articles) | [Admin](#admin) | [Letters](#letters) | [Other](#other-objects)

---

## Understanding Webling Relationships

### Relationship Types

1. **Parent-Child (Hierarchy)**
   - Defined in the `parents` field of an object
   - Child objects belong to and are contained by parent objects
   - Example: `member` is a child of `membergroup`
   - Expressed in filter queries: `$parents.$id = 550`

2. **Links (Associations)**
   - Defined in the `links` field of an object
   - Objects can link to other objects without a hierarchical relationship
   - Links are often bidirectional
   - Example: `member` links to `debitor` (invoices)
   - Expressed in filter queries: `$links.debitor.state = "open"`

3. **Special Link Types**
   - Some links have semantic names: `debit`, `credit`, `sender`, `owners`, `revenue`, `payment`, `writeoff`
   - These indicate the role of the linked object
   - Example: `entry` has `debit` and `credit` links (both point to `account` objects)

### Navigation Patterns

**Fetching Related Data**:
```python
# Step 1: Fetch primary objects with format=full
members = fetch("/member", params={"format": "full"})

# Step 2: Extract linked IDs
debitor_ids = [d_id for m in members for d_id in m.get("links", {}).get("debitor", [])]

# Step 3: Fetch linked objects
debitors = fetch("/debitor", params={"format": "full"})
debitors_dict = {d["id"]: d for d in debitors}

# Step 4: Enrich primary objects
for member in members:
    member["invoices"] = [
        debitors_dict[did] for did in member.get("links", {}).get("debitor", [])
        if did in debitors_dict
    ]
```

---

## Members

### member

**Parent**: `membergroup`
**Children**: none
**Links To**: comment, email, debitor, emailsent, letter, letterpdf, attendee, participant, postcomment, emotion

**Use Cases**:
- Get member with their invoices: Link to `debitor`
- Get member attendance: Link to `attendee` → parent `presencelist`
- Get member event signups: Link to `participant` → parent `calendarevent`
- Get member emails: Link to `email` or `emailsent`

---

### membergroup

**Parent**: `membergroup` (self-referencing for hierarchy)
**Children**: member, memberform, membergroup (subgroups), presencelist
**Links To**: presencelist, calendar, page

**Hierarchy Notes**:
- Membergroups can contain other membergroups (nested structure)
- Root membergroups have empty `parents` array
- Use `$ancestors.$id` to search across group hierarchy

**Use Cases**:
- Get all members in group and subgroups: `$ancestors.$id = 550`
- Get group calendar: Link to `calendar`
- Get group presence lists: Link to `presencelist`

---

### memberform

**Parent**: `membergroup`
**Children**: none
**Links To**: file

**Use Cases**:
- Public signup forms for collecting new member data
- Links to file for form attachments/documents

---

### presencelist

**Parent**: `membergroup` (optional)
**Children**: attendee
**Links To**: membergroup, calendarevent

**Relationship Notes**:
- Can be child of membergroup OR exist independently
- Can link to calendarevent for event attendance
- Contains attendee children that link back to members

**Use Cases**:
- Track attendance for events or regular meetings
- Link to calendarevent for event-specific attendance

---

### attendee

**Parent**: `presencelist`
**Children**: none
**Links To**: member

**Use Cases**:
- Individual attendance record linking member to presence list
- Query: Get attendees for specific list, then fetch member details

---

### calendar

**Parent**: none (root object)
**Children**: calendarevent
**Links To**: membergroup

**Use Cases**:
- Calendar container linked to a membergroup
- Contains calendar events as children

---

### calendarevent

**Parent**: `calendar`
**Children**: participant
**Links To**: presencelist, file

**Use Cases**:
- Event with participant signups (children)
- Can link to presencelist for attendance tracking
- Can link to files for attachments

---

### participant

**Parent**: `calendarevent`
**Children**: none
**Links To**: member

**Use Cases**:
- Event signup/RSVP linking member to calendar event
- Includes state (accepted, declined, maybe), questions, etc.

---

## Finance

### periodgroup

**Parent**: none (root object)
**Children**: period, periodchain, debitorcategory, payment, rnwmerchant
**Links To**: none

**Use Cases**:
- Root container for entire finance system
- Typically only one periodgroup per instance

---

### period

**Parent**: `periodgroup`
**Children**: accountgroup, entrygroup, debitor, costcenter, vat, sepa
**Links To**: periodchain (bidirectional)

**Use Cases**:
- Accounting period (e.g., "2024 Fiscal Year")
- Contains all financial data for that period
- Links to periodchain (chart of accounts template)

---

### periodchain

**Parent**: `periodgroup`
**Children**: accountgrouptemplate, bankaccount, saltedgeconnection
**Links To**: period (bidirectional)

**Use Cases**:
- Chart of accounts template
- Persists across periods (child of periodgroup, not period)
- Links back to periods that use this chart

---

### accountgroup

**Parent**: `period`
**Children**: account
**Links To**: accountgrouptemplate

**Use Cases**:
- Account category (e.g., "Assets", "Revenue")
- Contains individual accounts as children
- Links to template for cross-period consistency

---

### account

**Parent**: `accountgroup`
**Children**: none
**Links To**: comment, accounttemplate, entrygroup, entry, vat

**Use Cases**:
- Individual account (e.g., "Bank Account CHF")
- Links to entries (postings) via `entry` and `entrygroup`
- Links to accounttemplate for cross-period mapping

---

### accountgrouptemplate

**Parent**: `periodchain`
**Children**: accounttemplate
**Links To**: accountgroup

**Use Cases**:
- Template for account categories
- Links to accountgroups in different periods

---

### accounttemplate

**Parent**: `accountgrouptemplate`
**Children**: none
**Links To**: account, bankaccount

**Use Cases**:
- Template for individual accounts
- Links to accounts across different periods
- Links to bankaccounts for payment sync

---

### entrygroup

**Parent**: `period`
**Children**: entry
**Links To**: account

**Use Cases**:
- Collective posting (contains date, receipt info)
- Contains entry children (individual postings)

---

### entry

**Parent**: `entrygroup`
**Children**: none
**Links To**: debit (account), credit (account), account, costcenter, debitor, payment, vat, entry (self-linking)

**Special Link Types**:
- `debit` → account (debit side of double-entry)
- `credit` → account (credit side of double-entry)

**Use Cases**:
- Individual posting in double-entry accounting
- Links to two accounts (debit and credit)
- Can link to costcenter, debitor (for revenue), payment, vat

---

### debitor

**Parent**: `period`
**Children**: none
**Links To**: member, email, emailsent, letter, letterpdf, comment, debitorcategory, paymentrecord (payment), revenue (entry), payment (entry), writeoff (entry), entry

**Special Link Types**:
- `paymentrecord` → payment (payment records)
- `revenue` → entry (revenue entries)
- `payment` → entry (payment entries)
- `writeoff` → entry (writeoff entries)

**Use Cases**:
- Invoice linking to member
- Links to revenue entries (invoice items)
- Links to payment entries (payments received)
- Complex pattern: Fetch debitor → fetch linked revenue entries → fetch entry details

---

### debitorcategory

**Parent**: `periodgroup`
**Children**: none
**Links To**: debitor

**Use Cases**:
- Invoice categories (e.g., "Membership Fees", "Donations")
- Persists across periods (child of periodgroup)

---

### costcenter

**Parent**: `period`
**Children**: none
**Links To**: entry

**Use Cases**:
- Cost center for expense tracking
- Links to entries for cost allocation

---

### vat

**Parent**: `period`
**Children**: none
**Links To**: entry, account

**Use Cases**:
- VAT/tax rates
- Links to entries using this rate
- Links to VAT accounts

---

### payment

**Parent**: `periodgroup`
**Children**: none
**Links To**: debitor, entry, rnwform, bankaccount

**Use Cases**:
- Payment transaction records
- Links to debitor (invoice paid)
- Links to entry (accounting entry)
- Links to bankaccount and rnwform for online payments

---

### bankaccount

**Parent**: `periodchain`
**Children**: none
**Links To**: accounttemplate, payment, saltedgeconnection

**Use Cases**:
- Bank account for payment sync
- Child of periodchain to persist across periods
- Links to payments for transaction matching

---

### sepa

**Parent**: `period`
**Children**: none
**Links To**: debitor

**Use Cases**:
- SEPA direct debit batches
- Links to debitors for payment collection

---

### saltedgeconnection

**Parent**: `periodchain`
**Children**: none
**Links To**: bankaccount

**Use Cases**:
- Bank API connection for automatic sync
- Links to bankaccounts for transaction import

---

### rnwmerchant

**Parent**: `periodgroup`
**Children**: rnwform
**Links To**: none

**Use Cases**:
- RaiseNow payment processor configuration
- Contains payment form children

---

### rnwform

**Parent**: `rnwmerchant`
**Children**: none
**Links To**: payment, email

**Use Cases**:
- Online payment form
- Links to payments created via form
- Links to confirmation emails

---

## Documents

### document

**Parent**: `documentgroup`
**Children**: none
**Links To**: none

**Use Cases**:
- File storage
- Simple parent-child only (no complex links)

---

### documentgroup

**Parent**: `documentgroup` (self-referencing)
**Children**: document, documentgroup (subfolders)
**Links To**: usergroup, user, page

**Hierarchy Notes**:
- Self-referencing for folder hierarchy
- Root folders have empty `parents` array

**Use Cases**:
- Folder structure for documents
- Links to usergroup/user for permissions
- Links to page for portal publishing

---

## Articles

### article

**Parent**: `articlegroup`
**Children**: none
**Links To**: none

**Use Cases**:
- Inventory/product tracking
- Simple parent-child only

---

### articlegroup

**Parent**: none (root objects)
**Children**: article
**Links To**: none

**Notes**:
- Articlegroups do NOT have hierarchy (unlike membergroups)
- Each articlegroup is a root-level category

---

## Admin

### user

**Parent**: `usergroup`
**Children**: none
**Links To**: comment, post, letter (as sender/owner), email (as sender/owner)

**Use Cases**:
- User accounts
- Links to letters and emails they created (sender/owner roles)

---

### usergroup

**Parent**: none (root)
**Children**: user
**Links To**: none

**Use Cases**:
- User roles and permissions
- Simple parent-child only

---

### apikey

**Parent**: none (standalone)
**Children**: none
**Links To**: none

**Use Cases**:
- API access keys
- Standalone object with no relationships

---

## Letters

### letter

**Parent**: none (root)
**Children**: letterpdf, letterimage
**Links To**: member, debitor, sender (user), owners (user), email, file

**Special Link Types**:
- `sender` → user (who created the letter)
- `owners` → user (who can access the letter)

**Use Cases**:
- PDF letter generation
- Links to member or debitor as recipient
- Contains letterpdf children (generated PDFs)

---

### letterpdf

**Parent**: `letter`
**Children**: none
**Links To**: member, debitor, emailsent

**Use Cases**:
- Generated PDF from letter
- Links to recipient (member or debitor)
- Links to emailsent if PDF was emailed

---

### letterimage

**Parent**: `letter`
**Children**: none
**Links To**: none

**Use Cases**:
- Embedded images in letters
- Simple parent-child only

---

### email

**Parent**: none (root)
**Children**: emailsent, emailattachment, emailimage
**Links To**: sender (user), owners (user), member, debitor, letter, rnwform

**Special Link Types**:
- `sender` → user (who sent the email)
- `owners` → user (who can access the email)

**Use Cases**:
- Email campaign management
- Contains emailsent children (delivery records)
- Links to recipients (members/debitors) and related letters

---

### emailsent

**Parent**: `email`
**Children**: none
**Links To**: member, debitor, letterpdf

**Use Cases**:
- Individual email delivery record
- Links to recipient and attached letterpdf

---

### emailattachment

**Parent**: `email`
**Children**: none
**Links To**: none

**Use Cases**:
- File attachments to emails
- Simple parent-child only

---

### emailimage

**Parent**: `email`
**Children**: none
**Links To**: none

**Use Cases**:
- Embedded images in emails
- Simple parent-child only

---

## Other Objects

### comment

**Parent**: none (root)
**Children**: none
**Links To**: member, debitor, user, account

**Use Cases**:
- Comments/notes on various objects
- Links to the object being commented on

---

### post

**Parent**: none (root)
**Children**: postcomment, emotion
**Links To**: user

**Use Cases**:
- Social/news posts
- Contains comments and reactions as children
- Links to user who created the post

---

### postcomment

**Parent**: `post`
**Children**: none
**Links To**: member

**Use Cases**:
- Comment on a post
- Links to member who commented

---

### emotion

**Parent**: `post`
**Children**: none
**Links To**: member

**Use Cases**:
- Reaction/emoji on a post
- Links to member who reacted

---

### page

**Parent**: `page` (self-referencing)
**Children**: page (subpages)
**Links To**: file, documentgroup, membergroup

**Use Cases**:
- Portal/website pages
- Can have subpages (hierarchical)
- Links to files, documentgroups, and membergroups for content

---

### file

**Parent**: none (root)
**Children**: none
**Links To**: page, letter, calendarevent, memberform

**Use Cases**:
- File storage for various objects
- Links to the object using this file

---

### template

**Parent**: none (root)
**Children**: none
**Links To**: none

**Use Cases**:
- Email/letter templates
- Standalone object

---

### domain

**Parent**: none (root)
**Children**: none
**Links To**: none

**Use Cases**:
- Custom domain configuration
- Standalone object

---

### sms

**Parent**: none (root)
**Children**: none
**Links To**: none

**Use Cases**:
- SMS message records
- Standalone object

---

## Common Complex Queries

### Members with Open Invoices and Full Details

**Scenario**: Get members who have unpaid invoices, including invoice details and amounts.

**Approach**:
1. Fetch members with open debitors: `/member?filter=$links.debitor.state = "open"&format=full`
2. Fetch all open debitors: `/debitor?filter=state = "open"&format=full`
3. Create lookup dictionary and enrich members with debitor details
4. Calculate total unpaid per member

**Why This Pattern**:
- Filter finds correct members, but `links` only contain IDs
- Must fetch debitors separately to get full data
- This is THE fundamental pattern for working with links

---

### Financial Entries with Account Names

**Scenario**: Get all entries with full debit/credit account information.

**Approach**:
1. Fetch entries: `/entry?format=full`
2. Fetch entrygroups (for dates): `/entrygroup?format=full`
3. Fetch accounts (for names): `/account?format=full`
4. Enrich entries with:
   - Entrygroup data (date, receipt) from `parents`
   - Debit account data from `links.debit`
   - Credit account data from `links.credit`

**Why This Pattern**:
- Entries don't have dates (entrygroups do)
- Entries link to accounts via IDs (need account names)
- Multiple fetches required to get complete picture

---

### Event Participants with Member Details

**Scenario**: Get all participants for an event with full member information.

**Approach**:
1. Fetch participants: `/participant?filter=$parents.$id = {event_id}&format=full`
2. Extract member IDs from `links.member`
3. Fetch members: `/member` (filtered by IDs or fetch all)
4. Enrich participants with member details

**Why This Pattern**:
- Participants link to members
- Need member details (name, email, etc.) not just IDs

---

### Nested Hierarchy Navigation (Membergroups)

**Scenario**: Get all members in a group and all its subgroups.

**Approach Option 1 (Simple)**:
- Use `$ancestors`: `/member?filter=$ancestors.$id = 550`

**Approach Option 2 (Explicit)**:
1. Fetch all membergroups: `/membergroup?format=full`
2. Build group hierarchy tree from `children.membergroup`
3. Recursively collect all subgroup IDs
4. Fetch members: `/member?filter=$parents.$id IN (550,551,552,...)`

**Why This Pattern**:
- Membergroups are self-referencing (hierarchical)
- Need to traverse hierarchy to get all descendant groups
- `$ancestors` is simpler but explicit traversal gives more control

---

## Quick Reference Table

| To Find | Start From | Navigate Via | End At |
|---------|-----------|--------------|--------|
| Member's invoices | member | `links.debitor` | debitor |
| Member's payments | member | `links.debitor` → `links.payment` | entry |
| Invoice's member | debitor | `links.member` | member |
| Invoice's revenue | debitor | `links.revenue` | entry |
| Entry's accounts | entry | `links.debit`, `links.credit` | account |
| Entry's date | entry | `parents` | entrygroup |
| Event participants | calendarevent | `children.participant` | participant |
| Participant's member | participant | `links.member` | member |
| Attendance records | presencelist | `children.attendee` | attendee |
| Attendee's member | attendee | `links.member` | member |
| Member's group | member | `parents` | membergroup |
| Members in hierarchy | membergroup | use `$ancestors.$id` | member |
| Account's period | account | `parents` → `parents` | accountgroup → period |
| Period's accounts | period | `children.accountgroup` → `children.account` | account |
| Bank payments | bankaccount | `links.payment` | payment |
| Payment's invoice | payment | `links.debitor` | debitor |

---

## Best Practices

1. **Always use `format=full`** when you need object details, not just IDs
2. **Fetch related objects separately** - Don't try to get everything in one query
3. **Build lookup dictionaries** - Convert lists to dicts for O(1) access
4. **Check for existence** - IDs in `links` may reference deleted objects
5. **Use filters effectively** - Filter at API level, not in Python
6. **Understand bidirectional links** - Some links work both ways (e.g., member↔debitor)
7. **Know your parents** - `parents` and `children` define containment hierarchy
8. **Know your links** - `links` define associations without hierarchy
9. **Batch when possible** - Fetch all objects of a type once, create lookups
10. **Read this document** - When writing complex queries, reference this guide

---

## Need More Details?

For endpoint documentation and usage examples, refer to:
- [members.md](members.md) - Member, membergroup, calendar, events
- [finance.md](finance.md) - Accounting, invoices, payments
- [documents.md](documents.md) - Document storage
- [articles.md](articles.md) - Inventory management
- [admin.md](admin.md) - Users and permissions
- [letters.md](letters.md) - Letters and emails
- [core.md](core.md) - System configuration
- [replication.md](replication.md) - Change tracking
