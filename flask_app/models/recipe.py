
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
from flask_app.models import user
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Recipe:
    db = "recipe_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator_name = None
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models

    @classmethod
    def create_recipe(cls, recipe):
        if not cls.validate_recipe_data(recipe):
            return False
        query = """
        INSERT INTO recipes (
            name, 
            description, 
            instructions, 
            date_made, 
            under,
            user_id
            )
        VALUES (
            %(name)s, 
            %(description)s, 
            %(instructions)s, 
            %(date_made)s, 
            %(under)s, 
            %(user_id)s
            )
        ;"""
        results = connectToMySQL(cls.db).query_db(query, recipe)
        return results


    # Read Users Models

    @classmethod
    def get_all_recipes(cls):
        query = """
        SELECT *
        FROM recipes
        JOIN users
        ON recipes.user_id = users.id
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for recipe in results:
            this_recipe = cls(recipe)
            user_info = {
                'id' : recipe['users.id'],
                'first_name' : recipe['first_name'],
                'last_name' : recipe['last_name'],
                'email' : recipe['email'],
                'password' : "",
                'created_at' : recipe['users.created_at'],
                'updated_at' : recipe['users.updated_at']
            }
            this_recipe.creator_name = user.User(user_info)
            recipes.append(this_recipe)
        return recipes


    @classmethod
    def get_recipe_by_id(cls, recipe_id):
        data = { 'id' : recipe_id }
        query = """
        SELECT *
        FROM recipes
        JOIN users
        ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        if not result:
            return False
        result = result[0]
        this_recipe = cls(result)
        this_data = {
            'id' : result['id'],
            'first_name' : result['first_name'],
            'last_name' : result['last_name'],
            'email' : result['email'],
            'password' : "",
            'created_at' : result['users.created_at'],
            'updated_at' : result['users.updated_at']
        }
        this_recipe.creator_name = user.User(this_data)
        return this_recipe


    # Update Users Models

    @classmethod
    def update(cls, data):
        if not cls.validate_recipe_data(data):
            return False
        query = """
        UPDATE recipes
        SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under=%(under)s
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return True
    


    # Delete Users Models

    @classmethod
    def delete(cls, id):
        data = { 'id' : id }
        query = """
        DELETE FROM recipes
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)




    # Helper Methods
    
    @staticmethod
    def validate_recipe_data(data):
        is_valid = True
        if len(data['name']) < 3 :
            flash('Your recipe name is too small. Needs 3 characters. Try Again!')
            is_valid = False
        if len(data['description']) < 3 :
            flash('Your description needs to contain at least three characters. Try Again!')
            is_valid = False
        if len(data['instructions']) < 3 :
            flash('Your instructions needs to contain at least three characters. Try Again!')
            is_valid = False
        return is_valid
