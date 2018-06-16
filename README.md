# Welcome to Microblog!
A microblog based on [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

# learning points
flask, \_\_init.py\_\_, data modelling, alembic, jinja2, wtforms, gravatar, flask.g, environment variables, babel, yandex, elasticsearch, AJAX, task queue

## flask
Flask is a micro-framework, based on jinja2 and werkzeug WSGI (web server gateway interface). It is unopinionated, meaning that it can be integrated with almost everything and comes light.

## \_\_init\_\_.py
If you look into the file directory, you will see a lot of \_\_init\_\_.py files which are mostly empty, it just means that the code in the folder can be exported as a module in other code. Particularly in app/\_\_init\_\_.py you might see this
    
    from flask import Flask

    app = Flask(__name__)

    from app import routes
    
The first flask in from is the module name, followed by the Flask object. Flask(\_\_name\_\_) basically means that the name will change when you import it into other code. The final import code at the bottom is to avoid circular imports. If you look at app/routes.py you will see the following:

    from app import app

    @app.route('/')
    @app.route('/index')
    def index():
        return "Hello, World!"
        
Since the import is placed at the bottom after you have created the app, routes.py would have no problem using the @routes decorator   

## data modelling
Microblog uses the sqlalchemy ORM (object relational mapper) to map between the underlying database and the OOP object in the app. Before starting to code, we need to decide what objects we need as well as model their relationshisp between each other. This is where UML diagrams come in handy. Take the following UML class diagram between users and posts (all credits to Miguel Grinberg):

![UML](/images/ch04-users-posts.png)

There are 3 types of relationships: one-to-one, one-to-many, and many-to-many. Users and posts are considered one-to-many. 

    class User(PaginatedAPIMixin, UserMixin, db.Model):
        posts = db.relationship('Post', backref='author', lazy='dynamic')
        
    class Post(SearchableMixin, db.Model):
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

Here you can see how the relationship is represented by a db.relationship. The backref argument is telling the Post class to reference the user via the author attribute. Some people might be confused with the user_id in Post, but this has is different from author. Author stores the object while user_id stores the id of the author. This relationship is only established in the sqlalchemy ORM and is not stored in the db itself.

## alembic
Alembic is like git for db migration. Whenever you have made changes to your models, you will need to create a migration script, before migrating the data in the db.

## jinja2 
Jinja2 is the templating engine for flask, allowing you to use for loops and if statements in html. The syntax for writing jinja statements are `{% some logic %}`.

## wtforms
Wtforms is a library that allows you to write out forms and use them in your routers/controllers (in this application they seemed to be joined together), in your templates all you need to do is to call `{{ wtf.quick_form(form) }}` in order to render it. {{}} represents statements that are evaluated by the browser.

## flask.g
Flask.g is like a dict that lives in each context of the application, for each different users. 

## environment variables
The app sometimes will have environment variables that is private(say your Google API key); you will need to keep it safe. The best way is to keep it in an env file and reading it using python dotenv library as an os.environ variable.

## babel
A translation module that helps with translating strings of text in you web app

## yandex
Instead of using Microsoft translation services like in the tutorial, I used [Yandex api](https://translate.yandex.com/)

## elasticsearch
Elasticsearch is the search engine that allows you to fuzzy search, which means they consider the closeness of your query string with strings in the documents and return you the one with the highest match score. Elasticsearch is a service, which means you will have to start elasticsearch somewhere and connect to it with your web app.

## AJAX
AJAX stands for Asynchronous JavaScript And XML. It is used when you want to load something without refreshing the page as most data can only be retrieved from the server side from a GET or POST request

## task queues
Task queue uses queue (FILO - first in last out) to queue up task that are asynchronous to the web application itself, such as downloading data. The common task queue for python is called celery which needs to be run as a service. Note that Windows does not support celery anymore. To pass message in and out of task queues, you will also need a message broker, such as redis or rabbitmq. Task queues support states, which means you can use it to see which tasks are being queued, ran etc. One way to schedule a cron job that runs perpetually is to have a task that adds itself to the task queue once it has been done.

# future features
I think Microblog is an excellent tutorial and I am glad that I took it as my first web development course\
I think some great features that can be implemented further:
1. Options to allow people to upload photos to their profile
2. Options to allow people to upload files to their post
