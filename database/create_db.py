import random

from sqlalchemy import MetaData, Table, Column, Integer, String, Date, inspect

from config import ORDERS_COUNT, ORDERS_DATE_START, ORDERS_DATE_END

from datetime import datetime as dt
from datetime import timedelta

import database.crud as crud
from database.database import db, engine


def get_random_date(start, end):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))


names = ["Alana Rodriquez", "Noble Charles", "Wing Foley", "Brendan Lindsey", "Hillary Donaldson"]
items = [(1, "A", 600), (2, "B", 300), (3, "C", 400), (4, "D", 800), (5, "E", 500), (6, "F", 700), (7, "G", 100)]


def create_db():
    if not inspect(engine).has_table("cb_order"):
        metadata = MetaData(engine)

        Table("cb_order", metadata, Column("id", Integer, primary_key=True, nullable=False),
              Column("order_id", Integer), Column("name", String),
              Column("amount", Integer), Column("request_date", Date))

        metadata.create_all()

    if not inspect(engine).has_table("cb_order_item"):
        metadata = MetaData(engine)

        Table("cb_order_item", metadata, Column("id", Integer, primary_key=True, nullable=False),
              Column("id_item", Integer), Column("order_id", Integer),
              Column("item_name", String), Column("item_quantity", Integer),
              Column("item_amount", Integer))

        metadata.create_all()

    list_orders_id_items = list(range(1, ORDERS_COUNT + 1))

    orders_count = ORDERS_COUNT

    for order_id in range(1, ORDERS_COUNT + 1):
        rand = random.randrange(0, orders_count)
        order_item_id = list_orders_id_items[rand]
        list_orders_id_items.remove(order_item_id)

        orders_count -= 1

        temp_index_list = list()

        amount_ = 0

        for _ in range(random.randrange(1, 6)):
            rand = random.randrange(0, len(items))

            if rand in temp_index_list:
                continue

            item_id = int(items[rand][0])
            item_name = items[rand][1]
            amount = int(items[rand][2])

            quantity = random.randrange(1, 6)
            amount = amount * quantity

            amount_ += amount

            temp_index_list.append(rand)

            crud.create_order_item(db, int(item_id), int(order_id), item_name, int(quantity), int(amount))

        temp_index_list.clear()

        name = random.choice(names)

        start_dt = dt.strptime(ORDERS_DATE_START, '%d-%m-%Y')
        end_dt = dt.strptime(ORDERS_DATE_END, '%d-%m-%Y')

        date = dt.date(get_random_date(start_dt, end_dt))

        crud.create_order(db, order_id=order_id, name=name, amount=amount_, request_date=date)
