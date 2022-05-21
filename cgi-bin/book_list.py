import sqlite3
import datetime as dt
import io
import sys
import cgi

form = cgi.FieldStorage()
param_str = form.getvalue('param1', '')
current_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
table = ""


db_path = "bookdb.db"			# データベースファイル名を指定

con = sqlite3.connect(db_path)  # データベースに接続
con.row_factory = sqlite3.Row  # 属性名で値を取り出せるようにする
cur = con.cursor()				# カーソルを取得
try:
    # SQL文の実行
    cur.execute(
        "select * from BOOKLIST  WHERE (TITLE LIKE '%{param}%') OR (AUTHOR LIKE '%{author}%')".format(param=param_str,author=param_str))
    # cur.execute("select * from BOOKLIST where (TITLE='%Java%') AND (PRICE<3000) ")z
    rows = cur.fetchall()		# 検索結果をリストとして取得
    if not rows:				# リストが空のとき
        table=param_str + "という本，著者は存在しません"

    else:
        table = '<table><thead><tr><th>ID</th><th>タイトル</th><th>著者</th><th>出版社</th><th>価格</th><th>ISBN</th></tr></thead><tbody>'
        for row in rows:		# 検索結果を1つずつ処理
            table = table +  "<tr>"
            print("ID = %s" % row['ID'])
            table = table + "<td>" + str(row['ID']) + "</td>"
            table = table + "<td>" + "<a rel=\"noopener noreferrer\"  href='https://www.google.com/search?q={}' target='__blank'>".format(row['TITLE']) +  row['TITLE'] + "</a>" +  "</td>"
            table = table + "<td>" + "<a rel=\"noopener noreferrer\"  href='https://www.google.com/search?q={}' target='__blank'>".format(row['AUTHOR']) +  row['AUTHOR'] + "</a>" + "</td>"
            table = table + "<td>" + "<a rel=\"noopener noreferrer\"  href='https://www.google.com/search?q={}' target='__blank'>".format(row['PUBLISHER']) +  row['PUBLISHER'] + "</a>" + "</td>"
            table = table + "<td>" +  str(row['PRICE']) + "</td>"
            table = table + "<td>" + row['ISBN'] + "</td>"
            table = table +  "</tr>"
        table = table +  "</tbody></table>"

except sqlite3.Error as e:		# エラー処理
    table = table +  e.args[0]

con.commit()
con.close()

# html = '''
# <html lang=ja>
# <head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head>
# <body>
# <h2>システムアーキテクトプログラミング演習</h2>
# <h2>検索結果: {name}</h2>
# <div>{tables}</div>
# </body>
# </html>
# '''.format(name=param_str, tables=table)
with open("cgi-bin/book_list.html", encoding="utf-8") as f:
    html = f.read().format(name = param_str, tables = table)
print(html)
