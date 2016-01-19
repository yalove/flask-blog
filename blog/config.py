import os

class Config(object):
	SECRET_KEY = os.getenv('SECRET_KEY') or ''
	DEBUG = True
	basedir = os.path.abspath(os.path.dirname(__file__))
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'work.db')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

	DEBUG_TB_INTERCEPT_REDIRECTS = False
	DEBUG_TB_PROFILER_ENABLED = 'user-enabled'

	CACHE_TYPE = 'simple'
	CACHE_DEFAULT_TIMEOUT = 300


	SEND_LOGS = False
	INFO_LOG = "info.log"
	ERROR_LOG = "error.log"

	UPLOAD_FOLDER = '/home/pi/www/web/blog/tmp/'
	ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

class Testing(Config):
	pass
		

class ProductionConfig(Config):
	pass



config = {
	'default' : Testing
}
		