import text
import model

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_contacts(book: list[dict[str, str]], error: str):
    if book:
        print('\n' + '-' * 110)
        for contact in book:
            print(f'{contact.get("id"):>5}. {contact.get("name"):<40} | {contact.get("phone"):<20} | {contact.get("comment"):<40}')
        print(f'-' * 110 + '\n')
    else:
        print_message(error)


def input_contact(message) -> dict[str, str]:
    new = {}
    print(message)
    for key, txt in text.new_contact.items():
        value = input(txt)
        if value:
            new[key] = value
    return new


def input_search(message) -> str:
    return input(message)


def ask_user_for_save_pb():
    while True:
        save_or_not = input(text.save_or_not)
        if save_or_not == 'y':
            model.save_pb()
            break
        elif save_or_not == 'n':
            break