''' 
1. Don't execute this following script !!!
2. This is for revision purpose.
3. Content of this script can be used to learn CRUD operations in Python shell.
4. CRUD = CREATE, READ, UPDATE & DELETE 
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# In Terminal type, 'python manage.py shell' to open python shell
# Then import the models from the app
from Food.models import Recipe

# CREATE
recipe_obj = Recipe(recipe_name = 'A', recipe_description = 'ABC')
recipe_obj.save()

# Or we can autosave and avoid using the car.save() function.
# Example 1:
Recipe.objects.create(recipe_name = 'B', recipe_description = 'XYZ')

# Example 2:
recipe_dict = {'recipe_name': 'C', 'recipe_description': 'GHF'}
Recipe.objects.create(**recipe_dict)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# READ - We can access all the created data in MySQL database and also in shell using for loop
recipe_obj = Recipe.objects.all()

for recipe in recipe_obj:
    print(recipe.recipe_name,recipe.recipe_description)

'''Must remember!!!
1. Data can be instered into the table both via the shell and MySQL.
2. Incase we insert the data via MySQL, we need to exit() and start the shell again to see the change within the shell.
'''

# Let's make it better with 'f strings'
recipe_obj = Recipe.objects.all()

for recipe in recipe_obj:
    print(f'{recipe.recipe_name} contains {recipe.recipe_description}.')

'''
1. As I previously learned, Django automatically adds the 'ID' field to all models.
2. The 'ID' field represents the 'Primary Key' in the tables in MYSQL database.
3. So we can print the ID too.
'''
recipe_obj = Recipe.objects.all()

for recipe in recipe_obj:
    print(f'{recipe.id}, {recipe.recipe_name} contains {recipe.recipe_description}.')

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# UPDATE

# filter() - If a wrong 'ID' is provided, it will return an empty <Query Set []> instead of raising an exception.
Recipe.objects.filter(id = 3).update(recipe_name = 'Nissan', recipe_description = '180')

# get() - If a wrong 'ID' is provided, it will raise the DoesNotExist exception.
recipe_obj = Recipe.objects.get(id = 4)
recipe_obj.recipe_name = 'C'
recipe_obj.recipe_description = 'MNO'
recipe_obj.save()

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# DELETE

# !!! THIS IS DELETE ALL RECORDS !!!
Recipe.objects.all().delete() # Be Cautious.

# The right way
Recipe.objects.get(id = 1).delete()
# OR
Recipe.objects.filter(id=1).delete()

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# IMPORTANT - ways to handle the DoesNotExist exception

# 1 - using try and except
try:
    recipe = Recipe.objects.get(id = 2)
except Recipe.DoesNotExist:
    print("Recipe not found.")
else:
    print("Recipe found:", recipe)

# 2 - using the inbuilt 404 exception of Django
from django.shortcuts import get_object_or_404

recipe_obj = get_object_or_404(Recipe, id = 3)
print("Recipe found:", recipe_obj)