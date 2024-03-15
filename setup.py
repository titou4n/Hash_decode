# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build

from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "cd\ crack_password.py",icon = "create_setup_exe\pop_art.ico")
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.
'''
buildOptions = dict( 
        includes = ["module1","module2","module3",...],
        include_files = ["fichier1.txt", "mon_icone.ico"]
)'''

setup(
    name = "Crak password",
    version = "1.0",
    description = "Crak password",
    author = "TService",
    #options = dict(build_exe = buildOptions),
    executables = executables
)