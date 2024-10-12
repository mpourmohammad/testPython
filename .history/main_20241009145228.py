def get_credentials():
    user = input("Enter your username: ")
    pwd = input("Enter your password: ")
    return user, pwd

def main():
    user, pwd = get_credentials()

if __name__ == "__main__":
    main()