from data_base import db_employees

# ID [0] | Имя [1] | отображение в списке сотрудников (visible/hidden) [2] | Телеграмм ID [3]

staff = []


def updateStaff():
    staff.clear()
    for i in db_employees.get_all_employees():
        staff.append({
            'ID':       i[0],
            'Name':     i[1],
            'View':     i[2],
            'Telegram_ID': i[3]
        })


updateStaff()


def getStaff():
    return staff


def getName(id):
    for i in getStaff():
        if i['ID'] == id:
            return i['Name']


def getNames(id: list):
    listNames = list()
    for k in id:
        for i in getStaff():
            if i['ID'] == k:
                listNames.append(i['Name'])
                break
    return listNames


def idTel_to_name(tel_id: int):
    for i in getStaff():
        if i['Telegram_ID'] == tel_id:
            return i['Name']
    return ''

