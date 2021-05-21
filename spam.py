menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "sausage", "bacon", "spam"],
    ["spam", "sausage", "bacon", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "bacon", "spam", "spam", "tomato", "spam"],
]
#   * the COMMA after the last entry is redundant, but it'll help us in adding new items without error.
#   * the style guide suggests to use them always.

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("{} has a spam count of {}."
              .format(meal,meal.count("spam")))
