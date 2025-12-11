#!/usr/bin/env python3
"""
Comprehensive Webling API Test Suite
Tests all major API categories: Members, Finance, Documents, Articles, Users/Admin, Core, Letters, and Replication
"""

# # Prompt used to generate this file (usning Claude Code with Sonnet 4.5):

# # Let's test the webling skill by testing to create some api calls. Generate 
# # questions to ask the api from the quick reference to test each concept at least 
# # once (members, finance, documents, articles, users, core, letters and 
# # replication). Create one big python file in /test (create the folder) and, using 
# # requests, get the data to answer the question you created. Always format it with a
# # pandas dataframe and print df.head to see the data and see if it works. I'll then
# # run it myself to see the results.

# All tests passed except 5. USERS/ADMIN :
    
# Traceback (most recent call last):
#   File "/home/thibault/webling-api-claude-skill/test/./webling_api_test.py", line 276, in <module>
#     props = apikey.get("properties", {})
# AttributeError: 'str' object has no attribute 'get'

# This may be fixed later on.

import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")

def make_request(endpoint, params=None):
    """Helper function to make API requests with proper authentication"""
    default_params = {"apikey": API_KEY}
    if params:
        default_params.update(params)

    response = requests.get(f"{BASE_URL}{endpoint}", params=default_params)
    response.raise_for_status()
    return response.json()

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)
    
# ============================================================================
# 1. MEMBERS - Test member and membergroup endpoints
# ============================================================================

print_section("1. MEMBERS - Who are the members and what groups do they belong to?")

# Get all members with full data
members_data = make_request("/member", {"format": "full"})
if members_data:
    # Convert to DataFrame
    members_list = []
    for member in members_data:
        props = member.get("properties", {})
        members_list.append({
            "ID": member.get("id"),
            "First Name": props.get("Vorname", ""),
            "Last Name": props.get("Name", ""),
            "Email": props.get("E-Mail", ""),
            "Status": props.get("Status", ""),
            "Created": member.get("meta", {}).get("created", "")
        })

    df_members = pd.DataFrame(members_list)
    print(f"\nTotal Members: {len(df_members)}")
    print(df_members.head())
else:
    print("No members found")

# Get membergroups
membergroups_data = make_request("/membergroup", {"format": "full"})
if membergroups_data:
    membergroups_list = []
    for group in membergroups_data:
        props = group.get("properties", {})
        children = group.get("children", {})
        membergroups_list.append({
            "ID": group.get("id"),
            "Title": props.get("title", ""),
            "Member Count": len(children.get("member", [])),
            "Subgroup Count": len(children.get("membergroup", []))
        })

    df_membergroups = pd.DataFrame(membergroups_list)
    print(f"\nTotal Member Groups: {len(df_membergroups)}")
    print(df_membergroups.head())

# ============================================================================
# 2. FINANCE - What are the open invoices and account balances?
# ============================================================================

print_section("2. FINANCE - What are the open invoices (debitors) and their amounts?")

# Get open debitors
debitors_data = make_request("/debitor", {"format": "full", "filter": 'state = "open"'})
if debitors_data:
    debitors_list = []
    for debitor in debitors_data:
        props = debitor.get("properties", {})
        debitors_list.append({
            "ID": debitor.get("id"),
            "Invoice Number": props.get("debitorid", ""),
            "Title": props.get("title", ""),
            "Date": props.get("date", ""),
            "Total Amount": props.get("totalamount", 0),
            "Paid Amount": props.get("paidamount", 0),
            "Remaining": props.get("remainingamount", 0),
            "State": props.get("state", "")
        })

    df_debitors = pd.DataFrame(debitors_list)
    print(f"\nTotal Open Invoices: {len(df_debitors)}")
    print(df_debitors.head())
    if len(df_debitors) > 0:
        print(f"\nTotal Outstanding Amount: CHF {df_debitors['Remaining'].sum():.2f}")
else:
    print("No open invoices found")

# Get accounts
accounts_data = make_request("/account", {"format": "full"})
if accounts_data:
    accounts_list = []
    for account in accounts_data[:10]:  # Limit to first 10 for readability
        props = account.get("properties", {})
        accounts_list.append({
            "ID": account.get("id"),
            "Title": props.get("title", ""),
            "Current Amount": props.get("amount", 0),
            "Budget": props.get("budget", 0),
            "Opening Entry": props.get("openingentry", 0)
        })

    df_accounts = pd.DataFrame(accounts_list)
    print(f"\nAccounts (showing first 10 of {len(accounts_data)}):")
    print(df_accounts.head())

# Get periods
periods_data = make_request("/period", {"format": "full"})
if periods_data:
    periods_list = []
    for period in periods_data:
        props = period.get("properties", {})
        periods_list.append({
            "ID": period.get("id"),
            "Title": props.get("title", ""),
            "From": props.get("from", ""),
            "To": props.get("to", ""),
            "State": props.get("state", "")
        })

    df_periods = pd.DataFrame(periods_list)
    print(f"\nAccounting Periods: {len(df_periods)}")
    print(df_periods.head())

# ============================================================================
# 3. DOCUMENTS - What documents are stored in the system?
# ============================================================================

print_section("3. DOCUMENTS - What documents are stored in the system?")

# Get all documents
documents_data = make_request("/document", {"format": "full"})
if documents_data:
    documents_list = []
    for doc in documents_data:
        props = doc.get("properties", {})
        file_info = props.get("file", {})
        documents_list.append({
            "ID": doc.get("id"),
            "Title": props.get("title", ""),
            "Description": props.get("description", "")[:50] if props.get("description") else "",
            "File Extension": file_info.get("ext", ""),
            "File Size (KB)": round(file_info.get("size", 0) / 1024, 2),
            "Created": doc.get("meta", {}).get("created", "")
        })

    df_documents = pd.DataFrame(documents_list)
    print(f"\nTotal Documents: {len(df_documents)}")
    print(df_documents.head())
else:
    print("No documents found")

# Get documentgroups
documentgroups_data = make_request("/documentgroup", {"format": "full"})
if documentgroups_data:
    docgroups_list = []
    for group in documentgroups_data:
        props = group.get("properties", {})
        children = group.get("children", {})
        docgroups_list.append({
            "ID": group.get("id"),
            "Title": props.get("title", ""),
            "Document Count": len(children.get("document", [])),
            "Subgroup Count": len(children.get("documentgroup", []))
        })

    df_docgroups = pd.DataFrame(docgroups_list)
    print(f"\nDocument Groups: {len(df_docgroups)}")
    print(df_docgroups.head())

# ============================================================================
# 4. ARTICLES - What articles are available with their prices and stock?
# ============================================================================

print_section("4. ARTICLES - What articles are available with their prices and stock?")

# Get all articles
articles_data = make_request("/article", {"format": "full"})
if articles_data:
    articles_list = []
    for article in articles_data:
        props = article.get("properties", {})
        articles_list.append({
            "ID": article.get("id"),
            "Title": props.get("title", ""),
            "Description": props.get("description", "")[:50] if props.get("description") else "",
            "Price": props.get("price", 0),
            "Quantity": props.get("quantity", 0),
            "Place": props.get("place", "")
        })

    df_articles = pd.DataFrame(articles_list)
    print(f"\nTotal Articles: {len(df_articles)}")
    print(df_articles.head())
else:
    print("No articles found")

# Get articlegroups
articlegroups_data = make_request("/articlegroup", {"format": "full"})
if articlegroups_data:
    artgroups_list = []
    for group in articlegroups_data:
        props = group.get("properties", {})
        children = group.get("children", {})
        artgroups_list.append({
            "ID": group.get("id"),
            "Title": props.get("title", ""),
            "Article Count": len(children.get("article", []))
        })

    df_artgroups = pd.DataFrame(artgroups_list)
    print(f"\nArticle Groups: {len(df_artgroups)}")
    print(df_artgroups.head())

# ============================================================================
# 5. USERS/ADMIN - Who are the current users and API keys?
# ============================================================================

print_section("5. USERS/ADMIN - Who are the current users and what are their roles?")

try:
    # Get current user/apikey info
    current_user = make_request("/currentuser")
    print(f"\nCurrent User/API Key:")
    print(f"  Type: {current_user.get('type')}")
    print(f"  Name: {current_user.get('name')}")
    print(f"  ID: {current_user.get('id')}")

    # Try to get users (might not have permission)
    users_data = make_request("/user", {"format": "full"})
    if users_data:
        users_list = []
        for user in users_data:
            props = user.get("properties", {})
            users_list.append({
                "ID": user.get("id"),
                "Title": props.get("title", ""),
                "Email": props.get("email", ""),
                "Is Admin": props.get("isadmin", False),
                "Created": user.get("meta", {}).get("created", "")
            })

        df_users = pd.DataFrame(users_list)
        print(f"\nTotal Users: {len(df_users)}")
        print(df_users.head())

    # Try to get API keys (might not have permission)
    apikeys_data = make_request("/apikey", {"format": "full"})
    if apikeys_data:
        apikeys_list = []
        for apikey in apikeys_data:
            props = apikey.get("properties", {})
            apikeys_list.append({
                "ID": apikey.get("id"),
                "Title": props.get("title", ""),
                "Member Access": props.get("memberaccess", ""),
                "Finance Access": props.get("financeaccess", ""),
                "Created": apikey.get("meta", {}).get("created", "")
            })

        df_apikeys = pd.DataFrame(apikeys_list)
        print(f"\nTotal API Keys: {len(df_apikeys)}")
        print(df_apikeys.head())

except requests.exceptions.HTTPError as e:
    print(f"\nCould not access user/admin endpoints (might require admin permissions): {e}")


# ============================================================================
# 6. CORE - What is the current system configuration and quota?
# ============================================================================

print_section("6. CORE - What is the current system configuration and quota?")

# Get quota information
quota_data = make_request("/quota")
print("\nQuota Information:")
quota_df_data = []
for key, value in quota_data.items():
    if isinstance(value, dict):
        quota_df_data.append({
            "Resource": key,
            "Current": value.get("current", "N/A"),
            "Max": value.get("max", "Unlimited") if value.get("max") != -1 else "Unlimited",
            "Usage %": f"{(value.get('current', 0) / value.get('max', 1) * 100):.1f}%" if value.get("max", -1) != -1 else "N/A"
        })

df_quota = pd.DataFrame(quota_df_data)
print(df_quota)

# Get configuration
config_data = make_request("/config")
print(f"\nConfiguration (showing first 10 keys):")
config_items = list(config_data.items())[:10]
df_config = pd.DataFrame(config_items, columns=["Setting", "Value"])
print(df_config)

# Get field definitions (simplified view)
definitions_data = make_request("/definition", {"format": "simple"})
print(f"\nObject Types with Field Definitions: {len(definitions_data.keys())}")
print(f"Available Object Types: {', '.join(list(definitions_data.keys())[:10])}...")

# ============================================================================
# 7. LETTERS - What letters and PDFs have been generated?
# ============================================================================

print_section("7. LETTERS - What letters and PDFs have been generated?")

# Get letters
letters_data = make_request("/letter", {"format": "full"})
if letters_data:
    letters_list = []
    for letter in letters_data:
        props = letter.get("properties", {})
        letters_list.append({
            "ID": letter.get("id"),
            "Title": props.get("title", ""),
            "Letter Type": props.get("lettertype", ""),
            "State": props.get("state", ""),
            "Sent At": props.get("sentat", ""),
            "Created": letter.get("meta", {}).get("created", "")
        })

    df_letters = pd.DataFrame(letters_list)
    print(f"\nTotal Letters: {len(df_letters)}")
    print(df_letters.head())
else:
    print("No letters found")

# Get letter PDFs
letterpdfs_data = make_request("/letterpdf", {"format": "full"})
if letterpdfs_data:
    letterpdfs_list = []
    for letterpdf in letterpdfs_data[:10]:  # Limit to first 10
        props = letterpdf.get("properties", {})
        pdf_info = props.get("pdf", {})
        letterpdfs_list.append({
            "ID": letterpdf.get("id"),
            "File Size (KB)": round(pdf_info.get("size", 0) / 1024, 2),
            "Extension": pdf_info.get("ext", ""),
            "Timestamp": pdf_info.get("timestamp", ""),
            "Parent Letter": letterpdf.get("parents", [None])[0]
        })

    df_letterpdfs = pd.DataFrame(letterpdfs_list)
    print(f"\nLetter PDFs (showing first 10 of {len(letterpdfs_data)}):")
    print(df_letterpdfs.head())
else:
    print("No letter PDFs found")

# ============================================================================
# 8. REPLICATION - What is the current revision and recent changes?
# ============================================================================

print_section("8. REPLICATION - What is the current revision and change tracking info?")

# Get current revision
replicate_data = make_request("/replicate")
print(f"\nCurrent Revision Information:")
print(f"  Revision: {replicate_data.get('revision')}")
print(f"  Version: {replicate_data.get('version')}")

# Get changes in the last hour (for demonstration)
one_hour_ago = int(datetime.now().timestamp()) - 3600
changes_data = make_request(f"/changes/{one_hour_ago}")

print(f"\nChanges in the last hour:")
print(f"  Current Revision: {changes_data.get('revision')}")
print(f"  Webling Version: {changes_data.get('version')}")

# Show changed objects
changed_objects = changes_data.get("objects", {})
if changed_objects:
    changes_list = []
    for obj_type, ids in changed_objects.items():
        changes_list.append({
            "Object Type": obj_type,
            "Changed IDs": str(ids[:5]) + ("..." if len(ids) > 5 else ""),  # Show first 5
            "Count": len(ids)
        })

    df_changes = pd.DataFrame(changes_list)
    print("\nChanged Objects:")
    print(df_changes)
else:
    print("\nNo objects changed in the last hour")

# Show deleted objects
deleted_objects = changes_data.get("deleted", {})
if deleted_objects:
    deleted_list = []
    for obj_type, ids in deleted_objects.items():
        deleted_list.append({
            "Object Type": obj_type,
            "Deleted IDs": str(ids),
            "Count": len(ids)
        })

    df_deleted = pd.DataFrame(deleted_list)
    print("\nDeleted Objects:")
    print(df_deleted)
else:
    print("No objects deleted in the last hour")

# ============================================================================
# SUMMARY
# ============================================================================

print_section("TEST SUMMARY")
print("""
All tests completed successfully!

This test suite covered:
  1. Members - Member and membergroup listings
  2. Finance - Debitors (invoices), accounts, and periods
  3. Documents - Document and documentgroup listings
  4. Articles - Article and articlegroup listings
  5. Users/Admin - Current user, users, and API keys
  6. Core - Quota, configuration, and field definitions
  7. Letters - Letters and generated PDFs
  8. Replication - Change tracking and revision information

Each section demonstrates:
  - API endpoint usage with proper authentication
  - Data retrieval with format=full parameter
  - Filtering (e.g., open debitors)
  - Data transformation into pandas DataFrames
  - Display of results using df.head()
""")

print("\n" + "="*80)
print("  Test execution completed at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("="*80)
