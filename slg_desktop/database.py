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
            with Session(self.engine) as session:
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
                       print('The table supplied does not exist.')
                       return  # TODO: change to something more useful
                session.add(record)
                session.commit()
        except KeyError as err:
            # TODO: change to something more useful
            print(f'The following data was not provided: {err}')

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
            with Session(self.engine) as session:
                match data['table']:
                    case 'shopping_list':
                        record = session.get(ShoppingList, data['shopping_list_id'])
                    case 'store':
                        record = session.get(Store, data['store_id'])
                    case 'brand':
                        record = session.get(Brand, data['brand_id'])
                    case 'item':
                        record = session.get(Item, data['item_id'])
                    case 'shopping_list_item':
                        record = session.get(ShoppingListItem, (data['shopping_list_id'], data['item_id']))
                    case _:
                        print('The table supplied does not exist.')
                        return  # TODO: change to something more useful
                session.delete(record)
                session.commit()
        except KeyError as err:
            # TODO: change to something more useful
            print(f'The following data was not provided: {err}')

