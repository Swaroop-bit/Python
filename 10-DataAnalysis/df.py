# string concatenation (how to put strings together)
# suppose we want to create a string that says "subscrie to __"
youtuber = "Vidhi Arora" #some  string variable

# a few ways to do this
print("subscribe to" + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb")
famous_person= input("famous person: ")

madlib = f"Computer Engineering is so {adj}! It makes me so excited all the time bcoz\
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)