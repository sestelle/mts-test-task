from sqlalchemy.orm import Session
from sqlalchemy import func, and_

from datetime import date
import datetime

import database.models as models


def create_order_item(db: Session, id_item: int, order_id: int, item_name: str, item_quantity: int, item_amount: int):
    order_item = models.OrderItem(id_item=id_item, order_id=order_id, item_name=item_name, item_quantity=item_quantity,
                                  item_amount=item_amount)

    db.add(order_item)
    db.commit()
    db.refresh(order_item)


def create_order(db: Session, order_id: int, name: str, amount: int, request_date: date):
    order = models.Order(order_id=order_id, name=name, amount=amount, request_date=request_date)

    db.add(order)
    db.commit()
    db.refresh(order)


def get_last_week(db: Session):
    current_time = datetime.datetime.utcnow()
    one_week_ago = current_time - datetime.timedelta(weeks=1)

    orders = db.query(models.Order).filter(models.Order.request_date > one_week_ago).all()

    for order in orders:
        print(order.order_id, order.name, order.amount, order.request_date)


# select distinct order_id from cb_order_item where order_id in (
# select order_id from cb_order_item group by order_id
# having count(order_id) > 3) and item_amount/item_quantity > 1000
# order by order_id


def data_sampling(db: Session):
    subquery = db.query(models.OrderItem.order_id).group_by(models.OrderItem.order_id).having(func.count(
        models.OrderItem.order_id) > 3)

    order_ids = db.query(models.OrderItem.order_id).distinct(). \
        filter(and_(models.OrderItem.order_id.in_(subquery),
                    models.OrderItem.item_amount > 1000)).order_by(
        models.OrderItem.order_id.asc())

    for order_id in order_ids:
        orders = db.query(models.Order).filter(models.Order.order_id == order_id.order_id).limit(1)
        for order in orders:
            print(order.order_id, order.name, order.amount, order.request_date)
