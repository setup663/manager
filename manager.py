import shelve


class Manager:
    """
    Класс для сбора информации о менеджере
    ...
    Атрибуты
    --------
    manager_id : int
            уникальный номер менеджера
    name : str
            имя менеджера
    city : str
            город менеджера
    comm : float
            коммисионные менеджера
    Методы
    ------
    def __str__(self):
        Возвращает инфорацию о менеджера
    """
    def __init__(self, manager_id: int, name: str, city: str, comm: float):
        """
        Устанавливает все необходимые атрибуты для объекта Manager.
        Параметры
        ---------
        manager_id : int
            уникальный номер менеджера
        name : str
            имя менеджера
        city : str
            город менеджера
        comm : float
            comm менеджера
        """
        self.manager_id = manager_id
        self.name = name
        self.city = city
        self.comm = comm

    def __str__(self):
        return f"{self.manager_id}. {self.name} {self.city} {self.comm}"


def create_file():
    db = shelve.open('managers_sh.db')
    db.close()


def open_file():
    with shelve.open('managers_sh.db') as db:
        for key in db.keys():
            print(db[key])


def convert_to_shelve():
    with open('managers.txt', 'r', encoding='utf-8') as mans:
        for line in mans:
            man_id, name, city, comm = line.split(';')
            man_id = int(man_id)
            comm = float(comm)
            man = Manager(man_id, name, city, comm)
            with shelve.open('managers_sh.db') as db:
                db[str(man.manager_id)] = f'{man.manager_id} {man.name} {man.city} {man.comm}'


def add_string():
    with shelve.open('managers_sh.db') as db:
        man_id, name, city, comm = input('Введите id, имя, город и коммисионные менеджера: ').split()
        man_id = int(man_id)
        comm = float(comm)
        man = Manager(man_id, name, city, comm)
        db[str(man.manager_id)] = f'{man.manager_id} {man.name} {man.city} {man.comm}'


def edit_string():
    with shelve.open('managers_sh.db') as db:
        man_id = input('Введите id менеджера для редактирования: ')
        name, city, comm = input('Введите имя, город и коммисионные менеджера: ').split()
        man_id = int(man_id)
        comm = float(comm)
        man = Manager(man_id, name, city, comm)
        db[str(man.manager_id)] = f'{man.manager_id} {man.name} {man.city} {man.comm}'


def del_string():
    with shelve.open('managers_sh.db') as db:
        man_id = input('Введите id менеджера для удаления: ')
        for i in db:
            if man_id in i:
                del db[man_id]


def to_html():
    with shelve.open('managers_sh.db') as db:
        with open('managers.html', 'w') as mans:
            strings = '\n'.join(db.values())
            mans.write(f'<html><body><pre>{strings}</pre></body></html>')


with shelve.open('managers_sh.db') as db:
    print('Меню для работы с файлом "managers.txt"')
    while True:
        print('1. создать файл\n'
              '2. txt -> shelve\n'
              '3. открыть файл\n'
              '4. добавить строку\n'
              '5. изменить строку по номеру Manager_ID\n'
              '6. удалить строку по номеру Manager_ID\n'
              '7. вывести данные в HTML-файл\n'
              '0. Выйти'
              )
        choice = int(input('Введите пункт: '))
        match choice:
            case 1: create_file()
            case 2: convert_to_shelve()
            case 3: open_file()
            case 4: add_string()
            case 5: edit_string()
            case 6: del_string()
            case 7: to_html()
            case 0: break
