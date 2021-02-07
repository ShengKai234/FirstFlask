class BasicConfig:
    TYPE = 'THIS IS BASIC MODE'

class DevConfig(BasicConfig):
    TYPE = 'THIS IS DEV MODE'

class TestConfig(BasicConfig):
    TYPE = 'THIS IS TEST MODE'

config = {
    'dev': DevConfig,
    'test': TestConfig
}