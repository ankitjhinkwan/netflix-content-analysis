# 🚀 Ankit Jinkwan — Portfolio

A modern full-stack portfolio with a Node.js + Express backend that sends real emails through the contact form.

---

## 📁 Project Structure

```
portfolio/
├── public/              ← Frontend (served by Express)
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── backend/
│   └── server.js        ← Express server + contact form API
├── .env.example         ← Environment variables template
├── .env                 ← Your actual secrets (DO NOT commit!)
├── .gitignore
└── package.json
```

---

## ⚙️ Setup (3 Steps)

### Step 1 — Install Dependencies
```bash
npm install
```

### Step 2 — Configure Gmail

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. **Security** → Enable **2-Step Verification**
3. **Security** → **App Passwords**
4. Select **Mail** + **Windows Computer** → Generate
5. Copy the 16-character password

Create your `.env` file:
```bash
cp .env.example .env
```

Edit `.env`:
```
EMAIL_USER=ankitjhinkwan9@gmail.com
EMAIL_PASS=abcd efgh ijkl mnop   ← paste your App Password here
PORT=3000
```

### Step 3 — Run the Server
```bash
# Development (auto-restarts on changes)
npm run dev

# Production
npm start
```

Open your browser: **http://localhost:3000**

---

## 📬 How the Contact Form Works

1. User fills out the form and clicks **Send Message**
2. Frontend sends a `POST /api/contact` request
3. Backend validates and sanitizes the input
4. Two emails are sent simultaneously:
   - 📥 **You receive** a formatted notification email with the message
   - 📤 **Sender receives** a professional auto-reply confirmation
5. Rate limited to **5 messages per IP per 15 minutes** (anti-spam)

---

## 🌐 Deploying to Production

### Option A — Railway (easiest)
1. Push your code to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Add environment variables in Railway dashboard
4. Done! Railway provides a public URL

### Option B — Render
1. Push to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect repo, set `npm start` as start command
4. Add environment variables
5. Deploy

### Option C — VPS (DigitalOcean/AWS)
```bash
# Install PM2 for process management
npm install -g pm2
pm2 start backend/server.js --name "portfolio"
pm2 startup
pm2 save
```

---

## 🔒 Security Features
- ✅ Helmet.js security headers
- ✅ Rate limiting (5 req/IP/15min on contact form)
- ✅ Input validation & sanitization
- ✅ Environment variables for secrets
- ✅ CORS protection

---

## 🛠️ Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | HTML5, CSS3, Vanilla JS |
| Backend | Node.js, Express |
| Email | Nodemailer + Gmail SMTP |
| Security | Helmet, express-rate-limit |

---

Made with ❤️ by **Ankit Jinkwan** — Uttarakhand, India