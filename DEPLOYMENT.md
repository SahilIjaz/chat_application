# AgentFlow - Vercel Deployment Guide

## Monorepo Structure
```
chat_application/
├── frontend/          (Next.js frontend)
├── ai-backend/        (Python FastAPI backend source)
├── api/               (Vercel serverless function handler)
├── vercel.json        (Monorepo configuration)
└── README.md
```

## Pre-Deployment Checklist

1. **Environment Variables Ready?**
   - Frontend: `.env.local` (local), `.env.production` (production)
   - Backend: `.env` (local), Vercel dashboard (production)

2. **Git Repository Pushed?**
   - Both frontend and backend committed to GitHub
   - Repository structure: `https://github.com/SahilIjaz/chat_application`

## Step-by-Step Deployment

### 1. Connect GitHub to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project" → "Import Git Repository"
3. Select `SahilIjaz/chat_application`
4. Vercel auto-detects monorepo structure

### 2. Configure Vercel Settings

**Root Directory:** Leave as default (Vercel auto-detects)

**Build & Development Settings:**
- Build Command: `cd frontend && npm run build` (auto-detected)
- Output Directory: `frontend/.next` (auto-detected)
- Install Command: `npm install` (auto-detected)

### 3. Add Environment Variables

**In Vercel Dashboard → Project Settings → Environment Variables:**

#### Development Environment
```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=AgentFlow
```

#### Production Environment
```
NEXT_PUBLIC_API_URL=https://<YOUR_VERCEL_PROJECT>.vercel.app/api
NEXT_PUBLIC_APP_NAME=AgentFlow
GROQ_API_KEY=your_key_here
DATABASE_URL=your_db_url
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

### 4. Deploy

1. Click "Deploy"
2. Wait for build to complete (~2-3 minutes)
3. Frontend deploys to: `https://<YOUR_PROJECT>.vercel.app`
4. Backend (API) available at: `https://<YOUR_PROJECT>.vercel.app/api`

### 5. Test Deployment

```bash
# Test frontend
curl https://<YOUR_PROJECT>.vercel.app

# Test backend
curl -X POST https://<YOUR_PROJECT>.vercel.app/api/agent/run \
  -H "Content-Type: application/json" \
  -d '{"message":"2+2?","user_id":"test","thread_id":"t1"}'
```

## Local Development

### Frontend
```bash
cd frontend
npm install
npm run dev
# Runs on http://localhost:3000
```

### Backend
```bash
cd ai-backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
# Runs on http://localhost:8000
```

## Troubleshooting

### ❌ "Module not found" errors
**Solution:** Check `api/index.py` path references match your directory structure

### ❌ Backend endpoints return 404
**Solution:** Ensure `CORS_ORIGINS` in `app/main.py` includes your Vercel URL:
```python
origins = [
    "http://localhost:3000",
    "https://<YOUR_PROJECT>.vercel.app"
]
```

### ❌ Bad Gateway errors
**Solution:** 
1. Check backend logs: Vercel Dashboard → Deployments → Runtime Logs
2. Ensure all dependencies in `api/requirements.txt`
3. Verify `api/index.py` properly imports your FastAPI app

## Environment Variables Details

### Frontend (.env variables)
- `NEXT_PUBLIC_API_URL`: Backend API base URL (must start with `http://` or `https://`)
- `NEXT_PUBLIC_APP_NAME`: Display name for the app

### Backend (.env variables)
- `PORT`: Server port (Vercel auto-assigns, default 8000)
- `ENV`: Environment (development/production)
- `FRONTEND_URL`: For CORS configuration
- `GROQ_API_KEY`: Groq LLM API key (optional)
- `DATABASE_URL`: PostgreSQL connection string (optional)
- `SMTP_*`: Email configuration (optional)
- `SERPAPI_KEY`: Web search API key (optional)

## Next Steps

1. ✅ Push code to GitHub
2. ✅ Deploy on Vercel
3. 📧 Add real email sending (SMTP configuration)
4. 🔍 Integrate Groq LLM API
5. 💾 Add database persistence (Supabase/PostgreSQL)
6. 📊 Build monitoring dashboard

## Additional Resources

- [Vercel Docs - Python Support](https://vercel.com/docs/concepts/functions/serverless-functions/supported-languages#python)
- [FastAPI + Vercel](https://vercel.com/templates/python/fastapi)
- [Next.js Deployment](https://nextjs.org/learn/basics/deploying-nextjs-app/deploy)

---

**Questions?** Check the main README.md or contact support.
