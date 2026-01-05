# FedEx DCA AI Hub

An AI-powered Debt Collection Agency (DCA) management platform designed for the FedEx SMART Hackathon.

## Problem
Manual DCA operations cause delays, weak governance, and low recovery predictability.

## Solution
A centralized platform with:
- AI-based recovery prediction
- Automated case prioritization
- SLA tracking & analytics
- Secure DCA portals

## Tech Stack
- Backend: FastAPI
- AI/ML: Scikit-learn
- Frontend: HTML/CSS/JS
- Database: CSV (prototype)

## How to Run
```bash
pip install -r requirements.txt
python data_generator.py
python model.py
uvicorn main:app --reload
