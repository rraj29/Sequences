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

for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index] =="spam":
            del meal[index]
    print(meal)

print("-"*45)

for meal in menu:
    for item in meal:
        if item !="spam":
            print(item, end = ", ")
    print()


print("-"*45)

for meal in menu:
    new_meal = []
    for index in range(len(meal)-1,-1,-1):
        if meal[index] !="spam":
            new_meal.append(meal[index])
    print(new_meal)

