import os
from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.heroku import Heroku

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)
manager = Manager(app)
heroku = Heroku(app)

class BaseConfig(object):
	SQLALCHEMY_DATABASE_URI = 'postgres://localhost/helloflask'
	DEBUG = True
app.config.from_object(BaseConfig)

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()

@app.route('/')
def hello():
	return 'Hello world!'
	
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Unicode(120))
	text = db.Column(db.UnicodeText, nullable=False)

admin.add_view(ModelView(Post, db.session))
