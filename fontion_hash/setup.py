# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build

from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "fonction_hash.py",icon = "pop_art.ico")
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.
'''
buildOptions = dict( 
        includes = ["module1","module2","module3",...],
        include_files = ["fichier1.txt", "mon_icone.ico"]
)'''

setup(
    name = "Fontion Hash",
    version = "1.0",
    description = "Fonction Hash",
    author = "TitouEntreprise",
    #options = dict(build_exe = buildOptions),
    executables = executables
)