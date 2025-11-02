import bot_assistant
from address_book import AddressBook


def main():
    run_tests(AddressBook())


def run_tests(address_book: AddressBook) -> None:
    # Add Mike
    command, *args = bot_assistant.parse_input("add Mike 1234567890")
    bot_assistant.handle_input(address_book, command, *args)

    # Add him a birthday
    command, *args = bot_assistant.parse_input("add-birthday Mike 05.11.1997")
    bot_assistant.handle_input(address_book, command, *args)

    # Print his birthday
    command, *args = bot_assistant.parse_input("show-birthday Mike")
    bot_assistant.handle_input(address_book, command, *args)

    # Add Kate
    command, *args = bot_assistant.parse_input("add Kate 1111111111")
    bot_assistant.handle_input(address_book, command, *args)

    # Add her extra number
    command, *args = bot_assistant.parse_input("add Kate 1111111112")
    bot_assistant.handle_input(address_book, command, *args)

    # Add her b-day
    command, *args = bot_assistant.parse_input("add-birthday Kate 04.11.1998")
    bot_assistant.handle_input(address_book, command, *args)

    # Print all records
    command, *args = bot_assistant.parse_input("all")
    bot_assistant.handle_input(address_book, command, *args)

    # Change Mikes number and print updated number
    command, *args = (bot_assistant.parse_input
                      ("change Mike 1234567890 0987654321"))
    bot_assistant.handle_input(address_book, command, *args)
    command, *args = bot_assistant.parse_input("phone Mike")
    bot_assistant.handle_input(address_book, command, *args)

    # Get all upcoming b-days
    command, *args = bot_assistant.parse_input("birthdays")
    bot_assistant.handle_input(address_book, command, *args)

    # Add and remove Jovani, check that he is removed
    command, *args = bot_assistant.parse_input("add Jovani 1111111112")
    bot_assistant.handle_input(address_book, command, *args)
    command, *args = bot_assistant.parse_input("remove Jovani")
    bot_assistant.handle_input(address_book, command, *args)
    command, *args = bot_assistant.parse_input("all")
    bot_assistant.handle_input(address_book, command, *args)

    # Input mistakes
    command, *args = bot_assistant.parse_input("add Jovani 111111111")
    bot_assistant.handle_input(address_book, command, *args)

    command, *args = bot_assistant.parse_input("add Jovani OneOneOne")
    bot_assistant.handle_input(address_book, command, *args)

    command, *args = bot_assistant.parse_input("remove Jovani")
    bot_assistant.handle_input(address_book, command, *args)

    command, *args = bot_assistant.parse_input("phone Jovani")
    bot_assistant.handle_input(address_book, command, *args)

    command, *args = bot_assistant.parse_input("show-birthday Jovani")
    bot_assistant.handle_input(address_book, command, *args)

    command, *args = bot_assistant.parse_input("add-birthday Jovani")
    bot_assistant.handle_input(address_book, command, *args)
    command, *args = bot_assistant.parse_input("add-birthday Mike 20-11-1997")
    bot_assistant.handle_input(address_book, command, *args)
    command, *args = bot_assistant.parse_input("add-birthday Mike 20-11")
    bot_assistant.handle_input(address_book, command, *args)

    command, *args = bot_assistant.parse_input("change ")
    bot_assistant.handle_input(address_book, command, *args)
    command, *args = bot_assistant.parse_input("change Jovani ")
    bot_assistant.handle_input(address_book, command, *args)


if __name__ == "__main__":
    main()
