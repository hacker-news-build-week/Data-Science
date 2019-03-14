from flask import Flask, render_template, request
import sqlite3 as sql
import os

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])

def index():
   #initModel()
   #render out pre-built HTML file right on the index page
      return render_template("index.html")


@app.route('/result',methods=['GET', 'POST'])
def result():
   #if request.method == 'GET' :
   comment = request.form['comment']
   #name = int(comment)

   con = sql.connect("/Users/Srini/myflaskapp_new/Users.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select by,sentiment from data where by = name limit 20")
   
   rows = cur.fetchall();
   print (rows)
   return render_template("result.html",rows = rows)
   con.close()


if __name__ == '__main__':
   app.run(debug = True)