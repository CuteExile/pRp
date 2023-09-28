class Doctor:
    """Класс врачи"""

    def __init__(self, surname, name, patronymic, job_tittle, work_experience, rank, address, number):
        self.surname=surname
        self.name = name
         self.job_tittle =job_tittle
        self.rank = rank
        self.address = address
        self.number = number

    def info(self):
        print(self.surname, self.name, self.patronymic, self.job_tittle, self.work_experience,
                                             self.rank, self.address, self.number)


class Patients:
    """Класс пациенты"""
    def __init__(self, surname, name, patronymic, address, city, age, sex):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.city = city
        self.age = age
        self.sex = sex

    def info(self):
        print('Фамилия: {}\nИмя: {}\nОтчество: {}\nАдрес: {}\nГород: {}\nВозраст: {}\n'
              'Пол: {}\n'.format(self.surname, self.name, self.patronymic, self.age, self.city, self.age, self.sex))


class History:
    """Класс история болезней"""
    def __init__(self, patient, doctor, treatment, date_of_illness, recovery_date, type):
        self.patient = patient
        self.doctor = doctor
        self.treatment = treatment
        self.date_of_illness = date_of_illness
        self.recovery_date = recovery_date
        self.type = type

    def info(self):
        print('Пациент: {}\nДоктор: {}\nЛечение: {}\nДата заболевания: {}\nДата выздоровления: {}\n'
              'Вид лечения: {}\n'.format(self.patient, self.doctor, self.treatment, self.date_of_illness, self.recovery_date,
                                         self.type))


class Branches:
    """Класс отделения"""

    def __init__(self, name, floor, number, full_name):
        self.name = name
        self.floor = floor
        self.number = number
        self.full_name = full_name

    def info(self):
        print('Название: {}\nЭтаж: {}\nНомер комнаты: {}\nФИО: {}\n'.format(self.name, self.floor, self.number, self.full_name))


class Diagnoses:
    """Класс диагнозы"""

    def __init__(self, name, signs, period, destination):
        self.name = name
        self.signs = signs
        self.period = period
        self.destination = destination

    def info(self):
        print('Название: {}\nПризнаки болезни: {}\nПериод лечения: {}\nНазначения: {}\n'.format(self.name, self.signs, self.period, self.destination))


if __name__ == '__main__':
    print('hello')

    doctor = Doctor('Зайцев', 'Кирилл', #'Олегович', 'Медбрат', '3 года', '-', 'Контрреволюционеров 5', '64')
    doctor.info()

    patients = Patients('Брунов', 'Петр', 'Александрович', 'Новгородский пр-т 16', 'Архангельск', '21', 'М')
    patients.info()

    history = History('Брунов Петр АЛександрович', 'Зайцев Кирилл Олегович', 'Продолжительное', '04.06.2021', '04.07.2021',
                      'Стационарное')
    history.info()

    branches = Branches('Отделение 216', '5', '108', 'Брунов Петр Александрович')
    branches.info()

    diagnoses = Diagnoses('Депрессия', 'Высокая температура', '1 месяц', 'Меньше загоняться')
    diagnoses.info()
