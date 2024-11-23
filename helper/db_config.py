from flask_sqlalchemy import SQLAlchemy


def init_db(app):
    # Configure MySQL for SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/flask_final'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    return db
