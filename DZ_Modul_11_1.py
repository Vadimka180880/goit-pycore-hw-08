import pickle

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def get_contacts(self):
        return self.contacts

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print("Дані успішно збережено.")

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Файл збережених даних не знайдено. Повернення нової адресної книги.")
        return AddressBook()

def main():
    book = load_data()

    # Основний цикл програми
    while True:
        print("1. Додати контакт")
        print("2. Видалити контакт")
        print("3. Показати всі контакти")
        print("4. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я контакту: ")
            email = input("Введіть email контакту: ")
            contact = Contact(name, email)
            book.add_contact(contact)
            print("Контакт успішно додано!")
        elif choice == '2':
            print("Список контактів:")
            contacts = book.get_contacts()
            if not contacts:
                print("Список порожній.")
            else:
                for i, contact in enumerate(contacts):
                    print(f"{i + 1}. {contact.name}: {contact.email}")
                index = int(input("Виберіть номер контакту для видалення: ")) - 1
                if 0 <= index < len(contacts):
                    contact = contacts[index]
                    book.remove_contact(contact)
                    print("Контакт успішно видалено!")
                else:
                    print("Некоректний номер контакту!")
        elif choice == '3':
            print("Список контактів:")
            contacts = book.get_contacts()
            if not contacts:
                print("Список порожній.")
            else:
                for i, contact in enumerate(contacts):
                    print(f"{i + 1}. {contact.name}: {contact.email}")
        elif choice == '4':
            save_data(book)
            print("До побачення!")
            break
        else:
            print("Некоректний вибір!")

if __name__ == "__main__":
    main()
