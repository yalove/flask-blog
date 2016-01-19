# coding: utf-8

from flask.ext.login import LoginManager

lm = LoginManager()

def configure(app):
	lm.login_view = ''
	#lm.anonymous_user = Guest

	@lm.user_loader
	def load_user(user_id):
	    return User.query.get(int(user_id))
