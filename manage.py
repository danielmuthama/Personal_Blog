from app import create_app, db
from flask_script import Manager, Server
from app.models import User, NewBlog, Role
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin
from app.models import MyModelView
from flask_login import LoginManager, current_user
from flask_security import Security, SQLAlchemySessionUserDatastore


# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

#initiating Login Manager
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

admin = Admin(app)
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(NewBlog, db.session))

# user_datastore = SQLAlchemySessionUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

# Creating a python shell for  testing features in our apps and debugging using flask_script 

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, admin=admin)


if __name__ == '__main__':
    manager.run()