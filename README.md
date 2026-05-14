# CHARBT Telegram Bot

Telegram bot for the CHARBT trading project. It generates candlestick quiz images from historical BTCUSDT data, posts the answer and the next question to a Telegram channel, and schedules a daily poll.

## Features

- Loads local OHLCV CSV market data.
- Randomly selects a chart segment for a trading-direction quiz.
- Generates question and answer candlestick images with `mplfinance`.
- Posts images and a Telegram poll to a configured channel.
- Runs the publishing job on a daily schedule through `python-telegram-bot`.

## Tech Stack

- Python
- python-telegram-bot
- NumPy and pandas
- matplotlib and mplfinance

## Configuration

Create a local `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Set the Telegram bot token:

```env
TELEGRAM_API=replace-with-telegram-bot-token
```

Bot tokens must stay in local environment files or deployment secrets. Do not commit real Telegram credentials.

## Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate sample poll images:

```bash
python test.py
```

Run the bot:

```bash
python charbot.py
```

The bot expects market CSV files in `data/` and writes generated images to `post/question/` and `post/answer/`.
