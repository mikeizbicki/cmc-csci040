# Week 11: Flask I

<center>
<img width='80%' src=exploits_of_a_mom.png />
</center>

<center>
<img width='60%' src=6a00d8341d3df553ef01157073a04e970c-800wi.jpeg />
</center>

**Quiz:**
The completed `quiz.pdf` should be submitted to sakai by Sunday at midnight.

**Monday/Wednesday:**
We will go over how to use the flask library.
We will use the following tutorials as references:

1. https://www.tutorialspoint.com/flask/index.htm
1. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

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
Your `/` route should display all of the messages currently contained in your database file.

Your python file should also contain a route for static web resources served from the `static` folder.
In this folder, you should create a file `style.css` that contains the style sheets for your webpage.
I recommend you spend some time formatting the CSS so that the webpage looks nice;
this will make working on the project more fun,
and it will get you extra credit on the final homework.

**Submission:**
Since there's a lot of files, I'm NOT requiring that you upload them all to sakai.
Instead, take a screenshot of your `/` route as displayed in firefox and upload that to sakai.
