import modules

print("Welcome to phonebook application.\n")


def main_menu():
    print("Here is menu:",
          "1. Add new entries",
          "2. Search by first name",
          "3. Search by last name",
          "4. Search by full name",
          "5. Search by telephone number",
          "6. Search by city or state",
          "7. Delete a record for a given telephone number",
          "8. Update a record for a given telephone number",
          sep='\n', end='\n\n')

    user_choice = input("Choose any action you want:\n")
    return user_choice


def question():
    answer = input("Continue or exit? Type 'C' for continue or any letter for exit\n").lower()
    return answer


def perform(answer):
    if answer == "1":
        modules.add_new_entries()
        answer_local = question()
    elif answer == "2":
        modules.search_by_first_name()
        answer_local = question()
    elif answer == "3":
        modules.search_by_last_name()
        answer_local = question()
    elif answer == "4":
        modules.search_by_full_name()
        answer_local = question()
    elif answer == "5":
        modules.search_by_telephone_number()
        answer_local = question()
    elif answer == "6":
        modules.search_by_city_or_state()
        answer_local = question()
    elif answer == "7":
        modules.delete_record_by_number()
        answer_local = question()
    elif answer == "8":
        modules.update_record_by_number()
        answer_local = question()
    return answer_local


def main():
    choice = main_menu()
    answer = perform(choice)
    if answer == "c":
        main()
    else:
        quit()


main()
