from hash_brute_force_decode import hash_brute_force, hash_brute_force_wordlist_rules, hash_brute_force_list_with_name_rules
from hash_analyser import type_hash_analyser, list_hash_possible_hashcat
from choice_of_rules import choice_of_rules
from warning import warning
import time
import os



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

def crak_one_password():
    try:
        avertissement = str(input("En répondant 'Y', J'ai lu et accepté l'avertissement ci-dessus (Y/N) :"))
        if avertissement == "Y" or avertissement == "y":
            result=""
            #-------HASH-------------------------------------------------------------------------------#
            hash=str("912ea29a1e8116ff46d3c22c45c0aa03")
            #hash=str(input("Veuillez-entrez le hash à cracker : "))
            #------------------------------------------------------------------------------------------#
            '''
            #Nous faisons appel a la fonction permettant de nous renvoyer le type de hash le plus probable
            print(type_hash_analyser(hash))

            #Après que le terminal nous a proposé plusieur type de hash
            #Nous en choisissons un avec un Hashcat associer.
            type_hash = input("Veuillez-entrez le Hashcatmode correspondant (si aucun Hashcat Mode => N) : ")
            '''
            type_hash = list_hash_possible_hashcat(hash)
            if len(type_hash) == 0:
                error = "Hashcat ne peut pas décoder ce hash"
                print(error)
                return error
            else:
                type_hash = type_hash[0]
            if type_hash == "N" or type_hash == "n":
                print("Hashcat ne peut pas décoder ce hash")
            else:
                print("0-Straight")
                print("3-Brute-Force (Bon dernier des cas trop long)")
                print("9-Ataque personalisée")
                option=int(input("Please enter the desired attack type : "))
                if option==0:
                    start = time.time()
                    rules_y_n = str(input("Do you want to choose specific rules(Y/N) : "))
                    if rules_y_n == "Y" or rules_y_n == "y":
                        rules = choice_of_rules()
                        print(rules)
                        result = hash_brute_force_wordlist_rules(str(type_hash),hash,rules)
                    else:
                        result = hash_brute_force_wordlist_rules(str(type_hash),hash)
                    end = time.time()
                    elapsed = end - start
                if option==3:
                    print("Beginning of the Brute-force without wordlist and without rules")
                    start = time.time()
                    result = hash_brute_force(str(type_hash),hash)
                    end = time.time()
                    elapsed = end - start
                if option==9:
                    start = time.time()
                    name = str(input("Input the name of the victim : "))
                    personalized_attack(type_hash, hash, name)
                    end = time.time()
                    elapsed = end - start
                print(f'Execution time : {elapsed:.2}ms')
                print("\nresult : ",result)
                #fichier = open("data.txt", "a")
                #fichier.write(str(result))
                #fichier.close()
        else:
            print("Vous ne pouvez utiliser ce program")
    finally:
        print("\nBye !!!")

if __name__ == "__main__":
    while True:
        print(warning())
        crak_one_password()

