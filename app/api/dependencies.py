from app.db.database import session
"""
his module defines the get_db dependency, 
which creates a database session to be used within FastAPI endpoints. 
It ensures that the session is closed properly after each request.
"""
from sqlalchemy.orm import Session
from app.db.database import Session

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
