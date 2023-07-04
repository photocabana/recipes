from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, recipe # import entire file, rather than class, to avoid circular imports
from flask_app.models import recipe


# Create Users Controller


@app.route("/users/create", methods=['POST'])
def create_user():
    if user.User.create_user(request.form):
        return redirect('/recipes/all')
    return redirect('/')


# Read Users Controller

@app.route('/')
def index():
    return render_template('index.html')


# Update Users Controller



# Delete Users Controller





# Login / Logout

@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/users/login', methods=['POST'])
def login():
    if user.User.login(request.form):
        return redirect('/recipes/all')
    return redirect('/')




# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.