Outflow.AI - AI Automation Orchestration 



Smart Attendance System using Facial recognition
An offline facial recognition system that automates attendance using a laptop webcam. Users are first enrolled by capturing their facial embeddings, and during attendance mode the system detects faces in real time, compares embeddings, and logs verified matches with timestamps. It includes multi-frame confirmation to reduce false positives and prevents duplicate entries per session.

Tech Stack:
Language: Python
Computer Vision: OpenCV
Face Recognition: face_recognition (dlib-based deep learning embeddings)
Database: SQLite (local storage)
Export: CSV (attendance reports)
Platform: Offline laptop webcam application


API Key Management
A developer-focused SaaS that lets users generate, manage, and monitor API keys for their applications.
It includes secure key generation (hashed storage), rate limiting, request logging, and usage analytics. Developers can create projects, issue API keys, set limits, and view traffic statistics through a dashboard. Built with FastAPI middleware for validation and Supabase for storage, it demonstrates backend architecture, security practices, and real-time monitoring. 

Tech Stack:
Backend: FastAPI
Database/Auth: Supabase (Postgres + RLS)
Cache/Rate Limiting: Redis
Frontend: Next.js (TypeScript)
Deployment: Vercel (frontend), Railway/Render (backend)


Receipt-to-Expenses Pipeline
A consumer-facing data pipeline that converts receipt images into structured expense records.
Users upload receipt photos, the system performs OCR, extracts key fields (merchant, date, total), categorizes the transaction, and stores it in a database. It then generates spending summaries and category analytics through a dashboard. The project highlights ingestion, transformation, normalization, and analytics in a clean ETL workflow.

Tech Stack:
Frontend: Next.js (TypeScript)
Backend: FastAPI
OCR: Tesseract or Google Vision API
Database/Auth/Storage: Supabase (Postgres + Storage)
Background Jobs: APScheduler or Celery
Deployment: Vercel (frontend), Railway/Render (backend)


Portfolio 