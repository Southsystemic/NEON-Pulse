import json
import re

with open("suno.har", "r", encoding="utf-8") as f:
    har = json.load(f)

audio_links = []

for entry in har["log"]["entries"]:
    resp = entry.get("response", {})
    content = resp.get("content", {}).get("text", "")
    if '"clips"' in content:
        try:
            data = json.loads(content)
            for clip in data.get("clips", []):
                if clip.get("audio_url"):
                    title = clip.get("title", "untitled")
                    url = clip["audio_url"]
                    audio_links.append(f"{url}")
        except Exception:
            pass  # skip malformed entries

with open("suno_links.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(audio_links))

print(f"✅ Found {len(audio_links)} audio links. Saved to suno_links.txt")
