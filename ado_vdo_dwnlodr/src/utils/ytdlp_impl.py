from yt_dlp import YoutubeDL

import json
import rich


URL = "https://www.youtube.com/shorts/ju_oqO_MrPM?feature=share"

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ℹ️ ydl.sanitize_info makes the info json-serializable
    rich.print_json(json.dumps(ydl.sanitize_info(info)))
