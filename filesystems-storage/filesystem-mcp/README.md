# Local Filesystem MCP Server

Provides secure, configurable local directory read/write access to AI models, allowing direct file manipulation within allowed paths.

> Part of **[MCP Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Source URL**: [https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
- **Author**: Model Context Protocol Team
- **License**: MIT
- **Transport**: `stdio`
- **Date Added**: 2026-06-21

## Tools Exposed
- `read_file`:  Retrieve file content.
- `write_file`:  Write or overwrite file contents.
- `list_directory`:  List child files and folders in a path.
