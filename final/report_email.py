#!/usr/bin/env python3
"""Main functionality."""

import os
import datetime
import reports
import emails


def load_data(directory, file_list):
    """Load the contents of filename as a JSON file."""
    data = []
    for x in file_list:
        item = []
        with open(os.path.join(directory, x), 'r') as f:
            for line in f:
                item.append(line.strip())
        data.append([item[0], item[1]])
    return data


def list_to_pp(data):
    """Turn the data in data into a paragraph."""
    additional_info = ''
    for item in data:
        additional_info += 'name: ' + item[0] + '<br/>'
        additional_info += 'weight: ' + item[1] + '<br/><br/>'
    return additional_info


def main():
    """Make it do what it do."""
    directory = os.getcwd() + '/supplier-data/descriptions'
    filename = '/tmp/processed.pdf'
    title = 'Processed Update on ' + str(datetime.date.today())
    additional_info = ''
    sender = 'automation@example.com'
    recipient = 'username@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. \
            A detailed list is attached to this email.'
    attachment_path = filename
    file_list = [f for f in os.listdir(directory) if not f.startswith('.')]
    data = load_data(directory, file_list)
    additional_info += list_to_pp(data)
    print(additional_info)
    reports.generate_report(filename, title, additional_info)
    emails.send_email(emails.generate_email(sender, recipient,
                                            subject, body,
                                            attachment_path))


if __name__ == "__main__":
    main()
