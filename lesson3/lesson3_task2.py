while True:
    phone = input("Enter phone number. Please only use numbers without any symbols or characters "
                  "and country code (e.g. 0974356712). Also it must be not more than 10 digits:\n")
    if phone.isdecimal():
        if len(phone) == 10:
            print(f"Your phone {phone} is saved. Thank you! We will contact you soon.")
            break
    print("Phone number can't contain a character or be more/less than 10 digits. Try again!\n")
