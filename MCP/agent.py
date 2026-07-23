goal="find today weather"
print("goal:",goal)
print("planning..!")
steps=[
    "search the weather api",
    "prioritize the location",
    "read the result",
    "summerize"
]
for i in steps:
    print("executing",i)
    print()
print("goal finished")

# WAP to understand agent workflow

goal_completed=False 

while not goal_completed:
    print("thinking...!")
    action=input("enter the next action:")

    if action == "search":
        print("searching")
        print("observation:Articles found")
    elif action == "read":
        print("searching")
        print("read: the articles")
    elif action == "reasoning":
        print("reasoning")
        print("why/whatwe need...!")
    elif action == "finished":
        goal_completed=True
print("task completed")


#WAP to understand FUNCTION CALLING
def weather(city):
    return{
        "city":city,
        "temperature":39,
        "condition":"sunny"
    }

#callig the function
result=weather("Bangalore")
print("weather summary at:",result)

#WAP to implement calendar using function declaration
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
op=input("give any operation:")
if "add" in op.lower():
    nums=[int(x) for x in op.split() if x.isdigit()]
    result=add(nums[0],nums[1])
    print("addition:", result)
elif "sub" in op.lower():
    nums=[int(x) for x in op.split() if x.isdigit()]
    result=sub(nums[0],nums[1])
    print("subtraction:", result)
elif "mul" in op.lower():
    nums=[int(x) for x in op.split() if x.isdigit()]
    result=mul(nums[0],nums[1])
    print("multiplication:", result)
elif "div" in op.lower():
    nums=[int(x) for x in op.split() if x.isdigit()]
    result=div(nums[0],nums[1])
    print("division:", result)
elif "mod" in op.lower():
    nums=[int(x) for x in op.split() if x.isdigit()]
    result=mod(nums[0],nums[1])
    print("modulus:", result)
else:
    print("operation not found")