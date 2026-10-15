---
title: Myanmar Text to Speech
emoji: 🎙️
colorFrom: purple
colorTo: indigo
sdk: gradio
sdk_version: 5.0.0
app_file: app.py
pinned: false
---

# မြန်မာစာ အသံပြောင်းစက်

Thiha (အမျိုးသား) နှင့် Nilar (အမျိုးသမီး) Burmese neural voices ကို ရွေးချယ်ပြီး မြန်မာစာမှ MP3 အသံဖန်တီးနိုင်သော app ဖြစ်သည်။

## ကိုယ်ပိုင်စက်တွင် စမ်းသပ်ရန်

1. Python 3.10+ တပ်ဆင်ပါ။
2. Terminal/Command Prompt တွင် `pip install -r requirements.txt` ကို run ပါ။
3. `python app.py` ကို run ပါ။
4. ပြသလာသော local URL ကို browser ဖြင့်ဖွင့်ပါ။

အသံဖန်တီးရန် အင်တာနက်လိုအပ်သည်။ Edge TTS ဝန်ဆောင်မှု၏ ရရှိနိုင်မှုနှင့် စည်းမျဉ်းများအပေါ် မူတည်သည်။

## Hugging Face Spaces တွင် တင်ရန်

1. Hugging Face အကောင့်ဖွင့်ပြီး New Space ကိုနှိပ်ပါ။
2. SDK ကို Gradio ရွေးပါ။
3. `app.py`, `requirements.txt`, `README.md` ကို upload လုပ်ပါ။
4. Build ပြီးသွားလျှင် Space URL မှ app ကိုအသုံးပြုနိုင်ပါသည်။
