import datetime
import time
import sql_mod as sql
import os
import shutil

menu_selector = 'main'
db_folder = './MAIN/'
cars_folder = 'MAIN/app/static/cars'

def menu(menu_select):
    print('''
            МЕНЮ:
            -----
            1 - добавить запись в базу
            2 - просмотр всех записей (сокращенно)
            3 - просмотр записи по номеру (подробно)
            4 - просмотр записей по дате
            5 - просмотр неоплаченных работ
            6 - редактирование записи
            7 - удаление записи
            ''')
    x = input('=> ')
    if menu_selector == 'main':
        if x == '1':
            print('')
            print('Добавление новой записи')
            date = datetime.datetime.now().strftime('%d.%m.%Y')
            car_number = input('Номер авто: ')
            client = input('Контактные данные клиента: ')
            work = input('Произведенные работы: ')
            other = input('Примечание (не обязательно): ')
            payment = int(input('Сумма к оплате, руб: '))
            duty = int(input('Фактически оплачено, руб: '))
            os.mkdir(f'{cars_folder}/{car_number}')
            os.mkdir(f'{cars_folder}/{car_number}/{date}')
            shutil.copy('MAIN/app/static/garage.png', f'{cars_folder}/{car_number}/{date}')
            data = (date, car_number, client, work, other, payment, duty)
            sql.add_record(db_folder, data)
            print('Новая запись добавлена')
        elif x == '2':
            print('')
            print('Просмотр записей')
            records = sql.read_records(db_folder)
            for record in records:
                print(record[0], '\t', record[1], '\t', record[2], '\t', record[6], '\t', record[3])
                #print(record)
        elif x =='3':
            print('')
            print('Введите номер записи для подробного просмотра:')
            sel = int(input('=> '))
            record = sql.read_one_record(db_folder, sel)
            if record != None: print(record)
            else: print('Записи с таким номером не существует')
        elif x == '4':
            print('')
            print('Введите дату в формате ДД.ММ.ГГГГ (например 01.01.2025): ')
            date = input('=> ')
            records = sql.read_by_date(db_folder, date)
            print('')
            if records != []:
                for record in records:
                    print(record[0], '\t', record[1], '\t', record[2], '\t', record[6], '\t', record[3])
            else: print('Записи за указанную дату не найдены')
        elif x == '5':
            print('')
            print('Записи с незавершёнными оплатами:')
            total:int = 0
            records = sql.show_duty(db_folder)
            for record in records:
                print(record[0], '\t', record[1], '\t', record[2], '\t', record[6], '\t', record[7], '\t', record[3])
                total = total + (record[6] - record[7])
            print('\t\t\t\t  ------------')
            print(f'\t\t\t\t  ИТОГО: {total}')
        elif x == '6':
            print('')
            print('Введите номер записи для редактирования:')
            sel = int(input('=> '))
            rec = sql.read_one_record(db_folder, sel)
            rec = list(rec)
            if rec != None:
                print('')
                print(rec)
                print('')
                print('Нажатие ENTER без ввода данных = без изменений')
                #id=rec[0] date=rec[1] car=rec[2] client=rec[3] work=rec[4] other=rec[5] pay=rec[6] duty=rec[7]
                car = input('Номер авто: ')
                if car != '': rec[2] = car; print('Номер обновлен')
                else: print('Без изменений')
                client = input('Контактные данные клиента: ')
                if client != '': rec[3] = client; print('Клиент обновлён')
                else: print('Без изменений')
                work = input('Произведенные работы: ')
                if work != '': rec[4] = work; print('Работы обновлены')
                else: print('Без изменений')
                other = input('Примечания: ')
                if other != '': rec[5] = other; print('Примечания обновлены')
                else: print('Без изменений')
                pay = input('Сумма к оплате: ')
                if pay != '': rec[6] = int(pay); print('Сумма обновлена')
                else: print('Без изменений')
                duty = input('Фактически оплачено: ')
                if duty != '': rec[7] = int(duty); print('Оплата обновлена')
                else: print('Без изменений')
                #print(rec)
                data = [rec[2], rec[3], rec[4], rec[5], rec[6], rec[7]]
                id = rec[0]
                sql.update_record(db_folder, id, data)
                print('Запись обновлена')
            else: print('Записи с таким номером не существует')
        elif x == '7':
            print('')
            print('Введите номер записи для удаления: ')
            rec = int(input('=> '))
            sql.delete_record(db_folder, rec)
            print(f'Запись №{rec} удалена')    
        
        else:
            print('Неправильный ввод')
            time.sleep(2)



if __name__ == "__main__":
    while True:
        menu(menu_select = menu_selector)