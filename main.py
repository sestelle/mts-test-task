import os.path

from sqlalchemy import inspect

from database import crud
from database.database import db, engine
from database.create_db import create_db

from logs.create_logs import create_logs
from logs.count_success import count_success
from logs.create_error_file import create_error_file


if __name__ == "__main__":
    if not inspect(engine).has_table("cb_order"):
        create_db()

    print("\nСписок заказов, сделанных за последние 7 дней:\n")
    crud.get_last_week(db)
    print("\nЗаказы с количеством позиций больше 3 и суммой одной позиции больше 1000:\n")
    crud.data_sampling(db)

    if not os.path.exists("log"):
        create_logs()

    create_error_file()
    count_success()

