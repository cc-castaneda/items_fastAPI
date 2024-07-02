""" 
Módulo que proporciona la configuración y utilidades para la conexión 
a la base de datos.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv(".env.test")

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Generador para manejar la creación y cierre de sesiones de db

    Yields:
        SQLAlchemy Session: Una sesión de base de datos
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
