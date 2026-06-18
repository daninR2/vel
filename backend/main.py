from fastapi import FastAPI, Depends, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Minimalist Fragrance Dupe API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For production, narrow down to your specific Next.js domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/search")
def search_fragrances(q: str = Query(None), db: Session = Depends(get_db)):
    if not q:
        return []
    
    # Query database using simple case-insensitive substring matching
    results = db.query(models.Fragrance).filter(
        (models.Fragrance.name.ilike(f"%{q}%")) | 
        (models.Fragrance.brand.ilike(f"%{q}%"))
    ).all()
    
    output = []
    for f in results:
        output.append({
            "id": f.id,
            "brand": f.brand,
            "name": f.name,
            "notes": f.notes,
            "accords": f.accords,
            "price": f.price_estimate,
            "clones": [
                {
                    "brand": c.clone_brand,
                    "name": c.clone_name,
                    "similarity": c.similarity_score,
                    "price": c.price_estimate,
                    "notes_match": c.notes_match
                } for c in f.clones
            ]
        })
    return output

@app.post("/api/auth/register")
def register(user_data: dict, db: Session = Depends(get_db)):
    username = user_data.get("username")
    password = user_data.get("password")
    if not username or not password:
        raise HTTPException(status_code=400, detail="Missing fields")
    
    existing = db.query(models.User).filter(models.User.username == username).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    
    # Production note: Always hash passwords using bcrypt or passlib
    new_user = models.User(username=username, password_hash=password)
    db.add(new_user)
    db.commit()
    return {"status": "success", "message": "User registered successfully"}

@app.post("/api/auth/login")
def login(user_data: dict, db: Session = Depends(get_db)):
    username = user_data.get("username")
    password = user_data.get("password")
    user = db.query(models.User).filter(models.User.username == username, models.User.password_hash == password).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"status": "success", "token": "mock-jwt-auth-token"}
