# 🚀 AgentFlow - AI-Powered Agent Chat Platform

An intelligent conversational AI system with a modern dark-themed interface and powerful multi-tool agent backend.

## ✨ Features

- 💬 **Real-time Chat Interface** - Dark-themed, responsive UI built with Next.js 15
- 🧮 **Mathematical Computation** - Safely evaluates math expressions (2+2, 10*5, etc.)
- 🔍 **Web Search Integration** - Trigger web searches with `search: query` syntax
- ✉️ **Email Automation** - Send emails with `email: to|subject|body` syntax
- 💾 **Database Queries** - Execute database operations with `sql: query` syntax
- 📊 **Conversation History** - Tracks conversations with user and thread management
- 🎨 **Professional UI** - Dark mode, clean design, real-time message display

## 🏗️ Tech Stack

### Frontend
- **Next.js 15** - React framework for production
- **Tailwind CSS** - Utility-first CSS framework
- **TypeScript** - Type-safe JavaScript

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI web server
- **Python 3.9+** - Programming language

## 📁 Project Structure

```
chat_application/
├── frontend/              # Next.js frontend application
│   ├── app/
│   ├── components/
│   ├── package.json
│   └── .env.example
├── ai-backend/            # FastAPI backend application
│   ├── app/
│   │   ├── agents/       # Agent logic and tools
│   │   ├── main.py
│   │   └── __init__.py
│   ├── venv/             # Python virtual environment
│   ├── requirements.txt
│   └── .env.example
├── api/                   # Vercel serverless handler
│   ├── index.py          # ASGI handler for Vercel
│   └── requirements.txt
├── vercel.json           # Vercel monorepo configuration
├── DEPLOYMENT.md         # Complete deployment guide
├── README.md             # This file
└── .gitignore
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.9+
- Git

### Local Development

**1. Clone the repository**
```bash
git clone https://github.com/SahilIjaz/chat_application.git
cd chat_application
```

**2. Set up Frontend**
```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
# Frontend runs on http://localhost:3000
```

**3. Set up Backend** (in a new terminal)
```bash
cd ai-backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
# Backend runs on http://localhost:8000
```

**4. Test the Chat**
- Open http://localhost:3000
- Type a message like:
  - `2 + 2 ?` → Returns `4`
  - `search: python` → Searches the web
  - `what is 100/5?` → Returns `20`

## 🌐 Deployment on Vercel

### One-Click Deploy (Recommended)
1. Push code to GitHub: `git push origin main`
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project" → Import `SahilIjaz/chat_application`
4. Add environment variables (see below)
5. Deploy!

### Environment Variables for Vercel

**In Vercel Dashboard → Environment Variables:**

```
# Production
NEXT_PUBLIC_API_URL=https://<YOUR_PROJECT>.vercel.app/api
NEXT_PUBLIC_APP_NAME=AgentFlow
```

**Deployed URLs:**
- Frontend: https://<YOUR_PROJECT>.vercel.app
- Backend API: https://<YOUR_PROJECT>.vercel.app/api

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed setup instructions.

## 🛠️ API Endpoints

### POST `/agent/run`
Send a message to the agent.

**Request:**
```json
{
  "message": "2 + 2?",
  "user_id": "user@example.com",
  "thread_id": "thread_123"
}
```

**Response:**
```json
{
  "reply": "4"
}
```

**Examples:**
- Math: `"2 + 2?"` → `"4"`
- Web Search: `"search: AI trends 2024"` → `"Searching web for: AI trends 2024"`
- Email: `"email: user@example.com|Subject|Body"` → `"Email sent"`
- Database: `"sql: SELECT * FROM users"` → `"Result of DB query: ..."`

## 📝 Environment Variables

See `.env.example` files in each directory:
- `frontend/.env.example`
- `ai-backend/.env.example`

## 🔧 Configuration

### CORS Settings
Backend accepts requests from:
- `http://localhost:3000` (local frontend)
- `https://*.vercel.app` (production Vercel deployments)

Modify in `ai-backend/app/main.py` if needed.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Open a Pull Request

## 📚 Future Enhancements

- [ ] Document upload & RAG knowledge base
- [ ] Groq LLM integration for advanced reasoning
- [ ] Supabase integration for data persistence
- [ ] Real-time agent thought process dashboard
- [ ] Advanced workflow automation
- [ ] User authentication & multi-user support
- [ ] Conversation export (PDF, JSON)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Sahil Ijaz**
- GitHub: [@SahilIjaz](https://github.com/SahilIjaz)
- LinkedIn: [Sahil Ijaz](https://linkedin.com/in/sahil-ijaz)

## 📞 Support

For issues and questions:
1. Check [DEPLOYMENT.md](./DEPLOYMENT.md) for deployment help
2. Open a GitHub Issue with detailed information
3. Include error logs and environment setup details

---

**Built with ❤️ using Next.js, FastAPI, and Vercel**
