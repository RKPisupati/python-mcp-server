# Changes to make in `server.py`

Everything else in your file (the tools, the sample data) stays exactly the
same. Only the bottom `if __name__ == "__main__":` block changes.

## 1. Add an import at the top

```python
import os
```

## 2. Replace the bottom block

**Before:**

```python
if __name__ == "__main__":
    print("PythonDemoServer started successfully.")
    print("Waiting for an MCP client...")
    mcp.run()
```

**After:**

```python
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print("PythonDemoServer started successfully.")
    print(f"Listening for MCP clients on 0.0.0.0:{port}/mcp")
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
```

Reading `PORT` from the environment matters because Render, Railway, and Fly
all assign a random port at runtime and pass it in via `$PORT` — hardcoding
8000 will make the deploy fail its health check on some of these platforms.

## 3. (Strongly recommended) Add a simple auth check

Right now anyone with the URL can call every tool, including the sample
taxpayer lookups. FastMCP lets you require a bearer token via middleware.
Simplest version — add this before `mcp.run(...)`:

```python
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

API_KEY = os.environ.get("MCP_API_KEY")  # set this in your host's dashboard

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if API_KEY and request.headers.get("authorization") != f"Bearer {API_KEY}":
            return JSONResponse({"error": "unauthorized"}, status_code=401)
        return await call_next(request)

mcp.settings.middleware = [Middleware(AuthMiddleware)]
```

Then clients must send `Authorization: Bearer <your-key>` on every request.
If you skip this, at minimum don't put anything sensitive in the demo data.
