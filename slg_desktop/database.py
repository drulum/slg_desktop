from sqlalchemy import Column, create_engine, ForeignKey, Integer, Float, String
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()


class Database:

    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///slg.sqlite3', echo=True, future=True)

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def add(self, data):
        try:
            match data['table']:
                case 'shopping_list':
                    record = ShoppingList(date=data['date'])
                case 'store':
                    record = Store(name=data['store'], location=data['location'])
                case 'brand':
                    record = Brand(name=data['brand'])
                case 'item':
                    record = Item(name=data['item'], brand_id=data['brand'], size=data['size'], expected_cost=['cost'])
                case 'shopping_list_item':
                    record = ShoppingListItem(shopping_list_id=data['list'], item_id=data['item'], quantity=data['quantity'], store_id=data['store'])
                case _:
                   return
        except KeyError as err:
            print(f'The following data was not provided: {err}')
            return

        # record.add(self.engine, data)
        with Session(self.engine) as session:
            session.add(record)
            session.commit()


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
    __tablename__ = 'shopping_list_item'

    shopping_list_id = Column(Integer, ForeignKey('shopping_list.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)
    quantity = Column(Integer)
    store_id = Column(Integer, ForeignKey('store.id'))

    # TODO: add a __repr__ method that makes sense
    # def __repr__(self) -> str:
    #     return ''

