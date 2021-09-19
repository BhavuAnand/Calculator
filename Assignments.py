######### SIMPLE CALCULATOR: ASSIGNMENT 1.1 #########

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option=int(input("Enter choice from 1-4:")

if option==1:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a+b
    print("The sum is = ",c)
    
elif option==2:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a-b
    print("The difference is = ",c)
    
elif option==3:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a*b
    print("The product is = ",c)

elif option==4:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a/b
    print("The quotient is = ",c)
else:
    print("The choice is invalid!")

           

           
######### WORKING WITH STRINGS: ASSIGNMENT 1 ################         
           
## 1. CAPITALIZE METHOD ##           
txt = "hello, and welcome."
x = txt.capitalize()
print (x)           
           
txt = "python is FUN!"
x = txt.capitalize()
print (x)
           
txt = "19 is my age."
x = txt.capitalize()
print (x)           
           
           
## 2. CASEFOLD METHOD ##            
txt = "Hello, And Welcome To Python!"
x = txt.casefold()
print(x)           
           
           
## 3. CENTER METHOD ##           
txt = "novel"
x = txt.center(20)
print(x)           
           
txt = "novel"
x = txt.center(20, "J")
print(x)            
           
           
## 4. COUNT METHOD ##           
txt = "I like to read novels, novels are good to read!"
x = txt.count("novels")
print(x)
           
txt = "I like to read novels, novels are good to read!"
x = txt.count("novels", 10, 18)
print(x)           
           
           
## 5. ENCODE METHOD ##           
txt = "I like novels"
x = txt.encode()
print(x)           
           
## 6. ENDSWITH METHOD ##           
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)           
           
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)           
           

## 7. EXPANDTABS METHOD ##           
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))           
           
           
## 8. FIND METHOD ##            
txt = "Hello, welcome to my lab."
x = txt.find("welcome")
print(x)           
           
txt = "Hello, welcome to my lab."
x = txt.find("e", 5, 10)
print(x)           

           
## 9. FORMAT METHOD ##           
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))           

           
## 10. INDEX METHOD ##            
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)           
           
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)           
           
           
## 10. ISALNUM METHOD ##           
txt = "Novel543"
x = txt.isalnum()
print(x)           
           
           
## 11. ISALPHA METHOD ##           
txt = "Novel6756"
x = txt.isalpha()
print(x)           
           
           
## 12. ISDECIMAL METHOD ##            
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())           
           
           
## 13. ISDIGIT METHOD ## 
txt = "7877654"
x = txt.isdigit()
print(x)
           
           
## 14. ISIDENTIFIER METHOD ##            
txt = "Novel"
x = txt.isidentifier()
print(x)           
           
           
## 15. ISLOWER METHOD ##           
txt = "hello world!"
x = txt.islower()
print(x)           
           
           
## 16. ISNUMERIC METHOD ##
txt = "565543"
x = txt.isnumeric()
print(x)           
           
           
## 16. ISPRINTABLE METHOD ##           
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)           
           
           
## 17. ISSPACE METHOD ##           
txt = "   "
x = txt.isspace()
print(x)           
           
           
## 18. ISTITLE METHOD ##           
txt = "Hello, I Love Novels!"
x = txt.istitle()
print(x)
           
           
## 19. ISUPPER METHOD ##            
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS BHAWNA"

print(a.isupper())
print(b.isupper())
print(c.isupper())           
           
           
## 20. JOIN METHOD ##           
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)           
           
           
## 21. LJUST METHOD ##           
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")           
           
           
## 22. LOWER METHOD ##             
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
           
           
## 23. LSTRIP METHOD ##           
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")           
           
           
## 24. MAKETRANS METHOD ##           
txt = "Hello Bhawna!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))           
           
           
## 25. PARTITION METHOD ##             
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)           
           
           
## 26. RSPILT METHOD ##           
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)           
           
           
## 27. RSTRIP METHOD ##             
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")           
  
           
## 28. SPLIT METHOD ##           
txt = "i love novels"
x = txt.split()
print(x)
           
txt = "hello, my name is Bhawna, I am 19 years old"
x = txt.split(", ")
print(x)
           
           
## 29. SPLITLINES METHOD ##           
txt = "I like music\I like novels"
x = txt.splitlines()
print(x)           
 
txt = "I like music\I like novels"
x = txt.splitlines(True)
print(x) 
           
           
## 30. STARTSWITH METHOD ##            
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)           
           
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)           
           
           
## 31. SWAPCASE METHOD ##           
txt = "Hello My Name Is BHAWNA"
x = txt.swapcase()
print(x)
           
           
## 32. TRANSLATE METHOD ##            
mydict = {83:  80}
txt = "Hello Bhawna!"
print(txt.translate(mydict))

txt = "Hello Bhawna!"
mytable = txt.maketrans("h", "a")
print(txt.translate(mytable))           

txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))           
                      
           
## 33. ZFILL METHOD ##            
txt = "50"
x = txt.zfill(10)
print(x)           
           
a = "hello"
b = "i like to read novels"
c = "789.5000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))           
           
           

           
######### WORKING WITH LISTS: ASSIGNMENT 1 ################           
           
## 1. APPEND METHOD ##
things = ['pen', 'pencil', 'note']
things.append("book") 

a = ['pen', 'pencil', 'note']
b = ["Ford", "BMW", "Volvo"]
a.append(b)           
           
           
## 2. CLEAR METHOD ##           
things = ['pen', 'pencil', 'note']
things.clear()           

           
## 3. COPY METHOD ##           
things = ['pen', 'pencil', 'note']
x = things.copy()           
 
           
## 4. COUNT METHOD ##            
things = ['pen', 'pencil', 'note']
x = things.count("pen")         
           
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]           
x = points.count(9)
           
           
## 5. EXTEND METHOD ##           
things = ['pen', 'pencil', 'note']
cars = ['Ford', 'BMW', 'Volvo']
things.extend(cars)           
           
things = ['pen', 'pencil', 'note']
points = (1, 4, 5, 9)
things.extend(points)           
           
           
## 6. INDEX METHOD ##             
things = ['pen', 'pencil', 'note']
x = things.index("note")           
           
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]           
x = points.index(3)           
           
           
## 7. INSERT METHOD ##           
things = ['pen', 'pencil', 'note']           
things.insert(1, "book")           

           
## 8. POP METHOD ##            
things = ['pen', 'pencil', 'note']           
things.pop(1)           
           
things = ['pen', 'pencil', 'note']           
x = things.pop(1)           
           
           
## 9. REMOVE METHOD ##            
things = ['pen', 'pencil', 'note']
things.remove("note")            
           
           
## 9. REVERSE METHOD ##           
things = ['pen', 'pencil', 'note']           
things.pop()           
           
           
## 9. SORT METHOD ##             
things = ['pen', 'pencil', 'note']           
things.sort()           
           
things = ['pen', 'pencil', 'note']           
things.sort(reverse=True)           
           
def func(a):
  return len(a)
things = ['pen', 'pencil', 'note']
things.sort(key=func)           
           
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)           
           
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)           
           
           
           
           

           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
