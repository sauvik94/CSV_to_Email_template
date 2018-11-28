import csv
import re
import os

with open('sample_email.csv', newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['first_name'] + " " + row['last_name']
        email = row['email']
        cname = row['company_name']
        subject = row['subject']
        body = row['Email Boby']
        email_match = re.findall(r'[\w\.-]+@[\w\.-]+', body)
        phone_match = re.findall(r'([0-9]{3}-[0-9]{3}-[0-9]{4})', body)
        if email_match:
            email_match = str(email_match[0])
        if phone_match:
            phone_match = str(phone_match[0])

        # creating email templates for each user
        file = open(name + '.html', "w+")
        file.writelines("Email to: " + email + '\n\n')
        file.writelines("Subject Line: " + subject + '\n\n')
        file.writelines('Hi ' + name + ',' + '\n\n')
        file.writelines(body + '\n\n')
        file.writelines("Thanks," + '\n\n')
        file.write('fast_name last_name')

        # creating csv for existing email in in email body

        if email_match:
            if not os.path.isfile('fetched_email.csv'):
                fetch = open('fetched_email.csv', "w+")
                fetch.close()

            is_header = False
            with open('fetched_email.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                if reader.fieldnames:
                    is_header = True
            csvfile.close()

            with open('fetched_email.csv', 'a') as csvfile:
                fieldnames = ['name', 'email', 'fetched_email', 'company_name']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if not is_header:
                    writer.writeheader()
                writer.writerow({'name': name, 'email': email, 'fetched_email': email_match, 'company_name': cname})
            csvfile.close()

        # creating csv for existing phone in in email body

        if phone_match:
            if not os.path.isfile('fetched_phone.csv'):
                fetch = open('fetched_phone.csv', "w+")
                fetch.close()

            is_header = False
            with open('fetched_phone.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                if reader.fieldnames:
                    is_header = True
            csvfile.close()

            with open('fetched_phone.csv', 'a') as csvfile:
                fieldnames = ['name', 'email', 'fetched_phone', 'company_name']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if not is_header:
                    writer.writeheader()
                writer.writerow({'name': name, 'email': email, 'fetched_phone': phone_match, 'company_name': cname})
            csvfile.close()
