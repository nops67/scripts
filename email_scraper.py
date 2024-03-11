import os

def main():
    import re
    import csv

    if not os.path.exists('emails.txt'):
        with open('emails', 'w'):
            print("Created emails.txt")
    if not os.path.exists('emails.csv'):
        with open('emails.csv', 'w'):
            print("Created emails.csv")

    with open('emails.txt', 'r', errors="ignore") as file:
        line = file.read()

    new_emails = re.findall(r'[\w\.-]+@[\w\.-]+', line) # Regex to get emails
    print(len(new_emails),'emails from file')

    add_emails = []

    with open('emails.csv', 'r',errors="ignore") as csvFile:
        reader = csv.reader(csvFile)
        old_emails = [email[0] for email in reader]
        print('Old emails',len(old_emails))

        for email in new_emails:
            if email in old_emails:
                pass
            else:
                old_emails.append(email)
                add_emails.append(email)

    print('New emails',new_emails)
    print('Added emails',len(add_emails))
    print('Total emails',len(old_emails))

    with open('emails.csv','a', newline='') as fd:
        for email in add_emails:
            writer = csv.writer(fd)
            writer.writerow([email])

        print('Successfully written file')

main()
