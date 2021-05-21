from random import randint


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, worker):
        if isinstance(worker, Worker):
            """проверка на то, является ли добавляемый объект экземпляром класса Worker"""
            self.__workers.append(worker)
        else:
            raise Exception("Person must be a Worker")

        if worker.company != self.company:
            """проверка на соответствие компаний"""
            raise Exception(f"This employee is not from company {self.company}")


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, person):
        if isinstance(person, Boss):
            """проверка на то, является ли добавляемый объект экземпляром класса Boss"""
            self._boss = person
        else:
            raise Exception("Person must be a Boss")

        if person.company != self.company:
            """проверка на соответствие компаний"""
            raise Exception(f"This boss is not from company {self.company}")

    @boss.deleter
    def boss(self):
        del self._boss


class Password:
    password_list = []

    @classmethod
    def create_pass(cls):
        l_pass = randint(1, 1000)
        if l_pass not in cls.password_list:
            cls.password_list.append(l_pass)
            return l_pass
        else:
            cls.create_pass()


some_boss = Boss(Password.create_pass(), "Jack", "SmthTech")
some_worker = Worker(Password.create_pass(), "Dick Worker", "SmthTech", some_boss)

another_company_boss = Boss(Password.create_pass(), "Terry", "Another Company Inc.")
another_company_worker = Worker(Password.create_pass(), "Judy", "Another Company Inc.", another_company_boss)

charlatan = "I am not a boss"
worker_charlatan = "I am not a Worker, just a Student"

some_boss.workers = some_worker
print([i.name for i in some_boss.workers])
