import subprocess


new_recipe = dict()

new_recipe_name = input("Enter the name of the recipe: ")

new_recipe.update({"name": new_recipe_name})

new_recipe_serving_size = input("What is the serving size (in cups)? ")

new_recipe.update({"serving_size": new_recipe_serving_size})

new_recipe_calories = input("How many calories in one serving? ")

new_recipe.update({"calories": new_recipe_calories})

new_recipe_carbs = input("How many carbs in one serving? ")

new_recipe.update({"carbs": new_recipe_carbs})

new_recipe_protein = input("How many grams of protein in one serving? ")

new_recipe.update({"protein": new_recipe_protein})

print(new_recipe_name)

print(new_recipe)


# subprocess.Popen(["touch", f"Recipe: {new_recipe_name}"])

# Note: a Bash command in a subprocess is doable to create a file from the Python code, but it's not necessary because the "w" parameter in the open() method creates a file if the one specified to be opened doesn't exist

recipe = open("./" + f"Recipe: {new_recipe_name}", "w")

recipe.write(f"{new_recipe_name}" + "\n\n\n")
recipe.write("Nutritional Info:" + "\n\n")
recipe.write("Serving Size: " + f"{new_recipe_serving_size}" + "\n")
recipe.write("Calories: " + f"{new_recipe_calories}" + "\n")
recipe.write("Carbs: " + f"{new_recipe_carbs}" + "\n")
recipe.write("Protein: " + f"{new_recipe_protein}" + "\n")

recipe.close()