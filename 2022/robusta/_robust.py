def adjust_recipe(recipe, servings):
    new_recipe = [servings]
    old_servings = recipe[0]
    factor = servings / old_servings
    recipe.pop(0)
    while recipe:
        ingredient, amount, unit = recipe.pop(0)
        new_recipe.append((ingredient, amount * factor, unit))
    return new_recipe

adjust_recipe(3, 9)
