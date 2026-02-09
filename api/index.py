"""
Vercel Serverless Function Handler for FastAPI Backend
This wraps the FastAPI app for Vercel's serverless environment.
"""
import sys
import os

# Add the ai-backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ai-backend'))

from app.main import app

# This is required by Vercel to recognize this as a serverless function
handler = app
