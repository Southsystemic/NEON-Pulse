import os
import json
import re

# === CONFIG ===
HAR_FILE = "suno.har"          # your exported HAR file
MUSIC_DIR = "suno songs"        # folder where your mp3s are
EXTENSION = ".mp3"             # file extension to rename

# === LOAD HAR FILE ===
with open(HAR_FILE, "r", encoding="utf-8") as f:
    har = json.load(f)

id_to_title = {}

# === EXTRACT all clip titles and IDs from HAR ===
for entry in har["log"]["entries"]:
    content = entry.get("response", {}).get("content", {}).get("text", "")
    if '"clips"' in content:
        try:
            data = json.loads(content)
            for clip in data.get("clips", []):
                track_id = clip.get("id")
                title = clip.get("title", "untitled").strip()
                if track_id and title:
                    # Clean illegal filename characters
                    clean_title = re.sub(r'[\\/*?:"<>|]', "_", title)
                    id_to_title[track_id] = clean_title
        except Exception:
            pass

print(f"Found {len(id_to_title)} track entries in HAR.")

# === RENAME FILES ===
renamed_count = 0
name_conflicts = {}

for filename in os.listdir(MUSIC_DIR):
    if not filename.endswith(EXTENSION):
        continue

    base_name = filename.replace(EXTENSION, "")
    if base_name in id_to_title:
        new_name = id_to_title[base_name]
        # Handle duplicate titles
        if new_name in name_conflicts:
            name_conflicts[new_name] += 1
            new_name = f"{new_name}{name_conflicts[new_name]}"
        else:
            name_conflicts[new_name] = 0

        src = os.path.join(MUSIC_DIR, filename)
        dst = os.path.join(MUSIC_DIR, f"{new_name}{EXTENSION}")
        os.rename(src, dst)
        print(f"✅ {filename} → {new_name}{EXTENSION}")
        renamed_count += 1

print(f"\n🎵 Renamed {renamed_count} files successfully.")
