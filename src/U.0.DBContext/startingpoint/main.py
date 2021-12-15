from user_importer import UserImporter
from users import users

connection_string = 'Server=thor01;Database=Contoso;User Id=app;Password=5uper5ecret;'

def main():
    importer = UserImporter(connection_string)
    importer.import_users(users)

if __name__ == "__main__":
    print('\n\n************** Begin *****************\n')
    main()
    print('\n\n************* Done! ******************\n')

