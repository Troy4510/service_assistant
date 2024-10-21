import sqlite3
import datetime


def create_base(db_folder:str):
    connection = sqlite3.connect(db_folder + 'sql_base.db')
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS worktable (
    id INTEGER PRIMARY KEY,
    date TEXT,
    car_number TEXT,
    client TEXT,
    work TEXT,
    other TEXT,
    payment INTEGER,
    duty INTEGER)
    ''')
    
    date1 = datetime.datetime.now().strftime('%d.%m.%Y')
    query = ''' INSERT INTO worktable (date, car_number, client, work, other, payment, duty) 
                VALUES (?, ?, ?, ?, ?, ?, ?)'''
    data1 = (date1, 'car_123', 'client_test', 'work_test', 'comments_test', 1000, 100)
    cursor.execute(query, data1)
    
    connection.commit()
    connection.close()
    
    
    
def read_records(db_folder:str):
    connection = sqlite3.connect(db_folder + 'sql_base.db')
    cursor = connection.cursor()
    query = 'select * from worktable'
    cursor.execute(query)
    val = cursor.fetchall()
    connection.close()
    return val
    

def read_one_record(db_folder, num):
    connection = sqlite3.connect(db_folder + 'sql_base.db')
    cursor = connection.cursor()
    query = f'select * from worktable where id = {num}'
    cursor.execute(query)
    val = cursor.fetchone()
    connection.close()
    return val

    
def add_record(db_folder, data):
    connection = sqlite3.connect(db_folder + 'sql_base.db')
    cursor = connection.cursor()
    query = ''' INSERT INTO worktable (date, car_number, client, work, other, payment, duty) 
                VALUES (?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(query, data)
    connection.commit()
    connection.close()


def read_by_date(db_folder, date):
    connection = sqlite3.connect(db_folder + 'sql_base.db')
    cursor = connection.cursor()
    query = f'select * from worktable where date = "{date}"'
    cursor.execute(query)
    val = cursor.fetchall()
    connection.close()
    return val

    
def delete_record(db_folder, id):
    connection = sqlite3.connect(db_folder + 'sql_base.db')
    cursor = connection.cursor()
    query = f'delete from worktable where id = {id}'
    cursor.execute(query)
    connection.commit()
    connection.close()
    
    
def update_record(db_folder, id:int, data):
    connection = sqlite3.connect(db_folder + 'sql_base.db')
    cursor = connection.cursor()
    query = f''' update worktable set car_number = ?, client = ?, work = ?, other = ?,
                payment = ?, duty = ? where id = {id}'''
    cursor.execute(query,data)
    connection.commit()
    connection.close()
    

def show_duty(db_folder):
    connection = sqlite3.connect(db_folder + 'sql_base.db')
    cursor = connection.cursor()
    query = f'select * from worktable where (duty < payment) or (duty = 0)'
    cursor.execute(query)
    val = cursor.fetchall()
    connection.close()
    return val


if __name__ == "__main__":
    #create_base('./MAIN/')
    x = show_duty('./MAIN/')
    print(x)
    pass