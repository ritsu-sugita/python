from flaskr import app
from flask import redirect, render_template, url_for, request
import sqlite3

DATABASE = "database.db"


@app.route("/")  # Webアプリのトップurlを示す　トップへリクエスト来たら下のindexを返す

# # トップ画面にアクセスした時に実行される
# def index():
#     #   リストの作り方は以下
#     books = [
#         {"title": "はらべこあおむし", "price": 1200, "arrival_day": "2020年1月1日"},
#         {"title": "ぐりとぐら", "price": 1000, "arrival_day": "2020年2月3日"},
#     ]
#     return render_template("index.html", books=books)


def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute(
        "SELECT * FROM books"
    ).fetchall()  # fetchallを入れるとDBのデータがリストオブジェクトとして取得される
    con.close()

    books = []
    for row in db_books:
        books.append({"title": row[0], "price": row[1], "arrival_day": row[2]})

    return render_template("index.html", books=books)


# フォームが含まれたHTMLページを表示する処理
@app.route("/form")
def form():
    return render_template("form.html")


# 書籍の情報をデータベースに追加して、その後トップページにリダイレクトする処理
@app.route("/register", methods=["POST"])
def register():
    title = request.form["title"]
    price = request.form["price"]
    arrival_day = request.form["arrival_day"]

    con = sqlite3.connect(DATABASE)
    con.execute("INSERT INTO books VALUES(?,?,?)", [title, price, arrival_day])
    con.commit()
    con.close()
    return redirect(url_for("index"))


# 選択した列のデータを削除する処理
@app.route("/delete", methods=["POST", "DELETE"])
def delete():
    title = request.form["title"]

    con = sqlite3.connect(DATABASE)
    con.execute("DELETE FROM books WHERE title=?", (title,))
    con.commit()
    con.close()
    # return redirect(url_for("index"))
    return "OK", 200
