# Simple MCP Server running locally
A simple Python MCP server is one of the best ways to understand the Model Context Protocol.

# Project structure

<img width="672" height="228" alt="image" src="https://github.com/user-attachments/assets/6c465376-43f3-4718-85d5-81aded99435e" />

# Create a virtual env
D:\Python\python-mcp-server>mkdir python-mcp-server

D:\Python\python-mcp-server>cd python-mcp-server

D:\Python\python-mcp-server>.venv\Scripts\activate

D:\Python\python-mcp-server>pip install requirements.txt

D:\Python\python-mcp-server>pip show mcp

# Open the MCP inspector (Optional)
D:\Python\python-mcp-server>mcp --help

D:\Python\python-mcp-server>mcp dev server.py

<img width="895" height="202" alt="image" src="https://github.com/user-attachments/assets/56a5e2fd-c252-439f-871d-bb4a1ac8c3a4" />

# Run the Server
(.venv) D:\Python\python-mcp-server>python server.py

<img width="965" height="344" alt="image" src="https://github.com/user-attachments/assets/d46b65df-0091-438a-b101-caee906cd8e2" />


# Add the MCP to Claude - Restart Claude Desktop. It should detect all the tools automatically.

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
<img width="960" height="717" alt="image" src="https://github.com/user-attachments/assets/ee3dd569-f0da-4ff3-af8f-33c94721d437" />

# Run the prompts from Claude
<img width="1287" height="1008" alt="image" src="https://github.com/user-attachments/assets/281537ab-991a-4469-8fe6-976552e66430" />


