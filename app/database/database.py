import pymysql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load các biến môi trường từ file .env
load_dotenv()

# Lấy thông tin cấu hình từ các biến môi trường
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", "3306")

# URL kết nối tới MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Tạo database nếu chưa tồn tại
def create_database_if_not_exists():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        connection.close()
        print("Create database thành công!")  # Log thông báo khi tạo thành công
    except Exception as e:
        print(f"Lỗi khi tạo database: {e}")  # Log thông báo lỗi

create_database_if_not_exists()

# Kết nối tới database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency để lấy session kết nối
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
