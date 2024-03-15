import subprocess
import os

def type_hash_analyser(hash:str):
    '''
    type_hash_analyser(hash) -> renvoit le résultat de la commande "hashid -m"
    utilise "hashid -m" -> reperer les types de hash possibles
    '''
    assert type(hash) == str, "Le hash doit être un string"
    command_hash_type = "hashid -m "+ str(hash)
    result_command_hash_type = subprocess.check_output(command_hash_type, shell=True, stderr=subprocess.STDOUT).decode("utf-8")
    if result_command_hash_type == ("Analyzing '",hash,"'[+] Unknown hash"):
        return None
    else:
        return result_command_hash_type
    
def list_hash_possible_hashcat(hash:str):
    '''
    list_hash_possible_hashcat(hash:str) renvoie la liste des type de hashs posibles
    Mode de la fonction open()
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exist
    '''
    assert type(hash) == str, "Le hash doit être un string"
    os.makedirs("type_of_hash", exist_ok=True)
    fichier_name = open("type_of_hash\\type_of_hash.txt", "w")
    fichier_name.write(str(type_hash_analyser(hash)))
    fichier_name.close()
    list_type_of_hash = []
    with open("type_of_hash\\type_of_hash.txt",'r') as file:
        lines = file.readlines()
        for line in lines:
            if "[Hashcat Mode:" in line:
                occurence = int(line.find(":"))+1
                type_of_hash = line[occurence:-2]
                list_type_of_hash.append(int(type_of_hash))
    os.remove("type_of_hash\\type_of_hash.txt")
    os.rmdir("type_of_hash")
    return list_type_of_hash