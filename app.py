import asyncio
import os
import tempfile
import gradio as gr
import edge_tts

VOICES = {
    "Thiha — အမျိုးသားအသံ": "my-MM-ThihaNeural",
    "Nilar — အမျိုးသမီးအသံ": "my-MM-NilarNeural",
}

async def make_speech(text, voice_name, rate, volume):
    if not text or not text.strip():
        raise gr.Error("မြန်မာစာကို အရင်ထည့်ပေးပါ။")

    voice = VOICES[voice_name]
    communicate = edge_tts.Communicate(
        text.strip(),
        voice,
        rate=rate,
        volume=volume,
    )
    fd, output_path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)
    try:
        await communicate.save(output_path)
        return output_path
    except Exception as exc:
        if os.path.exists(output_path):
            os.remove(output_path)
        raise gr.Error(
            "အသံဖန်တီးမရပါ။ အင်တာနက်ချိတ်ဆက်မှုကို စစ်ဆေးပြီး ထပ်ကြိုးစားပါ။"
        ) from exc

def text_to_speech(text, voice_name, speed, loudness):
    rate = f"{int(speed):+d}%"
    volume = f"{int(loudness):+d}%"
    return asyncio.run(make_speech(text, voice_name, rate, volume))

with gr.Blocks(theme=gr.themes.Soft(), title="မြန်မာစာ အသံပြောင်းစက်") as demo:
    gr.Markdown(
        """
        # 🎙️ မြန်မာစာ → အသံ
        မြန်မာစာကို ရိုက်ထည့်ပါ။ Thiha သို့မဟုတ် Nilar အသံကို ရွေးပြီး MP3 အသံဖန်တီးနိုင်ပါတယ်။
        """
    )
    with gr.Group():
        text_input = gr.Textbox(
            label="ဖတ်ပြစေလိုသော စာသား",
            placeholder="ဥပမာ — မင်္ဂလာပါ။ နေကောင်းကြလား။",
            lines=7,
            max_lines=20,
        )
        voice = gr.Radio(
            choices=list(VOICES.keys()),
            value="Thiha — အမျိုးသားအသံ",
            label="အသံရွေးချယ်ပါ",
        )
        with gr.Row():
            speed = gr.Slider(-50, 50, value=0, step=5, label="အမြန်နှုန်း (%)")
            loudness = gr.Slider(-50, 50, value=0, step=5, label="အသံအတိုးအကျယ် (%)")
        generate = gr.Button("🔊 အသံဖန်တီးမည်", variant="primary")
    audio = gr.Audio(label="ဖန်တီးထားသောအသံ", type="filepath")
    generate.click(
        fn=text_to_speech,
        inputs=[text_input, voice, speed, loudness],
        outputs=audio,
    )
    gr.Markdown(
        "မှတ်ချက် — အသံဖန်တီးရန် အင်တာနက်လိုအပ်ပါတယ်။ Edge TTS ဝန်ဆောင်မှုရရှိနိုင်မှုအပေါ် မူတည်နိုင်ပါတယ်။"
    )

if __name__ == "__main__":
    
demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", "10000"))
)
