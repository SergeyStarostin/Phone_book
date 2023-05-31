import text
class PhoneBook:
    def __init__(self, path: str = 'phones.txt'):
        self.phone_book: list[dict[str, str]] = []
        self.path = path


    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            new = {'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]}
            self.phone_book.append(new)


    def save(self):
        data = []
        for contact in self.phone_book:
            data.append(':'.join([contact['id'], contact['name'], contact['phone'], contact['comment']]))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)


    def load(self):
        return self.phone_book


    def add(self, new: dict[str, str]) -> str:
        new_id = int(self.phone_book[-1].get('id')) + 1
        new['id'] = str(new_id)
        self.phone_book.append(new)
        return new.get('name')


    def search(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for contact in self.phone_book:
            for field in contact.values():
                if word.lower() in field.lower():
                    result.append(contact)
                    break
        return result


    def change(self, new: dict, index: int) -> str:
        for contact in self.phone_book:
            if index == contact.get('id'):
                contact['name'] = new.get('name', contact.get('name'))
                contact['phone'] = new.get('phone', contact.get('phone'))
                contact['comment'] = new.get('comment', contact.get('comment'))
                return contact.get('name')


    def delete(self, index_delete: str) -> list[dict[str, str]]:
        for contact in self.phone_book:
            for field in contact.values():
                if index_delete.lower() in field.lower():
                    self.phone_book.remove(contact)
                    break
        return self.phone_book


    def ask_user_for_save_pb(self):
        while True:
            save_or_not = input(text.save_or_not)
            if save_or_not == 'y':
                self.save()
                break
            elif save_or_not == 'n':
                break
