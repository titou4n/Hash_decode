import os
import random
def data(result):
    i = 0
    if os.path.exists("data.txt"):
        with open("C:\hash_decode\data.txt",'r') as file:
                passwords = file.readlines()
                for password in passwords:
                    if password == result:
                        i += 1
                    else:
                        pass
                if i < 1:
                    data = open("data.txt", "a")
                    data.write("\n"+result)
                    data.close()
                else :
                    pass
    else:
        data = open("data.txt", "a")
        data.write(result)
        data.close()


def del_data():
    os.remove("data.txt")
    
while True : 
    option = str(input("what : "))
    if option == "s":
        for i in range(25):
            i = random.randint(0,5)
            data(str(i))
    if option == "d":
        del_data()

