from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class ShoppingList(Base):
    __tablename__ = 'shopping_list'

    id = Column(Integer, primary_key=True)
    for_date = Column(Date, nullable=False)  # TODO: make field unique
    def __repr__(self) -> str:
        return f'Shopping list(id={self.id!r}, for_date={self.for_date!r})'


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

