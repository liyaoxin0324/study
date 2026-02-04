import path
from fastapi.params import Query
from fastapi import FastAPI
import datetime
import decimal
from pydantic import BaseModel

# 创建FastAPI对象,新增path导入
app = FastAPI()

class Employee(BaseModel):
    id: int = None
    name: str  #注意这个是必填字段
    birthday: datetime.date = None
    gender: str = None
    mobile: str = None
    email: str = None
    hiredate: datetime.date = None
    salary_base: decimal.Decimal = None
    salary_kpi: decimal.Decimal = None

class Book(BaseModel):
  book_id: int
  book_name: str
  book_year: int
  book_price: float

list_books = []
list_books.append(Book(book_id=1,book_name="第一天",book_year=2001,book_price=13.13))
list_books.append(Book(book_id=2,book_name="第二天",book_year=2002,book_price=12.12))
list_books.append(Book(book_id=3,book_name="第三天",book_year=2003,book_price=14.14))
list_books.append(Book(book_id=4,book_name="第四天",book_year=2004,book_price=15.15))
list_books.append(Book(book_id=5,book_name="第五天",book_year=2005,book_price=16.16))
list_books.append(Book(book_id=6,book_name="第六天",book_year=2006,book_price=17.17))
list_books.append(Book(book_id=7,book_name="第七天",book_year=2007,book_price=18.18))
list_books.append(Book(book_id=8,book_name="第八天",book_year=2008,book_price=19.19))

@app.get("/GET/books/{book_id}")
def get_book(book_id: int):
    result = None
    for book in list_books:
        if book.book_id == book_id:
            result = book
            break
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",          # 指定模块名:对象名
        host = "0.0.0.0",   # 监听地址
        port = 8088,           # 监听端口（80为默认端口）
        reload = True,      # 开发环境启用热重载
        log_level = "info"  # 日志级别
    )