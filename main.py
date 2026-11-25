"""Write the story-32 Wi-Fi name entry to /output/entry.txt.

The story is exactly 32 characters: a cat unplugs the router
mid-funeral, and the Zoom call — and the farewell — is gone.
"""

import os

STORY = "Cat unplugged Dad's funeral Zoom"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
