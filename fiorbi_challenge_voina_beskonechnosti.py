from random import randint

problem_list = [
    "Living Tree", "Furby Flying Saucer", "Spirit from the Parallel Universe", "Artificial Intelligense", "Captures of Brain", "Furrbytish Centipede", "Mad Godzilla", "Black Furby", "Titanium Robot"]

problem = problem_list[randint(0,len(problem_list)-1)]
print("The threat they faced -",problem)

list_of_heroes =[input(), input(), input()]

print("This Superheroes", list_of_heroes,"went a mission")