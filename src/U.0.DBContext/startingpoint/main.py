from user_importer import import_users
from users import users

def main():
    import_users(users)

if __name__ == "__main__":
    print('\n\n************** Begin *****************\n')
    main()
    print('\n\n************* Done! ******************\n')

