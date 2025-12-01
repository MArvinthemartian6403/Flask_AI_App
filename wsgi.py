# wsgi.py
from python_flask import app
from waitress import serve


if __name__ == '__main__':
    # Production server
    print("Starting Waitress production server...")
    serve(app, host='0.0.0.0', port=443)

    

application = app

if __name__ == "__main__":
    application.run()