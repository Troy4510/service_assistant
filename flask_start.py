from flask import Flask
from flask import request
from flask import render_template
import sql_mod as sql
import os

app = Flask(__name__, template_folder = 'app/templates', static_folder = 'app/static')
main_folder = './MAIN/'
db_folder = './MAIN/'
cars_folder = './MAIN/app/static/cars'


@app.route('/')
@app.route('/index.html')
def index():
    works = sql.read_records(db_folder)
    return render_template('index.html', works = works)

@app.route('/work/<num>')
#@app.route('/<num>')
def work(num):
    global cars_folder
    val = int(num)
    x = sql.read_one_record(db_folder, num)
    if x == None: return render_template('error.html')
    else:
        car_num = x[2]
        date = x[1]
        img_list = read_car(cars_folder, car_num, date)
        return render_template('work.html', val = x, imgs = img_list)


def read_cars_folder(car_folder):
    cars = os.listdir(car_folder)                     #получить список машин
    print(f'cars in car folder: {cars}')
    for car in cars:                                  #перебор папок с номерами машин
        print(f'car folder: {car}')                   
        dates = os.listdir(car_folder + '/' + car)          #в каждой папке с тачками прочитать список дат
        for date in dates:                            #перебор папок с датами
            print(f'dates in current car: {date}')
            images = os.listdir(car_folder + '/' + car + '/' + date)#в каждой папке с датами получить список фото
            #if 'IMG_20241009_100516_221.jpg' in images: print('it works!')
            for image in images:
                print(f'file: {image}')               #и отобразить их

                
def read_car(cars_folder, car_num:str, point_date):
    try:
        dates = os.listdir(cars_folder + '/' + car_num)
        #print(dates)
        result = []
        for date in dates:                   
            images = os.listdir(cars_folder + '/' + car_num + '/' + date)
            print(cars_folder + '/' + car_num + '/' + date)
            if date == point_date:
                for image in images:
                    #result.append(cars_folder + '/' + car_num + '/' + date + '/' + image)
                    result.append('/static/cars' + '/' + car_num + '/' + date + '/' + image)
        return result
    except: 
        return None


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050, debug=True)
    #app.run(host='192.168.1.66', port=5050, debug=True)
    #read_cars_folder(cars_folder)
    #read_car(cars_folder, 'MAN р933ау')
    #os.mkdir('MAIN/app/static/cars/test/1/2/3')
    pass