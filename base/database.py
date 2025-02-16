import redis

from base.constant import DATABASE_URL
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

def get_connection():
    pass

metadata = MetaData()
Base = declarative_base(metadata=metadata)

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Session = sessionmaker(bind=engine)

async def get_assync_session():
    async with async_session_maker as session:
        yield session


rcache = redis.Redis(host='localhost', port=6379, db=0)


# def create_database():
#     with get_connection() as conn:
#         with conn.cursor() as cursor:
#             cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS images (
#                     image_id SERIAL PRIMARY KEY,
#                     url TEXT
#                 );
#                 CREATE TABLE IF NOT EXISTS texts (
#                     text_id SERIAL PRIMARY KEY,
#                     type_content TEXT NOT NULL DEFAULT 'text',
#                     content TEXT NOT NULL DEFAULT ''
#                 );
#                 CREATE TABLE IF NOT EXISTS users (
#                     user_id SERIAL PRIMARY KEY,
#                     is_admin BOOLEAN NOT NULL DEFAULT FALSE,
#                     is_active BOOLEAN NOT NULL DEFAULT TRUE,
#                     date_reg DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
#                     first_name VARCHAR(255) NOT NULL,
#                     last_name VARCHAR(255) NOT NULL,
#                     email text NOT NULL UNIQUE,
#                     password text NOT NULL,
#                     special_word VARCHAR(40) NOT NULL DEFAULT '',
#                     avatar text,
#                     favorites JSON NOT NULL DEFAULT '{}'
#                 );
#                 CREATE TABLE IF NOT EXISTS pages (
#                     page_id SERIAL PRIMARY KEY,
#                     title TEXT,
#                     author INTEGER REFERENCES users(user_id),
#                     description TEXT NOT NULL DEFAULT '',
#                     url TEXT NOT NULL DEFAULT '',
#                     published_at DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
#                     content JSON NOT NULL DEFAULT '{}'
#                 );
#                 CREATE TABLE IF NOT EXISTS feedback (
#                     feedback_id SERIAL PRIMARY KEY,
#                     user_id INTEGER REFERENCES users(user_id),
#                     page_id INTEGER REFERENCES pages(page_id),
#                     content JSON
#                 );
#                 CREATE TABLE IF NOT EXISTS admins (
#                     user_id INTEGER REFERENCES users(user_id),
#                     token TEXT
#                 );
#                 CREATE TABLE IF NOT EXISTS supporting (
#                     supporting_id SERIAL PRIMARY KEY,
#                     user_id INTEGER REFERENCES users(user_id),
#                     date_sending DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
#                     content JSON NOT NULL DEFAULT '{}'
#                 );
#                 CREATE TABLE IF NOT EXISTS literary_sources (
#                     source_id SERIAL PRIMARY KEY,
#                     content JSON NOT NULL DEFAULT '{}'
#                 );
#                 CREATE TABLE IF NOT EXISTS favorite (
#                     user_id INTEGER REFERENCES users(user_id),
#                     page_id INTEGER REFERENCES pages(page_id),
#                     content JSON NOT NULL DEFAULT '{}'
#                 );
#             ''')
#             conn.commit()
