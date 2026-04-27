# Backend Webdev

<img width=200px src=img/6a00d8341d3df553ef01157073a04e970c-800wi.jpeg />

<br />
<img width=200px src=img/abstraction-5c17c1.jpg />

**Announcements 27 May 2026:**

1. Sorry I've been slow to grade projects :(

1. No lab class this week (due to data science capstone presentations)

    Still a lab assignment due (detailed below)

1. No quiz this week

    Last quiz will be last day of class: Wed 6 May

<!--
1. chatgpt updated:

    <https://openai.com/index/sycophancy-in-gpt-4o/>

    <https://news.ycombinator.com/item?id=43840842>

    <https://gist.github.com/simonw/51c4f98644cf62d7e0388d984d40f099/revisions>

1. 9-11AM next week (Wednesday 7 May - Friday 9 May)

   9-11AM finals week (Monday 12 May - Friday 16 May)

-->

## Notes

**SQL Review:**

Last topic covered SQL by itself.
This topic integrate SQL with Python and webpages.

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

  - Hundreds of lines of complex Python can be expressed in a single line of SQL.

- SQL databases provide **ACID guarantees**
    - ensures that data written to the database will actually be in the database
    - even in the event of "catastrophic hardware failures"

The downside of SQL is that it makes our webpages more prone to being "hacked" (in the muggle sense of the word).

- SQL injection

- <img width=600px src=img/exploits_of_a_mom.png />

**Backend Web Programming:**

Types of web programming:

1. Backend: Writing python that interfaces with the SQL database and generates HTML

1. Frontend: Writing HTML+CSS (+JavaScript sometimes)

1. Full-stack: both frontend and backend

There are many libraries for backend webdev in python:

1. **Django** is the most popular python framework.
   - Companies that use Django include: Instagram, Pinterest, and Spotify
   - This is what's called a "batteries-included" library because it does a lot of stuff for you automatically.
   - But the "batteries" are relatively complicated and so we will not use this project.

1. **Flask** used to be the most popular "simple" web framework.
    - Companies that use flask include: Airbnb, Netflix, Reddit, and Uber
    - For a full list, see: <https://github.com/rochacbruno/flask-powered>

    > *ASIDE:*
    > How did Flask get its name?
    >
    > - All python web frameworks must adhere to the WSGI protocol defined in [PEP 333](https://www.python.org/dev/peps/pep-0333/)
    >
    > - PEP stands for "Python Enhancement Proposal" and is Guido's system for standardizing the python development process
    >
    > - WSGI is pronounced like "whiskey", not W-S-G-I
    >
    > - The simplest/best way to drink whiskey is in a flask
    >
    > (obviously a very opinionated statement)
    >
    > - By analogy, Flask is the simplest/best WSGI library
    >
    > (obviously a very opinionated statement)
    >
    > - Programmers love obscure puns

1. There's a new popular framework called **FastAPI**
    - lots of the companies above (esp. the flask companies) are migrating over to this framework
        - almost a "drop in replacement" for Flask
        - uses ASGI instead of WSGI: <https://asgi.readthedocs.io/en/latest/introduction.html>
        - the A in ASGI stands for "async" programming (2-100x faster for some tasks, slightly more complicated)
        - FastAPI makes developing APIs much easier than flask
        - very popular for something called "microservices" used internally at companies
    - <https://towardsdatascience.com/understanding-flask-vs-fastapi-web-framework-fe12bb58ee75>

1. About 2 dozen other libraries, see: <https://wsgi.readthedocs.io/en/latest/frameworks.html>

1. Other popular companies (e.g. Google/Facebook/Microsoft/Amazon/Twitter) don't use python to serve their webpages.

    Facebook in particular is famous for being created by Mark Zuckerberg using (originally) very simple technologies.
    At the end of this class, you'll know everything that Mark used to implement the first versions of The Facebook at Harvard.
    (He used a programming language called PHP and a SQL database called MySQL,
    but the principles are all the same,
    and the Python/FastAPI/Sqlite3 stack is both simpler and faster.)

## Lab

For this lab, you should create a simple flask app.
Your final homework will extend the code you write in this lab.

**Requirement 0:**

Your project should be contained in a "reasonably structured" github repo.

> *HINT:*
> I am being intentionally vague about the phrase "reasonably structured" to get you all practice creating nice repos without step-by-step guidelines.
> You can see the requirements from previous assignments to get a sense of what makes a repo reasonable.

**Requirement 1:**

Your webpage should have 5 routes:
1. `/`
1. `/login`
1. `/logout`
1. `/create_message`
1. `/create_user`

Each route should have a corresponding html file in the `templates` folder,
and each of these html templates should extend a `base.html` template that contains the menu for your webpage.
The `base.html` template should have an `<h1>` tag that is the title of your webpage,
and the template for each route should contain an `<h2>` tag that is the title for that route.

**Requirement 2:**

The `/` route must open a connection to a database created by `db_create.py` and display all of the messages sorted with the most recent message at the top.
For each message, you must display:
1. the text of the message,
1. the timestamp it was created at,
1. the username of the user who created it,
1. and the age of the user who created it.

> *HINT:*
>
> Divide this task up into two steps.
> First, create a list of dictionaries;
> each dictionary would contain one message and would have the 4 key/value pairs specified above.
>
> Then, pass this list of dictionaries to the `render_template` function,
> and adjust your jinja2 code to process this list of dictionaries.
>
> You can use this reference to learn about all the jinja2 syntax (e.g. how to use lists/dictionaries/for loops): <https://realpython.com/primer-on-jinja-templating/>.

**Requirement 3:**

> *NOTE:*
>
> We will not cover in class how to complete this requirement.
> Instead, you should use [this reference](https://www.tutorialspoint.com/flask/flask_static_files.htm).
> The decision not to cover this material in class is intentional to force you to get practice using references.
> I'm still happy to answer any questions you have about this task.

Your python file should also contain a route for static web resources served from the `static` folder.
This folder should contain:
1. an image
1. a css file

You must modify your `/` route to display this image somewhere.

You must modify your `base.html` template to include the style sheet.
This should result in every route being styled with the template.

> *HINT:*
> One of the optional tasks in the Project 5 is to create a nice looking webpage,
> with nice navigation buttons and styling.
> Now would be a good time to do this.

**Submission:**

1. Add a screenshot that demonstrates the functionality of your `/` route to your README.
1. Create a new branch `lab-submission` that contains all of the code for this lab.
1. Submit a link to this branch on canvas.

> *WARNING:*
> After submitting, you should not modify the `lab-submission` branch,
> and instead should do all of your work in the `main`/`master` branch.
> Your final project will lose points if your `lab-submission` branch gets updated.
> It is very common when programming to need to have multiple branches of a project being updated at the same time,
> and part of the purpose of this project is to get you practice with this technique.
