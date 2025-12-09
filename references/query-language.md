# Query Language Reference

All GET endpoints returning lists support filtering via the `filter=` parameter.

## Basic Syntax

```
GET /member?filter=`Vorname` = "Hans"
```

**URL encoding required** for special characters in queries.

## Property Queries

| Syntax | Description |
|--------|-------------|
| `` `Name` = "Meier" `` | Query by property |
| `` `Betrag` > 100 `` | Numeric comparison |
| `* = "Müller"` | Search all properties |
| `` `Name`,`Vorname` = "Hans" `` | Search multiple properties |

**Note**: Properties with special characters must be enclosed in backticks.

## Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `<` | Less than | `` `PLZ` < 2000 `` |
| `<=` | Less or equal | `` `PLZ` <= 2000 `` |
| `>` | Greater than | `` `PLZ` > 2000 `` |
| `>=` | Greater or equal | `` `PLZ` >= 2000 `` |
| `=` | Equal | `` `Name` = "Meier" `` |
| `!=` | Not equal | `` `Name` != "Meier" `` |
| `FILTER` | Starts with | `` `Name` FILTER "Me" `` → Meier, Mettler |
| `CONTAINS` | Contains substring (slower) | `` `Name` CONTAINS "an" `` → Baumann |
| `IS EMPTY` | Empty/null value | `` `E-Mail` IS EMPTY `` |
| `IN` | Multiple values | `` `Status` IN ("Aktiv", "Passiv") `` |
| `WITH` | Multiple linked properties | `WITH $links.debitor (amount > 100 AND state = "open")` |

## Logical Operators

```sql
-- AND
`Name` = "Meier" AND `Vorname` = "Hans"

-- OR
`Name` = "Meier" OR `Name` = "Müller"

-- NOT
NOT `E-Mail` IS EMPTY
NOT($parents.$id = 100)

-- Parentheses
(`Name` = "Meier" OR `Name` = "Müller") AND `Vorname` = "Hans"

-- Complex nesting
`Vorname` = "Peter" OR (`Vorname` = "Hans" AND `Name` = "Meier" OR (`PLZ` > 1000 AND `PLZ` < 2000))
```

## Special Properties

| Property | Description |
|----------|-------------|
| `$parents.<property>` | Query parent property |
| `$ancestors.<property>` | Query any ancestor (members, membergroups, documents, documentgroups only) |
| `$children.<type>.<property>` | Query child property |
| `$links.<category>.<property>` | Query linked object property |
| `$reverselinks.<type>.<property>` | Query reverse links |
| `$readonly` | Boolean: object is read-only |
| `$writable` | Boolean: object is writable |
| `$label` | Object label (usually title) |
| `$id` | Object ID |

**Note**: Backticks not required for special properties.

## Functions

| Function | Description | Example |
|----------|-------------|---------|
| `LOWER(property)` | Convert to lowercase | `LOWER(\`Name\`) = "meier"` |
| `UPPER(property)` | Convert to uppercase | `UPPER(\`Name\`) = "MEIER"` |
| `TRIM(property)` | Trim whitespace | `TRIM(\`Name\`) = "Meier"` |
| `DAY(date)` | Extract day | `DAY(\`Geburtstag\`) = 15` |
| `MONTH(date)` | Extract month | `MONTH(\`Geburtstag\`) = 8` |
| `YEAR(date)` | Extract year | `YEAR(\`Eintrittsdatum\`) = 2020` |
| `AGE(date)` | Years since date | `AGE(\`Geburtstag\`) >= 18` |
| `AGETHISYEAR(date)` | Age at end of year | `AGETHISYEAR(\`Geburtstag\`) = 50` |
| `BIRTHDAY(date, m, d)` | Sort by birthday after date | `BIRTHDAY(\`Geburtstag\`, 8, 20)` |
| `TODAY()` | Current date | `` `Eintrittsdatum` > TODAY() `` |
| `COUNT(path)` | Count (order param only) | `?order=COUNT($links.debitor) DESC` |

## Multienum Operators

For multi-select fields:

| Operator | Description | Example |
|----------|-------------|---------|
| `IS` | Exact match | `` `Tags` IS ["Value"] `` |
| `CONTAINS ALL OF` | Has all values | `` `Tags` CONTAINS ALL OF ["A", "B"] `` |
| `CONTAINS NONE OF` | Has none of values | `` `Tags` CONTAINS NONE OF ["X", "Y"] `` |
| `CONTAINS ANY OF` | Has any of values | `` `Tags` CONTAINS ANY OF ["A", "B"] `` |

## Sorting

```
?order=`Vorname` ASC
?order=`Vorname` DESC
?order=`Vorname` DESC, `Nachname` ASC
?order=$label ASC
?order=$parents.title DESC
?order=DAY(`Geburtstag`) DESC
?order=COUNT($links.debitor) DESC
```

---

## Query Examples

### Basic Filtering
```bash
# Exact match
/member?filter=`Vorname` = "Hans"

# Multiple conditions
/member?filter=`Vorname` = "Hans" AND `Name` = "Meier"

# Case-insensitive
/member?filter=UPPER(`Name`) = "MEIER"
```

### Empty/Not Empty
```bash
# Empty field
/member?filter=`E-Mail` IS EMPTY

# Not empty
/member?filter=NOT `E-Mail` IS EMPTY
/member?filter=NOT(`E-Mail` IS EMPTY)
```

### IN Operator
```bash
# Multiple IDs
/member?filter=`ID` IN (22, 45, 67)

# Multiple values
/member?filter=`Status` IN ("Aktiv", "Passiv", "Ehrenmitglied")

# Multiple parent groups
/member?filter=$parents.$id IN (520, 612, 802)

# NOT IN
/member?filter=NOT($parents.$id IN (438, 748))
```

### Parent/Group Queries
```bash
# Members in specific group
/member?filter=$parents.$id = 555

# Members in any of these groups
/member?filter=$parents.$id = 100 OR $parents.$id = 101
/member?filter=$parents.$id IN (100, 101, 102)

# Members NOT in group
/member?filter=NOT($parents.$id = 100)

# Members in group with specific title
/member?filter=$parents.title = "Vorstand"

# Search in group and all subgroups
/member?filter=`Vorname` = "Tim" AND $ancestors.$id = 550
```

### Date Queries
```bash
# By age
/member?filter=AGE(`Geburtstag`) = 22
/member?filter=AGE(`Geburtstag`) >= 18

# Birthday in month
/member?filter=MONTH(`Geburtstag`) = 8
/member?filter=MONTH(`Geburtstag`) = 8&order=DAY(`Geburtstag`) ASC

# Birthday after date
/member?filter=MONTH(`Geburtstag`) > 8 OR (MONTH(`Geburtstag`) = 8 AND DAY(`Geburtstag`) > 20)

# Future dates
/member?filter=`Eintrittsdatum` > TODAY()

# Specific date
/member?filter=`Eintrittsdatum` = "2018-03-06"
/member?filter=`Eintrittsdatum` <= "2018-06-23"
```

### Linked Objects
```bash
# Member linked to specific debitor
/member?filter=$links.debitor.$id = 851

# Members with open invoices
/member?filter=$links.debitor.state = "open"

# Members with debitor of amount 100
/member?filter=$links.debitor.$links.revenue.amount = 100

# Members with any comments
/member?filter=$links.comment.$id > 0

# Debitor with label "Meier"
/entrygroup?filter=$children.entry.$links.debitor.$links.member.$label FILTER "Meier"
```

### WITH Operator

Without `WITH`, conditions are checked separately:
```bash
# Finds members with ANY debitor > 100 AND ANY debitor unpaid
# (could be different debitors!)
/member?filter=$links.debitor.totalamount > 100 AND $links.debitor.remainingamount > 0
```

With `WITH`, conditions apply to the SAME object:
```bash
# Finds members with a SINGLE debitor that is > 100 AND unpaid
/member?filter=WITH $links.debitor (totalamount > 100 AND remainingamount > 0)
```

### Comparing Fields
```bash
# Where two fields are equal
/member?filter=`E-Mail` = `E-Mail Geschäft`
```

### Membergroup Queries
```bash
# Groups with members in PLZ > 9000
/membergroup?filter=$children.member.PLZ > 9000
```

### Access Control
```bash
# Objects you can edit
/member?filter=$writable = true

# Read-only objects
/member?filter=$readonly = true
```

---

## EBNF Grammar

```ebnf
start ::= orExpr

orExpr ::= andExpr "OR" orExpr
andExpr ::= notExpr "AND" orExpr
notExpr ::= "NOT"? withExpr
withExpr ::= ( "WITH" axisExpr ( "." axisExpr )* )? bracketExpr
bracketExpr ::= ( "(" orExpr ")" ) | atomExpr

atomExpr ::= comparisonExpr | filterComparisonExpr | containsComparisonExpr
           | multienumComparisonExpr | emptyExpr | setExpr
comparisonExpr ::= contentExpr universalOpExpr contentExpr
filterComparisonExpr ::= contentExpr "FILTER" valueExpr
containsComparisonExpr ::= contentExpr "CONTAINS" stringExpr
multienumComparisonExpr ::= contentExpr multienumOpExpr jsonStringArrayExpr
emptyExpr ::= contentExpr "IS" "EMPTY"
setExpr ::= contentExpr "IN" "(" valueExpr ("," valueExpr)* ")"

universalOpExpr ::= "<" | "<=" | ">" | ">=" | "=" | "!="
multienumOpExpr ::= "CONTAINS ALL OF" | "IS" | "CONTAINS NONE OF" | "CONTAINS ANY OF"

contentExpr ::= valueExpr | jsonPathExpr | callExpr | pathExpr
valueExpr ::= stringExpr | numberExpr | boolExpr
callExpr ::= literalExpr "(" (contentExpr ("," contentExpr)* )? ")"
pathExpr ::= propertiesExpr | accessExpr | labelExpr | idExpr | ( axisExpr "." pathExpr )
propertiesExpr ::= "*" | ( propertyExpr ("," propertyExpr)* )
propertyExpr ::= literalExpr | backtickExpr

axisExpr ::= parentExpr | ancestorExpr | childExpr | linkExpr | reverseLinkExpr
parentExpr ::= "$parents"
ancestorExpr ::= "$ancestors"
childExpr ::= "$children" "." literalExpr
linkExpr ::= "$links" "." literalExpr
reverseLinkExpr ::= "$reverselinks" "." literalExpr

accessExpr ::= "$readonly" | "$writable"
labelExpr ::= "$label"
idExpr ::= "$id"

stringExpr ::= ("'" /[^"]* / "'") | ('"' /[^']* / '"')
backtickExpr ::= "`" /[^`]* / "`"
literalExpr ::= /\w* /
boolExpr ::= "TRUE" | "FALSE"
intExpr ::= "-"? /\d+/
numberExpr ::= "-"? /\d+/ ( "." /\d* / )?
jsonStringArrayExpr ::= "[" stringExpr ( "," stringExpr )* "]"
```
