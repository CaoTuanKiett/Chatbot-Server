from fastapi import FastAPI
from app.routers import users, items
from app.database.database import engine, Base

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

# Import router từ các module
app.include_router(users.router)
app.include_router(items.router)

# Khởi tạo cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI and MySQL!"}
