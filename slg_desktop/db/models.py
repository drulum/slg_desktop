from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# TODO: Learn ALembic and implement a schema update option without data loss.


class ShoppingList(Base):
    __tablename__ = 'shopping_list'

    id = Column(Integer, primary_key=True)
    for_date = Column(Date, nullable=False)  # TODO: make field unique

    shopping_list_items = relationship('ShoppingListItem', 'shopping_list')

    def __repr__(self) -> str:
        return f'Shopping list(id={self.id!r}, for_date={self.for_date!r})'


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    shopping_list_items = relationship('ShoppingListItem', 'store')

    def __repr__(self) -> str:
        return f'Store(id={self.id!r}, name={self.name!r}, location={self.location!r})'


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    items = relationship('Item', back_populates='brand')

    def __repr__(self) -> str:
        return f'Brand(id={self.id!r}, name={self.name!r})'


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    items = relationship('Item', back_populates='category')

    def __repr__(self):
        return f'Category(id={self.id!r}, name={self.name!r})'


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    name = Column(String, nullable=False)
    size = Column(String)
    expected_cost = Column(Float)

    brand = relationship('Brand', back_populates='items')
    category = relationship('Category', back_populates='items')
    shopping_list_items = relationship('ShoppingListItem', 'item')

    def __repr__(self) -> str:
        return f'Item(id={self.id!r}, name={self.name!r}, size={self.size!r}, expected_cost={self.expected_cost!r})'


class ShoppingListItem(Base):
    __tablename__ = 'shopping_list_item'

    id = Column(Integer, primary_key=True)
    shopping_list_id = Column(Integer, ForeignKey('shopping_list.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    quantity = Column(Integer)
    notes = Column(String, nullable=True)
    store_id = Column(Integer, ForeignKey('store.id'))

    shopping_list = relationship('ShoppingList', back_populates='shoppinglistitems')
    item = relationship('Item', back_populates='shoppinglistitems')
    store = relationship('Store', back_populates='shoppinglistitems')
    
    # TODO: add a __repr__ method that makes sense
    # def __repr__(self) -> str:
    #     return ''

