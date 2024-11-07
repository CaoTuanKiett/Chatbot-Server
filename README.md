## RUN APP

`uvicorn app.main:app --reload`

## INSTALL PACKAGE

`pip install -r requirements.txt`

## INIT DATABASE

`python app\database\database.py ` # Tạo database nếu chưa tồn tại
`python app\database\create_tables.py` or `python -m app.database.create_tables` # Tạo các bảng
`python app/database/initdatabase.py ` or `python -m app.database.initdatabase` # Init database demo
