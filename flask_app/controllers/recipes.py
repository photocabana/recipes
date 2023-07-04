from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, recipe # import entire file, rather than class, to avoid circular imports



# Create Users Controller

@app.route("/recipes/create", methods=['POST'])
def create_recipe():
    if "user_id" not in session:return redirect('/')
    if recipe.Recipe.create_recipe(request.form):
        return redirect('/recipes/all')
    return redirect('/create/recipes/page')



# Read Users Controller


@app.route('/recipes/all')
def recipes_all():
    if "user_id" not in session:return redirect('/')
    recipe_list = recipe.Recipe.get_all_recipes()
    return render_template('recipes_all.html', recipes_all = recipe_list)


@app.route('/create/recipes/page')
def new_recipe():
    if "user_id" not in session:return redirect('/')
    return render_template('recipes_new.html')


@app.route('/recipes/<int:recipe_id>/profile')
def profile(recipe_id):
    if "user_id" not in session:return redirect('/')
    profile_recipe = recipe.Recipe.get_recipe_by_id(recipe_id)
    return render_template('recipes_profile.html', recipe = profile_recipe)


@app.route('/recipes/<int:recipes_id>/edit')
def edit_recipe(recipes_id):
    if "user_id" not in session:return redirect('/')
    profile_recipe = recipe.Recipe.get_recipe_by_id(recipes_id)
    return render_template('recipes_edit.html', recipe = profile_recipe)


# Update Users Controller

@app.route('/recipes/edit', methods=['POST'])
def edit_recipe_page():
    if "user_id" not in session:return redirect('/')
    if recipe.Recipe.update(request.form):return redirect('/recipes/all')
    return redirect(f"/recipes/{request.form['id']}/edit")



# Delete Users Controller

@app.route('/recipes/<int:recipe_id>/delete')
def delete(recipe_id):
    if "user_id" not in session:return redirect('/')
    recipe.Recipe.delete(recipe_id)
    return redirect("/recipes/all")

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