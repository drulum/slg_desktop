from sqlalchemy import Column, create_engine, ForeignKey, Integer, Float, String
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()


class Database:

    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///slg.sqlite3', echo=True, future=True)

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def connect(self):
        pass

    def add_shopping_list(self, date):
        with Session(self.engine) as session:
            shopping_list = ShoppingList(date=date)
            session.add(shopping_list)
            session.commit()

    def add_store(self, store, location=None):
        with Session(self.engine) as session:
            store = Store(name=store, location=location)
            session.add(store)
            session.commit()

    def add_brand(self, brand):
        with Session(self.engine) as session:
            brand = Brand(name=brand)
            session.add(brand)
            session.commit()

    def add_item(self, item, brand=None, size=None, cost=None):
        with Session(self.engine) as session:
            item = Item(name=item, brand_id=brand, size=size, expected_cost=cost)
            session.add(item)
            session.commit()

    def add_shopping_list_item(self):
        pass


class ShoppingList(Base):
    __tablename__ = 'shopping_list'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f'Shopping list(id={self.id!r}, date={self.date!r})'


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    def __repr__(self) -> str:
        return f'Store(id={self.id!r}, name={self.name!r}, location={self.location!r})'


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    items = relationship('Item', back_populates='brand')

    def __repr__(self) -> str:
        return f'Brand(id={self.id!r}, name={self.name!r})'


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=True)
    name = Column(String, nullable=False)
    size = Column(String)
    expected_cost = Column(Float)

    brand = relationship('Brand', back_populates='items')

    def __repr__(self) -> str:
        return f'Item(id={self.id!r}, name={self.name!r}, size={self.size!r}, expected_cost={self.expected_cost!r})'


class ShoppingListItem(Base):
    __tablename__ = 'shopping_list_base'

    shopping_list_id = Column(Integer, ForeignKey('shopping_list.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)
    quantity = Column(Integer)
    store_id = Column(Integer, ForeignKey('store.id'))

    # TODO: add a __repr__ method that makes sense
    # def __repr__(self) -> str:
    #     return ''

