# coding: utf-8

def configure(app):
    @app.before_first_request
    def initialize():
    	from .db import db 
    	db.create_all()
        app.logger.info("Called only once, when the first request comes in")
