
class BaseConfig(object):
	ROTTEN_TOMATOES_API_KEY = '8n57f3ytdxe5e2vqtsh4q4xc'
	SECRET_KEY = 'secret squirrel'

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	WTF_CSRF_ENABLED = True

class ProductionConfig(BaseConfig):
	DEBUG = False
	WTF_CSRF_ENABLED = True

class UnitTestConfig(BaseConfig):
	DEBUG = True
	WTF_CSRF_ENABLED = False
	TESTING = True

class IntegrationTestConfig(BaseConfig):
	DEBUG = True
	WTF_CSRF_ENABLED = False
	TESTING = True

config = {
	'default': DevelopmentConfig,
	'development': DevelopmentConfig,
	'unit_test': UnitTestConfig,
	'integration_test': IntegrationTestConfig,
	'production': ProductionConfig
	}
