class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", 'a') as file:
            file.write(msg)


a = input("Enter any number which is less than 100:\n")

try:
    if not a.isdigit():
        raise CustomException("You have entered not a digit\n")
    a = int(a)
    if a > 100:
        raise CustomException("You have entered number more than 100\n")

except CustomException as ms:
    print(ms)
else:
    print(a)
