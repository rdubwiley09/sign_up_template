from flask import Flask
from views.views import app

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001)
