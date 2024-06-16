import app
import os

app = app.create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
  app.run()