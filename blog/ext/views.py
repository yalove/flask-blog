# coding: utf-8

import os
from flask import send_from_directory, current_app, request, g

from ..app.users import model as user
from ..app.topics import model as topic
from ..app.comments import model as comment

g.model = [user, topic, comment]
