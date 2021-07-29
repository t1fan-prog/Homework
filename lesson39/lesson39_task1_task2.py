from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric, ForeignKey, func, or_
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from datetime import date

engine = create_engine('sqlite:///hr.db', echo=False)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)


class Employees(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(25))
    email = Column(String(25))
    phone_number = Column(String(25))
    hire_date = Column(Date)
    job_id = Column(String(10), ForeignKey('jobs.job_id'))  # DATABASE
    salary = Column(Numeric(precision=2, scale=2))
    commission_pct = Column(Numeric(precision=2, scale=2))
    manager_id = Column(Integer, ForeignKey('employees.employee_id'))
    department_id = Column(Integer, ForeignKey('departments.department_id'))

    job = relationship("Jobs", back_populates='employees')  # ORM
    department = relationship("Departments", back_populates='employees')

    def __repr__(self):
        return f"ID: {self.employee_id} First name: {self.first_name}, Last name: {self.last_name}"


class Jobs(Base):
    __tablename__ = 'jobs'

    job_id = Column(String(10), primary_key=True)
    job_title = Column(String(25))
    min_salary = Column(Numeric(precision=2, scale=2))
    max_salary = Column(Numeric(precision=2, scale=2))

    employees = relationship("Employees", back_populates='job')

    def __repr__(self):
        return f"Job_id {self.job_id}, title: {self.job_title}"


class Departments(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True)
    depart_name = Column(String(20))
    manager_id = Column(Integer)
    location_id = Column(Integer, ForeignKey('locations.location_id'))

    employees = relationship("Employees", back_populates='department')
    location = relationship("Locations", back_populates='department')

    def __repr__(self):
        return f"Department_id: {self.department_id}, dep_name: {self.depart_name}, manager_id: {self.manager_id}," \
               f" location_id: {self.location_id}"


class Locations(Base):
    __tablename__ = 'locations'

    location_id = Column(Integer, primary_key=True)
    street_address = Column(String(25))
    postal_code = Column(String(12))
    city = Column(String(30))
    state_province = Column(String(12))
    country_id = Column(String(2))

    department = relationship("Departments", back_populates='location')

    def __repr__(self):
        return f"Location_id {self.location_id}, street_address: {self.street_address}, postal_code: " \
               f"{self.postal_code}, city: {self.city}, state_province: {self.state_province}, country_id: " \
               f"{self.country_id}"


Base.metadata.create_all(engine)
session = Session()


def add_user():
    """1. Добавление юзера"""
    hire_date = date(year=1993, month=1, day=31)
    vermalen = Employees(employee_id=210,
                         first_name='Tomas',
                         last_name='Vermalen',
                         email='tomas@gmail.com',
                         phone_number='2556.24.140',
                         hire_date=hire_date,
                         job_id="IT_PROG",
                         salary=43500,
                         commission_pct=0,
                         manager_id=100,
                         department_id=90)
    session.add(vermalen)
    try:
        session.commit()
    except IntegrityError:
        print('ERROR!')
        session.rollback()


def name_surname():
    """2. Выбор имени и фамилии"""
    employees = []
    for name, surname in session.query(Employees.first_name, Employees.last_name):
        employees.append(name + ' ' + surname)
    return employees


def surname_and_department():
    """3. Выбор имени и фамилии и department"""
    employees = []
    for name, surname, department_id in session.query(Employees.first_name,
                                                      Employees.last_name,
                                                      Departments.department_id).\
            filter(Employees.department_id == Departments.department_id).all():
        employees.append(f'{name} {surname}, {department_id}')
    return employees


def fourth_query():
    """4. SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province FROM departments d INNER JOIN
    employees e ON e.department_id = d.department_id INNER JOIN locations l ON d.location_id = l.location_id; """
    employees = []
    for name, surname, department_name, l_city, l_state_province in session.query(Employees.first_name,
                                                                                  Employees.last_name,
                                                                                  Departments.depart_name,
                                                                                  Locations.city,
                                                                                  Locations.state_province).filter(
        Employees.department_id == Departments.department_id, Departments.location_id == Locations.location_id).all():
        employees.append(f'{name}, {surname}, {department_name}, {l_city}, {l_state_province}')
    return employees


def fifth_query():
    """5. SELECT e.first_name, e.last_name, d.department_id, d.depart_name FROM employees e INNER JOIN departments d
    ON e.department_id = d.department_id WHERE d.department_id = 80 or d.department_id = 40;"""
    employees = []
    for name, surname, department_id, depart_name in session.query(Employees.first_name,
                                                      Employees.last_name,
                                                      Departments.department_id,
                                                      Departments.depart_name).\
            filter(Employees.department_id == Departments.department_id).\
            filter(or_(Departments.department_id == 40, Departments.department_id == 80)).all():
        employees.append(f'{name}, {surname}, {department_id}, {depart_name}')
    return employees


def sixth_query():
    """6. SELECT * FROM departments d LEFT JOIN employees e ON e.department_id = d.department_id;"""
    employees = []
    for instance in session.query(Departments).outerjoin(Employees):
        employees.append(instance)
    return employees


def seventh_query():
    """7. SELECT e.first_name, e.last_name, e.salary FROM departments d INNER JOIN employees e ON e.department_id =
    d.department_id INNER JOIN locations l ON d.location_id = l.location_id WHERE l.city = 'London';"""
    employees = []
    for name, surname, salary in session.query(Employees.first_name, Employees.last_name, Employees.salary).filter(
        Employees.department_id == Departments.department_id, Departments.location_id == Locations.location_id).\
            filter(Locations.city == 'London').all():
        employees.append(f'{name}, {surname}, {salary}')

    # Вариант №2
    # for name, surname, salary in session.query(Employees.first_name, Employees.last_name, Employees.salary).\
    #         join(Departments, Locations).filter(Locations.city == 'London').all():
    #     employees.append(f'{name}, {surname}, {salary}')
    return employees


def eighth_query():
    """8. SELECT d.depart_name, count(e.employee_id) as quantity_of_employees FROM employees e
    INNER JOIN departments d ON d.department_id = e.department_id GROUP BY d.depart_name;"""
    employees = []
    for depart_name, count_id in session.query(Departments.depart_name, func.count(Employees.employee_id)).\
            join(Departments).group_by(Departments.depart_name).all():
        employees.append(f'{depart_name}, {count_id}')
    return employees


def ninth_query():
    """9. SELECT j.job_title, avg(e.salary) as avg_salary FROM employees e
    INNER JOIN jobs j ON e.job_id = j.job_id GROUP BY job_title;"""
    employees = []
    for job_title, avg_salary in session.query(Jobs.job_title, func.avg(Employees.salary)).join(Jobs).\
            group_by(Jobs.job_title).all():
        employees.append(f'{job_title}, {avg_salary}')
    return employees


def tenth_query():
    """10. SELECT j.job_title, e.first_name, e.last_name, j.max_salary - e.salary as diff_from_max_salary
    FROM employees e INNER JOIN jobs j ON e.job_id = j.job_id;"""
    employees = []
    for job_title, employee_first_name, employee_last_name, dif_salary in session.query(Jobs.job_title,
                                                                                        Employees.first_name,
                                                                                        Employees.last_name,
                                                                                        Jobs.max_salary -
                                                                                        Employees.salary).join(Jobs).\
            all():
        employees.append(f'{job_title}, {employee_first_name}, {employee_last_name}, {dif_salary}')
    return employees
