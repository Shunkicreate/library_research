import csv
import sqlite3

db_path = "bookdb.db"			# データベースファイル名を指定

con = sqlite3.connect(db_path)  # データベースに接続
cur = con.cursor()				# カーソルを取得
cur.execute('''create table BOOKLIST
	(ID int primary key,
	AUTHOR varchar(256),
	TITLE varchar(512),
	PUBLISHER varchar(256),
	PRICE int,
	ISBN char(10))''')
with open('./data/BookList_sjis.csv', 'r') as file:		# CSVファイルをオープン
		reader = csv.reader(file)				# ファイルを読み込む
		for line in reader:						# 一行ずつ処理をする
			# SQL文の実行
			cur.execute('insert into BOOKLIST values (?,?,?,?,?,?);', line)

try:
    cur.execute('insert into BOOKLIST values (?,?,?,?,?,?);',
                (10, '夏目漱石', '坊っちゃん', 'ABC出版', 500, '1234567890'))		# SQL文の実行

except sqlite3.Error as e:		# エラー処理
    print("Error occurred:", e.args[0])

con.commit()					# データベース更新の確定
con.close()						# データベースを閉じる
