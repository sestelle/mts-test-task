from sqlalchemy import Column, Integer, String, Date, ForeignKey

from .database import Base


class Order(Base):
    __tablename__ = "cb_order"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    name = Column(String)
    amount = Column(Integer)
    request_date = Column(Date)


class OrderItem(Base):
    __tablename__ = "cb_order_item"

    id = Column(Integer, primary_key=True, index=True)
    id_item = Column(Integer)
    order_id = Column(Integer)
    item_name = Column(String)
    item_quantity = Column(Integer)
    item_amount = Column(Integer)
