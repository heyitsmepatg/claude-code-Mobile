#!/usr/bin/env python3
"""
YouTube Transcript Extractor
Usage: python3 get_transcript.py <youtube_url_or_video_id>
"""

import sys
import re


def extract_video_id(url_or_id: str) -> str:
    patterns = [
        r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})",
        r"^([A-Za-z0-9_-]{11})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract video ID from: {url_or_id}")


def get_transcript(video_id: str) -> str:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("Install dependency: pip install youtube-transcript-api")
        sys.exit(1)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)
    return " ".join(entry.text for entry in transcript)


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "ylvGv_nJryw"
    video_id = extract_video_id(target)
    print(f"Fetching transcript for video ID: {video_id}\n")
    text = get_transcript(video_id)
    print(text)

    output_file = f"{video_id}_transcript.txt"
    with open(output_file, "w") as f:
        f.write(text)
    print(f"\nTranscript saved to: {output_file}")


if __name__ == "__main__":
    main()
