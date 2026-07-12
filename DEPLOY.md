# Deploying python-mcp-server publicly

## Step 0 — Update your repo
1. Apply the changes in `server_py_changes.md` to `server.py`.
2. Copy `Dockerfile` into the repo root.
3. Commit and push:
   ```
   git add server.py Dockerfile
   git commit -m "Add HTTP transport + Dockerfile for remote hosting"
   git push
   ```

---

## Option A — Render (easiest, free tier, no card required)

1. Copy `render.yaml` into the repo root, commit, push.
2. Go to https://render.com → sign in with GitHub.
3. New → Blueprint → select `python-mcp-server` repo. Render reads
   `render.yaml` automatically and builds the Dockerfile.
4. In the service's Environment tab, note the auto-generated `MCP_API_KEY`
   value (or set your own).
5. Deploy. Your server will be live at:
   ```
   https://python-mcp-server-<random>.onrender.com/mcp
   ```
6. **Free tier caveat**: the service spins down after ~15 min of no traffic
   and takes ~30-50s to wake back up on the next request. Fine for personal
   use/testing, not for latency-sensitive production use.

---

## Option B — Fly.io (free allowance, faster cold starts)

1. Install the CLI: `curl -L https://fly.io/install.sh | sh`
2. `fly auth login`
3. From the repo root (with `fly.toml` copied in): `fly launch --no-deploy`
   (accept the existing `fly.toml`, don't let it overwrite it)
4. Set your API key as a secret:
   `fly secrets set MCP_API_KEY=$(openssl rand -hex 16)`
5. `fly deploy`
6. Your server is live at:
   ```
   https://python-mcp-server.fly.dev/mcp
   ```
7. **Free tier caveat**: Fly's free allowance covers a small always-on-ish
   VM, but `auto_stop_machines = true` above means it sleeps when idle and
   wakes on request — same tradeoff as Render, usually faster wake time.

---

## Option C — Railway (free trial credit, not a permanent free tier)

1. https://railway.app → New Project → Deploy from GitHub repo.
2. Railway auto-detects the Dockerfile and builds it.
3. Add variable `MCP_API_KEY` in the service's Variables tab.
4. Settings → Networking → Generate Domain to get a public HTTPS URL.
5. **Caveat**: Railway's free tier is trial credit ($5) that expires, not
   an indefinite free plan like Render/Fly — good for a quick demo, not
   for anything long-running.

---

## Connecting a client once deployed

```json
{
  "mcpServers": {
    "PythonDemoServer": {
      "url": "https://<your-deployed-url>/mcp",
      "headers": {
        "Authorization": "Bearer <your-MCP_API_KEY>"
      }
    }
  }
}
```

(Exact config format depends on the specific MCP client you're pointing at
it — Claude Desktop's remote-server config, a custom client, etc.)
