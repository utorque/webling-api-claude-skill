# Finance API Reference

> **Data Model Reference**: See `webling_data_graphviz.txt` for complete finance object definitions including debitor, debitorcategory, entry, entrygroup, account, accountgroup, accounttemplate, accountgrouptemplate, period, periodchain, periodgroup, costcenter, payment, bankaccount, and vat.

## Finance Object Hierarchy

```
periodgroup (root container)
  ├── period (accounting period)
  │     ├── accountgroup
  │     │     └── account → links to accounttemplate
  │     ├── entrygroup (financial posting)
  │     │     └── entry → links to debit/credit accounts
  │     ├── debitor (invoice) → links to member
  │     ├── costcenter
  │     └── vat
  ├── periodchain (chart of accounts template)
  │     ├── accountgrouptemplate
  │     │     └── accounttemplate
  │     └── bankaccount → links to accounttemplate
  ├── debitorcategory (invoice categories)
  └── payment (payment records)
```

## Debitor (Invoice)

A debitor is an invoice. It must be linked to at least one revenue entry.

**Object Type**: `debitor`
**Parent**: `period`
**Links**: member, email, emailsent, letter, letterpdf, debitorcategory, paymentrecord (payment), revenue (entry), payment (entry), writeoff (entry), entry

**Key Properties** (from graphviz):
- `title` [longtext] - Invoice title
- `date` [date] - Invoice date
- `state` [enum] - `open` or `paid`
- `totalamount`, `paidamount`, `remainingamount`, `writeoffamount` [numeric] - computed, read-only
- `invoiceitems` [json] - order of invoice items (linked revenue entries)
- `address` [longtext] - populated when linked member is deleted
- `comment` [longtext] - notes
- `duedate` [date] - payment due date
- `debitorid` [autoincrement] - unique invoice number

**Response Structure**:
```json
{
  "type": "debitor",
  "id": 1234,
  "meta": {
    "created": "2024-01-15 10:30:00",
    "createuser": { "label": "John Doe", "type": "user" }
  },
  "readonly": false,
  "properties": {
    "title": "Membership Fee 2024",
    "date": "2024-01-15",
    "state": "open",
    "totalamount": 100.00,
    "paidamount": 0.00,
    "remainingamount": 100.00
  },
  "parents": [3777],
  "children": {},
  "links": {
    "member": [504],
    "debitorcategory": [1099],
    "revenue": [5678]
  }
}
```

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

**Object Type**: `account`
**Parent**: `accountgroup`
**Links**: comment, accounttemplate, entrygroup, entry, vat

**Key Properties** (from graphviz):
- `title` [text] - Account name
- `amount` [numeric] - Current balance (computed, read-only)
- `budget` [numeric] - Budget (for expense/income accounts)
- `openingentry` [numeric] - Opening balance (for assets/liabilities)

**Response Structure**:
```json
{
  "type": "account",
  "id": 2001,
  "meta": {
    "created": "2024-01-01 00:00:00",
    "createuser": { "label": "Admin", "type": "user" }
  },
  "readonly": false,
  "properties": {
    "title": "Bank Account",
    "amount": 15250.50,
    "budget": 50000.00,
    "openingentry": 10000.00
  },
  "parents": [2243],
  "children": {},
  "links": {
    "accounttemplate": [4023],
    "entry": [3001, 3002, 3003]
  }
}
```

### List Accounts
```
GET /account?filter=&order=title ASC&format=
GET /account?filter=$parents.$id = 2243  # Accounts in specific accountgroup
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

**Object Type**: `period`
**Parent**: `periodgroup`
**Children**: accountgroup, entrygroup, debitor, costcenter, vat, sepa
**Links**: periodchain

**Key Properties** (from graphviz):
- `title` [text] - Period name (e.g., "2024")
- `from` [date] - Start date
- `to` [date] - End date
- `state` [enum] - Period state
- `budgetdescription` [longtext] - Budget notes
- `hasSpheres` [bool] - Whether period uses cost centers

**Response Structure**:
```json
{
  "type": "period",
  "id": 10312,
  "meta": {
    "created": "2024-01-01 00:00:00",
    "createuser": { "label": "Admin", "type": "user" }
  },
  "readonly": false,
  "properties": {
    "title": "2024",
    "from": "2024-01-01",
    "to": "2024-12-31",
    "state": "open"
  },
  "parents": [800],
  "children": {
    "accountgroup": [2240, 2241, 2242],
    "entrygroup": [3500, 3501],
    "debitor": [1200, 1201]
  },
  "links": {
    "periodchain": [7131]
  }
}
```

### List Periods
```
GET /period?filter=&order=title ASC&format=
GET /period?filter=$parents.$id = 800  # Periods in specific periodgroup
GET /period?filter=$links.periodchain.$id = 7131  # Periods using specific chart
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

Groups related periods (Kontenrahmen / Chart of Accounts). Child of periodgroup.

**Object Type**: `periodchain`
**Parent**: `periodgroup`
**Children**: accountgrouptemplate, bankaccount, saltedgeconnection
**Links**: period (bidirectional - periods link back to periodchain)

**Key Properties** (from graphviz):
- `title` [text] - Chart name (e.g., "Kontenrahmen")
- `sourcechart` [enum] - Template used: `null`, `"simple"`, `"deSkr49"`, `"deSkr42"`, `"chKmuSimple"`, `"deDsb"`, `"custom"`

**Response Structure** (real example):
```json
{
  "type": "periodchain",
  "id": 7131,
  "meta": {
    "created": "2019-03-13 08:36:57",
    "createuser": { "label": "Upgrade", "type": "apikey" },
    "lastmodified": "2025-01-03 17:12:25",
    "lastmodifieduser": { "label": "Demo Benutzer", "type": "user" }
  },
  "readonly": true,
  "properties": {
    "title": "Kontenrahmen",
    "sourcechart": null
  },
  "parents": [800],
  "children": {
    "accountgrouptemplate": [7132, 7138, 7140, 7144, 7147, 7152, 7155, 7157]
  },
  "links": {
    "period": [3269, 3943, 5712, 6337, 7180, 7943, 8580, 9234, 9653, 10312]
  }
}
```

**Navigation Pattern**:
```bash
# Get periodgroup with children
GET /periodgroup/800?format=full

# Navigate to periodchain from children
GET /periodchain/7131?format=full

# Get account group templates from children
GET /accountgrouptemplate/7132?format=full

# Get linked periods
GET /period/10312?format=full
```

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
