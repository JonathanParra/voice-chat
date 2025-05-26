import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG_MODE = False
    API-KEY-OPENIA= os.getenv("OPENIA-KEY")

class DevelopmentConfig(Config):
    DEBUG_MODE = True

class ProductionConfig(Config):
    pass

def get_config_for_environment():
    env=os.getenv("FLASK_ENV", "development")
    if env == 'production':
        return ProductionConfig
    elif env == 'development':
        return DevelopmentConfig
    else:
        return Config