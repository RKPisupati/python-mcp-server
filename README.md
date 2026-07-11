# Simple MCP Server running locally
A simple Python MCP server is one of the best ways to understand the Model Context Protocol.

# Project structure
python-mcp-server/
│
├── server.py
├── requirements.txt
└── README.md

# Create a virtual env
mkdir python-mcp-server
cd python-mcp-server
.venv\Scripts\activate
pip install requirements.txt
pip show mcp

# Open the MCP inspector (Optional)
mcp --help
mcp dev server.py

# Run the Server
python server.py

# Add the MCP to Claude - Restart Claude Desktop. It should detect the three tools automatically.

{
  "mcpServers": {
    "PythonDemoServer": {
      "command": "python",
      "args": [
        "D:\\Python\\python-mcp-server\\server.py"
      ]
    }
  }
}

