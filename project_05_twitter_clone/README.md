# Project 5: Twitter Clone

<img src=Strips-front-end-vs-le-back-end-650-finalenglish.jpg />

**Description:**
You will create a twitter clone using the FastAPI web framework and sqlite3.

**Learning objectives:**

1. create large Python programs that span multiple files
1. develop a CRUD (Create Read Update Delete) web app
1. understand how social media websites work under the hood
1. integrate the Python, Markdown, HTML, CSS, Jinja2, and SQL programming languages
1. practice using git

**Due date:**
You will live demo your project to me.
1. Graduating students: Schedule a time before Friday May 8 noon
1. Non-graduating students: During Finals Week (May 11-15)
    1. You will have to demo your project to me 1-1 over zoom.
    1. I will be on zoom starting at 9AM every day of finals week.
    1. Login whichever day you would like to submit.
    1. I will admit 1 student at a time into the meeting.
    1. Grading will take 5-15 minutes. I will give your grade on the project + grade in the course.
    1. You might have to wait a long time (up to 2-3 hours?) if you wait until Friday.

## Grading rubric

The assignment is worth:
1. Graduating students: 25 points
1. Non-graduating students: 48 points

There are 25 points of required tasks that you must complete.
There are 75 points worth of optional tasks that you may choose to complete,
so it is possible to earn up to 100/48 points on this assignment.

> **WARNING:**
> If I can hack your webpage using a [SQL injection attack](https://en.wikipedia.org/wiki/SQL_injection),
> then you will get a -10 point penalty added to your grade.

> **WARNING:**
> If I can hack your webpage using an [HTML injection attack](https://www.softwaretestinghelp.com/html-injection-tutorial/),
> then you will get a -4 point penalty added to your grade.

> **WARNING:**
> When grading, I will be trying to cause your webpage to get an `Internal Server Error`.
> If I ever get this error, you won't receive any points for the task that caused the error.

> **HINT:**
> I strongly encourage you to complete more tasks than you think you need to.
> That way you will have a "buffer" in case I am able to break your webpage
> or I do not award points for some task.

### Required Tasks

Each required task is worth 5 points and corresponds to one of the routes on your webpage:

1. Home
    1. a link to this page should always be visible in your menu, whether the user is logged in or not logged in
    1. this route displays all the messages in the system
    1. the messages should be ordered chronologically with the most recent message at the top
    1. each message should include the user account that created it, the time of creation, and the message contents
    1. at least one message must contain a single quote `'` and a double quote `"`

        (the purpose of this check is to help you prevent SQL/HTML injection attacks)

1. Log in
    1. a link to this page should only be visible in your menu if the user is not logged in
    1. this route will present a form for the user to enter their username/password;
       the password box must not display the user's password as they are typing it in

        > **HINT:**
        > Don't use `type=text` on your `input` tag.
        > Figure out the right type for a password box.

    1. you must display appropriate error messages if the user enters an incorrect username/password
    1. after a user successfully logs in, you must automatically redirect them to the homepage

1. Log out
    1. a link to this page should only be visible if the user is logged in
    1. this route will delete the cookies that the log in form creates, logging the user out

        > **HINT:**
        > We didn't cover how to delete cookies in class,
        > but you can find an explanation in [this stackoverflow post](https://stackoverflow.com/questions/14386304/flask-how-to-remove-cookies).

1. Create new user accounts
    1. a link to this page should only be visible in your menu if the user is not logged in
    1. if the user attempts to create an account that already exists, they should get an appropriate error message

        > **HINT:**
        > You know an account doesn't exist because when you try to run the `INSERT` command,
        > you get a sqlite error about violating a unique constraint.

    1. the user should be prompted to enter their password twice; if the passwords do not match, they should get an appropriate error message

1. Create a message
    1. a link to this page should only be visible in your menu if the user is logged in
    1. the user must be able to enter whatever message body they want,
       but you will also need to store the user id of the user that created a message and the time the message was created
    1. you will only get credit for this route if the message correctly shows up on the home route after creation

### Optional Tasks

The following tasks are worth 3 points each.

1. Create a nicely themed webpage with HTML/CSS.

   I will use my subjective aesthetic judgement to determine what is and is not "nicely themed",
   but you don't have to do anything fancy.
   Just the simple CSS we covered at the beginning of class would be fine.

1. Convert all URLs in messages to actual links to the webpage using the `<a>` tag.

1. Populate your twitter clone with at least 200 user accounts, each with 200 random messages (for 40000 messages total).

   > **HINT:**
   > Modify the `db_create.py` file to randomly generate comments.

1. Allow deleting individual messages.

1. Allow editing messages after they've been created.
   You must display a message that a comment has been edited along with the time of the most recent edit.

1. Allow deleting user accounts.

1. Automatically log a user into a newly created user account,
   and redirect the user to the home page (instead of the create user page)

1. Allow changing the password after creating an account.
   You must have a password reset form that forces the user to type in their old password and a new password twice.

1. Assign each user a unique image, and have that image appear with each post.
   The website <https://robohash.org> lets you do this easily.

1. Add a json endpoint for your messages route that returns the list of messages in json format instead of HTML format.

1. Publish your website so that it can be accessed from other computers.
   In order to get this credit, I must be able to access your webpage directly from my own computer by connecting to your IP address.
   This will likely require you to do a bit of research into networking.

   > **HINT:**
   > If you haven't actually tested connecting from a different computer that is not yours,
   > you will not have done the extra credit correctly and will not get the points.

The following tasks are worth 6 points each.
Each of these tasks requires either more advanced SQL queries (i.e. `SELECT` statements) or modifying the underlying table schemas.

1. Display only 50 messages at a time in the messages route,
   and include a button at the bottom to go to the "next" and "previous" message pages.
   You must use the `offset` and `limit` SQL commands so that this happens efficiently.

1. Add user profile pages that a user can edit to provide a description about themselves and other users can view this page.
   The profile page should also display the most recent messages posted by that user.

1. Allow users to `@` mention other users in their messages.
   Whenever text that looks like `@username` appears in a message,
   this text should be replaced with a link to all the messages from that user
   (or the user profile page if you completed that extra credit).

1. Add the ability to search for messages.
   The search should be done with SQL's `LIKE` operator,
   and not within python.
   If you use [sqlite's FTS5 extension](https://www.sqlite.org/fts5.html),
   you will get an additional 2 points of extra credit.

1. Allow resetting a user's password by sending an email with a new password.
   The user must change the password on their next login.

1. Add the ability to reply to other user's messages.
   The replies must display in a threaded fashion similar to reddit.
   For full credit, you do not need to be able to "reply to a reply", but only reply to "top level" messages.
   If you do add the ability to reply to all messages, you can get an additional +2 points.

1. Support switching the language of your interface.
   You must have at least 3 different languages that can be selected.

1. Allow Markdown formatting in your messages.

   > **HINT:**
   > You can use your hw1 to convert the markdown message into the html that will be displayed.

   > **HINT:**
   > This task is easy to combine with the URL 3 point optional task.

The following tasks are worth 9 points of extra credit:

1. Use Javascript to dynamically create/edit/remove posts without refreshing the webpage.

    Your FastAPI server should serve JSON endpoints for all of the tasks.
    Then you should have JavaScript code that modifies the DOM without actually refreshing the webpage.
    We won't be covering how to do this in Javascript, so you'll have to research this yourself.

1. Create a special AI user account.
    Whenever a message @mentions this user account,
    the AI will automatically reply to this message.
    The reply should use an LLM and the behavior should be similar to @grok on X.

    > **HINT:**
    > This is a good task to combine with the "reply" extra credit task worth 6 points.
