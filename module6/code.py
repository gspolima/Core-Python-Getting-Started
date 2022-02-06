def compose_banner(message, outer_border="-"):
    outer_border = outer_border * len(message)
    return f""" 
        {outer_border}
        {message}
        {outer_border}"""

banner = compose_banner("Python is sassy")
print(banner)

# A consequence of python's only-once-at-runtime evaluation policy
def add_ingredients(recipe, ingredients=[]):
    ingredients.append("eggs")
    ingredients.append("coffee")
    ingredients.append("whole wheat bread")
    print(recipe)
    print(ingredients)

add_ingredients("ingredients")