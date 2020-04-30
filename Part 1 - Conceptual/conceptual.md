### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  * PostgreSQL is a Relational Database Management System(RDBMS) that uses and extends the SQL language combined with many features to safely store and scale complicated data structures.

- What is the difference between SQL and PostgreSQL?
  * SQL server is a database management system which is mainly used for e-commerce and providing different data warehousing solutions.

  * PostgreSQL is an advanced version of SQL that provides support to different functions of SQL like foreign keys, subqueries, triggers, and different user-defined types and functions

- In `psql`, how do you connect to a database?
  * "`psql [database_name]`" OR "`\c [database_name]`"

- What is the difference between `HAVING` and `WHERE`?
  * `WHERE` cannot be used with aggregated data but `HAVING` can

- What is the difference between an `INNER` and `OUTER` join?
  * `INNER` joins don't include non-matching rows, while `OUTER` joins do include them

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  * `LEFT OUTER` and `RIGHT OUTER` dictate the priority of which rows to display

- What is an ORM? What do they do?
  * Object-Relational Mapping (ORM) is a programming technique for converting data between relational databases and object oriented programming languages. 
  * Example: SQLAlchemy

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?
  * Pros of client side requests:
    * Accessing an API on the client side can be faster and easier than accessing the API using a server
    * Same-Origin Policy
  * Pros of server side requests:
    * May want to store some data from API to your own database
    * May want to hide your personal information(api_key,password) from the browser


- What is CSRF? What is the purpose of the CSRF token?
  * Cross-Site Request Forgery (CSRF): is an attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated. CSRF attacks specifically target state-changing requests, not theft of data, since the attacker has no way to see the response to the forged request. 
  * A CSRF Token works as follows: The client requests an HTML page that contains a form. When the client submits the form, it must send both tokens back to the server. The client sends the cookie token as a cookie, and it sends the form token inside the form data.

- What is the purpose of `form.hidden_tag()`?
  * Generates a hidden field in a form that includes a CSRF token that is used to protect the form against CSRF attacks.