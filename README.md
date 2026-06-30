# URL Shortener Telegram Bot

A powerful Telegram bot that instantly shortens URLs, tracks clicks, and manages links directly from Telegram.

## Features

✅ Instant URL Shortening

✅ Custom Short Links

✅ Click Analytics & Tracking

✅ User-Friendly Telegram Commands

✅ Fast & Reliable Link Generation

✅ Multiple URL Shortener API Support

✅ User Management & Admin Controls

✅ MongoDB Database Integration

✅ URL Validation & Security Checks

✅ Easy Deployment on VPS, Railway, Render, Koyeb, and Heroku

---

## Usage

### How to Use

1. Start the bot using `/start`
2. Send any valid URL
3. Receive a shortened URL instantly
4. Track clicks and manage your links

---

## Commands

### User Commands

* `/start` — Start the bot
* `/help` — Show help menu
* `/shorten` — Shorten a URL
* `/stats` — View link statistics
* `/mylinks` — View your shortened links
* `/about` — About the bot

### Admin Commands

* `/users` — View total users
* `/broadcast` — Send message to all users
* `/ban` — Ban a user
* `/unban` — Unban a user
* `/logs` — View bot logs
* `/restart` — Restart the bot

---

## Required Environment Variables

| Variable      | Description            |
| ------------- | ---------------------- |
| API_ID        | Telegram API ID        |
| API_HASH      | Telegram API Hash      |
| BOT_TOKEN     | Telegram Bot Token     |
| OWNER_ID      | Bot Owner Telegram ID  |
| DATABASE_URL  | MongoDB Connection URI |
| DATABASE_NAME | MongoDB Database Name  |

---

## Tech Stack

### Backend

* Python 3.10+
* Pyrogram
* MongoDB

### Database

* MongoDB Atlas

### Deployment

* VPS
* Railway
* Render
* Koyeb
* Heroku

---

## Deployment

Clone the repository:

```bash
git clone https://github.com/karthikrshet/url-shortener-telegram-bot.git
cd url-shortener-telegram-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the bot:

```bash
python bot.py
```

---

## License

This project is licensed under the MIT License.

---

## Author

**Karthik Rajesh Shet**

Founder & CEO, CodeMyFYP

GitHub: https://github.com/karthikrshet

---

⭐ If you found this project useful, please give it a star on GitHub.
