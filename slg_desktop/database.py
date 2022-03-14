from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Brand, Item, ShoppingList, ShoppingListItem, Store


class Database:

    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///slg.sqlite3', echo=True, future=True)

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def insert(self, data):
        try:
            match data['table']:
                case 'shopping_list':
                    record = ShoppingList(for_date=date.fromisoformat(data['date']))
                case 'store':
                    record = Store(name=data['store'], location=data['location'])
                case 'brand':
                    record = Brand(name=data['brand'])
                case 'item':
                    record = Item(name=data['item'], brand_id=data['brand'], size=data['size'], expected_cost=data['cost'])
                case 'shopping_list_item':
                    record = ShoppingListItem(shopping_list_id=data['list'], item_id=data['item'], quantity=data['quantity'], store_id=data['store'])
                case _:
                   return  # TODO: change to something more useful
        except KeyError as err:
            # TODO: change to something more useful
            print(f'The following data was not provided: {err}')
            return

        with Session(self.engine) as session:
            session.add(record)
            session.commit()

    def update(self, data):
        try:
            match data['table']:
                case 'shopping_list':
                    pass
                case 'store':
                    pass
                case 'brand':
                    pass
                case 'item':
                    pass
                case 'shopping_list_item':
                    pass
                case _:
                    return  # TODO: change to something more useful
        except KeyError as err:
            # TODO: change to something more useful
            print(f'The following data was not provided: {err}')
            return


    def delete(self, data):
        try:
            match data['table']:
                case 'shopping_list':
                    pass
                case 'store':
                    pass
                case 'brand':
                    pass
                case 'item':
                    pass
                case 'shopping_list_item':
                    pass
                case _:
                    return  # TODO: change to something more useful
        except KeyError as err:
            # TODO: change to something more useful
            print(f'The following data was not provided: {err}')
            return

