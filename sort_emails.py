from os import remove, rename


def main():
    old_emails = []
    with open('emails.csv') as emails_csv:
        for line in emails_csv:
            email = line.lower().rstrip('\n')
            old_emails.append(email)

    old_emails.sort()
    new_emails = []
    for email in old_emails:
        if email not in new_emails:
            new_emails.append(email)

    with open('emails.tmp', 'a') as emails_tmp:
        for email in new_emails:
            emails_tmp.write(email + '\n')

    remove('emails.csv')
    rename('emails.tmp', 'emails.csv')


if __name__ == '__main__':
    main()
