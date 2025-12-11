# Articles API Reference

## Data Model Overview

This document covers article/inventory management in Webling. The article system allows tracking of physical items, merchandise, or products with pricing and stock levels.

### Complete Object Hierarchy

```
articlegroup (simple hierarchy)
  └── article
```

### Object Relationships Summary

| Object | Parent | Children | Links To |
|--------|--------|----------|----------|
| **article** | articlegroup | none | none |
| **articlegroup** | none (root) | article | none |

> **Note**: Articlegroups do not have parent-child relationships with each other (non-hierarchical).

> **Note**: For complex queries involving multiple object relationships, refer to `full-object-relations.md`

## Article

An article is a material item. Always a child of an articlegroup.

**Object Type**: `article`
**Parent**: `articlegroup`
**Links**: None

**Properties** (from graphviz):
- `title` [text] - Article name
- `description` [longtext] - Description
- `place` [text] - Storage location
- `price` [numeric] - Price
- `quantity` [int] - Stock quantity

### List Articles
```
GET /article?filter=&order=title ASC&format=
```

| Param | Type | Description |
|-------|------|-------------|
| `filter` | string | Filter using Query Language |
| `order` | string | Sort by property and direction |
| `format` | string | Use `full` for complete objects |

**Response 200**: List of article IDs or full objects

### Create Article
```
POST /article
```

**Request Body**:
```json
{
  "properties": {
    "title": "Club T-Shirt",
    "description": "Official club t-shirt",
    "price": 25.00,
    "stock": 100
  },
  "parents": [56]
}
```

**Response 201**: ID of newly created article

### Get Article
```
GET /article/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Article ID (e.g., `66`) |

**Response 200**: Article object

### Update Article
```
PUT /article/{id}
```

**Request Body**:
```json
{
  "properties": {
    "stock": 95,
    "price": 30.00
  }
}
```

**Response 204**: No content

### Delete Article
```
DELETE /article/{id}
```

**Response 204**: No content

---

## Articlegroup

Articlegroups contain articles. Also known as "Rubriken" (categories).

### List Articlegroups
```
GET /articlegroup?filter=&order=title ASC&format=
```

| Param | Type | Description |
|-------|------|-------------|
| `filter` | string | Filter using Query Language |
| `order` | string | Sort by property and direction |
| `format` | string | Use `full` for complete objects |

**Response 200**: List of articlegroup IDs or full objects

### Create Articlegroup
```
POST /articlegroup
```

**Request Body**:
```json
{
  "properties": {
    "title": "Merchandise"
  },
  "parents": []
}
```

**Response 201**: ID of newly created articlegroup

### Get Articlegroup
```
GET /articlegroup/{id}
```

| Param | Type | Description |
|-------|------|-------------|
| `id` | number | Articlegroup ID (e.g., `56`) |

**Response 200**: Articlegroup object with children info

### Update Articlegroup
```
PUT /articlegroup/{id}
```

**Request Body**:
```json
{
  "properties": {
    "title": "Updated Category Name"
  }
}
```

**Response 204**: No content

### Delete Articlegroup
```
DELETE /articlegroup/{id}
```

**Response 204**: No content

---

## Article Query Examples

```bash
# Articles in specific category
/article?filter=$parents.$id = 56

# Articles by price range
/article?filter=`price` >= 10 AND `price` <= 50

# Low stock articles
/article?filter=`stock` < 10

# Search articles by title
/article?filter=`title` FILTER "Shirt"

# All articles sorted by price
/article?order=`price` ASC
```
