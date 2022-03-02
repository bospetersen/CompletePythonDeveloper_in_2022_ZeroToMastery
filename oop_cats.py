#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Mis1', 7)
cat2 = Cat('Mis2', 8)
cat3 = Cat('Kitty', 1)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
   oldest = max(args) 
   return oldest

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'the oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)} years old')