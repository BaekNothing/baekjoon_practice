print(dir(input))
print('\033[95m',type(print),'\033[0m')
input = input()
print(dir(input))
print('\033[95m',type(input),'\033[0m')

def objectIsObejct() :
    print("Hello?")

objectIsObejct()
print(objectIsObejct)
newFunction = objectIsObejct
objectIsObejct = "Hello"
print(objectIsObejct)
newFunction()
