fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         }

print(fruit)

veg = {"sprouts":"have on tuesdays",
       "spinach": "popeye's favorite",
       "eggplant": "violet colored veggie"}

veg.update(fruit)
print(veg)

print(fruit.update(veg))    # Returns None
print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)