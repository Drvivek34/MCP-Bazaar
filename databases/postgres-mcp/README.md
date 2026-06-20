# PostgreSQL MCP Server

An official Model Context Protocol server that provides secure read/write access to PostgreSQL databases, allowing schema inspection and query execution.

> Part of **[MCP Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Source URL**: [https://github.com/modelcontextprotocol/servers/tree/main/src/postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)
- **Author**: Model Context Protocol Team
- **License**: MIT
- **Transport**: `stdio`
- **Date Added**: 2026-06-21

## Tools Exposed
- `query`:  Execute a read-only SELECT query.
- `describe_table`:  Inspect columns, keys, and indexes of a table.
- `list_tables`:  Retrieve all tables in the database.
