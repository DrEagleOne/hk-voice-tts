# HK-Voice-TTS 🇭🇰

A professional wrapper for high-quality Cantonese Text-to-Speech using Microsoft Edge TTS.

## Installation

```bash
pip install edge-tts
```

## Usage

```python
from tts import CantoneseTTS
import asyncio

async def main():
    # Default output directory is 'audio' relative to the script
    tts = CantoneseTTS()
    result = await tts.speak("你好，我係地道嘅廣東話 AI。")
    print(result) # Returns MEDIA:/path/to/file.mp3

asyncio.run(main())
```

## Configuration
- `default_voice`: Use `zh-HK-HiuMaanNeural` for natural Cantonese.
- `default_rate`: Use `+25%` for a professional yet energetic pace.
- `default_output_dir`: Specify where you want the .mp3 files saved.
