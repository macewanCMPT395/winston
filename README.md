# winston - CMPT 395 Assignment 1 - Web Application

To launch: clone the project and then in the winston folder, run php artisan serve
The site will be accessible via localhost:8000

Example user already in system
username: Green
password: Turtle


This is a basic web application using PHP and the Laravel framework.

In this web application, I use SQLite for the database and allow users to sign-in, get authenticated, edit the user's own details and post on a forum. Through this project, I learned some styles and syntax for CSS, PHP and SQL. The Eloquent and Blade features are really useful as well.

Upon completion of this project I had some issues working with the Laravel framework. I could not get Form::model binding to work properly and may have corrupted some features that were working. I tried to make features as functional as possible as time allowed.

Things that work pretty well
CSS Layouts
The webpage, SQL connections / structure of tables, Views.
Authentication works okay.
Creating new users is fine.
UserController and SessionController most features are fine except the Form::Model ones.


Things that likely don't work
-Cannot delete users within the form system, cannot fully edit user details, authentication does work for the majority.
I broke the message box features that tells you when you signed in incorrectly or successfully logged in/out.
