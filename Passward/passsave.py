import os
from os import path
def passsave(web,user,passward,makesure):
    if passward != makesure:
        print("please makesure passward the same")
        return
    system = []
    pas = [web, user, passward]
    system.append(pas)
    with open(f"./Psave/{web}.txt", 'a+') as opw:
        for i in system[0]:
            opw.write(i + '\n')

def passchange(web, user, passward, makesure):
    if passward != makesure:
        print("please makesure passward the same")
        return
    system = []
    pas = [web, user, passward]
    system.append(pas)
    with open(f"./Psave/{web}.txt", 'w+') as opw:
        for i in system[0]:
            opw.write(i + '\n')
def items():
    url = './Psave'
    file = os.listdir(url)
    return file

