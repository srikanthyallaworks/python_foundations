from user_importer import UserImporter
from user_service import UserService

connection_string = "Server=thor01;Database=Contoso;User Id=app;Password=5uper5ecret;"
uri = "https://example.com/users"


def main():
    service = UserService(uri)
    users = service.get_users()

    importer = UserImporter(connection_string)
    importer.import_users(users)


if __name__ == "__main__":
    print("\n\n************** Begin *****************\n")
    main()
    print("\n\n************* Done! ******************\n")
