
# Voice Message to Text

A Python script that transcribes WhatsApp voice messages into text using the OpenAI Whisper API. Supports 90+ languages and automatically handles right-to-left text for Hebrew, Arabic, Farsi, and Urdu.

## Features

- Transcribes WhatsApp `.ogg` voice messages to text
- Auto-detects language
- Correct right-to-left rendering for Hebrew, Arabic, Farsi and Urdu
- Simple command-line usage

## Requirements

- Python 3.10+
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/transcribe-idea.git
   cd transcribe-idea
   ```

2. Install dependencies:
   ```
   py -m pip install -r requirements.txt
   ```

3. Create a `.env` file based on `.env.example`:
   ```
   cp .env.example .env
   ```

4. Add your OpenAI API key to `.env`:
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxx
   ```

## Usage

Export the voice message from WhatsApp (hold the message → Forward → Share → Save to Files), then run:

```
py transcribe.py "path\to\your\audio.ogg"
```

Example:
```
py transcribe.py "C:\Users\you\Downloads\WhatsApp Ptt 2026-03-29 at 5.03.22 PM.ogg"
```

## Supported File Formats

`.ogg`, `.opus`, `.mp3`, `.mp4`, `.m4a`, `.wav`

## Cost

Transcription uses the OpenAI Whisper API (`whisper-1`) which costs approximately $0.006 per minute of audio.

## License

MIT
```

---

Now run this to generate your `requirements.txt`:
```
py -m pip freeze > requirements.txt
```

Then commit everything to GitHub:
```
git add .
git commit -m "Add README and requirements.txt"
git push
```

