# Finance API Reference

## Data Model Overview

This document covers all finance-related objects in Webling's double-entry accounting system. The finance module includes periods, accounts, entries (postings), invoices (debitors), and payment tracking.

### Complete Object Hierarchy

```
periodgroup (root container)
  ├── period (accounting period)
  │     ├── accountgroup (account categories)
  │     │     └── account → links to accounttemplate
  │     ├── entrygroup (collective posting)
  │     │     └── entry → links to debit/credit accounts
  │     ├── debitor (invoice) → links to member
  │     ├── costcenter (cost centers)
  │     ├── vat (tax records)
  │     └── sepa (SEPA direct debits)
  ├── periodchain (chart of accounts template)
  │     ├── accountgrouptemplate (account category templates)
  │     │     └── accounttemplate (account templates)
  │     ├── bankaccount → links to accounttemplate
  │     └── saltedgeconnection (bank sync)
  ├── debitorcategory (invoice categories)
  ├── payment (payment records/transactions)
  └── rnwmerchant (RaiseNow payment processor)
        └── rnwform (payment forms)
```

### Object Relationships Summary

| Object | Parent | Children | Links To |
|--------|--------|----------|----------|
| **periodgroup** | none (root) | period, periodchain, debitorcategory, payment, rnwmerchant | none |
| **period** | periodgroup | accountgroup, entrygroup, debitor, costcenter, vat, sepa | periodchain |
| **periodchain** | periodgroup | accountgrouptemplate, bankaccount, saltedgeconnection | period (bidirectional) |
| **accountgroup** | period | account | accountgrouptemplate |
| **account** | accountgroup | none | comment, accounttemplate, entrygroup, entry, vat |
| **accountgrouptemplate** | periodchain | accounttemplate | accountgroup |
| **accounttemplate** | accountgrouptemplate | none | account, bankaccount |
| **entrygroup** | period | entry | account |
| **entry** | entrygroup | none | debit (account), credit (account), account, costcenter, debitor, payment, vat, entry (self) |
| **debitor** | period | none | member, email, emailsent, letter, letterpdf, comment, debitorcategory, paymentrecord (payment), revenue (entry), payment (entry), writeoff (entry), entry |
| **debitorcategory** | periodgroup | none | debitor |
| **costcenter** | period | none | entry |
| **vat** | period | none | entry, account |
| **payment** | periodgroup | none | debitor, entry, rnwform, bankaccount |
| **bankaccount** | periodchain | none | accounttemplate, payment, saltedgeconnection |
| **sepa** | period | none | debitor |
| **saltedgeconnection** | periodchain | none | bankaccount |
| **rnwmerchant** | periodgroup | rnwform | none |
| **rnwform** | rnwmerchant | none | payment, email |

> **Note**: For complex queries involving multiple object relationships, refer to `full-object-relations.md`

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

## Periodgroup

Root container for all finance-related objects.

**Object Type**: `periodgroup`
**Parent**: none (root object)
**Children**: period, periodchain, debitorcategory, payment, rnwmerchant
**Links**: none

**Properties** (from data model):
- `title` [text] - Periodgroup name

**Relationship Notes**:
- Acts as the root container for the entire finance system
- All periods and period chains belong to a periodgroup
- Invoice categories and payments are also children of periodgroup

### CRUD Operations
```
GET /periodgroup?filter=&order=title ASC&format=
POST /periodgroup
GET /periodgroup/{id}
PUT /periodgroup/{id}
DELETE /periodgroup/{id}
```

---

## Costcenter

Cost centers for categorizing expenses and revenue. Child of period.

**Object Type**: `costcenter`
**Parent**: `period`
**Children**: none
**Links**: entry

**Properties** (from data model):
- `title` [text] - Cost center name

**Relationship Notes**:
- Entries can be linked to cost centers for expense tracking
- Cost centers are period-specific

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
  "properties": { "title": "Marketing" },
  "parents": [3777]
}
```

---

## VAT

Value-added tax (VAT) or sales tax records. Child of period.

**Object Type**: `vat`
**Parent**: `period`
**Children**: none
**Links**: entry, account

**Properties** (from data model):
- `title` [text] - VAT rate name (e.g., "Standard 19%", "Reduced 7%")
- `rate` [numeric] - Tax rate as decimal (e.g., 0.19 for 19%)

**Relationship Notes**:
- Links to entries that use this VAT rate
- Can link to VAT accounts for automatic tax calculation
- VAT records are period-specific

### CRUD Operations
```
GET /vat?filter=&order=title ASC&format=
POST /vat
GET /vat/{id}
PUT /vat/{id}
DELETE /vat/{id}
```

---

## Bankaccount

Bank account for payment synchronization. Child of periodchain.

**Object Type**: `bankaccount`
**Parent**: `periodchain`
**Children**: none
**Links**: accounttemplate, payment, saltedgeconnection

**Properties** (from data model):
- `title` [text] - Account name
- `balance` [numeric] - Current balance
- `iban` [text] - IBAN number
- `lastSync` [timestamp] - Last synchronization time
- `accounttype` [enum] - Account type
- `iconUrl` [text] - Bank logo URL
- `externalId` [text] - External account ID
- `data` [json] - Additional account data

**Relationship Notes**:
- Links to accounttemplate to map to accounting accounts
- Links to payment records for transaction matching
- Can be connected via saltedgeconnection for automatic sync
- Child of periodchain (not period) to persist across accounting periods

### CRUD Operations
```
GET /bankaccount?filter=&order=title ASC&format=
POST /bankaccount
GET /bankaccount/{id}
PUT /bankaccount/{id}
DELETE /bankaccount/{id}
```

---

## SEPA

SEPA direct debit batches. Child of period.

**Object Type**: `sepa`
**Parent**: `period`
**Children**: none
**Links**: debitor

**Properties** (from data model):
- `name` [text] - SEPA batch name
- `iban` [text] - Creditor IBAN
- `bic` [text] - Creditor BIC
- `seriennr` [text] - Sequential number
- `currency` [text] - Currency code (e.g., "EUR")
- `file` [file] - Generated SEPA XML file
- `duedate` [date] - Collection due date

**Relationship Notes**:
- Links to debitors (invoices) to be collected via SEPA
- Used for batch payment collection
- SEPA records are period-specific

---

## Saltedgeconnection

Bank synchronization connection via Salt Edge API. Child of periodchain.

**Object Type**: `saltedgeconnection`
**Parent**: `periodchain`
**Children**: none
**Links**: bankaccount

**Properties** (from data model):
- `title` [text] - Connection name
- `connectionId` [text] - Salt Edge connection ID
- `status` [text] - Connection status
- `connectionData` [json] - Connection details
- `providerData` [json] - Bank provider information
- `consentData` [json] - User consent data

**Relationship Notes**:
- Links to bankaccounts for automatic transaction sync
- Manages bank API connection credentials
- Child of periodchain to persist across periods

---

## RnwMerchant

RaiseNow payment processor merchant account. Child of periodgroup.

**Object Type**: `rnwmerchant`
**Parent**: `periodgroup`
**Children**: rnwform
**Links**: none

**Properties** (from data model):
- `title` [text] - Merchant name
- `approved` [bool] - Approval status
- `iban` [text] - Bank account IBAN
- `billingaddress` [text] - Billing address line 1
- `billingaddress2` [text] - Billing address line 2
- `billingpostalcode` [text] - Postal code
- `billingcity` [text] - City
- `billingcountry` [text] - Country
- `email` [text] - Contact email
- `firstname` [text] - Contact first name
- `lastname` [text] - Contact last name
- `merchantid` [text] - RaiseNow merchant ID
- `apikey` [text] - RaiseNow API key
- `widgetkey` [text] - Widget integration key

**Relationship Notes**:
- Contains rnwform children for payment forms
- Manages RaiseNow payment processor integration

---

## RnwForm

RaiseNow payment form configuration. Child of rnwmerchant.

**Object Type**: `rnwform`
**Parent**: `rnwmerchant`
**Children**: none
**Links**: payment, email

**Properties** (from data model):
- `title` [text] - Form name
- `sendaddress` [bool] - Whether to collect address
- `description` [longtext] - Form description
- `formtype` [enum] - Form type (donation, membership, etc.)
- `amounttype` [enum] - Amount type (fixed, variable, etc.)

**Relationship Notes**:
- Links to payment records created via this form
- Can link to email templates for confirmations
- Used for online payment collection

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

## Practical Pattern: Members with Unpaid Invoices

**Problem**: Get members with their unpaid invoices including full details.

**⚠️ Important**: The filter `$links.debitor.state = "open"` finds the right members, but responses only contain debitor IDs, not full debitor data.

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

# Step 1: Fetch members who have open debitors
members = fetch("/member", filter='$links.debitor.state = "open"')

# Step 2: Fetch all open debitors separately
debitors = fetch("/debitor", filter='state = "open"')

# Step 3: Create lookup dictionary
debitors_dict = {d["id"]: d for d in debitors}

# Step 4: Enrich members with full debitor data
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

# Now you have complete data
for member in members:
    props = member["properties"]
    print(f"{props.get('Vorname')} {props.get('Name')}")
    print(f"  Total unpaid: CHF {member['total_unpaid']:.2f}")
    for invoice in member["unpaid_invoices"]:
        inv_props = invoice["properties"]
        print(f"  - Invoice {invoice['id']}: CHF {inv_props.get('remainingamount', 0):.2f}")
```

## Practical Pattern: Financial Entries with Account Details

**Problem**: Get all financial entries with full debit/credit account information and dates.

**Correct Approach**:

```python
# Step 1: Fetch all related entity types
entries = fetch("/entry")
accounts = fetch("/account")
entrygroups = fetch("/entrygroup")

# Step 2: Create lookup dictionaries
accounts_dict = {a["id"]: a for a in accounts}
entrygroups_dict = {eg["id"]: eg for eg in entrygroups}

# Step 3: Enrich entries with related data
for entry in entries:
    # Add parent entrygroup data (contains date)
    entrygroup_id = entry.get("parents", [None])[0]
    entry["entrygroup"] = entrygroups_dict.get(entrygroup_id)

    # Add linked account data
    debit_id = entry.get("links", {}).get("debit", [None])[0]
    credit_id = entry.get("links", {}).get("credit", [None])[0]
    entry["debit_account"] = accounts_dict.get(debit_id)
    entry["credit_account"] = accounts_dict.get(credit_id)

    # Extract commonly needed fields
    entry["date"] = entry["entrygroup"]["properties"]["date"] if entry["entrygroup"] else None
    entry["debit_name"] = entry["debit_account"]["properties"]["title"] if entry["debit_account"] else None
    entry["credit_name"] = entry["credit_account"]["properties"]["title"] if entry["credit_account"] else None
    entry["amount"] = entry.get("properties", {}).get("amount", 0)

# Now you can work with complete entry data
for entry in entries:
    print(f"{entry['date']}: {entry['debit_name']} → {entry['credit_name']}: CHF {entry['amount']:.2f}")
```
