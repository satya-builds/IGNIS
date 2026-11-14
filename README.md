# 🔥 IGNIS: Spacecraft Fire Safety Intelligence & Synthesis Engine

> Developed for the **NASA Space Apps Challenge**. IGNIS bridges 26 years of microgravity combustion research (1997–2023) to protect future crewed habitats on the Moon, Mars, and Deep Space.

---

## 📂 Repository Architecture

```text
ignis-space-apps/
├── backend/                  # FastAPI & Deterministic SI Synthesis Engine
│   ├── server.py             # Main FastAPI application entrypoint
│   ├── seed.py               # Database & archive seeding script
│   ├── requirements.txt      # Python dependencies
│   ├── data/                 # 18 NASA PSI microgravity flight investigations & environments
│   │   ├── __init__.py
│   │   ├── environments.py
│   │   ├── part1.py
│   │   ├── part2.py
│   │   └── part3.py
│   ├── lib/                  # Core database & SI synthesis logic
│   │   ├── db.py
│   │   └── si.py
│   ├── models/               # Pydantic v2 schemas
│   │   ├── __init__.py
│   │   └── investigation.py
│   └── routers/              # API endpoints
│       ├── __init__.py
│       ├── ai.py
│       └── investigations.py
├── frontend/                 # React + TypeScript + Vite Dashboard
│   ├── index.html
│   ├── package.json
│   └── src/
│       ├── App.tsx
│       ├── index.css
│       ├── components/       # Reusable UI & data visualizations
│       │   ├── FlameVisualizer.tsx
│       │   ├── InvestigationCard.tsx
│       │   ├── PageTransition.tsx
│       │   ├── SiteHeader.tsx
│       │   └── charts.tsx
│       ├── lib/              # State management, types, colors & client SI engine
│       │   ├── colors.ts
│       │   ├── images.ts
│       │   ├── siEngine.ts
│       │   ├── store.ts
│       │   └── types.ts
│       └── pages/            # Route views
│           ├── AiInsights.tsx
│           ├── Compare.tsx
│           ├── InvestigationDetail.tsx
│           ├── Investigations.tsx
│           └── Overview.tsx
├── docs/                     # Architecture & project specifications
│   └── SPEC.md
└── .gitignore
```

---

## ⚙️ Quick Start

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn server:app --reload --port 8000
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
