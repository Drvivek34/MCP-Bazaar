#!/usr/bin/env python3
import os
import re
from datetime import datetime

MCP_BAZAAR_DIR = "/root/bazaars/MCP-Bazaar"

# Add a set of curated, real, high-quality MCP servers
CURATED_MCPS = [
    {
        "name": "GitHub MCP Server",
        "slug": "github-mcp-server",
        "category": "version-control",
        "desc": "GitHub's official Model Context Protocol server enabling agents to read/write repositories, manage issues, pull requests, and review code.",
        "url": "https://github.com/github/github-mcp-server",
        "author": "GitHub",
        "license": "MIT",
        "transport": "stdio",
        "tools": [
            "create_or_update_file: Create or update a file in a repository.",
            "search_code: Search for code inside a repository.",
            "get_issue: Retrieve issue details.",
            "create_pull_request: Open a new pull request."
        ]
    },
    {
        "name": "Chrome DevTools MCP",
        "slug": "chrome-devtools-mcp",
        "category": "dev-tools",
        "desc": "Official Chrome DevTools integration for coding agents, allowing them to inspect, debug, and interact with live web pages.",
        "url": "https://github.com/ChromeDevTools/chrome-devtools-mcp",
        "author": "Google Chrome DevTools Team",
        "license": "BSD-3-Clause",
        "transport": "stdio",
        "tools": [
            "navigate: Navigate the browser to a URL.",
            "click: Click on page elements.",
            "get_html: Retrieve the page's outer HTML structure.",
            "inspect: Query Chrome DevTools elements and styles."
        ]
    },
    {
        "name": "n8n MCP Server",
        "slug": "n8n-mcp",
        "category": "productivity",
        "desc": "An MCP server that allows Claude Desktop, Claude Code, and other editors to inspect, create, and build workflow automations inside n8n.",
        "url": "https://github.com/czlonkowski/n8n-mcp",
        "author": "czlonkowski",
        "license": "MIT",
        "transport": "stdio",
        "tools": [
            "list_workflows: Retrieve a list of n8n workflows.",
            "get_workflow: Fetch a specific workflow JSON configuration.",
            "create_workflow: Construct or modify a workflow.",
            "execute_workflow: Trigger a workflow run."
        ]
    },
    {
        "name": "Xiaohongshu MCP",
        "slug": "xiaohongshu-mcp",
        "category": "social-media",
        "desc": "Model Context Protocol server for integrating Xiaohongshu (RED) API actions, enabling search, analytics, and content publication.",
        "url": "https://github.com/xpzouying/xiaohongshu-mcp",
        "author": "xpzouying",
        "license": "MIT",
        "transport": "stdio",
        "tools": [
            "search_notes: Search public notes on Xiaohongshu.",
            "get_note_detail: Retrieve details of a specific post.",
            "publish_note: Create and publish a post."
        ]
    }
]

def main():
    today_str = datetime.today().strftime("%Y-%m-%d")
    count = 0

    for m in CURATED_MCPS:
        cat_dir = os.path.join(MCP_BAZAAR_DIR, m["category"], m["slug"])
        os.makedirs(cat_dir, exist_ok=True)

        tools_md = "\n".join(f"- `{t.split(':')[0]}`: {t.split(':')[1]}" if ":" in t else f"- `{t}`" for t in m["tools"])

        readme_content = f"""# {m['name']}

{m['desc']}

> Part of **[MCP Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Source URL**: [{m['url']}]({m['url']})
- **Author**: {m['author']}
- **License**: {m['license']}
- **Transport**: `{m['transport']}`
- **Date Added**: {today_str}

## Tools Exposed
{tools_md}
"""
        with open(os.path.join(cat_dir, "README.md"), "w") as f:
            f.write(readme_content)
        count += 1
        print(f"Imported MCP: {m['name']} -> {m['category']}/{m['slug']}")

    print(f"Successfully imported {count} MCP servers.")

if __name__ == "__main__":
    main()
