def enter (age((age))):


    if age < 0: #condition = 1
        raise ValueError("Only positive integers are allowed")
    if age % 2 == 0: #condition = 2
        print("age is even")
    else:
        print("age is odd")
   
   
 try:
     num = int(input("Enter your age: "))
     enter age(num)
    
except ValueError:
    print("only positive numbers are allowed")
except: 
    print("something is wrong")