[API Information](#api-information)

*   [Authentication](#header-authentication)
*   [Response format](#header-response-format)
*   [Objects](#header-objects)
*   [Property datatypes](#header-property-datatypes)
*   [Lists](#header-lists)
*   [Files](#header-files)
*   [Errors](#header-errors)
*   [Response Status Codes](#header-response-status-codes)
*   [Rate Limit](#header-rate-limit)
*   [Fetch Multiple Objects](#header-fetch-multiple-objects)
*   [Option 1: multiple IDs in the url](#header-option-1-multiple-ids-in-the-url)
*   [Option 2: fetch data instead of IDs](#header-option-2-fetch-data-instead-of-ids)
*   [Pagination](#header-pagination)
*   [Query Language](#header-query-language)
*   [Special Properties](#header-special-properties)
*   [Operators](#header-operators)
*   [Functions](#header-functions)
*   [Sort the results](#header-sort-the-results)
*   [Query Examples](#header-query-examples)
*   [WITH() operator](#header-with()-operator)
*   [EBNF](#header-ebnf)
*   [Examples](#header-examples)
*   [PHP](#header-php)
*   [JavaScript](#header-javascript)
*   [Development Resources](#header-development-resources)
*   [API Browser](#header-api-browser)
*   [PHP Webling Client](#header-php-webling-client)
*   [Code Examples](#header-code-examples)
*   [Symfony Bundle](#header-symfony-bundle)
*   [WordPress Plugin](#header-wordpress-plugin)
*   [Newsletter](#header-newsletter)
*   [Changelog](#header-changelog)

[Account](#account)

*   [Account List](#account-account-list)
    *   [Get Account List](#account-account-list-get)
    *   [Create Account](#account-account-list-post)
*   [Account](#account-account)
    *   [Get Account](#account-account-get)
    *   [Update Account](#account-account-put)
    *   [Delete Account](#account-account-delete)

[Accountgroup](#accountgroup)

*   [Accountgroup List](#accountgroup-accountgroup-list)
    *   [Get Accountgroup List](#accountgroup-accountgroup-list-get)
    *   [Create Accountgroup](#accountgroup-accountgroup-list-post)
*   [Accountgroup](#accountgroup-accountgroup)
    *   [Get Accountgroup](#accountgroup-accountgroup-get)
    *   [Update Accountgroup](#accountgroup-accountgroup-put)
    *   [Delete Accountgroup](#accountgroup-accountgroup-delete)

[Accountgrouptemplate](#accountgrouptemplate)

*   [Accountgrouptemplate List](#accountgrouptemplate-accountgrouptemplate-list)
    *   [Get Accountgrouptemplate List](#accountgrouptemplate-accountgrouptemplate-list-get)
    *   [Create Accountgrouptemplate](#accountgrouptemplate-accountgrouptemplate-list-post)
*   [Accountgrouptemplate](#accountgrouptemplate-accountgrouptemplate)
    *   [Get Accountgrouptemplate](#accountgrouptemplate-accountgrouptemplate-get)
    *   [Update Accountgrouptemplate](#accountgrouptemplate-accountgrouptemplate-put)
    *   [Delete Accountgrouptemplate](#accountgrouptemplate-accountgrouptemplate-delete)

[Accounttemplate](#accounttemplate)

*   [Accounttemplate List](#accounttemplate-accounttemplate-list)
    *   [Get Accounttemplate List](#accounttemplate-accounttemplate-list-get)
    *   [Create Accounttemplate](#accounttemplate-accounttemplate-list-post)
*   [Accounttemplate](#accounttemplate-accounttemplate)
    *   [Get Accounttemplate](#accounttemplate-accounttemplate-get)
    *   [Update Accounttemplate](#accounttemplate-accounttemplate-put)
    *   [Delete Accounttemplate](#accounttemplate-accounttemplate-delete)

[Apikey](#apikey)

*   [Apikey List](#apikey-apikey-list)
    *   [Get Apikey List](#apikey-apikey-list-get)
    *   [Create Apikey](#apikey-apikey-list-post)
*   [Apikey](#apikey-apikey)
    *   [Get Apikey](#apikey-apikey-get)
    *   [Update Apikey](#apikey-apikey-put)
    *   [Delete Apikey](#apikey-apikey-delete)
*   [Apikey last used](#apikey-last-used-get)

[Article](#article)

*   [Article List](#article-article-list)
    *   [Get Article List](#article-article-list-get)
    *   [Create Article](#article-article-list-post)
*   [Article](#article-article)
    *   [Get Article](#article-article-get)
    *   [Update Article](#article-article-put)
    *   [Delete Article](#article-article-delete)

[Articlegroup](#articlegroup)

*   [Articlegroup List](#articlegroup-articlegroup-list)
    *   [Get Articlegroup List](#articlegroup-articlegroup-list-get)
    *   [Create Articlegroup](#articlegroup-articlegroup-list-post)
*   [Articlegroup](#articlegroup-articlegroup)
    *   [Get Articlegroup](#articlegroup-articlegroup-get)
    *   [Update Articlegroup](#articlegroup-articlegroup-put)
    *   [Delete Articlegroup](#articlegroup-articlegroup-delete)

[Config](#config)

*   [Get Config Values](#config-config-get)

[Costcenter](#costcenter)

*   [Costcenter List](#costcenter-costcenter-list)
    *   [Get Costcenter List](#costcenter-costcenter-list-get)
    *   [Create Costcenter](#costcenter-costcenter-list-post)
*   [Costcenter](#costcenter-costcenter)
    *   [Get Costcenter](#costcenter-costcenter-get)
    *   [Update Costcenter](#costcenter-costcenter-put)
    *   [Delete Costcenter](#costcenter-costcenter-delete)

[Currentuser](#currentuser)

*   [Get Current User](#currentuser-current-user-get)

[Debitor](#debitor)

*   [Debitor List](#debitor-debitor-list)
    *   [Get Debitor List](#debitor-debitor-list-get)
    *   [Create Debitor](#debitor-debitor-list-post)
*   [Debitor](#debitor-debitor)
    *   [Get Debitor](#debitor-debitor-get)
    *   [Update Debitor](#debitor-debitor-put)
    *   [Delete Debitor](#debitor-debitor-delete)

[Debitorcategory](#debitorcategory)

*   [Debitorcategory List](#debitorcategory-debitorcategory-list)
    *   [Get Debitorcategory List](#debitorcategory-debitorcategory-list-get)
    *   [Create Debitorcategory](#debitorcategory-debitorcategory-list-post)
*   [Debitorcategory](#debitorcategory-debitorcategory)
    *   [Get Debitorcategory](#debitorcategory-debitorcategory-get)
    *   [Update Debitorcategory](#debitorcategory-debitorcategory-put)
    *   [Delete Debitorcategory](#debitorcategory-debitorcategory-delete)

[Definitions](#definitions)

*   [Get Definitions](#definitions-definitions-get)

[Document](#document)

*   [Document List](#document-document-list)
    *   [Get Document List](#document-document-list-get)
    *   [Create Document](#document-document-list-post)
*   [Document](#document-document)
    *   [Get Document](#document-document-get)
    *   [Get Header of Document](#document-document-head)
    *   [Update Document](#document-document-put)
    *   [Delete Document](#document-document-delete)
*   [Get Document Content](#document-document-content-get)

[Documentgroup](#documentgroup)

*   [Documentgroup List](#documentgroup-documentgroup-list)
    *   [Get Documentgroup List](#documentgroup-documentgroup-list-get)
    *   [Create Documentgroup](#documentgroup-documentgroup-list-post)
*   [Documentgroup](#documentgroup-documentgroup)
    *   [Get Documentgroup](#documentgroup-documentgroup-get)
    *   [Update Documentgroup](#documentgroup-documentgroup-put)
    *   [Delete Documentgroup](#documentgroup-documentgroup-delete)
*   [Get Documentgroup Archive](#documentgroup-archive-get)

[Entry](#entry)

*   [Entry List](#entry-entry-list)
    *   [Get Entry List](#entry-entry-list-get)
    *   [Create Entry](#entry-entry-list-post)
*   [Entry](#entry-entry)
    *   [Get Entry](#entry-entry-get)
    *   [Get Header of Entry](#entry-entry-head)
    *   [Update Entry](#entry-entry-put)
    *   [Delete Entry](#entry-entry-delete)

[Entrygroup](#entrygroup)

*   [Entrygroup List](#entrygroup-entrygroup-list)
    *   [Get Entrygroup List](#entrygroup-entrygroup-list-get)
    *   [Create Entrygroup](#entrygroup-entrygroup-list-post)
*   [Entrygroup](#entrygroup-entrygroup)
    *   [Get Entrygroup](#entrygroup-entrygroup-get)
    *   [Update Entrygroup](#entrygroup-entrygroup-put)
    *   [Delete Entrygroup](#entrygroup-entrygroup-delete)

[Letter](#letter)

*   [Get Letter List](#letter-letter-list-get)
*   [Letter](#letter-letter)
    *   [Get Letter](#letter-letter-get)
    *   [Delete Letter](#letter-letter-delete)
*   [Create PDF's](#letter-create-pdfs-post)

[Letterpdf](#letterpdf)

*   [Get Letterpdf List](#letterpdf-letterpdf-list-get)
*   [Letterpdf](#letterpdf-letterpdf)
    *   [Get Letterpdf](#letterpdf-letterpdf-get)
    *   [Get Header of Letterpdf](#letterpdf-letterpdf-head)
    *   [Delete Letterpdf](#letterpdf-letterpdf-delete)

[Member](#member)

*   [Member List](#member-member-list)
    *   [List Members](#member-member-list-get)
    *   [Create Member](#member-member-list-post)
*   [Member](#member-member)
    *   [Get Member](#member-member-get)
    *   [Update Member](#member-member-put)
    *   [Delete Member](#member-member-delete)
*   [Images](#member-images)
    *   [Get Member Image](#member-images-get)
    *   [Get Header of Member Image](#member-images-head)
*   [Files](#member-files)
    *   [Get Member File](#member-files-get)
    *   [Get Header of Member File](#member-files-head)

[Membergroup](#membergroup)

*   [Membergroup List](#membergroup-membergroup-list)
    *   [Get Membergroup List](#membergroup-membergroup-list-get)
    *   [Create Membergroup](#membergroup-membergroup-list-post)
*   [Membergroup](#membergroup-membergroup)
    *   [Get Membergroup](#membergroup-membergroup-get)
    *   [Update Membergroup](#membergroup-membergroup-put)
    *   [Delete Membergroup](#membergroup-membergroup-delete)

[Object](#object)

*   [Create Object](#object-object-list-post)
*   [Object](#object-object)
    *   [Get Object](#object-object-get)
    *   [Update Object](#object-object-put)
    *   [Delete Object](#object-object-delete)

[Period](#period)

*   [Period List](#period-period-list)
    *   [Get Period List](#period-period-list-get)
    *   [Create Period](#period-period-list-post)
*   [Period](#period-period)
    *   [Get Period](#period-period-get)
    *   [Update Period](#period-period-put)
    *   [Delete Period](#period-period-delete)

[Periodchain](#periodchain)

*   [Periodchain List](#periodchain-periodchain-list)
    *   [Get Periodchain List](#periodchain-periodchain-list-get)
    *   [Create Periodchain](#periodchain-periodchain-list-post)
*   [Periodchain](#periodchain-periodchain)
    *   [Get Periodchain](#periodchain-periodchain-get)
    *   [Update Periodchain](#periodchain-periodchain-put)
    *   [Delete Periodchain](#periodchain-periodchain-delete)

[Periodgroup](#periodgroup)

*   [Periodgroup List](#periodgroup-periodgroup-list)
    *   [Get Periodgroup List](#periodgroup-periodgroup-list-get)
    *   [Create Periodgroup](#periodgroup-periodgroup-list-post)
*   [Periodgroup](#periodgroup-periodgroup)
    *   [Get Periodgroup](#periodgroup-periodgroup-get)
    *   [Update Periodgroup](#periodgroup-periodgroup-put)
    *   [Delete Periodgroup](#periodgroup-periodgroup-delete)

[Quota](#quota)

*   [Get Quota](#quota-quota-get)
*   [Get Storage Details](#quota-storage-quota-get)

[Settings](#settings)

*   [Settings](#settings-settings)
    *   [Get Settings](#settings-settings-get)
    *   [Update Settings](#settings-settings-put)

[Track Changes / Replicate](#track-changes-replicate)

*   [How it works](#header-how-it-works)
*   [Get changes by time (/changes)](#header-get-changes-by-time-(-changes))
*   [Get changes by revision (/replicate)](#header-get-changes-by-revision-(-replicate))
*   [Example](#header-example)
*   [Get Changes](#track-changes-replicate-get-changes-since-timestamp-get)
*   [Current Revision](#track-changes-replicate-current-revision-get)
*   [Get Changes](#track-changes-replicate-get-changes-after-a-revision-get)

[User](#user)

*   [User List](#user-user-list)
    *   [Get User List](#user-user-list-get)
    *   [Create User](#user-user-list-post)
*   [User](#user-user)
    *   [Get User](#user-user-get)
    *   [Update User](#user-user-put)
    *   [Delete User](#user-user-delete)
*   [Send Onboarding Mail](#user-onboarding-post)

[Usergroup](#usergroup)

*   [Usergroup List](#usergroup-usergroup-list)
    *   [Get Usergroup List](#usergroup-usergroup-list-get)
    *   [Create Usergroup](#usergroup-usergroup-list-post)
*   [Usergroup](#usergroup-usergroup)
    *   [Get Usergroup](#usergroup-usergroup-get)
    *   [Update Usergroup](#usergroup-usergroup-put)
    *   [Delete Usergroup](#usergroup-usergroup-delete)

Webling API
===========

API Information [¶](#api-information)
-------------------------------------

This API lets you interact with your [Webling](http://www.webling.ch) Database.

The API is available at the following URL:

`https://<yourdomain>.webling.ch/api/1/`

See the [Examples](#header-examples) section on how to use the API.

Authentication [¶](#header-authentication)
------------------------------------------

The authentication is done by passing an API-Key. As an Administrator you can generate your API-Key in the Web App (Administration > API).

To authenticate, add the apikey parameter (`/api/1/member?apikey=<your_api_key>`) or add an apikey header (`apikey: <your_api_key>`) to every request.

Response format [¶](#header-response-format)
--------------------------------------------

Response body is in JSON format (except images/files). There are different JSON structures that are being used by the API:

### Objects [¶](#header-objects)

All objects have the following basic structure:

    {
        "type": "objecttype",
        "meta": { 
            "created" => "2018-04-06 01:20:04",
            "lastmodified" => "2017-05-23 11:43:54"
        },
        "readonly": false,
        "properties": {},
        "children": {},
        "parents": [],
        "links": {}
    }

These are the properties you find in the basic object structure:

Property

Description

`type` string

The object type, e.g `member` or `membergroup`

`meta` object

Contains the creation and last modify date of the object. For members it also contains the lat and lng of the address if available.

`readonly` boolean

Is set to `true` if the object is read only for the user, otherwise `false`

`properties` object

Contains all object data (mixed datatypes), see below for a list of datatypes

`children` object

Contains a list of objects with a list of all children, grouped by type. This property is read-only, you can change the parent attribute of the children objects instead.

`parents` array

A list of all parent (IDs). Every object must have at least one parent.

`links` array

A list of all linked objects (IDs).

### Property datatypes [¶](#header-property-datatypes)

Every property in `properties` has a datatype, which is one of the following:

Datatype

Description

`text`

String with a maximum size of 255 characters

`longtext`

String with a maximum size of 2 Gb

`bool`

Boolean value, `true` or `false`.

`enum`

Value out of a list of predefined values.

`multienum`

Array of one or several values out of a list of predefined values. (e.g. `["foo", "bar"]`)

`numeric`

Fixed floating point value with two digits accuracy.

`int`

Integer value

`autoincrement`

Immutable integer value, unique for objects of the same type.

`date`

Date value in the format YYYY-MM-DD (eg 2008-09-17)

`timestamp`

Time and date of the form YYYY-MM-DD hh:mm:ss (eg eg 2008-09-17 16:13:42)

`file`

Contains the metadata of a file, see below

`image`

Contains the metadata of an image, see below

`binary`

Contains the metadata of a binary file, can either be an image or a file, see below

Metadata of a file:

    {
        "href": text, // absolute path to the file data
        "size": int, // size of the file in bytes
        "ext": text, // file extension
        "mime": text, // mime type 
        "timestamp": timestamp // creation date
    }

Metadata of an image:

    {
        "href": text, // absolute path to the image data
        "size": int, // size of the image in bytes
        "ext": text, // file extension
        "mime": text, // mime type 
        "timestamp": timestamp, // creation date
        "dimensions": {
            "width": int, // width in pixels
            "height": int // height in pixels
        }
    }

Metadata of a binary:

    {
        "href": text, // absolute path to the file data
        "size": int, // size of the file in bytes
        "name": text, // filename
        "lastmodified": timestamp, // last modified date
        "hrefthumb": string // link to the preview, if the file has a preview (only if it's an image)
    }

### Lists [¶](#header-lists)

Lists contain object IDs (e.g: a list of member IDs):

    {
        "objects": [12,23,34,45]
    }

### Files [¶](#header-files)

Files, images or binaries are returned as binary data with the appropriate content-type (e.g. image/png, application/xyz)

### Errors [¶](#header-errors)

Errors have the following structure:

    {
        "error": "Error message"
    }

Response Status Codes [¶](#header-response-status-codes)
--------------------------------------------------------

If possible, [HTTP Response Status Codes](https://github.com/for-GET/know-your-http-well/blob/master/status-codes.md) are used:

*   200 OK: Request successful
    
*   201 Created: Resource has been created
    
*   204 No Content: The request was successful, no content is returned
    
*   304 Not Modified: The content has not changed
    
*   400 Bad Request: Invalid parameter passed
    
*   401 Unauthorized: Authentication failed
    
*   403 Forbidden: No permission to perform the request
    
*   404 Not Found: The resource was not found
    
*   413 Request Entity Too Large: try to split your request into multiple requests
    
*   425 Quota Exceeded: The limit of your Webling subscription was reached
    
*   429 Too many requests: your host has sent too many requests and has been blocked for a short period
    
*   500 Server Error: An internal server error occurred
    
*   501 Not Implemented: This call is not yet implemented
    
*   503 Service Unavailable: The server can not handle the request, e.g a deadlock occurred
    

Rate Limit [¶](#header-rate-limit)
----------------------------------

The API currently enforces a rate limit of 500 requests per minute. If you hit the rate limit, you will get an HTTP 429 Error. You can [fetch multiple objects](#header-fetch-multiple-objects) in one call if you get the error code 429. The rate limit may be lowered in the future. Applications should be designed to not send more than 50 requests per minute. You can use caching to reduce the number of requests.

See the section [Track Changes / Replicate](#track-changes-replicate) for more information about how to detect changed data and only update these objects to reduce requests.

Fetch Multiple Objects [¶](#header-fetch-multiple-objects)
----------------------------------------------------------

There are two ways to fetch multiple objects with one request:

### Option 1: multiple IDs in the url [¶](#header-option-1-multiple-ids-in-the-url)

You can request multiple objects with one call (multiget). To do so, concatenate all IDs with a comma:

    /api/1/member/536,525,506,535

This also works for DELETE Requests.

### Option 2: fetch data instead of IDs [¶](#header-option-2-fetch-data-instead-of-ids)

When loading lists like `/member` or `/membergroup` by default you get object IDs only. This is due to the fact that large stores will take a while to return all object data.

If you are dealing with a lot of data, using a caching mechanism is really recommended. See [Replicate](#track-changes-replicate).

You can fetch full data, instead of the IDs only, by appending the `format=full` parameter.

Example:

    /api/1/member?format=full

This will return all member objects (with full data).

You can also combine this with other parameters like `filter` to only load certain members:

    /api/1/member?format=full&filter=$parents.$id=552

This will return all members which are in the membergroup with the id 552.

Pagination [¶](#header-pagination)
----------------------------------

You can limit the number of results with the pagination parameters:

    /api/1/member?page=1&per_page=100
    /api/1/member?format=full&page=4&per_page=10

*   `page`: page number, starting with 1 for the first page
    
*   `per_page`: number of results per page
    

Query Language [¶](#header-query-language)
------------------------------------------

All GET endpoints, which return a list of object IDs, can be filtered using the following query language. A query is passed by the `filter=` parameter.

Example:

    https://demo.webling.ch/api/1/member?filter=`Vorname` = "Hans"&apikey=__YOUR_API_KEY__

Explanation of the query language syntax:

Feature

Example

Objects can be queried by properties (fields)

`` `Name` = "Meier" `` or `` `Betrag` > 100 ``

Properties containing special characters must be enclosed by backticks

`` `Zweiter Name` FILTER "Mei" ``

All properties can be queried by \*

`* = "Müller"`

A value can be searched in several properties. Separate the properties by comma

`` `Name`,`Betrag` = "Müller" ``

A property can be checked if it is empty or not empty

`` `Name` IS EMPTY `` or ``NOT `Betrag` IS EMPTY``

The set expression checks if a property is in a list

`` `Name` IN ("Hans", "Jürg") ``

Multiple conditions can be joined by AND, OR and brackets

``(`Name` = "Meier" OR `Name` = "Müller") AND `Vorname` = "Hans"``

### Special Properties [¶](#header-special-properties)

There are some special properties you can use beside the normal properties:

Special Property

Description

`$parents.<property>`

query a property of a parent

`$ancestors.<property>`

query a property of any ancestor. The ancestors operator is only allowed for members, membergroups, documents and documentgroups (e.g. used for search in subgroups)

`$children.<childtype>.<property>`

query a property of a child

`$links.<category>.<property>`

query a property of a link

`$readonly`, `$writable`

bool value indicating if the object is readonly/writable

`$label`

label of the object (usually the title)

`$id`

id of the object

The backtick is not required for these special properties.

### Operators [¶](#header-operators)

You can use the following comparison operators:

Operator

Description

Example

`<`

less than

`` `PLZ` < 2000 ``

`<=`

less or equal than

`` `PLZ` <= 2000 ``

`>`

greater than

`` `PLZ` > 2000 ``

`>=`

greater or equal than

`` `PLZ` >= 2000 ``

`=`

equal

`` `Name` = "Meier" ``

`!=`

not equal

`` `Name` != "Meier" ``

`FILTER`

matches all strings starting with the argument.

`` `Name` FILTER "Me" `` matches Meier, Mettler, …

`CONTAINS`

searches whole strings for matches (Note: `CONTAINS` is much slower than `FILTER`, use `FILTER` whenever possible).

`` `Name` CONTAINS "an" `` matches Andermatt, Baumann, …

`IS EMPTY`

matches all empty values (`null` and empty string).

`` `E-Mail` IS EMPTY ``

`IN`

matches multiple values

`` `Lizenz` IN ("Junior", "1. Liga") `` matches all members with Lizenz “Junior” or “1. Liga”

`WITH`

links queries of multiple properties in a linked object

`WITH $links.debitor (totalamount > 100 AND title = "Jahresrechnung")` matches only if both conditions are satisfied by the same debitor object

### Functions [¶](#header-functions)

The following functions are available:

Name

Description

`LOWER(<string>)`

converts a text or longtext property to lower case

`TRIM(<string>)`

trims a text or longtext property

`UPPER(<string>)`

converts a text or longtext property to upper case

`DAY(<date>)`

returns the day of a date property

`MONTH(<date>)`

returns the month of a date property

`YEAR(<date>)`

returns the year of a date property

`AGE(<date>)`

returns the age of a date property

`AGETHISYEAR(<date>)`

returns the age the person will reach at the end of this year

`BIRTHDAY(<date>, month, day)`

returns a number which can be used to sort by birthdays after the given day

`TODAY()`

returns the current date

`COUNT(<path>)`

call to order the results by the number of link, children or parents. This call is only available in the order parameter.

### Sort the results [¶](#header-sort-the-results)

The results can be sorted by the `order` parameter, using the following pattern:

    ?order=`Vorname` ASC
    ?order=`Vorname` DESC, `Nachname` ASC

Special properties are also allowed:

    ?order=$label ASC 
    ?order=$parents.title DESC
    ?order=DAY(`Geburtstag`) DESC

### Query Examples [¶](#header-query-examples)

To filter for members, use the filter argument in the URL like this:

    https://demo.webling.ch/api/1/member?filter=`Vorname` = "Hans" OR `Name` = "Weber"&apikey=__YOUR_API_KEY__

Get all members in a specific membergroup (id = 555) and sort them by “Vorname”:

    member?filter=$parents.$id = 555&order=`Vorname` ASC

You can nest AND and OR conditions and use parentheses:

    member?filter=`Vorname` = "Peter" OR (`Vorname` = "Hans" AND `Name` = "Meier" OR (`PLZ` > 100 AND `PLZ` <= 4000))

Get all members that are in one of the membergroups 100, 101 or 102:

    member?filter=$parents.$id = 100 OR $parents.$id = 101 OR $parents.$id = 102
    member?filter=$parents.$id IN (100, 101, 102)

Get all members that are in a membergroup with the title “Vorstand”:

    member?filter=$parents.title = "Vorstand"

Get all members that are not in the membergroup with the id 100:

    member?filter=NOT($parents.$id = 100)

Use IN to search for multiple values:

    member?filter=`ID` IN (22, 45, 67)
    member?filter=`Status` IN ("Aktiv", "Passiv", "Ehrenmitglied")
    member?filter=$parents.$id IN (520, 612, 802, 1023)
    member?filter=NOT($parents.$id IN (438, 748, 893))

Get all members, where the field “E-Mail” equals the field “E-Mail Geschäft”:

    member?filter=`E-Mail` = `E-Mail Geschäft`
    

Get all members with an empty E-Mail field:

    member?filter=`E-Mail` IS EMPTY

Get all members where the E-Mail field is not empty:

    member?filter=NOT(`E-Mail` IS EMPTY)
    member?filter=NOT `E-Mail` IS EMPTY

Filter by Age (years):

    member?filter=AGE(`Geburtstag`) = 22
    member?filter=AGE(`Eintrittsdatum`) > 5

Use of the UPPER function to match case-insensitive:

    member?filter=UPPER(`Name`) = "MEIER"

Find all members with birthday in August:

    member?filter=MONTH(`Geburtstag`) = 8

You can also sort the results by day:

    member?filter=MONTH(`Geburtstag`) = 8&sort=DAY(`Geburtstag`) ASC

Find all members with birthday after August 20th:

    member?filter=MONTH(`Geburtstag`) > 8 OR (MONTH(`Geburtstag`) = 8 AND DAY(`Geburtstag`) > 20)

Search for dates relative to today (all future dates):

    member?filter=`Eintrittsdatum` > TODAY()

Comparing dates:

    member?filter=`Eintrittsdatum` <= "2018-06-23"
    member?filter=`Eintrittsdatum` = "2018-03-06"

Use of multienum operators:

    member?filter=`Mehrfachauswahlfeld` IS ["Wert"]
    member?filter=`Mehrfachauswahlfeld` CONTAINS ALL OF ["Wert", "Wert 1"]
    member?filter=`Mehrfachauswahlfeld` CONTAINS NONE OF ["Wert 1", "Wert 2"]
    member?filter=`Mehrfachauswahlfeld` CONTAINS ANY OF ["Wert 2"]

Get the member that is linked to the debitor with the id 851:

    member?filter=$links.debitor.$id=851

Get all members with open debitors:

    member?filter=$links.debitor.state="open"

Get all members with a debitor of amount 100:

    member?filter=$links.debitor.$links.revenue.amount = 100

Find all members with comments:

    member?filter=$links.comment.$id > 0

Combine $links and $children to find all entrygroups that have links to a debitor with the $label “Meier”:

    entrygroup?filter=$children.entry.$links.debitor.$links.member.$label filter "Meier"

Get all membergroups that have members with a PLZ over 9000:

    membergroup?filter=$children.member.PLZ > 9000

Search in group and subgroups of membergroup 550:

    member?filter=`Vorname` = "Tim" AND $ancestors.$id = 550

Get all members you have write access to:

    member?filter=$writable=true

#### WITH() operator [¶](#header-with()-operator)

> Using multiple filters in linked objects may lead to unexpected results, since the conditions are executed separately.
> 
>     member?filter=$links.debitor.totalamount > 100 AND $links.debitor.remainingamount > 0
> 
> Will give you all members that have a debitor with totalamount > 100 and a _different_ debitor with remainingamount > 0.  
> If you want to filter by multiple properties of a linked object, use the `WITH` operator:
> 
>     member?filter=WITH $links.debitor (totalamount > 100 AND remainingamount > 0)
> 
> This will find members with a debitor over 100, which are not yet paid in full.

Don’t forget to [encode the URL](http://www.url-encode-decode.com) if you are using special chars in your query.

### EBNF [¶](#header-ebnf)

If you want to dig deeper, this is the formal definition of the query language:

    start                   ::= orExpr
    
    orExpr                  ::= andExpr "OR" orExpr
    andExpr                 ::= notExpr "AND" orExpr
    notExpr                 ::= "NOT"? withExpr
    withExpr                ::= ( "WITH" axisExpr ( "." axisExpr )* )? bracketExpr
    bracketExpr             ::= ( "(" orExpr ")" ) | atomExpr
    
    atomExpr                ::= comparisonExpr | filterComparisonExpr | containsComparisonExpr | multienumComparisonExpr | emptyExpr | setExpr
    comparisonExpr          ::= contentExpr universalOpExpr contentExpr
    filterComparisonExpr    ::= contentExpr "FILTER" valueExpr
    containsComparisonExpr  ::= contentExpr "CONTAINS" stringExpr
    multienumComparisonExpr ::= contentExpr multienumOpExpr jsonStringArrayExpr
    emptyExpr               ::= contentExpr "IS" "EMPTY"
    setExpr                 ::= contentExpr "IN" "(" valueExpr ("," valueExpr)* ")"
    
    universalOpExpr         ::= "<" | "<=" | ">" | ">=" | "=" | "!="
    multienumOpExpr         ::= "CONTAINS ALL OF" | "IS" | "CONTAINS NONE OF" | "CONTAINS ANY OF"
    
    contentExpr             ::= valueExpr | jsonPathExpr | callExpr | pathExpr
    valueExpr               ::= stringExpr | numberExpr | boolExpr
    callExpr                ::= literalExpr "(" (contentExpr ("," contentExpr)* )? ")"
    pathExpr                ::= propertiesExpr | accessExpr | labelExpr | idExpr | ( axisExpr "." pathExpr )
    propertiesExpr          ::= "*" | ( propertyExpr ("," propertyExpr)* )
    propertyExpr            ::= literalExpr | backtickExpr
    jsonPathExpr            ::= "JSON" ( pathExpr ) ( "[" ( stringExpr | intExpr ) "]" )*
    axisExpr                ::= parentExpr | ancestorExpr | childExpr | linkExpr | reverseLinkExpr
    parentExpr              ::= "$parents"
    ancestorExpr            ::= "$ancestors"
    childExpr               ::= "$children" "." literalExpr
    linkExpr                ::= "$links" "." literalExpr
    reverseLinkExpr         ::= "$reverselinks" "." literalExpr ( "{" literalExpr "}" )? "." pathExpr
    axisExpr                ::= parentExpr | ancestorExpr | childExpr | linkExpr | reverseLinkExpr
    parentExpr              ::= "$parents"
    ancestorExpr            ::= "$ancestors"
    childExpr               ::= "$children" "." literalExpr
    linkExpr                ::= "$links" "." literalExpr
    reverseLinkExpr         ::= "$reverselinks" "." literalExpr
    
    accessExpr              ::= "$readonly" | "$writable"
    labelExpr               ::= "$label"
    idExpr                  ::= "$id"
    
    stringExpr              ::= ("'" /[^"]* / "'") | ('"' /[^']* / '"')
    backtickExpr            ::= "`" /[^`]* / "`"
    literalExpr             ::= /\w* /
    boolExpr                ::= "TRUE" | "FALSE"
    intExpr                 ::= "-"? /\d+/
    numberExpr              ::= "-"? /\d+/ ( "." /\d* / )?
    jsonStringArrayExpr     ::= "[" stringExpr ( "," stringExpr )* "]"
    

Examples [¶](#header-examples)
------------------------------

Some simple examples how to use the API.

More examples can be found on our GitHub page: [github.com/usystems/webling-api-examples](https://github.com/usystems/webling-api-examples)

### PHP [¶](#header-php)

This is a simple example to get the title of a Membergroup in PHP:

    $apiurl = "https://demo.webling.ch";
    $apikey = "<your_api_key>";
    
    $url = $apiurl . "/api/1/membergroup/1?apikey=" . $apikey;
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $data = json_decode(curl_exec($curl), true);
    echo $data["properties"]["title"];

This is a simple example that shows how to create a new member in PHP:

    $apiurl = "https://demo.webling.ch";
    $apikey = "<your_api_key>";
    
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_POST, 1);
    curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode(array(
        "properties" => array(
            "Vorname" => "Fritz",
            "Name" => "Meier",
            "E-Mail" => "fritz.meier@example.ch"
        ),
        // ID of the membergroup where the member should be added, replace with your own ID
        "parents" => array(550)
    )));
    curl_setopt($curl, CURLOPT_URL, $apiurl . "/api/1/member?apikey=" . $apikey);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($curl);
    $code = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    if ($code != 201) {
        echo 'Error: '. $response . ' HTTP-Status Code: '.$code;
    } else {
        echo 'Creation successful. ID of new member: '.$response;
    }

### JavaScript [¶](#header-javascript)

This is a simple example to get the title of a Membergroup in JavaScript:

**WARNING:** Don’t use this example in production, as the Apikey is exposed to the user!

    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
        <script>
            var apiurl = "https://demo.webling.ch";
            var apikey = "<your_api_key>";
            $(function(){
                $.ajax(apiurl + "/api/1/membergroup/1?apikey=" + apikey).then(
                    function(data) {
                        $('#title').html(data.properties.title)
                    },
                    function(jqXHR, textStatus, errorThrown) {
                        console.error(jqXHR, textStatus, errorThrown);
                    }
                );
            })
        </script>
    </head>
    <body>
        <div id="title"></div>
    </body>
    </html>

Development Resources [¶](#header-development-resources)
--------------------------------------------------------

Some resources that may be helpful during development.

### API Browser [¶](#header-api-browser)

Easily browse the API with our [API Browser](/browser). It’s an easy way to find objects and their id’s.

### PHP Webling Client [¶](#header-php-webling-client)

A lightweight Webling API wrapper: [github.com/usystems/webling-api-php](https://github.com/usystems/webling-api-php)

Install this [package](https://packagist.org/packages/usystems/webling-api-php) with [Composer](https://getcomposer.org/):

    composer require usystems/webling-api-php

The library simplifies Webling API requests:

    $api = new Webling\API\Client('https://demo.webling.ch','MY_APIKEY')
    $response = $api->get('member/123')

See the [GitHub page](https://github.com/usystems/webling-api-php) for more information.

### Code Examples [¶](#header-code-examples)

Some code examples that use the API: [github.com/usystems/webling-api-examples](https://github.com/usystems/webling-api-examples)

### Symfony Bundle [¶](#header-symfony-bundle)

A third-party Symfony 2 Bundle, made by Terminal42: [github.com/terminal42/webling-bundle](https://github.com/terminal42/webling-bundle)

### WordPress Plugin [¶](#header-wordpress-plugin)

A [WordPress Plugin](https://wordpress.org/plugins/webling/) to create member lists and registration forms.

Newsletter [¶](#header-newsletter)
----------------------------------

We have an API newsletter to notify users about changes. [Sign up here](http://eepurl.com/cxT6Fn)

Changelog [¶](#header-changelog)
--------------------------------

Breaking Changes are listed here.

**Release 08-2025**

In anticipation of the upcoming VAT and split-entry integration, the following changes have been made to entries and entrygroups:

*   Moved property `entryid` from `/entry` to `/entrygroup`
    
*   Moved property `receipt` from `/entry` to `/entrygroup`
    
*   Moved property `receiptfile` from `/entry` to `/entrygroup`
    
*   Moved property `isEBill` from `/entry` to `/entrygroup`
    

> **Temporary:** The moved properties are currently still available in `/entry` as a transparent read/write proxy object, but will be removed in future release.

**Release 08-2022**

*   Fix: Empty objects of links, children and definitions now return an empty object `{}` instead of an empty array `[]`

**Release 11-2021**

*   `/debitor`: added `date` property which is now used as the general invoice date.

**Release 03-2021**

Debitors can now have multiple revenues (Rechnungsposten).

*   `/debitor`: added `title` property which is now used as the general invoice title
    
*   `/debitor`: added `invoiceitems` property to store the order of invoice items
    

**Release 01-2021**

Debitors can now be written off (ausbuchen).

*   `/debitor`: added a third split `writeoff` for the writeoff entries
    
*   `/debitor`: added `writeoffamount` with the written off amount of the debitor
    

**Release 12-2020**

The object `costcentertemplate` has been removed, as it was never used in the Webling UI.

**Release 11-2019**

Debitorcategories are now children of the periodgroup.

This means: debitorcategories are available in all periods of the periodgroup and do not need to be created if a new period is created. The structure of the following endpoints are affected:

*   `/debitorcategory`: the parents of the debitorcategories are now periodgroups
    
*   `/period`: the period no longer has children of the type debitorcategory
    
*   `/periodgroup`: the periodgroup now has children of the type debitorcategory
    

**Release 07-2017**

*   Website features are removed from the API by default. They are only present if the website is enabled.
    *   `/apikey` and `/user`: property `webaccess` removed
    *   `/quota`: property `web` removed

**Release 06-2017**

*   Document contents URL has changed. Old: `/document/{id}/{filename}.{extension}` New: `/document/{id}/file/{filename}.{extension}`
    
*   Some changes to the search Query Language:
    
    *   The filter query param is now `?filter=<your_query>` instead of `?query=<your_query>`
    *   Most EBNF features are now supported
    *   Global `"NOT"` Operator introduced. The old syntax `"IS NOT"` and `"NOT LIKE"` and `"NOT IN"` is not supported anymore
    *   Operator `"START WITH"` has been removed, use `"FILTER"` instead
    *   Properties containing special characters must now be enclosed by backticks instead of quotes. Old: `"Zweiter Name" = "Meier"` New: `` `Zweiter Name` = "Meier" ``
    *   Properties can now be used on the left and the right side of a comparison. Example: `` `Vorname` = `Nachname` ``
    *   The special property `$type` has been removed
*   Changed and improved the sorting options. Old query params were `?sort=Vorname&direction=ASC`, the new param is `?order=Vorname ASC, Nachname DESC`. Multiple sort fields are now possible.
    
*   The unofficial finance endpoints have changed due to a large internal refactoring
    

Account [¶](#account)
---------------------

An account is a finance item (Konto) and is always a child of an accountgroup. An account has links to all entries and entrygroups that are connected to this account.

A link to an [accounttemplate](#accounttemplate) is required.

`amount` is a computed property and cannot be changed.

`budget` can only be set for expense and income accounts

`openingentry` can only be set for assets and liabilitys accounts

### Account List  [¶](#account-account-list)

#### 

Get Account List

[GET](#account-account-list-get)`/account{?filter,order,format}`

Lists all available account IDs

#### Example URI

GET /account?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the account list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        99,
        116,
        206
      ]
    }

#### 

Create Account

[POST](#account-account-list-post)`/account`

Create an account

Returns the ID of the newly created account.

#### Example URI

POST /account

**Request**

HideShow

##### Body

    {
      "type": "account",
      "readonly": false,
      "properties": {
        "title": "Bank",
        "openingentry": 6000
      },
      "children": {},
      "links": {
        "accounttemplate": [
          4117
        ]
      },
      "parents": [
        96
      ]
    }

**Response  `201`**

HideShow

##### Body

    18010

### Account  [¶](#account-account)

#### 

Get Account

[GET](#account-account-get)`/account/{id}`

Get an account

#### Example URI

GET /account/99

**URI Parameters**

HideShow

id

`number` (required) **Example:** 99

Account ID

**Response  `200`**

HideShow

JSON Representation of the Account.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "account",
      "readonly": false,
      "properties": {
        "amount": 5920,
        "title": "Bank",
        "budget": null,
        "openingentry": 6000
      },
      "children": {},
      "links": {
        "entry": [
          179
        ],
        "entrygroup": [
          2718
        ],
        "accounttemplate": [
          4117
        ]
      },
      "parents": [
        96
      ]
    }

#### 

Update Account

[PUT](#account-account-put)`/account/{id}`

Update an account

#### Example URI

PUT /account/99

**URI Parameters**

HideShow

id

`number` (required) **Example:** 99

Account ID

**Request**

HideShow

##### Body

    {
      "type": "account",
      "readonly": false,
      "properties": {
        "amount": 5920,
        "title": "Bank",
        "budget": null,
        "openingentry": 6000
      },
      "links": {},
      "parents": [
        96
      ]
    }

**Response  `204`**

#### 

Delete Account

[DELETE](#account-account-delete)`/account/{id}`

Delete an account

#### Example URI

DELETE /account/99

**URI Parameters**

HideShow

id

`number` (required) **Example:** 99

Account ID

**Response  `204`**

Accountgroup [¶](#accountgroup)
-------------------------------

An accountgroup is a finance item group (Kontengruppe) and is always a child of a period. An accountgroup has a link to the accountgrouptemplate, for linking accountgroups in different periods together. Children of an accountgroup are accounts.

A link to an [accountgrouptemplate](#accountgrouptemplate) is required.

`type` specifies to which group it belongs. It can be one `expense`, `income`, `assets` or `liabilitys`

### Accountgroup List  [¶](#accountgroup-accountgroup-list)

#### 

Get Accountgroup List

[GET](#accountgroup-accountgroup-list-get)`/accountgroup{?filter,order,format}`

Lists all available accountgroup IDs

#### Example URI

GET /accountgroup?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the accountgroup list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        187,
        195,
        197
      ]
    }

#### 

Create Accountgroup

[POST](#accountgroup-accountgroup-list-post)`/accountgroup`

Create an accountgroup

Returns the ID of the newly created accountgroup.

#### Example URI

POST /accountgroup

**Request**

HideShow

##### Body

    {
      "type": "accountgroup",
      "readonly": false,
      "properties": {
        "title": "Eigenkapital",
        "type": "liabilitys"
      },
      "links": {
        "accountgrouptemplate": [
          4152
        ]
      },
      "parents": [
        2230
      ]
    }

**Response  `201`**

HideShow

##### Body

    18010

### Accountgroup  [¶](#accountgroup-accountgroup)

#### 

Get Accountgroup

[GET](#accountgroup-accountgroup-get)`/accountgroup/{id}`

Get an accountgroup

#### Example URI

GET /accountgroup/2243

**URI Parameters**

HideShow

id

`number` (required) **Example:** 2243

Accountgroup ID

**Response  `200`**

HideShow

JSON Representation of the Accountgroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "accountgroup",
      "readonly": false,
      "properties": {
        "title": "Eigenkapital",
        "type": "liabilitys"
      },
      "children": {
        "account": [
          2244,
          2245
        ]
      },
      "links": {
        "accountgrouptemplate": [
          4152
        ]
      },
      "parents": [
        2230
      ]
    }

#### 

Update Accountgroup

[PUT](#accountgroup-accountgroup-put)`/accountgroup/{id}`

Update an accountgroup

#### Example URI

PUT /accountgroup/2243

**URI Parameters**

HideShow

id

`number` (required) **Example:** 2243

Accountgroup ID

**Request**

HideShow

JSON Representation of the Accountgroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "accountgroup",
      "readonly": false,
      "properties": {
        "title": "Eigenkapital",
        "type": "liabilitys"
      },
      "children": {
        "account": [
          2244,
          2245
        ]
      },
      "links": {
        "accountgrouptemplate": [
          4152
        ]
      },
      "parents": [
        2230
      ]
    }

**Response  `204`**

#### 

Delete Accountgroup

[DELETE](#accountgroup-accountgroup-delete)`/accountgroup/{id}`

Delete an accountgroup

#### Example URI

DELETE /accountgroup/2243

**URI Parameters**

HideShow

id

`number` (required) **Example:** 2243

Accountgroup ID

**Response  `204`**

Accountgrouptemplate [¶](#accountgrouptemplate)
-----------------------------------------------

An accountgrouptemplate is a finance item (Kontengruppenvorlage) and is always a child of a periodchain. It serves as a link between accountgroups in different periods. Accountgrouptemplates are used to determine a corresponding accountgroup in a following/previous period. The children of an accountgrouptemplate are accounttemplates, that serve a similar purpose but for accounts.

### Accountgrouptemplate List  [¶](#accountgrouptemplate-accountgrouptemplate-list)

#### 

Get Accountgrouptemplate List

[GET](#accountgrouptemplate-accountgrouptemplate-list-get)`/accountgrouptemplate{?filter,order,format}`

Lists all available accountgrouptemplate IDs

#### Example URI

GET /accountgrouptemplate?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the accountgrouptemplate list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        4133,
        4152
      ]
    }

#### 

Create Accountgrouptemplate

[POST](#accountgrouptemplate-accountgrouptemplate-list-post)`/accountgrouptemplate`

Create an accountgrouptemplate

Returns the ID of the newly created accountgrouptemplate.

#### Example URI

POST /accountgrouptemplate

**Request**

HideShow

##### Body

    {
      "type": "accountgrouptemplate",
      "readonly": false,
      "properties": {
        "title": "Eigenkapital",
        "type": "liabilitys"
      },
      "children": {},
      "links": {},
      "parents": [
        4126
      ]
    }

**Response  `201`**

HideShow

##### Body

    18010

### Accountgrouptemplate  [¶](#accountgrouptemplate-accountgrouptemplate)

#### 

Get Accountgrouptemplate

[GET](#accountgrouptemplate-accountgrouptemplate-get)`/accountgrouptemplate/{id}`

Get an accountgrouptemplate

#### Example URI

GET /accountgrouptemplate/4152

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4152

Accountgrouptemplate ID

**Response  `200`**

HideShow

JSON Representation of the Accountgrouptemplate.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "accountgrouptemplate",
      "readonly": false,
      "properties": {
        "title": "Eigenkapital",
        "type": "liabilitys"
      },
      "children": {
        "accounttemplate": [
          4153,
          4154
        ]
      },
      "links": {
        "accountgroup": [
          197,
          814,
          2243
        ]
      },
      "parents": [
        4126
      ]
    }

#### 

Update Accountgrouptemplate

[PUT](#accountgrouptemplate-accountgrouptemplate-put)`/accountgrouptemplate/{id}`

Update an accountgrouptemplate

#### Example URI

PUT /accountgrouptemplate/4152

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4152

Accountgrouptemplate ID

**Request**

HideShow

JSON Representation of the Accountgrouptemplate.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "accountgrouptemplate",
      "readonly": false,
      "properties": {
        "title": "Eigenkapital",
        "type": "liabilitys"
      },
      "children": {
        "accounttemplate": [
          4153,
          4154
        ]
      },
      "links": {
        "accountgroup": [
          197,
          814,
          2243
        ]
      },
      "parents": [
        4126
      ]
    }

**Response  `204`**

#### 

Delete Accountgrouptemplate

[DELETE](#accountgrouptemplate-accountgrouptemplate-delete)`/accountgrouptemplate/{id}`

Delete an accountgrouptemplate

#### Example URI

DELETE /accountgrouptemplate/4152

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4152

Accountgrouptemplate ID

**Response  `204`**

Accounttemplate [¶](#accounttemplate)
-------------------------------------

An accounttemplate is a finance item (Kontenvorlage) and is always a child of an accountgrouptemplate. It serves as a link between accounts in different periods. Accounttemplates are used to determine a corresponding account in a following/previous period.

### Accounttemplate List  [¶](#accounttemplate-accounttemplate-list)

#### 

Get Accounttemplate List

[GET](#accounttemplate-accounttemplate-list-get)`/accounttemplate{?filter,order,format}`

Lists all available accounttemplate IDs

#### Example URI

GET /accounttemplate?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the accounttemplate list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        4007,
        4023
      ]
    }

#### 

Create Accounttemplate

[POST](#accounttemplate-accounttemplate-list-post)`/accounttemplate`

Create an accounttemplate

Returns the id of the newly created accounttemplate.

#### Example URI

POST /accounttemplate

**Request**

HideShow

##### Body

    {
      "type": "accounttemplate",
      "readonly": false,
      "properties": {
        "title": "Kasse"
      },
      "children": {},
      "links": {
        "account": [
          3603,
          3658,
          3722
        ]
      },
      "parents": [
        4022
      ]
    }

**Response  `201`**

HideShow

##### Body

    18010

### Accounttemplate  [¶](#accounttemplate-accounttemplate)

#### 

Get Accounttemplate

[GET](#accounttemplate-accounttemplate-get)`/accounttemplate/{id}`

Get an accounttemplate

#### Example URI

GET /accounttemplate/4023

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4023

Accounttemplate ID

**Response  `200`**

HideShow

JSON Representation of the Accounttemplate.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "accounttemplate",
      "readonly": false,
      "properties": {
        "title": "Kasse"
      },
      "children": {},
      "links": {
        "account": [
          3603,
          3658,
          3722
        ]
      },
      "parents": [
        4022
      ]
    }

#### 

Update Accounttemplate

[PUT](#accounttemplate-accounttemplate-put)`/accounttemplate/{id}`

Update an accounttemplate

#### Example URI

PUT /accounttemplate/4023

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4023

Accounttemplate ID

**Request**

HideShow

JSON Representation of the Accounttemplate.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "accounttemplate",
      "readonly": false,
      "properties": {
        "title": "Kasse"
      },
      "children": {},
      "links": {
        "account": [
          3603,
          3658,
          3722
        ]
      },
      "parents": [
        4022
      ]
    }

**Response  `204`**

#### 

Delete Accounttemplate

[DELETE](#accounttemplate-accounttemplate-delete)`/accounttemplate/{id}`

Delete an accounttemplate

#### Example URI

DELETE /accounttemplate/4023

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4023

Accounttemplate ID

**Response  `204`**

Apikey [¶](#apikey)
-------------------

Only administrators have access to the `/apikey` endpoints.

### Apikey List  [¶](#apikey-apikey-list)

#### 

Get Apikey List

[GET](#apikey-apikey-list-get)`/apikey{?filter,order,format}`

Lists all available apikey IDs.

#### Example URI

GET /apikey?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the apikey list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        1812,
        1791,
        1793,
        1789
      ]
    }

#### 

Create Apikey

[POST](#apikey-apikey-list-post)`/apikey`

Create an apikey

Returns the ID of the newly created apikey.

#### Example URI

POST /apikey

**Request**

HideShow

JSON Representation of the Apikey.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "apikey",
      "readonly": false,
      "properties": {
        "title": "Api Key",
        "custommemberaccess": {
          "552": "+r",
          "555": "+r+w",
          "558": "+r"
        },
        "customfinanceaccess": {
          "800": "+r+w",
          "1814": "+r"
        },
        "memberaccess": "custom",
        "financeaccess": "custom",
        "articleaccess": "none",
        "administrator": false
      },
      "children": {},
      "parents": [],
      "links": {}
    }

**Response  `201`**

HideShow

##### Body

    1793

### Apikey  [¶](#apikey-apikey)

#### 

Get Apikey

[GET](#apikey-apikey-get)`/apikey/{id}`

Get an apikey

#### Example URI

GET /apikey/1793

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1793

Apikey ID

**Response  `200`**

HideShow

JSON Representation of the Apikey.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "apikey",
      "readonly": false,
      "properties": {
        "title": "Api Key",
        "custommemberaccess": {
          "552": "+r",
          "555": "+r+w",
          "558": "+r"
        },
        "customfinanceaccess": {
          "800": "+r+w",
          "1814": "+r"
        },
        "memberaccess": "custom",
        "financeaccess": "custom",
        "articleaccess": "none",
        "administrator": false
      },
      "children": {},
      "parents": [],
      "links": {}
    }

#### 

Update Apikey

[PUT](#apikey-apikey-put)`/apikey/{id}`

Update an apikey

#### Example URI

PUT /apikey/1793

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1793

Apikey ID

**Request**

HideShow

JSON Representation of the Apikey.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "apikey",
      "readonly": false,
      "properties": {
        "title": "Api Key",
        "custommemberaccess": {
          "552": "+r",
          "555": "+r+w",
          "558": "+r"
        },
        "customfinanceaccess": {
          "800": "+r+w",
          "1814": "+r"
        },
        "memberaccess": "custom",
        "financeaccess": "custom",
        "articleaccess": "none",
        "administrator": false
      },
      "children": {},
      "parents": [],
      "links": {}
    }

**Response  `204`**

#### 

Delete Apikey

[DELETE](#apikey-apikey-delete)`/apikey/{id}`

Delete an apikey

#### Example URI

DELETE /apikey/1793

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1793

Apikey ID

**Response  `204`**

### Last used  [¶](#apikey-last-used)

#### 

Apikey last used

[GET](#apikey-last-used-get)`/apikey/{id}/lastused`

Get info when an apikey was used the last time.

#### Example URI

GET /apikey/1791/lastused

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1791

Apikey ID

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "timestamp": "2015-12-28 11:39:42",
      "ip": "192.168.19.1"
    }

Article [¶](#article)
---------------------

An article is a material item and is always a child of an articlegroup.

### Article List  [¶](#article-article-list)

#### 

Get Article List

[GET](#article-article-list-get)`/article{?filter,order,format}`

Lists all available article IDs

#### Example URI

GET /article?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the article list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        64,
        65,
        66
      ]
    }

#### 

Create Article

[POST](#article-article-list-post)`/article`

Create an article

Returns the ID of the newly created article.

#### Example URI

POST /article

**Request**

HideShow

JSON Representation of the Article.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "article",
      "readonly": false,
      "properties": {
        "description": "1 Defekt",
        "title": "Freistossdummies",
        "place": "Materiallager",
        "price": 0,
        "quantity": 4
      },
      "children": {},
      "parents": [
        56
      ],
      "links": {}
    }

**Response  `201`**

HideShow

##### Body

    18010

### Article  [¶](#article-article)

#### 

Get Article

[GET](#article-article-get)`/article/{id}`

Get an article

#### Example URI

GET /article/66

**URI Parameters**

HideShow

id

`number` (required) **Example:** 66

Article ID

**Response  `200`**

HideShow

JSON Representation of the Article.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "article",
      "readonly": false,
      "properties": {
        "description": "1 Defekt",
        "title": "Freistossdummies",
        "place": "Materiallager",
        "price": 0,
        "quantity": 4
      },
      "children": {},
      "parents": [
        56
      ],
      "links": {}
    }

#### 

Update Article

[PUT](#article-article-put)`/article/{id}`

Update an article

#### Example URI

PUT /article/66

**URI Parameters**

HideShow

id

`number` (required) **Example:** 66

Article ID

**Request**

HideShow

JSON Representation of the Article.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "article",
      "readonly": false,
      "properties": {
        "description": "1 Defekt",
        "title": "Freistossdummies",
        "place": "Materiallager",
        "price": 0,
        "quantity": 4
      },
      "children": {},
      "parents": [
        56
      ],
      "links": {}
    }

**Response  `204`**

#### 

Delete Article

[DELETE](#article-article-delete)`/article/{id}`

Delete an article

#### Example URI

DELETE /article/66

**URI Parameters**

HideShow

id

`number` (required) **Example:** 66

Article ID

**Response  `204`**

Articlegroup [¶](#articlegroup)
-------------------------------

An articlegroup contains articles.

Articlegroups are also known as “Rubriken”.

### Articlegroup List  [¶](#articlegroup-articlegroup-list)

#### 

Get Articlegroup List

[GET](#articlegroup-articlegroup-list-get)`/articlegroup{?filter,order,format}`

Lists all available articlegroup IDs.

#### Example URI

GET /articlegroup?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the articlegroup list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        56,
        57
      ]
    }

#### 

Create Articlegroup

[POST](#articlegroup-articlegroup-list-post)`/articlegroup`

Create an articlegroup

Returns the ID of the newly created group.

#### Example URI

POST /articlegroup

**Request**

HideShow

JSON Representation of the Articlegroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "articlegroup",
      "readonly": false,
      "properties": {
        "title": "Artikel"
      },
      "children": {
        "article": [
          65
        ]
      },
      "parents": [],
      "links": {}
    }

**Response  `201`**

HideShow

##### Body

    1809

### Articlegroup  [¶](#articlegroup-articlegroup)

#### 

Get Articlegroup

[GET](#articlegroup-articlegroup-get)`/articlegroup/{id}`

Get an articlegroup

#### Example URI

GET /articlegroup/56

**URI Parameters**

HideShow

id

`number` (required) **Example:** 56

Articlegroup ID

**Response  `200`**

HideShow

JSON Representation of the Articlegroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "articlegroup",
      "readonly": false,
      "properties": {
        "title": "Artikel"
      },
      "children": {
        "article": [
          65
        ]
      },
      "parents": [],
      "links": {}
    }

#### 

Update Articlegroup

[PUT](#articlegroup-articlegroup-put)`/articlegroup/{id}`

Update an articlegroup

#### Example URI

PUT /articlegroup/56

**URI Parameters**

HideShow

id

`number` (required) **Example:** 56

Articlegroup ID

**Request**

HideShow

JSON Representation of the Articlegroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "articlegroup",
      "readonly": false,
      "properties": {
        "title": "Artikel"
      },
      "children": {
        "article": [
          65
        ]
      },
      "parents": [],
      "links": {}
    }

**Response  `204`**

#### 

Delete Articlegroup

[DELETE](#articlegroup-articlegroup-delete)`/articlegroup/{id}`

Delete an articlegroup

#### Example URI

DELETE /articlegroup/56

**URI Parameters**

HideShow

id

`number` (required) **Example:** 56

Articlegroup ID

**Response  `204`**

Config [¶](#config)
-------------------

### Config  [¶](#config-config)

#### 

Get Config Values

[GET](#config-config-get)`/config`

Returns the config values for the current webling store. These are the same for every user.

#### Example URI

GET /config

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "name": "Demo Verein",
      "domain": "demo",
      "language": "de",
      "defaultSmsSender": "webling.ch",
      "userImageEnabled": true,
      "cardDavEnabled": true,
      "apiEnabled": true,
      "emailEnabled": true,
      "smsEnabled": true,
      "sepaEnabled": true
    }

Costcenter [¶](#costcenter)
---------------------------

Costcenters can be used to categorize [entries](#entry). Entries can be linked to a costcenter. Costcenters are children of a period.

### Costcenter List  [¶](#costcenter-costcenter-list)

#### 

Get Costcenter List

[GET](#costcenter-costcenter-list-get)`/costcenter{?filter,order,format}`

Lists all available costcenter IDs.

#### Example URI

GET /costcenter?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the costcenter list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        1098,
        1864
      ]
    }

#### 

Create Costcenter

[POST](#costcenter-costcenter-list-post)`/costcenter`

Create a costcenter

Returns the id of the newly created costcenter.

#### Example URI

POST /costcenter

**Request**

HideShow

JSON Representation of the Costcenter.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "costcenter",
      "readonly": false,
      "properties": {
        "title": "Spielbetrieb"
      },
      "children": {},
      "links": {
        "entry": [
          3593
        ]
      },
      "parents": [
        2309
      ]
    }

**Response  `201`**

HideShow

##### Body

    1809

### Costcenter  [¶](#costcenter-costcenter)

#### 

Get Costcenter

[GET](#costcenter-costcenter-get)`/costcenter/{id}`

Get a costcenter

#### Example URI

GET /costcenter/3598

**URI Parameters**

HideShow

id

`number` (required) **Example:** 3598

Costcenter ID

**Response  `200`**

HideShow

JSON Representation of the Costcenter.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "costcenter",
      "readonly": false,
      "properties": {
        "title": "Spielbetrieb"
      },
      "children": {},
      "links": {
        "entry": [
          3593
        ]
      },
      "parents": [
        2309
      ]
    }

#### 

Update Costcenter

[PUT](#costcenter-costcenter-put)`/costcenter/{id}`

Update a costcenter

#### Example URI

PUT /costcenter/3598

**URI Parameters**

HideShow

id

`number` (required) **Example:** 3598

Costcenter ID

**Request**

HideShow

JSON Representation of the Costcenter.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "costcenter",
      "readonly": false,
      "properties": {
        "title": "Spielbetrieb"
      },
      "children": {},
      "links": {
        "entry": [
          3593
        ]
      },
      "parents": [
        2309
      ]
    }

**Response  `204`**

#### 

Delete Costcenter

[DELETE](#costcenter-costcenter-delete)`/costcenter/{id}`

Delete a costcenter

#### Example URI

DELETE /costcenter/3598

**URI Parameters**

HideShow

id

`number` (required) **Example:** 3598

Costcenter ID

**Response  `204`**

Currentuser [¶](#currentuser)
-----------------------------

### Current User  [¶](#currentuser-current-user)

#### 

Get Current User

[GET](#currentuser-current-user-get)`/currentuser`

Returns id and name of the currently logged-in user or apikey.

#### Example URI

GET /currentuser

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "id": 1789,
      "name": "Api-Test Key"
    }

Debitor [¶](#debitor)
---------------------

A debitor is an invoice (Rechnung).

*   A debitor needs to be linked to at least one revenue [entry](#entry) (Rechnungsposten).
    
*   If it is paid it is also linked to one or more payment entries.
    
*   It can also have one or more writeoff entries if the amount was reduced.
    
*   It is always a child of a [period](#period).
    
*   It will usually be linked to a member, but this is optional.
    
*   If a pdf was generated, the [letter](#letter) and the [letterpdf](#letterpdf) are also linked (only for pdfs created with the new editor).
    
*   The invoice items (Rechnungsposten) are the linked entries in `links->revenue`
    
*   The order of the invoice items is stored in the `invoiceitems` property. You can omit the `invoiceitems` property when creating a debitor. It can be null for older debitors with only one invoiceitem.
    
*   The `address` property gets populated with the last known address, when the linked member is deleted.
    
*   The `*amount` properties are readonly and are calculated from the linked entries.
    

Not all properties of the invoice are stored in the debitor itself. Some of them are stored in linked objects.

*   Paydates (Bezahldatum): `links->payment[*]->parents[0]->properties->date`
    
*   Receipt (Beleg Nr.): `links->payment[0]->properties->receipt`
    
*   PDFs: `links->letterpdf[*]->properties->pdf->href` (PDF url)
    

### Debitor List  [¶](#debitor-debitor-list)

#### 

Get Debitor List

[GET](#debitor-debitor-list-get)`/debitor{?filter,order,format}`

Lists all available debitor IDs

#### Example URI

GET /debitor?filter=&order=debitorid ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** debitorid ASC

Sort the debitor list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        3832,
        3840,
        3854
      ]
    }

#### 

Create Debitor

[POST](#debitor-debitor-list-post)`/debitor`

You always need to create an [entry](#entry) and attach it to the debitor within the same request. A debitor cannot exist without an entry.

See the _Request_ data for an example how to create an entry and a debitor with the inline method.

Returns the ID of the newly created debitor.

#### Example URI

POST /debitor

**Request**

HideShow

##### Body

    {
      "properties": {
        "title": "Jahresrechnung",
        "date": "2016-03-27",
        "duedate": "2016-04-27"
      },
      "parents": [
        2230
      ],
      "links": {
        "revenue": [
          {
            "properties": {
              "amount": 50,
              "title": "Mitgliederbeitrag 2016",
              "receipt": "12A"
            },
            "parents": [
              {
                "properties": {
                  "date": "2016-03-27",
                  "title": "Mitgliederbeitrag 2016"
                },
                "parents": [
                  2230
                ]
              }
            ],
            "links": {
              "credit": [
                2257
              ],
              "debit": [
                2236
              ]
            }
          }
        ],
        "member": [
          469
        ],
        "debitorcategory": [
          1097
        ]
      }
    }

**Response  `201`**

HideShow

##### Body

    15013

### Debitor  [¶](#debitor-debitor)

#### 

Get Debitor

[GET](#debitor-debitor-get)`/debitor/{id}`

Get a debitor. By default, the debitor also returns the data of the entries in the response.

#### Example URI

GET /debitor/4333

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4333

Debitor ID

**Response  `200`**

HideShow

JSON Representation of the Debitor.

##### Headers

    Content-Type: application/json

##### Body

    {
      "meta": {
        "created": "2020-03-13 17:05:32",
        "lastmodified": "2020-03-13 17:06:31"
      },
      "type": "debitor",
      "readonly": false,
      "properties": {
        "title": "Mitgliederbeitrag Jassverein 2020",
        "address": null,
        "comment": null,
        "date": "2020-03-12",
        "duedate": "2020-04-12",
        "debitorid": 535,
        "state": "paid",
        "remainingamount": 0,
        "totalamount": 50,
        "paidamount": 50,
        "writeoffamount": 0,
        "invoiceitems": "[{\"entryId\":4895}]"
      },
      "children": {},
      "parents": [
        2230
      ],
      "links": {
        "revenue": [
          {
            "type": "entry",
            "meta": {
              "created": "2020-03-13 17:05:32",
              "lastmodified": "2020-03-13 17:05:32"
            },
            "readonly": false,
            "properties": {
              "amount": 50,
              "title": null,
              "receipt": null,
              "entryid": 32,
              "receiptfile": null
            },
            "children": {},
            "links": {
              "credit": [
                2257
              ],
              "debit": [
                2236
              ],
              "debitor": [
                4333
              ]
            },
            "parents": [
              4332
            ],
            "id": 4331
          }
        ],
        "payment": [
          {
            "type": "entry",
            "meta": {
              "created": "2020-03-13 17:06:31",
              "lastmodified": "2020-03-13 17:06:31"
            },
            "readonly": false,
            "properties": {
              "amount": 50,
              "title": null,
              "receipt": null,
              "entryid": 108,
              "receiptfile": null
            },
            "children": {},
            "links": {
              "credit": [
                2236
              ],
              "debit": [
                2235
              ],
              "debitor": [
                4333
              ]
            },
            "parents": [
              4638
            ],
            "id": 4639
          }
        ],
        "member": [
          476
        ],
        "debitorcategory": [
          1097
        ]
      }
    }

#### 

Update Debitor

[PUT](#debitor-debitor-put)`/debitor/{id}`

Update a debitor

#### Example URI

PUT /debitor/4333

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4333

Debitor ID

**Request**

HideShow

JSON Representation of the Debitor.

##### Headers

    Content-Type: application/json

##### Body

    {
      "meta": {
        "created": "2020-03-13 17:05:32",
        "lastmodified": "2020-03-13 17:06:31"
      },
      "type": "debitor",
      "readonly": false,
      "properties": {
        "title": "Mitgliederbeitrag Jassverein 2020",
        "address": null,
        "comment": null,
        "date": "2020-03-12",
        "duedate": "2020-04-12",
        "debitorid": 535,
        "state": "paid",
        "remainingamount": 0,
        "totalamount": 50,
        "paidamount": 50,
        "writeoffamount": 0,
        "invoiceitems": "[{\"entryId\":4895}]"
      },
      "children": {},
      "parents": [
        2230
      ],
      "links": {
        "revenue": [
          {
            "type": "entry",
            "meta": {
              "created": "2020-03-13 17:05:32",
              "lastmodified": "2020-03-13 17:05:32"
            },
            "readonly": false,
            "properties": {
              "amount": 50,
              "title": null,
              "receipt": null,
              "entryid": 32,
              "receiptfile": null
            },
            "children": {},
            "links": {
              "credit": [
                2257
              ],
              "debit": [
                2236
              ],
              "debitor": [
                4333
              ]
            },
            "parents": [
              4332
            ],
            "id": 4331
          }
        ],
        "payment": [
          {
            "type": "entry",
            "meta": {
              "created": "2020-03-13 17:06:31",
              "lastmodified": "2020-03-13 17:06:31"
            },
            "readonly": false,
            "properties": {
              "amount": 50,
              "title": null,
              "receipt": null,
              "entryid": 108,
              "receiptfile": null
            },
            "children": {},
            "links": {
              "credit": [
                2236
              ],
              "debit": [
                2235
              ],
              "debitor": [
                4333
              ]
            },
            "parents": [
              4638
            ],
            "id": 4639
          }
        ],
        "member": [
          476
        ],
        "debitorcategory": [
          1097
        ]
      }
    }

**Response  `204`**

#### 

Delete Debitor

[DELETE](#debitor-debitor-delete)`/debitor/{id}`

Delete a debitor

#### Example URI

DELETE /debitor/4333

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4333

Debitor ID

**Response  `204`**

Debitorcategory [¶](#debitorcategory)
-------------------------------------

Debitorcategories can be used to categorize [debitors](#debitor). Debitors can be linked to a debitorcategory. Debitorcategories are children of a periodgroup and can be used in all child periods of that periodgroup.

### Debitorcategory List  [¶](#debitorcategory-debitorcategory-list)

#### 

Get Debitorcategory List

[GET](#debitorcategory-debitorcategory-list-get)`/debitorcategory{?filter,order,format}`

Lists all available debitorcategory IDs.

#### Example URI

GET /debitorcategory?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the debitorcategory list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        1098,
        1864
      ]
    }

#### 

Create Debitorcategory

[POST](#debitorcategory-debitorcategory-list-post)`/debitorcategory`

Create a debitorcategory

Returns the id of the newly created debitorcategory.

#### Example URI

POST /debitorcategory

**Request**

HideShow

JSON Representation of the Debitorcategory.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "debitorcategory",
      "readonly": false,
      "properties": {
        "title": "Materialbezug"
      },
      "children": {},
      "links": {
        "debitor": [
          2291
        ]
      },
      "parents": [
        800
      ]
    }

**Response  `201`**

HideShow

##### Body

    1809

### Debitorcategory  [¶](#debitorcategory-debitorcategory)

#### 

Get Debitorcategory

[GET](#debitorcategory-debitorcategory-get)`/debitorcategory/{id}`

Get a debitorcategory

#### Example URI

GET /debitorcategory/1099

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1099

Debitorcategory ID

**Response  `200`**

HideShow

JSON Representation of the Debitorcategory.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "debitorcategory",
      "readonly": false,
      "properties": {
        "title": "Materialbezug"
      },
      "children": {},
      "links": {
        "debitor": [
          2291
        ]
      },
      "parents": [
        800
      ]
    }

#### 

Update Debitorcategory

[PUT](#debitorcategory-debitorcategory-put)`/debitorcategory/{id}`

Update a debitorcategory

#### Example URI

PUT /debitorcategory/1099

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1099

Debitorcategory ID

**Request**

HideShow

JSON Representation of the Debitorcategory.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "debitorcategory",
      "readonly": false,
      "properties": {
        "title": "Materialbezug"
      },
      "children": {},
      "links": {
        "debitor": [
          2291
        ]
      },
      "parents": [
        800
      ]
    }

**Response  `204`**

#### 

Delete Debitorcategory

[DELETE](#debitorcategory-debitorcategory-delete)`/debitorcategory/{id}`

Delete a debitorcategory

#### Example URI

DELETE /debitorcategory/1099

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1099

Debitorcategory ID

**Response  `204`**

Definitions [¶](#definitions)
-----------------------------

### Definitions  [¶](#definitions-definitions)

#### 

Get Definitions

[GET](#definitions-definitions-get)`/definition{?format}`

Returns the field configuration of all objects.

#### Example URI

GET /definition?format=

**URI Parameters**

HideShow

format

`string` (optional) 

Format of the definition. The following formats are available:

*   `simple`: this format is more human-readable, but does not contain all information
    
*   `full`: the full definition with all details. This format is also used to change the definitions
    
*   `zapier`: this format is used to connect Webling to Zapier. More information can be found on [support.webling.ch](https://support.webling.ch/hc/de/articles/360018293372-Automatisierungen-mit-Zapier).
    

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    /* ?format=simple */
    {
        "member": {
            "label": [
                "Vorname",
                "Name"
            ],
            "ordered": false,
            "properties": {
                "ID": {
                    "id": 236,
                    "datatype": "autoincrement",
                    "category": 1,
                    "order": 0
                },
                "Vorname": {
                    "id": 83,
                    "datatype": "text",
                    "category": 1,
                    "order": 1,
                    "type": "firstname"
                },
                "Lizenz": {
                    "id": 71,
                    "datatype": "enum",
                    "category": 1,
                    "order": 13,
                    "values": [
                        "1.Liga",
                        "2.Liga",
                        "Junior"
                    ]
                },
                "Geburtstag": {
                    "id": 68,
                    "datatype": "date",
                    "category": 1,
                    "order": 15,
                    "type": "birthday"
                },
                /* more properties ... */
            },
            "children": {},
            "parents": "membergroup",
            "links": {
                "debitor": "debitor"
            },
            "categories": {
                "1": "Mitgliederdaten",
                "2": "Zweite Kategorie"
            }
        },
        "user": {
            "label": [ "title" ],
            "ordered": false,
            "properties": { 
                /* user properties ... */ 
            },
            "children": {},
            "parents": "usergroup",
            "links": {},
            "categories": []
        },
        /* more datatypes (membergroup, article, document, ...) */
    }

Document [¶](#document)
-----------------------

### Document List  [¶](#document-document-list)

#### 

Get Document List

[GET](#document-document-list-get)`/document{?filter,order,format}`

Lists all available document IDs

#### Example URI

GET /document?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the document list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        1796,
        1805,
        1808,
        1804
      ]
    }

#### 

Create Document

[POST](#document-document-list-post)`/document`

Create a document

Returns the id of the newly created document.

#### Example URI

POST /document

**Request**

HideShow

##### Body

    {
      "type": "document",
      "readonly": true,
      "properties": {
        "title": "factsheet_webling.pdf",
        "content": "base64 encoded file content"
      },
      "children": {},
      "parents": [
        577
      ],
      "links": {}
    }

**Response  `201`**

HideShow

##### Body

    18010

### Document  [¶](#document-document)

A document is equivalent to a file on the filesystem.

#### 

Get Document

[GET](#document-document-get)`/document/{id}`

Get a document

#### Example URI

GET /document/1804

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1804

Document ID

**Response  `200`**

HideShow

JSON Representation of the Document.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "document",
      "readonly": true,
      "properties": {
        "title": "factsheet_webling.pdf",
        "description": "Webling Factsheet",
        "href": "/api/1/document/1805/file/factsheet_webling.pdf",
        "size": 1142037,
        "lastmodified": "2015-05-15 11:27:40",
        "isProtected": true,
        "protectedBy": "Administrator",
        "file": {
          "name": "factsheet_webling.pdf",
          "href": "/api/1/document/1805/file/factsheet_webling.pdf",
          "size": 1142037,
          "lastmodified": "2015-05-15 11:27:40"
        }
      },
      "children": {},
      "parents": [
        577
      ],
      "links": {}
    }

#### 

Get Header of Document

[HEAD](#document-document-head)`/document/{id}`

Get only the header of a document

#### Example URI

HEAD /document/1804

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1804

Document ID

**Response  `200`**

#### 

Update Document

[PUT](#document-document-put)`/document/{id}`

Update a document

#### Example URI

PUT /document/1804

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1804

Document ID

**Request**

HideShow

JSON Representation of the Document.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "document",
      "readonly": true,
      "properties": {
        "title": "factsheet_webling.pdf",
        "description": "Webling Factsheet",
        "href": "/api/1/document/1805/file/factsheet_webling.pdf",
        "size": 1142037,
        "lastmodified": "2015-05-15 11:27:40",
        "isProtected": true,
        "protectedBy": "Administrator",
        "file": {
          "name": "factsheet_webling.pdf",
          "href": "/api/1/document/1805/file/factsheet_webling.pdf",
          "size": 1142037,
          "lastmodified": "2015-05-15 11:27:40"
        }
      },
      "children": {},
      "parents": [
        577
      ],
      "links": {}
    }

**Response  `204`**

#### 

Delete Document

[DELETE](#document-document-delete)`/document/{id}`

Delete a document

#### Example URI

DELETE /document/1804

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1804

Document ID

**Response  `204`**

### Document Content  [¶](#document-document-content)

#### 

Get Document Content

[GET](#document-document-content-get)`/document/{id}/file/{filename}.{extension}`

Get the content of the file

#### Example URI

GET /document/1805/file/Jahresabschluss.xlsx

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1805

Document ID.

filename

`string` (required) **Example:** Jahresabschluss

Name of the file without extension

extension

`string` (required) **Example:** xlsx

File extension of the file

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/zip

##### Body

    binary data

Documentgroup [¶](#documentgroup)
---------------------------------

A documentgroup contains documents and other documentgroups.

Documentgroups are also known as Folders, “Ordner”.

### Documentgroup List  [¶](#documentgroup-documentgroup-list)

#### 

Get Documentgroup List

[GET](#documentgroup-documentgroup-list-get)`/documentgroup{?filter,order,format}`

Lists all available documentgroup IDs. Object “roots” lists the IDs of all root documentgroups, which can be used to build the documentgroup tree.

#### Example URI

GET /documentgroup?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the documentgroup list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        1806,
        577,
        1807,
        1795
      ],
      "roots": [
        577
      ]
    }

#### 

Create Documentgroup

[POST](#documentgroup-documentgroup-list-post)`/documentgroup`

Create a documentgroup

Returns the ID of the newly created documentgroup.

#### Example URI

POST /documentgroup

**Request**

HideShow

JSON Representation of the Documentgroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "documentgroup",
      "readonly": false,
      "properties": {
        "title": "Dokumente"
      },
      "children": {
        "document": [
          1808
        ],
        "documentgroup": [
          1807
        ]
      },
      "parents": [
        577
      ],
      "links": {}
    }

**Response  `201`**

HideShow

##### Body

    1809

### Documentgroup  [¶](#documentgroup-documentgroup)

#### 

Get Documentgroup

[GET](#documentgroup-documentgroup-get)`/documentgroup/{id}`

Get a documentgroup

#### Example URI

GET /documentgroup/1806

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1806

Documentgroup ID

**Response  `200`**

HideShow

JSON Representation of the Documentgroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "documentgroup",
      "readonly": false,
      "properties": {
        "title": "Dokumente"
      },
      "children": {
        "document": [
          1808
        ],
        "documentgroup": [
          1807
        ]
      },
      "parents": [
        577
      ],
      "links": {}
    }

#### 

Update Documentgroup

[PUT](#documentgroup-documentgroup-put)`/documentgroup/{id}`

Update a documentgroup

#### Example URI

PUT /documentgroup/1806

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1806

Documentgroup ID

**Request**

HideShow

JSON Representation of the Documentgroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "documentgroup",
      "readonly": false,
      "properties": {
        "title": "Dokumente"
      },
      "children": {
        "document": [
          1808
        ],
        "documentgroup": [
          1807
        ]
      },
      "parents": [
        577
      ],
      "links": {}
    }

**Response  `204`**

#### 

Delete Documentgroup

[DELETE](#documentgroup-documentgroup-delete)`/documentgroup/{id}`

Delete a documentgroup

#### Example URI

DELETE /documentgroup/1806

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1806

Documentgroup ID

**Response  `204`**

### Archive  [¶](#documentgroup-archive)

#### 

Get Documentgroup Archive

[GET](#documentgroup-archive-get)`/documentgroup/{id}/archive.zip`

Get a zip archive of all documents and sub documentgroups

#### Example URI

GET /documentgroup/577/archive.zip

**URI Parameters**

HideShow

id

`number` (required) **Example:** 577

Documentgroup ID

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/zip

##### Body

    binary data

Entry [¶](#entry)
-----------------

An entry is a financial posting (Buchung) linked to two accounts and is a child of an [entrygroup](#entrygroup).

An entry can be linked to a debitor to indicate a revenue or payment.

An entry can be linked to a [costcenter](#costcenter) to categorize entries.

> **WARNING:** the following properties are moved to `/entrygroup` and are considered deprecated in `/entry`.  
> They will be removed in a future release:  
> `receipt`, `receiptfile`, `isEBill`, `entryid`

### Entry List  [¶](#entry-entry-list)

#### 

Get Entry List

[GET](#entry-entry-list-get)`/entry{?filter,order,format}`

Lists all available entry IDs

#### Example URI

GET /entry?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the entry list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        175,
        176,
        180
      ]
    }

#### 

Create Entry

[POST](#entry-entry-list-post)`/entry`

Create an entry You always need to create an [entrygroup](#entrygroup) and attach the entry within the same request. An entry cannot exist without an entrygroup.

See the _Request_ data for an example how to create an entry and an entrygroup with the inline method.

Returns the id of the newly created entry.

#### Example URI

POST /entry

**Request**

HideShow

##### Body

    {
            "properties": {
                "amount": 50,
                "title": "Mitgliederbeitrag 2024",
    
            },
            "parents": [
                {
                    "properties": {
                        "date": "2024-03-27",
                        "title": "Mitgliederbeitrag 2024"
                        "receipt": "12A"
                    },
                    "parents": [
                        2230
                    ]
                }
            ],
            "links": {
                "credit": [
                    2236
                ],
                "debit": [
                    2235
                ]
            }
        }

**Response  `201`**

HideShow

##### Body

    7800

### Entry  [¶](#entry-entry)

#### 

Get Entry

[GET](#entry-entry-get)`/entry/{id}`

Get an entry

#### Example URI

GET /entry/180

**URI Parameters**

HideShow

id

`number` (required) **Example:** 180

Entry ID

**Response  `200`**

HideShow

JSON Representation of the Entry.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "entry",
      "readonly": false,
      "properties": {
        "amount": 200,
        "title": "",
        "receipt": "6",
        "entryid": 13,
        "skrSphere": null,
        "receiptfile": null
      },
      "parents": [
        2719
      ],
      "children": {},
      "links": {
        "credit": [
          122
        ],
        "debit": [
          97
        ]
      }
    }

#### 

Get Header of Entry

[HEAD](#entry-entry-head)`/entry/{id}`

Get only the header of an Entry

#### Example URI

HEAD /entry/180

**URI Parameters**

HideShow

id

`number` (required) **Example:** 180

Entry ID

**Response  `200`**

#### 

Update Entry

[PUT](#entry-entry-put)`/entry/{id}`

Update an entry

#### Example URI

PUT /entry/180

**URI Parameters**

HideShow

id

`number` (required) **Example:** 180

Entry ID

**Request**

HideShow

JSON Representation of the Entry.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "entry",
      "readonly": false,
      "properties": {
        "amount": 200,
        "title": "",
        "receipt": "6",
        "entryid": 13,
        "skrSphere": null,
        "receiptfile": null
      },
      "parents": [
        2719
      ],
      "children": {},
      "links": {
        "credit": [
          122
        ],
        "debit": [
          97
        ]
      }
    }

**Response  `204`**

#### 

Delete Entry

[DELETE](#entry-entry-delete)`/entry/{id}`

Delete an entry

#### Example URI

DELETE /entry/180

**URI Parameters**

HideShow

id

`number` (required) **Example:** 180

Entry ID

**Response  `204`**

Entrygroup [¶](#entrygroup)
---------------------------

An entrygroup is a collective financial posting (Sammelbuchung) linked to two accounts and is always a child of a [period](#period). It cannot exist without a period. An entrygroup can only have one entry as a child.

### Entrygroup List  [¶](#entrygroup-entrygroup-list)

#### 

Get Entrygroup List

[GET](#entrygroup-entrygroup-list-get)`/entrygroup{?filter,order,format}`

Lists all available entrygroup IDs

#### Example URI

GET /entrygroup?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the entrygroup list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        3096,
        3100,
        3047
      ]
    }

#### 

Create Entrygroup

[POST](#entrygroup-entrygroup-list-post)`/entrygroup`

You always need to create an [entry](#entry) and attach it to the entrygroup within the same request. An entrygroup cannot exist without an entry.

See the _Request_ data for an example how to create an entry and an entrygroup with the inline method.

Returns the id of the newly created entrygroup.

#### Example URI

POST /entrygroup

**Request**

HideShow

##### Body

    {
      "properties": {
        "date": "2011-03-27",
        "title": "Spesen"
      },
      "children": {
        "entry": [
          {
            "properties": {
              "amount": 200,
              "receipt": "6",
              "isEBill": false
            },
            "links": {
              "credit": [
                122
              ],
              "debit": [
                97
              ]
            }
          }
        ]
      },
      "parents": [
        94
      ]
    }

**Response  `201`**

HideShow

##### Body

    18010

### Entrygroup  [¶](#entrygroup-entrygroup)

#### 

Get Entrygroup

[GET](#entrygroup-entrygroup-get)`/entrygroup/{id}`

Get an entrygroup

#### Example URI

GET /entrygroup/4288

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4288

Entrygroup ID

**Response  `200`**

HideShow

JSON Representation of the Entrygroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "entrygroup",
      "readonly": false,
      "properties": {
        "title": "Getränkeverkauf",
        "date": "2020-10-03",
        "receipt": "V-21",
        "entryid": 15,
        "receiptfile": null,
        "isEBill": false
      },
      "parents": [
        2230
      ],
      "children": {
        "entry": [
          4289
        ]
      },
      "links": {
        "account": [
          2234,
          2259
        ]
      }
    }

#### 

Update Entrygroup

[PUT](#entrygroup-entrygroup-put)`/entrygroup/{id}`

Update an entrygroup

#### Example URI

PUT /entrygroup/4288

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4288

Entrygroup ID

**Request**

HideShow

JSON Representation of the Entrygroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "entrygroup",
      "readonly": false,
      "properties": {
        "title": "Getränkeverkauf",
        "date": "2020-10-03",
        "receipt": "V-21",
        "entryid": 15,
        "receiptfile": null,
        "isEBill": false
      },
      "parents": [
        2230
      ],
      "children": {
        "entry": [
          4289
        ]
      },
      "links": {
        "account": [
          2234,
          2259
        ]
      }
    }

**Response  `204`**

#### 

Delete Entrygroup

[DELETE](#entrygroup-entrygroup-delete)`/entrygroup/{id}`

Delete an entrygroup

#### Example URI

DELETE /entrygroup/4288

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4288

Entrygroup ID

**Response  `204`**

Letter [¶](#letter)
-------------------

The letter object is used by the letter editor to write and send letters. They can be printed but also sent by e-mail.

If a PDF has been generated, the [letterpdfs](#letterpdf) are linked and the state of the letter is “sent”. A sent letter becomes immutable.

Not all letter actions are available to API users (e.g. send letters by e-mail or saving drafts).

Note: This is only available for letters created with the new editor

### Letter List  [¶](#letter-letter-list)

#### 

Get Letter List

[GET](#letter-letter-list-get)`/letter{?filter,order,format}`

Lists all available letter IDs.

#### Example URI

GET /letter?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the letter list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        1098,
        1864
      ]
    }

### Letter  [¶](#letter-letter)

#### 

Get Letter

[GET](#letter-letter-get)`/letter/{id}`

Get a letter

#### Example URI

GET /letter/1099

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1099

Letter ID

**Response  `200`**

HideShow

JSON Representation of the Letter.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "letter",
      "meta": {
        "created": "2021-01-15 16:44:38",
        "lastmodified": "2021-01-15 16:45:21"
      },
      "readonly": false,
      "properties": {
        "title": "Rechnung",
        "state": "sent",
        "sentat": "2021-01-15 16:45:20",
        "sentby": "Demo Benutzer <demo@example.ch>",
        "data": "... letter content ...",
        "preview": {
          "href": "/api/1/letter/4812/image/preview.png",
          "hrefthumb": "/api/1/letter/4812/thumb/preview.png",
          "size": 126668,
          "name": "preview.png",
          "lastmodified": "2021-01-15 16:45:09",
          "dimensions": {
            "width": 400,
            "height": 570
          }
        },
        "isattachment": true,
        "lettertype": "debitor"
      },
      "children": {
        "letterpdf": [
          4814,
          4815,
        ]
      },
      "links": {
        "debitor": [
          4546,
          4543,
        ],
        "sender": [
          584
        ]
      },
      "parents": []
    }

#### 

Delete Letter

[DELETE](#letter-letter-delete)`/letter/{id}`

Delete a letter

#### Example URI

DELETE /letter/1099

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1099

Letter ID

**Response  `204`**

### Create PDFs  [¶](#letter-create-pdfs)

#### 

Create PDF's

[POST](#letter-create-pdfs-post)`/letter/new/send`

This endpoint is used to create new PDF’s for members or debitors. The generated pdf is returned and the individual pdfs are saved as letterpdf objects for later retrieval.

Properties:

*   `title`: the title that is shown in the UI
    
*   `state`: only “sent” is allowed for this request
    
*   `data`: this contains the letter template to render the pdf. To see all options, the easiest way is to create a letter with the UI and check the resulting code. The format may change in the future, when new features are added.
    
*   `lettertype`: must either be “member” or “debitor”, depending on the type of links
    

Links: A letter can either be linked to members or debitors. You can pass multiple members or debitors at once, to generate multiple pdf’s.

Response: A pdf binary is returned. If you are creating pdf’s for multiple members or debitors, the individual pdf’s are combined into one pdf with multiple pages.

Below is a minimal example to generate a PDF:

#### Example URI

POST /letter/new/send

**Request**

HideShow

##### Body

    {
      "properties": {
        "title": "my letter",
        "state": "sent",
        "data": "{\"body\":[[{\"start\":0,\"width\":12,\"id\":\"1\",\"type\":\"html\",\"padding\":{\"top\":0,\"right\":0,\"bottom\":0,\"left\":0},\"content\":{\"html\":\"<h1>Hallo {{Vorname}}</h1>\"}}]]}",
        "lettertype": "member"
      },
      "links": {
        "member": [
          525
        ]
      }
    }

**Response  `200`**

Letterpdf [¶](#letterpdf)
-------------------------

The generated pdf from a [letter](#letter) is saved as a letterpdf object. To get the actual PDF you need to call the href that is returned with this object.

A letterpdf is either linked to a member or a debitor and is always a child of a letter.

Letterpdfs are immutable and cannot be created or updated manually. To create a new PDF, use the `/letter/new/send` endpoint.

Note: This is only available for pdfs created with the new editor

### Letterpdf List  [¶](#letterpdf-letterpdf-list)

#### 

Get Letterpdf List

[GET](#letterpdf-letterpdf-list-get)`/letterpdf{?filter,format}`

Lists all available letterpdf IDs.

#### Example URI

GET /letterpdf?filter=&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        4814,
        4815,
        4816
      ]
    }

### Letterpdf  [¶](#letterpdf-letterpdf)

#### 

Get Letterpdf

[GET](#letterpdf-letterpdf-get)`/letterpdf/{id}`

Get a letterpdf

#### Example URI

GET /letterpdf/4816

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4816

Letterpdf ID

**Response  `200`**

HideShow

JSON Representation of the Letterpdf.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "letterpdf",
      "meta": {
        "created": "2021-01-15 16:44:03",
        "lastmodified": "2021-01-15 16:44:03"
      },
      "readonly": false,
      "properties": {
        "pdf": {
          "href": "/api/1/letterpdf/4808/file/pdf.pdf",
          "size": 19334,
          "name": "pdf.pdf",
          "lastmodified": "2021-01-15 16:44:02"
        }
      },
      "children": {},
      "links": {
        "debitor": [
          4552
        ]
      },
      "parents": [
        4807
      ]
    }

#### 

Get Header of Letterpdf

[HEAD](#letterpdf-letterpdf-head)`/letterpdf/{id}`

Get only the header of a letterpdf

#### Example URI

HEAD /letterpdf/4816

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4816

Letterpdf ID

**Response  `200`**

#### 

Delete Letterpdf

[DELETE](#letterpdf-letterpdf-delete)`/letterpdf/{id}`

Delete a letterpdf

#### Example URI

DELETE /letterpdf/4816

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4816

Letterpdf ID

**Response  `204`**

Member [¶](#member)
-------------------

### Member List  [¶](#member-member-list)

#### 

List Members

[GET](#member-member-list-get)`/member{?filter,order,format}`

Lists all available Member IDs

#### Example URI

GET /member?filter=&order=Name ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** Name ASC

Sort the member list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        536,
        525,
        497,
        535,
        474,
        533,
        499
      ]
    }

#### 

Create Member

[POST](#member-member-list-post)`/member`

Create a member. Only “properties”, “parents” and “links” can be set. Other attributes will be ignored and can be omitted in the request. A member needs at least one parent.

The “content” property of images and files need to be base64 encoded.

If you omit a field it will be empty. This means you only need to pass the fields you wish to set.

Returns the id of the newly created member.

#### Example URI

POST /member

**Request**

HideShow

##### Body

    {
      "type": "member",
      "readonly": false,
      "properties": {
        "Vorname": "Quentin",
        "Name": "Moser",
        "Firma": null,
        "Strasse": "Kirchgasse  32",
        "PLZ": "9000",
        "Ort": "St. Gallen",
        "Telefon": "079 336 47 50",
        "Mobile": "077 336 47 50",
        "E-Mail": "Moser@nospam-webling.ch",
        "Lizenz": "Junior",
        "Geschlecht": "m",
        "Geburtstag": "1997-07-13",
        "Checkbox": true,
        "Mehrfachauswahlfeld": [
          "Wert 1",
          "Wert 2"
        ],
        "Mitgliederbild": {
          "name": "filename.gif",
          "content": "R0lGODlhAQABAIAAAAUEBAAAACwAAAAAAQABAAACAkQBADs="
        }
      },
      "children": {},
      "parents": [
        555
      ],
      "links": {
        "debitor": [
          883,
          1136,
          1900,
          2388
        ]
      }
    }

**Response  `201`**

HideShow

##### Body

    540

### Member  [¶](#member-member)

#### 

Get Member

[GET](#member-member-get)`/member/{id}`

Get a member.

#### Example URI

GET /member/504

**URI Parameters**

HideShow

id

`number` (required) **Example:** 504

Member ID

**Response  `200`**

HideShow

JSON Representation of the Member.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "member",
      "readonly": false,
      "properties": {
        "Vorname": "Quentin",
        "Name": "Moser",
        "Firma": null,
        "Strasse": "Kirchgasse  32",
        "PLZ": "9000",
        "Ort": "St. Gallen",
        "Telefon": "079 336 47 50",
        "Mobile": "077 336 47 50",
        "E-Mail": "Moser@nospam-webling.ch",
        "Lizenz": "Junior",
        "Geschlecht": "m",
        "Geburtstag": "1997-07-13",
        "Checkbox": false,
        "Mitgliederbild": {
          "href": "/api/1/member/504/image/Mitgliederbild.jpg",
          "size": 325743,
          "name": "Mitgliederbild.jpg",
          "lastmodified": "2015-05-15 11:26:55",
          "dimensions": {
            "width": 640,
            "height": 480
          }
        },
        "Datei": {
          "href": "/api/1/member/504/file/Datei.pdf",
          "size": 117539,
          "name": "Datei.pdf",
          "lastmodified": "2015-05-15 11:26:55"
        }
      },
      "children": {},
      "parents": [
        555
      ],
      "links": {
        "debitor": [
          883,
          1136,
          1900,
          2388
        ]
      }
    }

#### 

Update Member

[PUT](#member-member-put)`/member/{id}`

Update a member. Only “properties”, “parents” and “links” may be changed. Other attributes will be ignored and can be omitted in the request. Note that a member needs at least one parent.

You can empty a field by passing `null` as a value.

The “content” property of images and files need to be base64 encoded.

If you omit a field it won’t be changed. This means you can either pass the whole object or just the fields you wish to change.

#### Example URI

PUT /member/504

**URI Parameters**

HideShow

id

`number` (required) **Example:** 504

Member ID

**Request**

HideShow

##### Body

    {
      "type": "member",
      "readonly": false,
      "properties": {
        "Vorname": "Quentin",
        "Name": "Moser",
        "Firma": null,
        "Strasse": "Kirchgasse  32",
        "PLZ": "9000",
        "Ort": "St. Gallen",
        "Telefon": "079 336 47 50",
        "Mobile": "077 336 47 50",
        "E-Mail": "Moser@nospam-webling.ch",
        "Lizenz": "Junior",
        "Geschlecht": "m",
        "Geburtstag": "1997-07-13",
        "Checkbox": true,
        "Mehrfachauswahlfeld": [
          "Wert 1",
          "Wert 2"
        ],
        "Mitgliederbild": {
          "name": "filename.gif",
          "content": "R0lGODlhAQABAIAAAAUEBAAAACwAAAAAAQABAAACAkQBADs="
        }
      },
      "children": {},
      "parents": [
        555
      ],
      "links": {
        "debitor": [
          883,
          1136,
          1900,
          2388
        ]
      }
    }

**Response  `204`**

#### 

Delete Member

[DELETE](#member-member-delete)`/member/{id}`

Delete a member

#### Example URI

DELETE /member/504

**URI Parameters**

HideShow

id

`number` (required) **Example:** 504

Member ID

**Response  `204`**

### Images  [¶](#member-images)

#### 

Get Member Image

[GET](#member-images-get)`/member/{id}/image/{fieldname}.{extension}{?size}`

Get Image of a member by fieldname

Available sizes are: `original` (default), `thumb` and `mini`

#### Example URI

GET /member/504/image/Mitgliederbild.png?size=

**URI Parameters**

HideShow

id

`number` (required) **Example:** 504

Member ID

fieldname

`string` (required) **Example:** Mitgliederbild

Name of the datafield

extension

`string` (required) **Example:** png

File extension of the image

size

`string` (optional) **Default:** original 

Preferred image size

**Choices:** `original` `thumb` `mini`

**Response  `200`**

HideShow

##### Headers

    Content-Type: image/jpeg

##### Body

    binary data

#### 

Get Header of Member Image

[HEAD](#member-images-head)`/member/{id}/image/{fieldname}.{extension}{?size}`

Get only the header of an Image of a member by fieldname

#### Example URI

HEAD /member/504/image/Mitgliederbild.png?size=

**URI Parameters**

HideShow

id

`number` (required) **Example:** 504

Member ID

fieldname

`string` (required) **Example:** Mitgliederbild

Name of the datafield

extension

`string` (required) **Example:** png

File extension of the image

size

`string` (optional) **Default:** original 

Preferred image size

**Choices:** `original` `thumb` `mini`

**Response  `200`**

### Files  [¶](#member-files)

#### 

Get Member File

[GET](#member-files-get)`/member/{id}/file/{fieldname}.{extension}`

Get file of a member by fieldname

#### Example URI

GET /member/504/file/Datei.pdf

**URI Parameters**

HideShow

id

`number` (required) **Example:** 504

Member ID

fieldname

`string` (required) **Example:** Datei

Name of the datafield.

extension

`string` (required) **Example:** pdf

File extension of the file

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/pdf

##### Body

    binary data

#### 

Get Header of Member File

[HEAD](#member-files-head)`/member/{id}/file/{fieldname}.{extension}`

Get only the header of a file of a member by fieldname

#### Example URI

HEAD /member/504/file/Datei.pdf

**URI Parameters**

HideShow

id

`number` (required) **Example:** 504

Member ID

fieldname

`string` (required) **Example:** Datei

Name of the datafield.

extension

`string` (required) **Example:** pdf

File extension of the file

**Response  `200`**

Membergroup [¶](#membergroup)
-----------------------------

A membergroup contains members and other membergroups.

### Membergroup List  [¶](#membergroup-membergroup-list)

#### 

Get Membergroup List

[GET](#membergroup-membergroup-list-get)`/membergroup{?filter,order,format}`

Lists all available membergroup IDs. Object “roots” lists the IDs of all root membergroups, which can be used to build the membergroup tree.

#### Example URI

GET /membergroup?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the membergroup list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        536,
        525,
        497,
        535,
        474,
        533,
        499
      ],
      "roots": [
        525
      ]
    }

#### 

Create Membergroup

[POST](#membergroup-membergroup-list-post)`/membergroup`

Create a membergroup

Returns the ID of the newly created membergroup.

#### Example URI

POST /membergroup

**Request**

HideShow

JSON Representation of the Membergroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "membergroup",
      "readonly": false,
      "properties": {
        "title": "Präsidium"
      },
      "children": {
        "member": [
          469,
          492
        ]
      },
      "parents": [
        552
      ],
      "links": {}
    }

**Response  `201`**

HideShow

##### Body

    560

### Membergroup  [¶](#membergroup-membergroup)

#### 

Get Membergroup

[GET](#membergroup-membergroup-get)`/membergroup/{id}`

Get a membergroup

#### Example URI

GET /membergroup/554

**URI Parameters**

HideShow

id

`number` (required) **Example:** 554

Membergroup ID

**Response  `200`**

HideShow

JSON Representation of the Membergroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "membergroup",
      "readonly": false,
      "properties": {
        "title": "Präsidium"
      },
      "children": {
        "member": [
          469,
          492
        ]
      },
      "parents": [
        552
      ],
      "links": {}
    }

#### 

Update Membergroup

[PUT](#membergroup-membergroup-put)`/membergroup/{id}`

Update a membergroup

#### Example URI

PUT /membergroup/554

**URI Parameters**

HideShow

id

`number` (required) **Example:** 554

Membergroup ID

**Request**

HideShow

JSON Representation of the Membergroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "membergroup",
      "readonly": false,
      "properties": {
        "title": "Präsidium"
      },
      "children": {
        "member": [
          469,
          492
        ]
      },
      "parents": [
        552
      ],
      "links": {}
    }

**Response  `204`**

#### 

Delete Membergroup

[DELETE](#membergroup-membergroup-delete)`/membergroup/{id}`

Delete a membergroup

#### Example URI

DELETE /membergroup/554

**URI Parameters**

HideShow

id

`number` (required) **Example:** 554

Membergroup ID

**Response  `204`**

Object [¶](#object)
-------------------

The `/object` endpoint is a generic endpoint to get any Webling object by ID. This might be useful if you don’t know the datatype.

The difference to the more specific datatype endpoints (like `/member` or `/document`) is, that its properties are not indexed by name, but its internal ID.

Example: the title property of a membergroup is “85” (the internal property ID) not “title”. These IDs are especially useful when dealing with member properties, because their name can be changed. You can get these IDs by calling the `/definition` endpoint. The IDs may be different in another Webling account.

Note: `/object` does not support object listing, only single object operations.

### Object List  [¶](#object-object-list)

#### 

Create Object

[POST](#object-object-list-post)`/object`

Create an object.

If you omit a field it will be empty. This means you only need to pass the fields you wish to set.

Returns the ID of the newly created object.

#### Example URI

POST /object

**Request**

HideShow

##### Body

    {
      "type": "membergroup",
      "properties": {
        "85": "New Membergroup"
      },
      "parents": [
        550
      ]
    }

**Response  `201`**

HideShow

##### Body

    640

### Object  [¶](#object-object)

#### 

Get Object

[GET](#object-object-get)`/object/{id}`

Get an object.

#### Example URI

GET /object/557

**URI Parameters**

HideShow

id

`number` (required) **Example:** 557

object ID

**Response  `200`**

HideShow

JSON Representation of the Object.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "membergroup",
      "meta": {
        "created": null,
        "lastmodified": "2014-12-07 17:57:21"
      },
      "readonly": false,
      "properties": {
        "85": "Kassier"
      },
      "children": {
        "member": [
          519
        ]
      },
      "links": {},
      "parents": [
        552
      ]
    }

#### 

Update Object

[PUT](#object-object-put)`/object/{id}`

Update an object.

If you omit a field it won’t be changed. This means you can either pass the whole object or just the fields you wish to change.

#### Example URI

PUT /object/557

**URI Parameters**

HideShow

id

`number` (required) **Example:** 557

object ID

**Request**

HideShow

##### Body

    {
      "type": "membergroup",
      "properties": {
        "85": "Kassier"
      },
      "parents": [
        552
      ]
    }

**Response  `204`**

#### 

Delete Object

[DELETE](#object-object-delete)`/object/{id}`

Delete an object

#### Example URI

DELETE /object/557

**URI Parameters**

HideShow

id

`number` (required) **Example:** 557

object ID

**Response  `204`**

Period [¶](#period)
-------------------

A period is an accounting period. A period is linked to a [period chain](#periodchain) which groups together the succeeding account periods. It is always a child of a [periodgroup](#periodgroup). It cannot exist without a periodchain.

### Period List  [¶](#period-period-list)

#### 

Get Period List

[GET](#period-period-list-get)`/period{?filter,order,format}`

Lists all available period IDs

#### Example URI

GET /period?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the period list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        3655,
        2144,
        2230,
        3719
      ]
    }

#### 

Create Period

[POST](#period-period-list-post)`/period`

You always need to link or create a [periodchain](#periodchain) to the period within the same request. A period cannot exist without a periodchain.

Returns the ID of the newly created period.

#### Example URI

POST /period

**Request**

HideShow

##### Body

    {
      "type": "period",
      "readonly": false,
      "properties": {
        "title": "Rechnungsjahr 2019",
        "from": "2019-01-01",
        "state": "open",
        "to": "2019-12-31",
        "budgetdescription": null
      },
      "children": {
        "accountgroup": [
          3721,
          3726,
          3730,
          3732
        ]
      },
      "links": {
        "periodchain": [
          4003
        ]
      },
      "parents": [
        3599
      ]
    }

**Response  `201`**

HideShow

##### Body

    18010

### Period  [¶](#period-period)

#### 

Get Period

[GET](#period-period-get)`/period/{id}`

Get a period

#### Example URI

GET /period/3777

**URI Parameters**

HideShow

id

`number` (required) **Example:** 3777

Period ID

**Response  `200`**

HideShow

JSON Representation of the Period.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "period",
      "readonly": false,
      "properties": {
        "title": "Onlinezahlungen",
        "from": "2017-01-01",
        "state": "open",
        "to": "2025-12-31",
        "budgetdescription": null
      },
      "children": {
        "debitor": [
          3830,
          3831,
          3832,
          3833,
          3834,
          3835,
          3836,
          3837,
          3838,
          3839,
          3840,
          3841,
          3842,
          3843,
          3844,
          3845,
          3846,
          3847,
          3848,
          3849,
          3850,
          3851,
          3852,
          3853,
          3854,
          3855,
          3856,
          3857
        ],
        "entrygroup": [
          4000,
          3997,
          3995,
          3990,
          3968,
          3965,
          3962,
          3959,
          3951,
          3950,
          3949,
          3948,
          3947,
          3913,
          3912,
          3911,
          3910,
          3909,
          3908,
          3907,
          3906,
          3905,
          3904,
          3903,
          3902,
          3901,
          3900,
          3899,
          3898,
          3897,
          3896,
          3895,
          3894,
          3893,
          3892,
          3891,
          3890,
          3889,
          3888,
          3887,
          3886
        ],
        "accountgroup": [
          3779,
          3784,
          3787,
          3789,
          3793,
          3799,
          3802,
          3806
        ]
      },
      "links": {
        "periodchain": [
          4189
        ]
      },
      "parents": [
        800
      ]
    }

#### 

Update Period

[PUT](#period-period-put)`/period/{id}`

Update a period

#### Example URI

PUT /period/3777

**URI Parameters**

HideShow

id

`number` (required) **Example:** 3777

Period ID

**Request**

HideShow

JSON Representation of the Period.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "period",
      "readonly": false,
      "properties": {
        "title": "Onlinezahlungen",
        "from": "2017-01-01",
        "state": "open",
        "to": "2025-12-31",
        "budgetdescription": null
      },
      "children": {
        "debitor": [
          3830,
          3831,
          3832,
          3833,
          3834,
          3835,
          3836,
          3837,
          3838,
          3839,
          3840,
          3841,
          3842,
          3843,
          3844,
          3845,
          3846,
          3847,
          3848,
          3849,
          3850,
          3851,
          3852,
          3853,
          3854,
          3855,
          3856,
          3857
        ],
        "entrygroup": [
          4000,
          3997,
          3995,
          3990,
          3968,
          3965,
          3962,
          3959,
          3951,
          3950,
          3949,
          3948,
          3947,
          3913,
          3912,
          3911,
          3910,
          3909,
          3908,
          3907,
          3906,
          3905,
          3904,
          3903,
          3902,
          3901,
          3900,
          3899,
          3898,
          3897,
          3896,
          3895,
          3894,
          3893,
          3892,
          3891,
          3890,
          3889,
          3888,
          3887,
          3886
        ],
        "accountgroup": [
          3779,
          3784,
          3787,
          3789,
          3793,
          3799,
          3802,
          3806
        ]
      },
      "links": {
        "periodchain": [
          4189
        ]
      },
      "parents": [
        800
      ]
    }

**Response  `204`**

#### 

Delete Period

[DELETE](#period-period-delete)`/period/{id}`

Delete a period

#### Example URI

DELETE /period/3777

**URI Parameters**

HideShow

id

`number` (required) **Example:** 3777

Period ID

**Response  `204`**

Periodchain [¶](#periodchain)
-----------------------------

A periodchain is a container for periods that belong together (also known as “Kontenrahmen”). A periodchain has links to one or more [periods](#period) to group together the succeeding account periods. The periods in a periodchain are ordered by date to build a chain of periods. Therefore, the end date of the previous period and the start date of the next period should match. Any “holes” in the chain are not allowed. A periodchain is always a child of a [periodgroup](#periodgroup).

### Periodchain List  [¶](#periodchain-periodchain-list)

#### 

Get Periodchain List

[GET](#periodchain-periodchain-list-get)`/periodchain{?filter,order,format}`

Lists all available periodchain ids

#### Example URI

GET /periodchain?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the periodchain list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        4003,
        4037
      ]
    }

#### 

Create Periodchain

[POST](#periodchain-periodchain-list-post)`/periodchain`

Returns the id of the newly created periodchain.

`sourcechart` is the base acchountchart that it is based of. It can be any of: `null`, `"simple"`, `"deSkr49"`, `"deSkr42"`, `"chKmuSimple"`, `"deDsb"`, `"custom"`

#### Example URI

POST /periodchain

**Request**

HideShow

##### Body

    {
      "type": "periodchain",
      "readonly": false,
      "properties": {
        "title": "Kontenrahmen",
        "sourcechart": null
      },
      "children": {
        "accountgrouptemplate": [
          4004,
          4011,
          4013,
          4015
        ]
      },
      "links": {
        "period": [
          3600,
          3655,
          3719
        ]
      },
      "parents": [
        3599
      ]
    }

**Response  `201`**

HideShow

##### Body

    18010

### Periodchain  [¶](#periodchain-periodchain)

#### 

Get Periodchain

[GET](#periodchain-periodchain-get)`/periodchain/{id}`

Get a periodchain

#### Example URI

GET /periodchain/4126

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4126

Periodchain ID

**Response  `200`**

HideShow

JSON Representation of the Periodchain.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "periodchain",
      "readonly": false,
      "properties": {
        "title": "Kontenrahmen",
        "sourcechart": null
      },
      "children": {
        "accountgrouptemplate": [
          4004,
          4011,
          4013,
          4015
        ]
      },
      "links": {
        "period": [
          185,
          802,
          2230
        ]
      },
      "parents": [
        800
      ]
    }

#### 

Update Periodchain

[PUT](#periodchain-periodchain-put)`/periodchain/{id}`

Update a periodchain

#### Example URI

PUT /periodchain/4126

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4126

Periodchain ID

**Request**

HideShow

JSON Representation of the Periodchain.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "periodchain",
      "readonly": false,
      "properties": {
        "title": "Kontenrahmen",
        "sourcechart": null
      },
      "children": {
        "accountgrouptemplate": [
          4004,
          4011,
          4013,
          4015
        ]
      },
      "links": {
        "period": [
          185,
          802,
          2230
        ]
      },
      "parents": [
        800
      ]
    }

**Response  `204`**

#### 

Delete Periodchain

[DELETE](#periodchain-periodchain-delete)`/periodchain/{id}`

Delete a periodchain

#### Example URI

DELETE /periodchain/4126

**URI Parameters**

HideShow

id

`number` (required) **Example:** 4126

Periodchain ID

**Response  `204`**

Periodgroup [¶](#periodgroup)
-----------------------------

A periodgroup contains periods.

### Periodgroup List  [¶](#periodgroup-periodgroup-list)

#### 

Get Periodgroup List

[GET](#periodgroup-periodgroup-list-get)`/periodgroup{?filter,order,format}`

Lists all available periodgroup IDs.

#### Example URI

GET /periodgroup?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the periodgroup list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        3599,
        1814,
        2143,
        800
      ]
    }

#### 

Create Periodgroup

[POST](#periodgroup-periodgroup-list-post)`/periodgroup`

Create a periodgroup

Returns the ID of the newly created periodgroup.

#### Example URI

POST /periodgroup

**Request**

HideShow

JSON Representation of the Periodgroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "periodgroup",
      "readonly": false,
      "properties": {
        "title": "Buchhaltung"
      },
      "children": {
        "period": [
          3600,
          3655,
          3719,
          4279
        ],
        "periodchain": [
          4037
        ],
        "debitorcategory": [
          1863,
          1864,
          1862
        ]
      },
      "links": {},
      "parents": []
    }

**Response  `201`**

HideShow

##### Body

    560

### Periodgroup  [¶](#periodgroup-periodgroup)

#### 

Get Periodgroup

[GET](#periodgroup-periodgroup-get)`/periodgroup/{id}`

Get a periodgroup

#### Example URI

GET /periodgroup/1814

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1814

Periodgroup ID

**Response  `200`**

HideShow

JSON Representation of the Periodgroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "periodgroup",
      "readonly": false,
      "properties": {
        "title": "Buchhaltung"
      },
      "children": {
        "period": [
          3600,
          3655,
          3719,
          4279
        ],
        "periodchain": [
          4037
        ],
        "debitorcategory": [
          1863,
          1864,
          1862
        ]
      },
      "links": {},
      "parents": []
    }

#### 

Update Periodgroup

[PUT](#periodgroup-periodgroup-put)`/periodgroup/{id}`

Update a periodgroup

#### Example URI

PUT /periodgroup/1814

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1814

Periodgroup ID

**Request**

HideShow

##### Body

    {
      "type": "periodgroup",
      "readonly": false,
      "properties": {
        "title": "Buchhaltung"
      },
      "children": {},
      "links": {},
      "parents": []
    }

**Response  `204`**

#### 

Delete Periodgroup

[DELETE](#periodgroup-periodgroup-delete)`/periodgroup/{id}`

Delete a periodgroup

#### Example URI

DELETE /periodgroup/3599

**URI Parameters**

HideShow

id

`number` (required) **Example:** 3599

Periodgroup ID

**Response  `204`**

Quota [¶](#quota)
-----------------

### Quota  [¶](#quota-quota)

#### 

Get Quota

[GET](#quota-quota-get)`/quota`

Returns current and available quota for the current webling store.

A store cannot exceed it’s max value. Upgrade your plan to increase the max quota.

The values of “storage” are in bytes.

A value of `-1` means unlimited.

#### Example URI

GET /quota

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "members": {
        "used": 78,
        "max": 250
      },
      "entries": {
        "used": 486,
        "max": -1
      },
      "periodgroups": {
        "used": 3,
        "max": 3
      },
      "storage": {
        "used": 2688375,
        "max": 262144000
      },
      "credits": {
        "available": 4.9
      }
    }

### Storage Quota  [¶](#quota-storage-quota)

#### 

Get Storage Details

[GET](#quota-storage-quota-get)`/quota/storage`

Returns detailed storage usage. Usage is specified in bytes.

#### Example URI

GET /quota/storage

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "used": 2688375,
      "max": 262144000,
      "member": 1531692,
      "finance": 0,
      "letter": 0,
      "document": [
        {
          "name": "Öffentliche Daten",
          "type": "documentgroup",
          "id": "577",
          "document": 1142810,
          "email": 0,
          "letter": 0
        },
        {
          "name": "Trainer",
          "type": "usergroup",
          "id": "456",
          "document": 0,
          "email": 0,
          "letter": 0
        },
        {
          "name": "Demo Benutzer",
          "type": "user",
          "id": "584",
          "document": 53460,
          "email": 0,
          "letter": 346634
        },
        {
          "name": "Administrator",
          "type": "user",
          "id": "586",
          "document": 0,
          "email": 635868,
          "letter": 0
        }
      ]
    }

Settings [¶](#settings)
-----------------------

### Settings  [¶](#settings-settings)

#### 

Get Settings

[GET](#settings-settings-get)`/setting`

Returns the setting values for the current webling store.

#### Example URI

GET /setting

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "currency": "CHF",
      "country": "Schweiz"
    }

#### 

Update Settings

[PUT](#settings-settings-put)`/setting`

Update settings.

You can omit settings that you do not want to change.

#### Example URI

PUT /setting

**Request**

HideShow

##### Body

    {
      "currency": "CHF",
      "country": "Schweiz"
    }

**Response  `204`**

Track Changes / Replicate [¶](#track-changes-replicate)
-------------------------------------------------------

### How it works [¶](#header-how-it-works)

Every change in the webling dataset creates a new revision with a revision ID (increases with every change). The data you see in the webling frontend is at the latest revision. If you want to synchronize your dataset with the latest changes from Webling, you can use the /replicate or the /changes endpoint. Both endpoints have the same return format.

### Get changes by time (/changes) [¶](#header-get-changes-by-time-(-changes))

The easiest way to get changes ist to call the `/changes/{timestamp}` endpoint. It will return all changes that happened since {timestamp}. The result contains the IDs of the objects with changes. This is especially useful for things that run at a specific interval (e.g. cronjobs).

### Get changes by revision (/replicate) [¶](#header-get-changes-by-revision-(-replicate))

The other option is calling the `/replicate/{revision}` endpoint. It will return all changes that happened since a specific revision. This is especially useful when you are not syncing in a regular interval.

When you start syncing, you need to save the revision ID from the current sync. When you start the next sync cycle, first check if the revision has changed. To do that, you call `/replicate/{revision-id-on-last-sync}` and you’ll get the latest revision ID and all object IDs that have changed (if any). You only need to fetch the objects that changed.

#### Example [¶](#header-example)

Let’s say the current revision is 100:

Calling `/replicate/97` returns all changes in revision 98, 99 and 100.

Calling `/replicate/98` returns all changes in revision 99 and 100.

Calling `/replicate/99` returns all changes in revision 100.

Calling `/replicate/100` returns no changes, since it is the current revision

You would usually call the replicate command with the last known revision (e.g. `/replicate/100`). As soon as there is a new revision, and you call `/replicate/100`, you’ll get the changes and the latest revision in the API response. Now save the new revision as the “latest known revision” for further API calls (next call may be `/replicate/102`).

If you make any changes to the permissions of the API-Key, the endpoint will return `-1` when calling `/replicate/<revision_id>`. You need to clean your cache (if you have any - and you should) and start syncing again, because you may now see different data than before.

### Get Changes since Timestamp  [¶](#track-changes-replicate-get-changes-since-timestamp)

#### 

Get Changes

[GET](#track-changes-replicate-get-changes-since-timestamp-get)`/changes/{timestamp}`

Get all changed objects since the passed timestamp.

`objects` contains all changed object IDs, grouped by type.

`deleted` contains all deleted object IDs. All IDs in deleted are also contained in objects.

`context` reserved for future use

`definitions` if the definition of datatypes has changed, the types will be listed here

`quota` is set to tue if /quota data has changed

`subscription` is set to true if /subscription data has changed

`revision` Latest revision.

`version` Current Webling version.

#### Example URI

GET /changes/1631167410

**URI Parameters**

HideShow

timestamp

`number` (required) **Example:** 1631167410

Unix timestamp since when you want to synchronize

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": {
        "member": [
          469,
          492
        ],
        "membergroup": [
          554,
          552
        ],
        "debitor": [
          848
        ]
      },
      "deleted": [
        492
      ],
      "context": [],
      "definitions": [],
      "quota": true,
      "subscription": false,
      "revision": 1530,
      "version": 720
    }

### Current Revision  [¶](#track-changes-replicate-current-revision)

#### 

Current Revision

[GET](#track-changes-replicate-current-revision-get)`/replicate`

`revision` Latest revision.

`version` Current Webling version.

#### Example URI

GET /replicate

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "revision": 1530,
      "version": 720
    }

### Get Changes after a Revision  [¶](#track-changes-replicate-get-changes-after-a-revision)

#### 

Get Changes

[GET](#track-changes-replicate-get-changes-after-a-revision-get)`/replicate/{id}`

Get all changed objects since a specific revision compared to the latest revision.

`objects` contains all changed object IDs, grouped by type.

`deleted` contains all deleted object IDs. All IDs in deleted are also contained in objects.

`context` reserved for future use

`definitions` if the definition of datatypes has changed, the types will be listed here

`quota` is set to tue if /quota data has changed

`subscription` is set to true if /subscription data has changed

`revision` Latest revision.

`version` Current Webling version.

#### Example URI

GET /replicate/1529

**URI Parameters**

HideShow

id

`number` (required) **Example:** 1529

Revision ID

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": {
        "member": [
          469,
          492
        ],
        "membergroup": [
          554,
          552
        ],
        "debitor": [
          848
        ]
      },
      "deleted": [
        492
      ],
      "context": [],
      "definitions": [],
      "quota": true,
      "subscription": false,
      "revision": 1530,
      "version": 720
    }

User [¶](#user)
---------------

Only administrators have access to the `/user` endpoints.

The fields “financeaccess” and “memberaccess” can be one of these values:

*   `none` No access
    
*   `read` Read access
    
*   `read+write` Read & Write access
    

The field “articleaccess” can be one of these values:

*   `none` No access
    
*   `read+write` Read & Write access
    

### User List  [¶](#user-user-list)

#### 

Get User List

[GET](#user-user-list-get)`/user{?filter,order,format}`

Lists all available user IDs

#### Example URI

GET /user?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the user list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        62,
        29,
        30
      ]
    }

#### 

Create User

[POST](#user-user-list-post)`/user`

Create a user

If you do not want to set a password, omit the password field or send `null`.

Returns the ID of the newly created user.

#### Example URI

POST /user

**Request**

HideShow

JSON Representation of the user.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "user",
      "readonly": false,
      "properties": {
        "administrator": false,
        "memberaccess": "none",
        "financeaccess": "none",
        "articleaccess": "none",
        "smsaccess": false,
        "email": "trainer",
        "title": "Demo Trainer",
        "password": null
      },
      "children": {},
      "links": {},
      "parents": [
        456
      ]
    }

**Response  `201`**

HideShow

##### Body

    18010

### User  [¶](#user-user)

#### 

Get User

[GET](#user-user-get)`/user/{id}`

Get a user

The password field is always `null` when fetching data from the Server.

#### Example URI

GET /user/29

**URI Parameters**

HideShow

id

`number` (required) **Example:** 29

User ID

**Response  `200`**

HideShow

JSON Representation of the user.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "user",
      "readonly": false,
      "properties": {
        "administrator": false,
        "memberaccess": "none",
        "financeaccess": "none",
        "articleaccess": "none",
        "smsaccess": false,
        "email": "trainer",
        "title": "Demo Trainer",
        "password": null
      },
      "children": {},
      "links": {},
      "parents": [
        456
      ]
    }

#### 

Update User

[PUT](#user-user-put)`/user/{id}`

Update a user

If you do not want to update the password, omit the password field or send `null`.

#### Example URI

PUT /user/29

**URI Parameters**

HideShow

id

`number` (required) **Example:** 29

User ID

**Request**

HideShow

JSON Representation of the user.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "user",
      "readonly": false,
      "properties": {
        "administrator": false,
        "memberaccess": "none",
        "financeaccess": "none",
        "articleaccess": "none",
        "smsaccess": false,
        "email": "trainer",
        "title": "Demo Trainer",
        "password": null
      },
      "children": {},
      "links": {},
      "parents": [
        456
      ]
    }

**Response  `204`**

#### 

Delete User

[DELETE](#user-user-delete)`/user/{id}`

Delete a user

#### Example URI

DELETE /user/29

**URI Parameters**

HideShow

id

`number` (required) **Example:** 29

User ID

**Response  `204`**

### Onboarding  [¶](#user-onboarding)

#### 

Send Onboarding Mail

[POST](#user-onboarding-post)`/user/{id}/onboarding`

Send a mail to a user with info about his account.

The text `{{invite-link}}` will be replaced with the unique password reset link.

#### Example URI

POST /user/29/onboarding

**URI Parameters**

HideShow

id

`number` (required) **Example:** 29

User ID

**Request**

HideShow

##### Body

    {
      "subject": "Onboarding Mail Title",
      "message": "Onboarding Mail Message, Reset Link: {{invite-link}}"
    }

**Response  `204`**

Usergroup [¶](#usergroup)
-------------------------

Only administrators have access to the `/usergroup` endpoints.

Usergroups are also known as Roles, “Rollen”.

A usergroup contains users and cannot have any parents.

The “customfinanceaccess” and “custommemberaccess” objects contains key value pairs. The key is either a membergroup ID or a periodgroup ID. The value is an access rule, described below.

An access rule is a combination of the following:

*   `+r` add read access
    
*   `-r` remove read access
    
*   `+w` add write access
    
*   `-w` remove write access
    

The access tree is hierarchic and access rules are inherited on subgroups. E.g. if you allow read on the root group, the user can see all descendant child groups too. If you allow writing on a subgroup, this group and all descendants inherit the write-rule.

You can combine the rules to get something like `+r+w` to allow read and write.

### Usergroup List  [¶](#usergroup-usergroup-list)

#### 

Get Usergroup List

[GET](#usergroup-usergroup-list-get)`/usergroup{?filter,order,format}`

Lists all available usergroup IDs.

#### Example URI

GET /usergroup?filter=&order=title ASC&format=

**URI Parameters**

HideShow

filter

`string` (optional) 

Filter the list using the [Query Language](#header-query-language)

order

`string` (optional) **Example:** title ASC

Sort the usergroup list by property and direction

format

`string` (optional) 

Specify `format=full` to get the full object instead of a list of IDs

**Response  `200`**

HideShow

##### Headers

    Content-Type: application/json

##### Body

    {
      "objects": [
        56,
        57
      ]
    }

#### 

Create Usergroup

[POST](#usergroup-usergroup-list-post)`/usergroup`

Create a usergroup

Returns the id of the newly created group.

#### Example URI

POST /usergroup

**Request**

HideShow

JSON Representation of the Usergroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "usergroup",
      "readonly": false,
      "properties": {
        "title": "Kassier",
        "custommemberaccess": {
          "552": "+r+w"
        },
        "customfinanceaccess": {
          "800": "+r+w",
          "1814": "+r"
        }
      },
      "children": {
        "user": [
          62,
          30
        ]
      },
      "parents": [],
      "links": {}
    }

**Response  `201`**

HideShow

##### Body

    1809

### Usergroup  [¶](#usergroup-usergroup)

#### 

Get Usergroup

[GET](#usergroup-usergroup-get)`/usergroup/{id}`

Get a usergroup

#### Example URI

GET /usergroup/2224

**URI Parameters**

HideShow

id

`number` (required) **Example:** 2224

Usergroup ID

**Response  `200`**

HideShow

JSON Representation of the Usergroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "usergroup",
      "readonly": false,
      "properties": {
        "title": "Kassier",
        "custommemberaccess": {
          "552": "+r+w"
        },
        "customfinanceaccess": {
          "800": "+r+w",
          "1814": "+r"
        }
      },
      "children": {
        "user": [
          62,
          30
        ]
      },
      "parents": [],
      "links": {}
    }

#### 

Update Usergroup

[PUT](#usergroup-usergroup-put)`/usergroup/{id}`

Update a usergroup

#### Example URI

PUT /usergroup/2224

**URI Parameters**

HideShow

id

`number` (required) **Example:** 2224

Usergroup ID

**Request**

HideShow

JSON Representation of the Usergroup.

##### Headers

    Content-Type: application/json

##### Body

    {
      "type": "usergroup",
      "readonly": false,
      "properties": {
        "title": "Kassier",
        "custommemberaccess": {
          "552": "+r+w"
        },
        "customfinanceaccess": {
          "800": "+r+w",
          "1814": "+r"
        }
      },
      "children": {
        "user": [
          62,
          30
        ]
      },
      "parents": [],
      "links": {}
    }

**Response  `204`**

#### 

Delete Usergroup

[DELETE](#usergroup-usergroup-delete)`/usergroup/{id}`

Delete a usergroup

#### Example URI

DELETE /usergroup/2224

**URI Parameters**

HideShow

id

`number` (required) **Example:** 2224

Usergroup ID

**Response  `204`**

Generated by [aglio](https://github.com/danielgtaylor/aglio) on 19 Nov 2025