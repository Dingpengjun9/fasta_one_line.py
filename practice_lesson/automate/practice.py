print("he","tr","ds",sep=",")
print("ff",end="")

def spam():
    eggs="spam"
    print(eggs)
def bacon():
    eggs="local"
    print(eggs)
    spam()
    print(eggs)
eggs="global"
bacon()
print(eggs)

def spam():
    global eggs
    eggs='spp'
eggs="global"
spam()
print(eggs)

def spam():
    print(eggs)
    eggs='local'
eggs='global'
spam()