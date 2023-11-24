#Program 1

data = [10,501,22,37,100,999,87,351]
result = filter (lambda x: x>4,data)
print(list(result))

##OUTPUT — [10, 501, 22, 37, 100, 999, 87, 351]

#............................................................................................................#

#Program 2

from functools import reduce

test_list = [[5,6,3],["Gfg", 3, "is"],[9, "best", 4]]

print("The original list : " + str(test_list))

res = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], test_list, [])

print("The string instances : " + str(res))

res1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], test_list, [])

print("The string instances : " + str(res1))

#output
The original list : [[5, 6, 3], ['Gfg', 3, 'is'], [9, 'best', 4]] 
The string instances : ['Gfg', 'is', 'best'] 
The string instances : [5, 6, 3, 3, 9, 4]

#................................................................................................#

#Program 3

def fibonacci(count):
 fib_list = [0, 1]
 any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
 range(2, count)))
 return(fib_list[:count])
print(fibonacci(50))

#output
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#.......................................................................................................................#

#Program 4

#1
import re  
  
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  
  
def emailValid(email):  
    if re.fullmatch(regex, email):  
      print("The given mail is valid")  
    else:  
      print("The given mail is invalid")  
        
        
emailValid("sachin.sharma@gmail.com")  
emailValid("johnsnow123@yahoo.co.uk")  
emailValid("mathew123@...uk")  
emailValid("...@domain.us")

#output
The given mail is valid
The given mail is valid
The given mail is invalid
The given mail is invalid

#........................................................................................................#

#2
import re

def validate_phone_number(regex, phone_number):
    match = re.search(regex, phone_number)
    if match:
        return True
    return False

pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

test_phone_numbers = [
    "+1 (555) 123-4567",
    "555-123-4567",
    "555 123 4567",
    "+44 (0) 20 1234 5678",
    "02012345678",
    "invalid phone number"
]

for number in test_phone_numbers:
    print(f"{number}: {validate_phone_number(pattern, number)}")

#output
+1 (555) 123-4567: True
555-123-4567: True
555 123 4567: True
+44 (0) 20 1234 5678: True
02012345678: True
invalid phone number: False

#.......................................................................................................#




