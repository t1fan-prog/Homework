from validate_email import validate_email


class Base:

    def __init__(self, email):
        self.emails_list = []
        self.emails_list.append(self.validate(email))

    @classmethod
    def validate(cls, l_email):
        if validate_email(l_email) is True:
            return l_email
        else:
            raise Exception("Enter correct email")


base1 = Base("etwg@fa.com")
print(base1.emails_list)
