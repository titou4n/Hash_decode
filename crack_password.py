from hash_brute_force_decode import hash_brute_force, hash_brute_force_wordlist_rules, hash_brute_force_list_with_name_rules
from hash_analyser import type_hash_analyser, list_hash_possible_hashcat
from choice_of_rules import choice_of_rules
from warning import warning
import time
import os



def give_time():
    return time.time()




def personalized_attack(type_hash, hash, name):
    os.makedirs("personalized_attack", exist_ok=True)
    fichier_name = open("personalized_attack\\"+name+".txt", "a")
    fichier_name.write(str(name))
    fichier_name.close()
    print("Please enter information of the victim in the document 'personalized_attack\\"+name+".txt' : ")
    validation = str(input("Avez-vous fini de remplir les information (Y/N) : "))
    if validation == "Y" or validation == "y":
        result = hash_brute_force_list_with_name_rules(str(type_hash),hash, name)
        return result

def crak_one_password(hash):
    result=""
    #Fonction permettant de nous renvoyer le type de hash le plus probable :
    list_type_hash = list_hash_possible_hashcat(hash)
    if list_type_hash == []:
        print(f"Hashcat ne peut pas décoder ce hash")
        return None
    else:
        type_hash = list_type_hash[0]
        print("0-Straight")
        print("3-Brute-Force (Bon dernier des cas car trop long)")
        print("9-Ataque personalisée")
        option=str(input("Please enter the desired attack type : "))
        if option=="0":
            rules_y_n = str(input("Do you want to choose specific rules(Y/N) : "))
            if rules_y_n == "Y" or rules_y_n == "y":
                rules = choice_of_rules()
                print(rules)
                start = give_time()
                result = hash_brute_force_wordlist_rules(str(type_hash),hash,rules)
            else:
                start = give_time()
                result = hash_brute_force_wordlist_rules(str(type_hash),hash)
            end = give_time()
            elapsed = end - start
        if option=="3":
            print("Beginning of the Brute-force without wordlist and without rules")
            start = give_time()
            result = hash_brute_force(str(type_hash),hash)
            end = give_time()
            elapsed = end - start
        if option=="9":
            start = give_time()
            name = str(input("Input the name of the victim : "))
            personalized_attack(type_hash, hash, name)
            end = give_time()
            elapsed = end - start
        else:
            print("Veuillez faire un choix")
            crak_one_password(hash)
        print(f'Execution time : {elapsed:.2}ms')
        print("\nresult : ",result)
        fichier = open("data.txt", "a")
        fichier.write(str(result))
        fichier.close()


if __name__ == "__main__":
    while True:
        print(warning())
        avertissement = str(input("En répondant 'Y', J'ai lu et accepté l'avertissement ci-dessus (Y/N) :"))
        if avertissement == "Y" or avertissement == "y":
            #-------HASH-------------------------------------------------------------------------------#
            hash=str(input("Veuillez-entrez le hash à cracker : "))
            #------------------------------------------------------------------------------------------#
            crak_one_password(hash)
        else:
            print("Vous ne pouvez utiliser ce programe")


