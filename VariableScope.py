# See "SimpleCombat.py" for info about these two "random" lines
import random
random.seed()

# ~~~~~~~~~~~~~~~~~~~~ A Brief Public Service Announcement About Variable Scope ~~~~~~~~~~~~~~~~~~~~
# When you use a variable, unless you specify otherwise, Python will assume you are referring to a "local"
# variable. A local variable is one that is created within a specific "scope". A "scope" is defined by any
# place you have an indentation. This would be, for example, a function declaration, an if statement, a for loop,
# a while loop, etc.

# These are some global variables we can access inside our "while" loop
globalNumber = 3
globalRunLoop = True

# We'll run our while loop until we randomly pick a number that matches the "globalNumber" variable
while globalRunLoop:
    localNumber = random.randint(0, 5)
    localSuccess = False
    print(localNumber)
    if localNumber == globalNumber:
        # Even though we've created a new scope with this "if" statement, we can still access "localSuccess" because
        # the scope of the "if" statement exists inside the scope of the "while" statement
        localSuccess = True
        innerLocalVar = "stuff"
        print("Success?", localSuccess)
        break
    # This statement won't work, however, because "innerLocalVar" was declared inside the scope of the "if" statement
    # and does not exist outside of it. This will generate an error because "innerLocalVar" is not defined within the
    # scope of the "while" statement.
    # print(innerLocalVar)
print("Done with loop\n")


def foo():
    # When creating a function that uses a global variables, we need to state that explicitly, otherwise Python will
    # think we're just declaring a local variable that happens to share the same name.
    global globalNumber
    globalNumber = 5
    print("Global number inside foo():", globalNumber)


def baz():
    globalNumber = 10
    print("Global number inside baz():", globalNumber)


print("Global number:", globalNumber)
foo()
print("Global number:", globalNumber)
baz()
print("Global number:", globalNumber)
# Notice that "globalNumber" doesn't permanently change after we run "baz()". This is because we weren't actually
# referring to the global "globalNumber" variable, we were merely creating a local variable that happened to
# be called "globalVariable"
