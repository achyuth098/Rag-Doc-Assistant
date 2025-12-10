📄 RAG Doc Assistant (Local Llama 3 + FastAPI + Streamlit)

A fully local, privacy-friendly Retrieval-Augmented Generation (RAG) assistant that lets you upload PDFs, indexes them into a vector database, and answers questions using Llama 3 via Ollama — all running on your machine with zero API costs.

Built with:

FastAPI — backend API

Ollama — local Llama 3 LLM

SentenceTransformers — local embeddings

ChromaDB — persistent local vector database

Streamlit — clean chat UI

Python — main application logic

This project allows you to ingest documents, ask questions, get contextual answers, and see exactly which document chunks were used to generate the answer.

🚀 Features
🔍 Local Document Search (RAG)

Ingest PDFs/text files from data/raw/

Automatic text extraction, chunking, embedding

Semantic search using ChromaDB

Llama 3 generates contextual answers based on retrieved chunks

🧠 100% Local AI

Uses Ollama to run Llama 3 models locally



💬 Chat UI (Streamlit)

Chat-like interface

Shows answers + cited sources

Keeps chat history

Fast and responsive

⚙️ FastAPI Backend

/api/ask — query RAG pipeline

/api/health — system check

Fully modular code structure
