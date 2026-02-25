# Telegram Event Bot

## What it does
- **`/start`**: sends a “first flag found” message + sends the **second clue** as an audio (or falls back to sending the link).
- **`32`**: sends a progress message + the **final clue**: `@neonnomadzz`
- **Anything else**: replies with “wrong message, try again.”

## Setup (Windows PowerShell)
1) Open PowerShell in this folder:

```powershell
cd C:\Users\asjid\telegram-event-bot
```

2) Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3) Set your bot token (do **not** paste it into code):

```powershell
$env:TELEGRAM_BOT_TOKEN="PASTE_YOUR_TOKEN_HERE"
```

4) Run the bot:

```powershell
python .\main.py
```

## Audio clue link
The bot tries to send this as an audio file; if Telegram can’t fetch it as a direct audio, it will send the link instead:
- `https://jumpshare.com/s/uRcvNh4j8ybmW5jRpWxD`

## Security note
If you’ve shared your bot token anywhere public, revoke it via **@BotFather** and generate a new one.
਍