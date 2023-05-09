from flask import Flask, render_template, request, redirect, url_for, flash
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=8001)
