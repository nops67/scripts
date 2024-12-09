#Simple login/sign up system

import os, getpass, hashlib, csv

def createFile(fname):
    if not os.path.exists(fname):
        open(fname, 'w')
    return fname

def getInfo(fname):
    udict = {}
    with open(fname) as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            udict[line[0]] = line[1]
    return udict

def getPassword():
    pwd,pwd2 = 'a','b'
    while str(pwd) != str(pwd2):
        pwd = getpass.getpass("Password: ")
        pwd2 = getpass.getpass("Confirm your password: ")
        if str(pwd) != str(pwd2):
            print("Passwords do not match. Try again!")
        else:
            print("Registration complete!")
    pwhashed = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    return pwhashed
        
def saveInfo(fname, username, pwhashed):
    with open(fname, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([username] + [pwhashed])
         
def main():
    fname = createFile('users.csv') 
    users = getInfo(fname)

    option = input('''
            1 - Login
            2 - Sign Up

            Choose one option > ''')

    if option == '1':
        while True:
            username = input("Username: ")
            if username in users:
                pwd = getpass.getpass("Password: ")
                pwhashed = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
                if pwhashed in users[username]:
                    print("Logged in!")
                    break
                print("Password doesn't match. Try again!")
            else:
                print("Username doesn't exist. Try again!")
    elif option == '2':
        while True:
            username = input("Username: ")
            if username not in users:
                break
            print("Username already exists. Try again.")
        pwhashed = getPassword()
        saveInfo(fname, username, pwhashed)
    else:
        print("\nInvalid option. Try again!")

if __name__ == '__main__':
    main()
