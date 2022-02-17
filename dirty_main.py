from application.salary import *
from application.db.people import *
from datetime import *


if __name__ == '__main__':
    print(datetime.now())

    print('start main')
    calculate_salary()
    get_employees()
    print('finish main')