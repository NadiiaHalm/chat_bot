numbers_book = {}


def input_error(func):
    def inner():
        try:
            func()
        except KeyError or ValueError or IndexError:
            print("Give me name and phone please")
            func()
    return inner


def conversation(answer):
    chat = True
    if answer == "hello":
        print("How can I help you?")
    elif answer.startswith("add"):
        start, name, number = answer.split(' ')
        numbers_book[name] = number
        print("I saved this contact")
    elif answer.startswith("change"):
        start, name, number = answer.split(' ')
        if name not in numbers_book:
            print('Your numbers book does not provide this contact name')
        else:
            numbers_book[name] = number
            print("I changed this number")
    elif answer.startswith("phone"):
        start, name = answer.split(' ')
        print(numbers_book[name], "is number what you need")
    elif answer == "show all":
        print(numbers_book)
    elif answer == "good bye" or answer == "close" or answer == "exit":
        print("Good bye!")
        chat = False
    return chat


@input_error
def main():
    loop = True
    while loop:
        rep = input().lower()
        loop = conversation(rep)


if __name__ == '__main__':
    main()
