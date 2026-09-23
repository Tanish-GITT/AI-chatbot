# Render Deployment Guide

## Quick Deploy to Render

### 1. Create Render Account
- Go to https://render.com
- Sign up with GitHub

### 2. Create Web Service
- Click "New +" → "Web Service"
- Connect your GitHub repo: `AI-chatbot`
- Select the repo

### 3. Configure Service
Fill in these settings:

**Name:** `ai-chatbot` (or any name)

**Environment:** `Python 3`

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn app:app
```

### 4. Add Environment Variables
Click "Advanced" → "Add Environment Variable"

Add:
```
OPENAI_API_KEY=sk-your-actual-key-here
FLASK_ENV=production
PORT=10000
```

### 5. Deploy
- Click "Create Web Service"
- Render will build and deploy automatically
- You'll get a URL like: `https://ai-chatbot-xxxxx.onrender.com`

### 6. Update Portfolio
After deployment, update your portfolio's `index.html`:

```javascript
window.CHATBOT_API_URL = 'https://ai-chatbot-xxxxx.onrender.com';
```

Then push the portfolio changes.

---

## Free Tier Notes

- **Spins down after 15 min of inactivity** (wakes on first request, ~30 sec delay)
- **Monthly limits:** Generous for hobby use
- No credit card required for first month

## If You Hit Issues

1. Check Render logs: Dashboard → Service → Logs
2. Verify OPENAI_API_KEY is set in Render env vars
3. Test API: `curl https://your-url/` should return status OK

## Next: Production Improvements

After initial deploy works, consider:
- PostgreSQL instead of SQLite (Render offers free tier)
- Increase model timeout if needed
- Add rate limiting
