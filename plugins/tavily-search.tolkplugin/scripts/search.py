#!/usr/bin/env python3
import json, os, sys, urllib.request

args = json.loads(os.environ.get("OPENTOLK_TOOL_ARGS", "{}"))
api_key = os.environ.get("OPENTOLK_SETTINGS_TAVILY_API_KEY", "").strip()

if not api_key:
    print("Error: Tavily API key not configured. Please set it in the plugin settings.", file=sys.stderr)
    sys.exit(1)

query = args.get("query", "").strip()
if not query:
    print("Error: No search query provided.", file=sys.stderr)
    sys.exit(1)

body = {
    "api_key": api_key,
    "query": query,
    "search_depth": args.get("search_depth", "basic"),
    "topic": args.get("topic", "general"),
    "max_results": max(1, min(int(args.get("max_results", 5)), 20)),
    "include_answer": True,
    "include_raw_content": False,
}

req = urllib.request.Request(
    "https://api.tavily.com/search",
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

answer = data.get("answer", "")
results = data.get("results", [])

if answer:
    print("## Answer\n")
    print(answer)
    print("\n---\n")

print("## Sources\n")
for r in results:
    title = (r.get("title") or "").strip()
    url = (r.get("url") or "").strip()
    content = (r.get("content") or "").strip()
    score = r.get("score")
    if not title or not url:
        continue
    score_str = f" (relevance: {score*100:.0f}%)" if score else ""
    print(f"- **{title}**{score_str}")
    print(f"  {url}")
    if content:
        snippet = content[:300] + ("..." if len(content) > 300 else "")
        print(f"  {snippet}")
    print()
