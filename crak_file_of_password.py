import os
from hash_analyser import list_hash_possible_hashcat
import time
from hash_brute_force_decode import hash_brute_force_wordlist_rules
from data import data
from warning import warning

def verif_format_file(chemin):
    point = int(chemin.find("."))
    format = chemin[point:]
    if format == ".txt":
        return True
    else:
        return False

def name_of_file(chemin):
    point = int(chemin.find("."))
    inverse = "".join(reversed(chemin))
    back_slash  = int(inverse.find("\\"))
    name = chemin[-back_slash:point]
    return name

def crak_file_password_hash(file_hash="C:\hash_decode\hash_append\hash.txt"):
    assert type(file_hash)==str, "Le fichier contenant les hashs doit etre un chemin d'accès en str"
    
    #assert verif_format_file(file_hash)==True, "Le fichier doit être au format '.txt'"
    if verif_format_file(file_hash)==True:
        assert os.path.exists(file_hash)==True, "Le chemin donné n'est pas valide"
        start = time.time()
        #------CREATE-FILE----------------------------------------------#
        os.makedirs("hash_result", exist_ok=True)
        chemin_file_hash_result = "hash_result\\result_"+name_of_file(file_hash)+".txt"
        chemin_file_hash_result_with_method = "hash_result\\result_with_method_"+name_of_file(file_hash)+".txt"
        file_hash_result = open(chemin_file_hash_result, "a")
        file_hash_result.close()
        file_hash_result_with_method = open(chemin_file_hash_result_with_method, "a")
        file_hash_result_with_method.close()
        #---------------------------------------------------------------#
        with open(file_hash,'r') as file:
            hashs = file.readlines()
            for hash in hashs:
                #------LIST-OF-HASH-POSSIBLE-------------------------------------------#
                method_hash = list_hash_possible_hashcat(hash)
                #----------------------------------------------------------------------#
                if len(method_hash) == 0:
                    error = "Hashcat ne peut pas décoder ce hash"
                    print("Hashcat ne peut pas décoder ce hash : "+str(hash))
                    return error
                else:
                    method_hash = str(method_hash[0])
                    hash = hash.strip()
                    #------BRUTE-FORCE-------------------------------------------#
                    result = hash_brute_force_wordlist_rules(method_hash,hash)
                    result = result.strip()
                    #------------------------------------------------------------#
                    end = time.time()
                    elapsed = end - start
                    #------INFORMATION-RETURN-USER--------------------------------------------#
                    print("\nINFORMATION ON THIS HASHCAT")
                    print("\n"+hash+" : "+result)
                    print("Type of hash uses : "+method_hash)
                    print(f'Execution time    : {elapsed:.2}ms')
                    #------APPEND-HASH-IN-FILE----------------------------------------------#
                    os.makedirs("hash_result", exist_ok=True)
                    file_hash_result = open(chemin_file_hash_result, "a")
                    file_hash_result.write("\n"+str(result))
                    file_hash_result.close()
                    file_hash_result_with_method = open(chemin_file_hash_result_with_method, "a")
                    file_hash_result_with_method.write("\n"+str(hash)+"  ("+str(method_hash)+"):    "+result)
                    file_hash_result_with_method.close()
                    #data(result)
                    #-----------------------------------------------------------------------#
    else:
        print("Le fichier doit être au format '.txt'")
        return "Le fichier doit être au format '.txt'"


if __name__ == "__main__":
    while True:
        print(warning())
        chemin = str(input("Veuillez entrez le chemin du fichier '.txt' contenant les hashs : "))
        crak_file_password_hash(chemin)