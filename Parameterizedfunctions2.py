#parameterized functions
#positional parameters
def greeting(salut, name):
            print(salut + " " +  name)



greeting("Good afternoon", "seth")
greeting("Good night", "seth")

greeting("seth", "Good evening")

greeting("Good morning", "amos")
#TypeError: greeting() missing 1 required positional argument: 'name'
