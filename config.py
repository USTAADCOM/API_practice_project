#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
#import os
#basedir=os.path.abspath(os.path.dirname(__file__))
#app=Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://student.db"
#app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:////"+ os.path.join(basedir,"student.db")
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
#basedir = os.path.abspath(os.path.dirname(__file__))
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] =\
#        'sqlite:///'+ os.path.join(basedir,'student.db')
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#db = SQLAlchemy(app)
#ma=Marshmallow(app)


import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'student.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

