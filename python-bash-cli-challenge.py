new_recipe = dict()

new_recipe_name = input("Enter the name of the recipe: ")

new_recipe.update({"name": new_recipe_name})

new_recipe_serving_size = input("What is the serving size (in cups)? ")

new_recipe.update({"serving_size": new_recipe_serving_size})

new_recipe_calories = input("How many calories in one serving? ")

new_recipe.update({"calories": new_recipe_calories})


print(new_recipe_name)

print(new_recipe)


# ***** Task 2 Solution *****

# Leave Task 1 code as is and uncomment the two lines below to see Task 2 at work.

# import subprocess

# subprocess.Popen(["touch", f"Recipe: {new_recipe_name}"])


# ***** Task 1 Solution *****

recipe = open("./" + f"Recipe: {new_recipe_name}", "w")

recipe.write(f"{new_recipe_name}" + "\n\n\n")
recipe.write("Nutritional Info:" + "\n\n")
recipe.write("Serving Size: " + f"{new_recipe_serving_size}" + "\n")
recipe.write("Calories: " + f"{new_recipe_calories}" + "\n")

recipe.close()