#!/usr/bin/env python3
import json, os, sys, urllib.request

args = json.loads(os.environ.get("OPENTOLK_TOOL_ARGS", "{}"))
api_key = os.environ.get("OPENTOLK_SETTINGS_TAVILY_API_KEY", "").strip()

if not api_key:
    print("Error: Tavily API key not configured. Please set it in the plugin settings.", file=sys.stderr)
    sys.exit(1)

url = args.get("url", "").strip()
if not url:
    print("Error: No URL provided.", file=sys.stderr)
    sys.exit(1)

body = {
    "api_key": api_key,
    "urls": [url],
}

req = urllib.request.Request(
    "https://api.tavily.com/extract",
    data=json.dumps(body).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
except urllib.error.HTTPError as e:
    print(f"Tavily API error ({e.code}): {e.read().decode()}", file=sys.stderr)
    sys.exit(1)

results = data.get("results", [])
failed = data.get("failed_results", [])

for r in results:
    r_url = (r.get("url") or "").strip()
    content = (r.get("raw_content") or "").strip()
    print(f"# {r_url}\n")
    print(content or "(no content extracted)")
    print("\n---\n")

if failed:
    print("## Failed URLs\n")
    for f in failed:
        print(f"- {f.get('url', '')}: {f.get('error', 'unknown error')}")
