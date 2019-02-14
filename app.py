import os, time, datetime
from bottle import error, route,run, get,post,request, template,static_file,redirect
import sqlite3

@route('/')
def top():
    return "TOP PAGE!!"
    
@route('/index')
def hello():
    name = "StartUpCafe"
    age = 12345
    address = "Heaven"
    return template("index",name_tpl =name,age_tpl = age, address_tpl = address)
# run(host = 'localhost', port = 8080, reloader =True)


@route('/user/<name>')
def user(name):
    return name

@route(('/object/<id:int>'))
def callback(id):
    assert isinstance(id,int)

@route ('/hello/<text>')
def textGuest(guest):
    return("Hi,",guest)

@route('/temptest')
def temptest():
    name = "StartUpCafe"
    age = 12345
    address = "Heaven"
    return template("index",name_tpl =name,age_tpl = age, address_tpl = address)

@route('/time')
def time_rr():
    today = datetime.date.today()
    now = str(datetime.datetime.now()).split(" ")
    # print(now[1])
    today.day #これは今日の日付
    today.weekday() #これは曜日の数字を取得
    days = ("月","火", "水", "木", "金", "土", "日")

    today_str = ("今日は"+str(today.year)+"年 "+str(today.month)+"月"+ str(today.day)+"日、" + days[today.weekday()]+"曜日です")
    

    return template("time_re", today_str_tpl = today_str)

@route('/dbtest')
def dbtest():
    #access to db
    conn = sqlite3.connect('test20190213.db')

    c=conn.cursor()
    c.execute('select name,age,address from users where id=1;')
    user_info =c.fetchone()
# disconnect 
    c.close()
    print(user_info)
    return template('dbtest',user_info_tpl=user_info)

@route('/list')
def showlist():

    conn = sqlite3.connect('test20190213.db')
    c=conn.cursor()
    c.execute('select name, age, address from users;')
    user_list = []
    for row in c.fetchall():
        user_list.append({
            "name": row[0],
            "age": row[1],
            "address": row[2]
        })
# disconnect 
    c.close()
    print(user_list)
    print(type(user_list))
    headers = ['Name', 'Age', 'Address']
    return template('list',user_list_tpl=user_list, headers_tpl = headers)

@route('/add', method = ["GET"])
def add_get():
    return template('add.tpl') 

@route('/add', method =["POST"])
def add_post():
    # Obtain current time
    now = datetime.datetime.today()
    # Convert into the format
    now = ('{0:%Y-%m-%d %H:%M:%S}'.format(now))
    task=request.POST.getunicode('task')
    #Connect database
    conn = sqlite3.connect('test20190213.db')
    #command to use sql 
    c=conn.cursor()
    c.execute("insert into task values (null,?,?);",(task,now,))
    #save data
    conn.commit()
    #Disconect
    conn.close()

    return redirect('/showtask')

@route('/showtask')
def show_task():

    conn = sqlite3.connect('test20190213.db')
    c=conn.cursor()
    c.execute('select id, task,time from task;')
    # Define an empty list 
    task_list = []
    # Adding list in the task_list
    # By using fetchall, getting all elements from the db 
    for row in c.fetchall():
        task_list.append({
            "id": row[0],
            "task": row[1],
            "time": row[2],
        })
    c.close()
    headers = ['ID', 'Task','Created Time']
    return template('showtask',task_list_tpl=task_list, headers_tpl = headers)

@route("/delete/<task_id:int>")
def delete(task_id):
    delete_task(task_id)
    return redirect("/showtask")

def delete_task(task_id):
    conn = sqlite3.connect('test20190213.db')
    c = conn.cursor()
    delete = "delete from task where id=?"
    c.execute(delete, (task_id,))
    conn.commit()
    conn.close()


@error(404)
def notfunction(code):
    return "You are dead..."
run( port = 8080, reloader =True)