import sys
import os
import unicodedata
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
client = OpenAI()  # automatically picks up OPENAI_API_KEY from .env

# Unicode ranges for RTL scripts
RTL_RANGES = [
    (0x0590, 0x05FF),  # Hebrew
    (0x0600, 0x06FF),  # Arabic
    (0x0700, 0x074F),  # Syriac
    (0x0750, 0x077F),  # Arabic Supplement
    (0x0800, 0x083F),  # Samaritan
    (0x08A0, 0x08FF),  # Arabic Extended-A
    (0xFB1D, 0xFDFF),  # Hebrew/Arabic Presentation Forms
    (0xFE70, 0xFEFF),  # Arabic Presentation Forms-B
]


def is_rtl(text):
    rtl_count = sum(
        1 for ch in text
        if any(start <= ord(ch) <= end for start, end in RTL_RANGES)
    )
    return rtl_count > len(text) * 0.2


def format_for_display(text):
    if not is_rtl(text):
        return text
    try:
        from bidi.algorithm import get_display
        try:
            import arabic_reshaper
            text = arabic_reshaper.reshape(text)
        except ImportError:
            pass
        return get_display(text)
    except ImportError:
        # Fallback: prepend RLM marker so terminals that support it render correctly
        return "\u200F" + text


def transcribe(audio_path):
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
        )

    return transcript.text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py transcribe.py <audio_file_path>")
        sys.exit(1)

    text = transcribe(sys.argv[1])
    print(format_for_display(text))
