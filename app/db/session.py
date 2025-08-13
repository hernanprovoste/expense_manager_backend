from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    connect_args={},
    pool_pre_ping=True
)

def create_db_and_tables():
    """
        Function that create database and tables defined by SQLModel if not exists.
    """
    SQLModel.metadata.create_all(engine)
    print("Database and tables created successfully.")

def get_session():
    """
        Generate session that will used by dependency injection.
    """
    with Session(engine) as session:
        yield session