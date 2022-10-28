import sys


def add_new_task():
    print(">>> Lancement de la fonction add <<<")
    print("\nTâche ajoutée fictivement")


def define_task_as_done():
    pass


def update_task():
    pass


def show_active_tasks():
    pass


def show_closed_tasks():
    pass


def show_all_tasks():
    pass


def interactive_menu():
    # fixme if user input = empty/blank
    # todo for quit use a python sys.exit() or raise a specific exception related
    display_menu()
    user_prompt_input = input("Merci de choisir votre commande: ")
    print(f"Vous avez choisi la commande : {user_prompt_input}")
    try:
        if user_prompt_input == 'add':
            add_new_task()
        elif user_prompt_input == 'done':
            define_task_as_done()
        elif user_prompt_input == 'update':
            update_task()
        elif user_prompt_input == 'list':
            show_active_tasks()
        elif user_prompt_input == 'list_done':
            show_closed_tasks()
        elif user_prompt_input == 'list_all':
            show_all_tasks()
        elif user_prompt_input == 'quit':
            print(">>> Lancement de la fonction quit <<<")
            print("A bientôt :)")
            sys.exit()
        raise ValueError
    except ValueError as e:
        print(e)
    else:
        raise ValueError

def display_menu():
    print("---------- To Do List Application menu-----------")
    print('''
    - Ajouter une tâche                 ->  [add]
    - Effectuer une tâche               ->  [done]
    - Modifier le libellé d'une tâche   ->  [update] 
    - Lister les tâches en cours        ->  [list]
    - Lister les tâches terminées       ->  [list_done]
    - Lister toutes les tâches          ->  [list_all]
    - Quitter                           ->  [quit]
    ''')


def run_app():
    # interactive_menu will manage the IHM
    interactive_menu()


# Lancer l'application
run_app()
