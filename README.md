# Webling API Claude Skill

A comprehensive Claude skill that provides complete guidance for interacting with the [Webling](https://webling.ch) API, an association membership management and accounting software.

**⚠️ Beta Status**: This project is provided as-is without any warranty. Some basic testing was done and proved that the skill works but mistakes WILL be made by the agent. Human validation and thorough testing of generated code is required.

**Disclaimer**: This is an independent project and is not affiliated with, endorsed by, or officially connected to Webling or webling.ch in any way.

## What It Does

This skill enables Claude to understand and work with Webling's complete API, including:
#### Fairly Tested :
- **Member Management**: Members, groups, forms, attendance tracking
- **Finance & Accounting**: Invoices, entries, accounts, periods, cost centers
#### Lightly tested :
- **Documents**: File management and folders
- **Articles**: Inventory and material management
- **Other Features**: Query language, replication/sync, data model navigation
#### Untested or tests failed :
- **Administration**: Users, roles, API keys

## Installation for Claude Code

### Add the marketplace
```bash
/plugin marketplace add utorque/webling-api-claude-skill
```

### Install the skill
```bash
/plugin install webling-api@webling-api
```

Or browse and install interactively:
```bash
/plugin
```

### Verify Installation
List your installed plugins:
```bash
/plugin list
```

## Direct Installation

1. Download the latest `.skill` file from [Releases](https://github.com/utorque/webling-api-claude-skill/releases)
2. Upload it to your Claude environment via the Skills interface

## Usage

Once installed, the skill automatically activates when you work with Webling API operations. Simply ask Claude to help with Webling tasks. Here are two tested examples :
```
"Create a webling api call using python and requests to get a dataframe of all members and their detail."
"Do one to get all bookkeeping entries as a dataframe with columns "Date", "Debit Account", "Credit Account", "Value", "Text"."
```

## What's Included

- Complete endpoint documentation (50+ object types)
- Query language reference with examples
- Data model visualization showing all relationships
- Best practices for API usage and rate limiting
- Real-world usage patterns and workflows

## Contributing

Contributions, bug reports, and feedback are welcome. Please test thoroughly before submitting.

## License

MIT License - See [LICENSE](LICENSE) for details
