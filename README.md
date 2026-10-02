# 🛰️ ISS Overhead Notifier

An automated Python notifier that emails you when the **International Space Station** is passing over your location — but only when it's **dark outside**, so you can actually see it.

Built as a learning project to practice **REST APIs**, **SMTP email**, and **datetime handling** in Python.

---

## 📸 How It Works

Every 60 seconds the script:

1. Fetches the **current ISS position** from [Open Notify](http://open-notify.org/)
2. Fetches **sunrise & sunset times** for your location from [Sunrise-Sunset API](https://sunrise-sunset.org/api)
3. Checks two conditions:
   - ☀️ **Is it dark?** → current hour is after sunset OR before sunrise
   - 📍 **Is the ISS close?** → within ±5° latitude and longitude of your coordinates
4. If **both** are true → sends an email: **"Look up!"**

---

## ✨ Features

- 🛰️ Real-time ISS position tracking
- 🌅 Timezone-aware sunrise & sunset (via `tzid` parameter)
- 📏 Configurable proximity tolerance (±5° by default)
- 🔐 Secrets stored in `.env` — never committed to git
- ♻️ Runs continuously with error recovery
- 📧 SMTP email alerts via Gmail

---

## 🧠 What I Learned

This project was built to practice three core Python concepts:

### 1. Working with REST APIs (`requests`)
- Making GET requests with `requests.get()`
- Passing query parameters via `params=`
- Checking response status with `raise_for_status()`
- Parsing JSON with `response.json()`
- Navigating nested dictionaries

```python
response = requests.get(
    "https://api.sunrise-sunset.org/json",
    params={"lat": 41.29, "lng": 69.24, "formatted": 0}
)
response.raise_for_status()
data = response.json()
```

### 2. Sending Email (`smtplib`)
- Connecting to Gmail's SMTP server
- Using `starttls()` for a secure connection
- Logging in with an **App Password**
- Composing and sending a message with `sendmail()`
- Properly closing the connection with a `with` block

```python
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs=TO, msg="Subject:Hi\n\nBody")
```

### 3. Date & Time (`datetime`)
- Getting the current local hour with `datetime.now().hour`
- Comparing hours to determine day vs. night
- Understanding timezones and how to stay consistent (UTC vs. local)
- Working with the `tzid` parameter so the API returns local times

```python
hour = datetime.now().hour
is_dark = hour >= sunset or hour <= sunrise
```

---

## 🚀 Setup

### 1. Clone the repository

```bash
git clone git@github.com:kama13a/ISS-Overhead-Notifier.git
git checkout develop
cd ex03
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file

Create a file named `.env` in the project root:

```
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_16_char_app_password
TO_EMAIL=recipient@example.com
MY_LAT=41.299496
MY_LONG=69.240074
```

> ⚠️ `MY_PASSWORD` must be a **Gmail App Password**, not your regular account password. See below.

### 4. Get a Gmail App Password

Gmail blocks regular passwords for SMTP since 2025. You need an App Password:

1. Enable **2-Step Verification** on your Google account
   → https://myaccount.google.com/security
2. Go to **App Passwords**
   → https://myaccount.google.com/apppasswords
3. Generate a new password (e.g. name it "Python SMTP")
4. Copy the 16-character password → paste it into `.env` as `MY_PASSWORD`

### 5. Run the script

```bash
python main.py
```

You'll see a status line every 60 seconds. Press **Ctrl+C** to stop.

---

## 📂 Project Structure

```
ISS-Overhead-Notifier/
├── main.py              # Main script
├── .env                 # Your secrets (NOT committed)
├── .gitignore           # Ignores .env, .venv, etc.
└── README.md            # This file
```

---

## 🧪 Example Output

**When conditions are met:**
```
hour=22 sunrise=6 sunset=18 dlat=1.24 dlon=3.08 dark=True close=True
✅ Email sent
```

**When it's daytime:**
```
hour=14 sunrise=6 sunset=18 dlat=0.80 dlon=2.15 dark=False close=True
❌ Not dark. hour=14, sunrise=6, sunset=18
```

**When the ISS is far away:**
```
hour=23 sunrise=6 sunset=18 dlat=12.40 dlon=8.11 dark=True close=False
❌ ISS too far. dlat=12.40, dlon=8.11
```

---

## 📦 Requirements

- **Python** 3.10+
- **requests** — for API calls
- **python-dotenv** — for loading `.env`


## 📚 APIs Used

- [Open Notify — ISS Location](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
- [Sunrise-Sunset API](https://sunrise-sunset.org/api)

---

## 📜 License

MIT — free to use, modify, and share.

---

## 🙏 Acknowledgements

Built as part of a Python learning journey (Day 33 of 100 Days of Code).
Practiced: **REST APIs**, **SMTP**, and **datetime handling**.