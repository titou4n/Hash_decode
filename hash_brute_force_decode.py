import os
import subprocess

def folder_path():
    folder_path = os.getcwd()
    return folder_path

def clean_result(result_of_command, hash):
    len_hash= int(len(hash))+1
    return result_of_command[len_hash:]


def hash_brute_force(method_hash, hash):
    '''
    hash_brute_force(method_hash: str or int, hash: str)
    return hash_decode:str

    '''
    assert type(hash)==str, ("Le hash doit etre en string")
    assert type(method_hash)==str or type(method_hash)==int , ("Le hash doit etre en string")
    os.system("cd "+folder_path()+"\hashcat-6.2.6 && hashcat -m "+ str(method_hash) +" -a 3 "+str(hash)+" ?a?a?a?a?a?a?a?a?a?a?a --increment")
    command=str("cd "+folder_path()+"\hashcat-6.2.6 && hashcat -m "+ str(method_hash) +" -a 3 "+str(hash)+" ?a?a?a?a?a?a?a?a?a?a?a --increment --show")
    result_of_command=subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8")
    return clean_result(result_of_command, hash)

def hash_brute_force_wordlist_rules(method_hash, hash, rules = "rules_hash\pantagrule-master\\rules\hashesorg.v6\pantagrule.hashorg.v6.raw1m.rule.gz"):
    '''
    hash_brute_force_wordlist_rules(method_hash: str or int, hash: str)
    return result:str
    '''
    assert type(hash)==str, ("Le hash doit etre en string")
    assert type(method_hash)==str or type(method_hash)==int , ("Le hash doit etre en string")
    os.system("cd "+folder_path()+"\hashcat-6.2.6 && hashcat --loopback -m "+str(method_hash)+" -a 0 -r "+folder_path()+"\\"+ str(rules) +" "+str(hash)+" "+folder_path()+"\wordlists\\rockyou.txt")
    command=str("cd "+folder_path()+"\hashcat-6.2.6 && hashcat --loopback -m "+str(method_hash)+" -a 0 -r "+folder_path()+"\\"+ str(rules) +" "+str(hash)+" "+folder_path()+"\wordlists\\rockyou.txt --show")
    result_of_command=subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8")
    return clean_result(result_of_command, hash)

def hash_brute_force_list_with_name_rules(method_hash, hash,name):
    '''
    hash_brute_force_list_with_name_rules(method_hash:str or int, hash:str ,name:str)
    return result:str
    '''
    assert type(hash)==str, ("Le hash doit etre en string")
    assert type(method_hash)==str or type(method_hash)==int , ("Le hash doit etre en string")
    assert type(name)==str, ("Le name doit etre en string")
    os.system("cd "+folder_path()+"\hashcat-6.2.6 && hashcat --loopback -m "+str(method_hash)+" -a 0 -r "+folder_path()+"\\rules_hash\pantagrule-master\\rules\hashesorg.v6\pantagrule.hashorg.v6.raw1m.rule.gz "+str(hash)+" C:\hash_decode\personalized_attack\\"+str(name)+".txt C:\\hash_decode\wordlists\\rockyou.txt")
    command=str("cd "+folder_path()+"\hashcat-6.2.6 && hashcat --loopback -m "+str(method_hash)+" -a 0 -r "+folder_path()+"\\rules_hash\pantagrule-master\\rules\hashesorg.v6\pantagrule.hashorg.v6.raw1m.rule.gz "+str(hash)+" C:\hash_decode\personalized_attack\\"+str(name)+".txt C:\\hash_decode\wordlists\\rockyou.txt --show")
    result_of_command=subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8")
    return clean_result(result_of_command, hash)
