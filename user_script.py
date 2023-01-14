"""
Complete the script.
"""

movie = input("Pick a movie from the following. Iron Man, Captain American, Thor")

if movie == "Iron Man":
    print("Iron Man stars Robert Downey Jr. and made $585 Million at the Box Office")
elif movie == "Captian America":
    print("Captain America stars Chris Evans and made $714 Million at the Box Office")
elif movie == "Thor":
    print("Thor stars Chris Hemsworth and made $449 Million at the Box Office")
else:
    print("That wasn't an option")

profits = [585, 714, 449]

minimum = min(profits)
maximum = max(profits)
average = sum(profits)/3
total = sum(profits)
print("The profit range was {} to {} million dollars.".format(minimum, maximum))






