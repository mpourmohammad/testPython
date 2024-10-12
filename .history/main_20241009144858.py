def get_credentials():
    user = input("Enter your username: ")
    pwd = input("Enter your password: ")
    return user, pwd


if __name__ == "__main__":
    user, pwd = get_credentials()
    print(user, pwd, user + pwd)