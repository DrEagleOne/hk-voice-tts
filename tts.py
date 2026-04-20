import asyncio
import edge_tts
import os
from datetime import datetime

class CantoneseTTS:
    def __init__(self, default_voice="zh-HK-HiuMaanNeural", default_rate="+25%", default_output_dir="audio"):
        self.voice = default_voice
        self.rate = default_rate
        self.default_output_dir = default_output_dir

    async def speak(self, text, rate=None, output_dir=None):
        current_rate = rate if rate else self.rate
        target_dir = output_dir if output_dir else self.default_output_dir
        os.makedirs(target_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"voice_{timestamp}.mp3"
        filepath = os.path.abspath(os.path.join(target_dir, filename))
        communicate = edge_tts.Communicate(text, self.voice, rate=current_rate)
        await communicate.save(filepath)
        return f"MEDIA:{filepath}"

if __name__ == "__main__":
    import sys
    async def run():
        text = sys.argv[1] if len(sys.argv) > 1 else "你好，我係地道嘅廣東話 AI。"
        tts = CantoneseTTS()
        print(await tts.speak(text))
    asyncio.run(run())
