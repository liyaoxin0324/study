from fastapi import FastAPI
app = FastAPI()
# 创建FastAPI对象


# 定义路由
class bookname:
    # @app.get("/id/tittle/year/price")
    def __init__(self, id: int, name: str, price: float, year: int):
        self.id = id
        self.name = name
        self.price = price
        self.year = year

book1 = bookname(1, "第二天", 12.23, 2021)
book2 = bookname(2, "第三天", 11.11, 2022)
book3 = bookname(3, "第四天", 13.33, 2023)
book4 = bookname(4, "第五天", 14.44, 2024)
book5 = bookname(5, "第六天", 15.55, 2025)
book6= bookname(6, "第七天", 16.66, 2026)
book7 = bookname(7, "第八天", 17.77, 2027)
book8 = bookname(8, "第九天", 18.88, 2028)

cont=[book1, book2, book3, book4, book5, book6, book7, book8]
for i in cont :
    print(i)


@app.get("/")
def home():
    return cont
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",  # 指定模块名:对象名
        host="0.0.0.0",  # 监听地址
        port=8088,  # 监听端口（80为默认端口）
        reload=True,  # 开发环境启用热重载
        log_level="info"  # 日志级别
  )
