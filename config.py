
class Config(object):
	ROTTEN_TOMATOES_API_KEY = '8n57f3ytdxe5e2vqtsh4q4xc'
	SECRET_KEY = 'secret squirrel'

class DevelopmentConfig(Config):
	DEBUG = True
	WTF_CSRF_ENABLED = True

class ProductionConfig(Config):
	DEBUG = False
	WTF_CSRF_ENABLED = True

class TestConfiguration(Config):
	TESTING = True
	WTF_CSRF_ENABLED = False
	#DEBUG = True

config = {
	'default': DevelopmentConfig,
	'development': DevelopmentConfig,
	'test': TestConfiguration,
	'production': ProductionConfig
	}