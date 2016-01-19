import datetime
from flask import Blueprint, render_template, current_app
from ..models import User, Topic
from ..ext import cache, db
from ..dashboard.dashmodel import DashModel


index = Blueprint('index', __name__)


@index.route("/")
@cache.cached(timeout=50)
def indexs():
    time = datetime.datetime.now()
    users = User.query.all()

    # zz = dict()
    # xx =dict()
    # tt = dict()
    # for column in User.__table__._columns:
    #     zz[column.name] = {'label': column.name,
    #                        'column': getattr(User, column.name)}
    # for column in Topic.__table__._columns:
    #     xx[column.name] = {'label': column.name,
    #                        'column': getattr(Topic, column.name)}
    # for column in User.__table__._columns:

    #     for user in User.query.all():
    #         hh =dir(user)
    #         x = column.name
    #         print x
    #         tt['%s--%s'% (user,column.name)] = recursive_getattr(user, x)

    return render_template('z.html', time=time, users=users,)


@index.route("/t")
def ttt():
    return "hello"



