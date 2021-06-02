import logging


class MyOpenFunc:

    __counter = 0

    @classmethod
    def counter(cls):
        return cls.__counter

    @classmethod
    def inc_counter(cls):
        cls.__counter += 1

    def __init__(self, name: str):
        self.file_name = name
        self.logger = logging.getLogger("lesson19_task1.py")
        self.logger.setLevel(logging.INFO)

        # create the logging file handler
        fh = logging.FileHandler("counter.log")

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # add handler to logger object
        self.logger.addHandler(fh)

    def __enter__(self):
        self.logger.info(f"{self.file_name} is opened")
        self.file_obj = open(self.file_name, 'r')
        self.inc_counter()
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        self.logger.info(f"{self.file_name} is closed")


if __name__ == '__main__':
    with MyOpenFunc('phonebook.json') as f:
        print(f.read())

    print(MyOpenFunc.counter())
