from flask import Blueprint, render_template, request, jsonify, redirect, url_for
 
views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html', name='Theo')

@views.route('/profile')
def profile():
    args = request.args
    object = args.get('object')
    return render_template('profile.html', object=object)

@views.route('/json')
def get_json():
    return jsonify({'name': 'Theo', 'age': 30})

@views.route('go-home')
def go_home():
    return redirect(url_for('views.index'))