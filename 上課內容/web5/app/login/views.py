from . import login
from ..model import db,User,Role

@login.route("/")
def login():
    user=User.query.filter_by(username='john').first()
    return f"<h1>{user.username}</h1>"