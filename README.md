# Welcome to Microblog!
A microblog based on [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

# learning points
flask, \_\_init.py\_\_, data modelling, alembic, jinja2, wtforms, flask.g, environment variables, unit testing, babel, string translation, elasticsearch, AJAX, popups, task queue

## flask
Flask is a micro-framework, based on jinja2 and werkzeug WSGI (web server gateway interface). It is unopinionated, meaning that it ccan be intergrated with almost everything and comes light.

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
Alembic is like git for db migration. Whenever you have made changes to your models, you will need to create a migration script, before migrating the data in the db for the new schema.

## jinja2 
Jinja2 is the templating engine for flask, allowing you to use for loops and if statements in html. The syntax for writing jinja statements are `{% some logic %}`.

## wtforms
Wtforms is a library that allows you to write out forms and use them in your routers/controllers (in this application they seemed to be joined together), in your templates all you need to do is to call `{{ wtf.quick_form(form) }}` in order to render it. {{}} represents statements that are evaluated by the browser.

## flask.g
Flask.g is like a dict that lives in each context of the application, basically for each different users they will have their own flask.g. You can store state in flask.g that is global for the user.

## environment variables
The app sometimes will have environment variables that is private(say your Google API key); you will need to keep it save. The best way is to keep it in an env file and reading it using python dotenv library.

## unit testing
The whole point of unit testing is to test functions piecewise, and it is best to create unit test for each module that you have completed as you go along. Luckily for us, python has a builtin unittest library. It uses the assert syntax 

## babel

## translation

## elasticsearch

## AJAX

## popups

## task queues

# future features
