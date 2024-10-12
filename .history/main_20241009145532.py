def get_credentials():
    user = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if user == "admin" and pwd == "admin":
        print("Welcome admin")
    else:
        print("Invalid credentials")
        exit()
    return user, pwd

def main():
    user, pwd = get_credentials()
    print(user, pwd)

if __name__ == "__main__":
    main()