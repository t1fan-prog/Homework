SELECT e.first_name, e.last_name, d.department_id, d.depart_name FROM employees e INNER JOIN departments d ON e.department_id = d.department_id;
SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province FROM departments d INNER JOIN employees e ON e.department_id = d.department_id INNER JOIN locations l ON d.location_id = l.location_id;
SELECT e.first_name, e.last_name, d.department_id, d.depart_name FROM employees e INNER JOIN departments d ON e.department_id = d.department_id WHERE d.department_id = 80 or d.department_id = 40;
SELECT * FROM departments d LEFT JOIN employees e ON e.department_id = d.department_id;
SELECT e.first_name, m.first_name FROM employees e INNER JOIN employees m on e.employee_id = m.manager_id;
SELECT j.job_title, e.first_name, e.last_name, j.max_salary - e.salary as diff_from_max_salary FROM employees e INNER JOIN jobs j ON e.job_id = j.job_id;
SELECT j.job_title, avg(e.salary) as avg_salary FROM employees e INNER JOIN jobs j ON e.job_id = j.job_id GROUP BY job_title;
SELECT e.first_name, e.last_name, e.salary FROM departments d INNER JOIN employees e ON e.department_id = d.department_id INNER JOIN locations l ON d.location_id = l.location_id WHERE l.city = 'London';
SELECT d.depart_name, count(e.employee_id) as quantity_of_employees FROM employees e INNER JOIN departments d ON d.department_id = e.department_id GROUP BY d.depart_name;