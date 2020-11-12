# HW 5: Creating a twitter clone

<img src=Strips-front-end-vs-le-back-end-650-finalenglish.jpg />

**Description:**
You will create a twitter clone using the Flask web framework.

**Due:**
Finals week (30 Nov-06 Dec).
You will have to schedule a time to demo your website with me over zoom.

Details TBD.

**Learning objectives:**

1. create large Python programs that span multiple files
1. develop a CRUD (Create Read Update Delete) web app
1. understand how social media websites work under the hood
1. integrate the Python, HTML, CSS, Jinja2, and SQL programming languages

## Grading rubric

Your webpage must have a menu with links to the following pages:

1. Log in
    1. this item should only be visible if the user is not logged in
    1. this will present a form for the user to enter their username/password
    1. you must display appropriate error messages if the user enters an incorrect username/password
1. Log out
    1. this item should only be visible if the user is logged in
1. Create new user accounts
    1. this item should only be visible if the user is not logged in
    1. if the user attempts to create an account that already exists, they should get an appropriate error message
    1. the user should be prompted to enter their password twice, and you need to check that both versions of the password match
1. Create a message
    1. this item should only be visible if the user is logged in
    1. the user must be able to enter whatever message body they want, but you should also store the username that created a message and the time the message was created
1. View all messages
    1. this item should always be visible, whether the user is logged in or not logged in
    1. the messages should be ordered chronologically with the most recent message at the top
    1. each message should include the user account that created it, the time of creation, and the message contents

Each of these pages is worth 3 points, for a total of 15 points.

The assignment is out of 25 points, and to get the remaining 10 points you must complete some of the extra credit.

If I can hack your webpage using an [HTML injection attack](https://www.softwaretestinghelp.com/html-injection-tutorial/) or [SQL injection attack](https://en.wikipedia.org/wiki/SQL_injection), then you will lose -15 points.

## Extra credit

You can get 2pts of extra credit if you:

1. create a nicely themed webpage with HTML/CSS (this is the only subjective criteria)

1. can access your twitter clone from other computers (see for example https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network)

1. populate your twitter clone with at least 20 user accounts, each with 20 random messages (for 400 messages total)

1. can delete individual messages

1. can edit messages after they've been created

1. can delete user accounts

1. can change the password after creating an account

1. add user profile pages that a user can edit to provide a description about themselves and other users can view this page

1. assign each user a unique image, and have that image appear with each post

1. add a json endpoint for your messages route that returns the list of messages in json format instead of HTML format

You can get 4pts of extra credit if you:

1. display only 50 messages at a time in the messages route,
   and include a button at the bottom to go to the "next" and "previous" messages

1. can reset a user's password by sending an email with a new password

1. add the ability to search for messages 

1. add the ability to reply to other user's messages (the replies must display in a threaded fashion similar to reddit)

1. support switching the language of your interface

1. use the `flask-login` package and password hashing (as described in the [Flask Mega-Tutorial Section V](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)) to make your login system more secure

You can get 6pts of extra credit if:

1. your webpage uses AJAX to dynamically change content on the page for all of your implemented features
   (partial credit will be awarded if some features work)

## Submission

You will demo your project to me over zoom.
This should take 5-10 minutes.

Details will be announced later.
