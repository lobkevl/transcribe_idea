import sys
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
client = OpenAI()  # automatically picks up OPENAI_API_KEY from .env


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
    print(text)
