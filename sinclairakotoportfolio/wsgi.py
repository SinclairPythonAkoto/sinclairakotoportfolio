from whitenoise import WhiteNoise

from app import sinclairakotoportfolio

application = WhiteNoise(app)
application.add_files('static/', prefix='static/')