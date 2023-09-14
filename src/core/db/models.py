from sqlalchemy import (
    DECIMAL,
    CheckConstraint,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.core.db.enums import OperationType

Base = declarative_base()


class Asset(Base):
    __tablename__ = "asset"
    __table_args__ = (CheckConstraint("price >= 0", name="check_non_negative_price"),)

    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), nullable=False, unique=True)
    price = Column(DECIMAL, nullable=False)


class User(Base):
    __tablename__ = "user"
    __table_args__ = (
        CheckConstraint("balance >= 0", name="check_non_negative_user_balance"),
    )

    id = Column(Integer, primary_key=True)
    balance = Column(DECIMAL, nullable=False, server_default="0")


class TransactionLog(Base):
    __tablename__ = "transaction_log"
    __table_args__ = (CheckConstraint("value > 0", name="check_positive_value"),)

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    asset_id = Column(Integer, ForeignKey(Asset.id), nullable=False)
    operation_type = Column(Enum(OperationType), nullable=False)
    datetime = Column(DateTime, nullable=False, server_default=func.now())
    value = Column(DECIMAL, nullable=False)

    user = relationship(User, uselist=False, lazy="joined")
    asset = relationship(Asset, uselist=False, lazy="joined")
