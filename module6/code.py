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

# add_ingredients("ingredients")


# The global keyword in python scoping
weigth_to_lift_in_kg = 20
def change_weigth(new_weight):
    global weigth_to_lift_in_kg
    weigth_to_lift_in_kg = new_weight
    print("weight changed!")


def show_current_weigth_charge():
    print(weigth_to_lift_in_kg, "kg are being lifted at the moment.")

show_current_weigth_charge()
change_weigth(25)
show_current_weigth_charge()