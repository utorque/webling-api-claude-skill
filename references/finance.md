# Finance API Reference

## Debitor (Invoice)

A debitor is an invoice. It must be linked to at least one revenue entry.

**Key Properties**:
- `title` - Invoice title
- `date` - Invoice date
- `state` - `open` or `paid`
- `totalamount`, `paidamount`, `remainingamount`, `writeoffamount` - computed, read-only
- `invoiceitems` - order of invoice items (linked revenue entries)
- `address` - populated when linked member is deleted

**Related Data** (in linked objects):
- Pay dates: `links->payment[*]->parents[0]->properties->date`
- Receipt: `links->payment[0]->properties->receipt`
- PDFs: `links->letterpdf[*]->properties->pdf->href`

### List Debitors
```
GET /debitor?filter=&order=debitorid ASC&format=
```

### Create Debitor
```
POST /debitor
```
Must create an entry and attach it in the same request (inline method).

**Request Body**:
```json
{
  "properties": {
    "title": "Membership Fee 2024"
  },
  "parents": [3777],
  "links": {
    "member": [504],
    "debitorcategory": [1099],
    "revenue": [{
      "properties": {
        "title": "Annual Fee",
        "amount": 100.00
      },
      "parents": [{
        "properties": { "date": "2024-01-15" },
        "parents": [3777]
      }],
      "links": {
        "debit": [2001],
        "credit": [2002]
      }
    }]
  }
}
```

**Response 201**: ID of newly created debitor

### Get Debitor
```
GET /debitor/{id}
```
Returns debitor with entry data included.

### Update Debitor
```
PUT /debitor/{id}
```

### Delete Debitor
```
DELETE /debitor/{id}
```

---

## Debitorcategory

Categories for debitors. Children of periodgroup (available in all child periods).

### List Debitorcategories
```
GET /debitorcategory?filter=&order=title ASC&format=
```

### Create Debitorcategory
```
POST /debitorcategory
```

**Request Body**:
```json
{
  "properties": { "title": "Membership Fees" },
  "parents": [1814]
}
```

### Get/Update/Delete Debitorcategory
```
GET /debitorcategory/{id}
PUT /debitorcategory/{id}
DELETE /debitorcategory/{id}
```

---

## Entry

A financial posting linked to two accounts. Child of an entrygroup.
Can link to debitor (revenue/payment) and costcenter.

**Note**: `receipt`, `receiptfile`, `isEBill`, `entryid` are deprecated in `/entry` - use `/entrygroup`.

### List Entries
```
GET /entry?filter=&order=title ASC&format=
```

### Create Entry
```
POST /entry
```
Must create entrygroup and attach entry in same request.

**Request Body**:
```json
{
  "properties": {
    "title": "Entry Title",
    "amount": 150.00
  },
  "parents": [{
    "properties": {
      "date": "2024-01-15",
      "receipt": "INV-001"
    },
    "parents": [3777]
  }],
  "links": {
    "debit": [2001],
    "credit": [2002],
    "costcenter": [3598]
  }
}
```

### Get/Update/Delete Entry
```
GET /entry/{id}
HEAD /entry/{id}
PUT /entry/{id}
DELETE /entry/{id}
```

---

## Entrygroup

Collective financial posting. Child of period. Has one entry child.

### List Entrygroups
```
GET /entrygroup?filter=&order=title ASC&format=
```

### Create Entrygroup
```
POST /entrygroup
```
Must include entry child in same request.

**Request Body**:
```json
{
  "properties": {
    "date": "2024-01-15",
    "receipt": "REC-001",
    "entryid": "E001"
  },
  "parents": [3777],
  "children": {
    "entry": [{
      "properties": { "title": "Posting", "amount": 100.00 },
      "links": { "debit": [2001], "credit": [2002] }
    }]
  }
}
```

### Get/Update/Delete Entrygroup
```
GET /entrygroup/{id}
PUT /entrygroup/{id}
DELETE /entrygroup/{id}
```

---

## Account

Finance account (Konto). Child of accountgroup. Links to accounttemplate required.
`amount` is computed (read-only). `budget` for expense/income only. `openingentry` for assets/liabilities only.

### List Accounts
```
GET /account?filter=&order=title ASC&format=
```

### Create Account
```
POST /account
```

**Request Body**:
```json
{
  "properties": {
    "title": "Bank Account",
    "number": "1000",
    "budget": 50000.00
  },
  "parents": [2243],
  "links": {
    "accounttemplate": [4023]
  }
}
```

### Get/Update/Delete Account
```
GET /account/{id}
PUT /account/{id}
DELETE /account/{id}
```

---

## Accountgroup

Account group (Kontengruppe). Child of period. Links to accountgrouptemplate required.
`type`: `expense`, `income`, `assets`, or `liabilitys`

### List/Create/Get/Update/Delete Accountgroup
```
GET /accountgroup?filter=&order=title ASC&format=
POST /accountgroup
GET /accountgroup/{id}
PUT /accountgroup/{id}
DELETE /accountgroup/{id}
```

---

## Accounttemplate

Template linking accounts across periods. Child of accountgrouptemplate.

### CRUD Operations
```
GET /accounttemplate?filter=&order=title ASC&format=
POST /accounttemplate
GET /accounttemplate/{id}
PUT /accounttemplate/{id}
DELETE /accounttemplate/{id}
```

---

## Accountgrouptemplate

Template linking accountgroups across periods. Child of periodchain.

### CRUD Operations
```
GET /accountgrouptemplate?filter=&order=title ASC&format=
POST /accountgrouptemplate
GET /accountgrouptemplate/{id}
PUT /accountgrouptemplate/{id}
DELETE /accountgrouptemplate/{id}
```

---

## Period

Accounting period. Child of periodgroup. Must link to periodchain.

### List Periods
```
GET /period?filter=&order=title ASC&format=
```

### Create Period
```
POST /period
```
Must link or create periodchain in same request.

**Request Body**:
```json
{
  "properties": {
    "title": "2024",
    "from": "2024-01-01",
    "to": "2024-12-31"
  },
  "parents": [1814],
  "links": {
    "periodchain": [4126]
  }
}
```

### Get/Update/Delete Period
```
GET /period/{id}
PUT /period/{id}
DELETE /period/{id}
```

---

## Periodgroup

Container for periods.

### CRUD Operations
```
GET /periodgroup?filter=&order=title ASC&format=
POST /periodgroup
GET /periodgroup/{id}
PUT /periodgroup/{id}
DELETE /periodgroup/{id}
```

---

## Periodchain

Groups related periods (Kontenrahmen). Child of periodgroup.
`sourcechart`: `null`, `"simple"`, `"deSkr49"`, `"deSkr42"`, `"chKmuSimple"`, `"deDsb"`, `"custom"`

### CRUD Operations
```
GET /periodchain?filter=&order=title ASC&format=
POST /periodchain
GET /periodchain/{id}
PUT /periodchain/{id}
DELETE /periodchain/{id}
```

**Create Request**:
```json
{
  "properties": { "title": "Main Chart" },
  "parents": [1814],
  "sourcechart": "chKmuSimple"
}
```

---

## Costcenter

Categorize entries. Child of period.

### CRUD Operations
```
GET /costcenter?filter=&order=title ASC&format=
POST /costcenter
GET /costcenter/{id}
PUT /costcenter/{id}
DELETE /costcenter/{id}
```

**Create Request**:
```json
{
  "properties": { "title": "Marketing", "number": "CC001" },
  "parents": [3777]
}
```

---

## Finance Query Examples

```bash
# All open debitors
/debitor?filter=state = "open"

# Members with unpaid invoices
/member?filter=$links.debitor.state = "open"

# Members with debitor amount > 100 and unpaid
/member?filter=WITH $links.debitor (totalamount > 100 AND remainingamount > 0)

# Debitor linked to specific member
/debitor?filter=$links.member.$id = 504

# Entries in specific account
/entry?filter=$links.debit.$id = 2001 OR $links.credit.$id = 2001

# Entries with costcenter
/entry?filter=$links.costcenter.$id = 3598
```
