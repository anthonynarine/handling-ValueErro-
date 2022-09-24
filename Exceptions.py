# https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@bd6e4b312f2b4e8d9e89ec63708a367a/block-v1:HarvardX+CS50P+Python+type@vertical+block@cb3e9f779e7a46ff9af9a64d3efbee01


#string will break this code, cat

try:
    x = int(input("What's  x? "))
    print (f"x is {x}")
except ValueError:
    print("x should be an integer")

#refined below


try:
    x = int(input("What's  x? "))  #we want to have min amout of line under try
except ValueError:
    print("x should be an integer")
else:
    print (f"x is {x}")


#final refinement
while True:    
    try:
        x = int(input("What's  x? "))    #this while loop will keep prompting the user 
    except ValueError:                   # for an entry until it gets a valid entry
        print("x should be an integer")
    else:
        break
    
print (f"x is {x}")  #after look break we print x


