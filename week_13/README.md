# Week 13: Backend Webdev I

<img width=600px src=6a00d8341d3df553ef01157073a04e970c-800wi.jpeg />

**SQL Review:**

Last week, we covered SQL by itself.
We'll start this week by integrating SQL with Python and webpages.

Our goal is to create a **CRUD app**.
This is a technical term that describes most interactive webpages on the internet (e.g. Facebook/Twitter).

- **C**reate: `INSERT`

- **R**ead: `SELECT`

- **U**pdate: `UPDATE`

- **D**estroy: `DELETE`

We use SQL to store data (instead of **"flat files"** like JSON/CSV) because:

- SQL is MUCH faster, especially when working with millions of datapoints

  - The data is not loaded into memory unless absolutely necessary

  - Every SQL query corresponds to some equivalent python code,
    and SQL is "guaranteed" to generate the fastest possible code

    (Technically, SQL code is "asymptotically optimal".)

- SQL is much less verbose than python

  - Hundreds of lines of complex Python can be expressed in a singleline of SQL.

- SQL databases provide **ACID guarantees**
    - ensures that data written to the database will actually be in the database
    - even in the event of "catastrophic hardware failures"

The downside of SQL is that it makes our webpages more prone to being "hacked" (in the muggle sense of the word).

- SQL injection

- <img width=600px src=exploits_of_a_mom.png />

**Backend Web Programming:**

Types of web programming:

1. Backend: Writing python that interfaces with the SQL database and generates HTML

1. Frontend: Writing HTML+CSS (+JavaScript sometimes)

1. Full-stack: both frontend and backend

There are many libraries for backend webdev in python:

1. **Flask** is the most popular "easy to use" library,
    so that's what we'll use.

    - Companies that use flask include: Airbnb, Netflix, Reddit, and Uber 

    - For a full list, see: https://github.com/rochacbruno/flask-powered

1. The other popular python library is called **Django**.
   - This is what's called a "batteries-included" library because it does a lot of stuff for you automatically.
   - Companies that use Django include: Instagram, Pinterest, and Spotify

1. There's a new popular framework called FastAPI

    - lots of the companies above (esp. the flask companies) are migrating over to this framework

    - requires something called "async" programming

    - that's a lot of additional complexity, so we're not going to use it

    - https://towardsdatascience.com/understanding-flask-vs-fastapi-web-framework-fe12bb58ee75

1. About 2 dozen other libraries, see: https://wsgi.readthedocs.io/en/latest/frameworks.html

Other popular companies (e.g. Google/Facebook/Microsoft/Amazon) don't use python to serve their webpages

How did Flask get its name?

- All python web frameworks must adhere to the WSGI protocol defined in [PEP 333](https://www.python.org/dev/peps/pep-0333/)

    - PEP stands for "Python Enhancement Proposal" and is Guido's system for standardizing the python development process

- WSGI is pronounced like "whiskey", not W-S-G-I

- The simplest/best way to drink whiskey is in a flask

  (obviously a very opinionated statement)

- By analogy, Flask is the simplest/best WSGI library

  (obviously a very opinionated statement)

- Programmers love obscure puns

References:

1. basic: https://www.tutorialspoint.com/flask/index.htm 
1. advanced: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Lab

For this lab, you should create a simple flask app similar to the app you will create for homework.
It should have 5 routes:
1. `/`
1. `/login`
1. `/logout`
1. `/create_message`
1. `/create_user`
Each route should have a corresponding html webpage in the `templates` folder,
and each of these html templates should extend a `base.html` template that contains the menu for your webpage.

All of your routes should have an `<h2>` tag that identifies which route you have selected.
The `/` route must open a connection to a database created by `db_create.py` and display all of the messages.
You must display:
1. the text of the message,
1. the timestamp it was created at,
1. the username of the user who created it,
1. and the age of the user who created it.

Your python file should also contain a route for static web resources served from the `static` folder.
In this folder, you should create a file `style.css` that contains the style sheets for your webpage.
I recommend you spend some time formatting the CSS so that the webpage looks nice;
this will make working on the project more fun,
and it will get you extra credit on the final homework.

**Submission:**
Since there's a lot of files, I'm NOT requiring that you upload them all to sakai.
Instead, take a screenshot of your `/` route as displayed in firefox and upload that to sakai.
