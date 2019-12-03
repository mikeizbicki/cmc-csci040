# HW 6: Creating a twitter clone

**Description:** 
You will create a twitter clone using the Flask web framework.

**Due:** 
Wednesday, 18 December

**Learning objectives:**

1. create large Python programs that span multiple files
1. develop a CRUD (Create Read Update Delete) web app
1. understand how social media websites work under the hood

## Grading rubric

Your webpage must have a menu with 4 items, each item corresponding to a route in your flask app.
The required items/routes you must implement are:

1. Log in 
    1. this item should only be visible if the user is not logged in
    1. you must display appropriate error messages if the user enters an incorrect name/password
1. Create new user accounts
    1. this item should only be visible if the user is not logged in
    1. if the user attempts to create an account that already exists, they should get an error message 
1. Create a message
    1. this item should only be visible if the user is logged in
    1. the user must be able to enter whatever message body they want, but you should also store the username that created a message and the time the message was created
1. View all messages 
    1. this menu item should appear whether the user is logged in or not
    1. the messages should be ordered chronologically with the most recent message at the top
    1. each message should include the user account that created it, the time of creation, and the message contents

Each of these menu items is worth 20 points, for a total of 80 points.

The assignment is out of 100 points, and to get the remaining 20 points you must complete some of the extra credit.

If I can hack your webpage using an [HTML injection attack](https://www.softwaretestinghelp.com/html-injection-tutorial/), then you will lose -20 points.

## Extra credit

You can get 5pts extra credit if you:

1. can access your twitter clone from other computers (see for example https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network)

1. populate your twitter clone with at least 10 user accounts, each with 10 random messages 

You can get 10pts of extra credit if you:

1. can delete individual messages

1. can edit messages after they've been created

1. can delete user accounts

1. can change the password after creating an account

1. add user profile pages that a user can edit to provide a description about themselves and other users can view this page

1. assign each user a unique image, and have that image appear with each post

1. use the `flask-login` package and password hashing (as described in the [Flask Mega-Tutorial Section V](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)) to make your login system more secure

You can get 20pts of extra credit if you:

1. implement a search function

1. add the ability to reply to other user's messages (the replies must display in a threaded fashion similar to twitter or reddit)

1. support switching the language of your interface

1. implement any of the above features using AJAX

<!--1. use SQLite3 instead of JSON to store-->

## Submission

You must bring a laptop to my office and demo your project to me.
(This should take 5-10 minutes.)

You may schedule a time in advance of the due date to privately show your project to me,
or wait until the due date and do it as a group during special office hours (TBD).
