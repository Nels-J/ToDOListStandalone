def interactive_menu():
    pass


def display_menu():
    print("---------- To Do List Application menu-----------")
    print('''Ajouter une tâche ( commande [add] ),
    - Effectuer une tâche ( commande [done] ),
    - Modifier le libellé d'une tâche ( commande [update] ),
    - Lister les tâches en cours ( commande [list] ),
    - Lister les tâches terminées ( commande [list_done] ),
    - Lister toutes les tâches ( commande [list_all] ),
    - Quitter ( commande [quit] ).
    ''')


def run_app():
    # interactive_menu will manage the IHM
    interactive_menu()
    # display_menu will manage all the print's required for the interactive menu
    display_menu()


# Lancer l'application
run_app()
