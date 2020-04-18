#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Health Check.

Checks for various system problems, and notifies the administrator to check
the condition of the machine.
"""

import psutil
import emails
import socket


sender = 'automation@example.com'
recipient = '<username>@example.com'
body = 'Please check your system and resolve the issue as soon as possible.'
collector = {'sender': sender, 'recipient': recipient, 'subject': '', \
             'body': body}


def chk_cpu():
    """Check CPU."""
    cpu = psutil.cpu_percent()
    assert (cpu < 80), 'Error - CPU usage is over 80%'
    print("cpu looks good!")


def chk_storage():
    """Check storage."""
    usage = psutil.disk_usage('/')
    assert (usage[3] < 80), 'Error - Available disk space is less than 20%'
    print("disk usage is fine!")


def chk_memory():
    """Check RAM."""
    memory = psutil.virtual_memory()
    assert (memory[1] / 1024000 > 500), 'Error - Available memory \
            is less than 500MB'
    print("sufficient available RAM!")


def chk_server():
    """Check localhost resolves to loopback IP."""
    resolution = socket.gethostbyname('localhost')
    assert (resolution == '127.0.0.1'), 'Error - localhost cannot \
            be resolved to 127.0.0.1'
    print("localhost resolves to correct IP!")


def main():
    """Make it do what it do."""
    email_list = []
    try:
        chk_cpu()
    except AssertionError as error:
        print('adding email to queue')
        collector['subject'] = error.args[0]
        email_list.append(list(collector.values()))
    try:
        chk_storage()
    except AssertionError as error:
        print('adding email to queue')
        collector['subject'] = error.args[0]
        email_list.append(list(collector.values()))
    try:
        chk_memory()
    except AssertionError as error:
        print('adding email to queue')
        collector['subject'] = error.args[0]
        email_list.append(list(collector.values()))
    try:
        chk_server()
    except AssertionError as error:
        print('adding email to queue')
        collector['subject'] = error.args[0]
        email_list.append(list(collector.values()))
    for message in email_list:
        emails.send_email(message)


if __name__ == "__main__":
    main()
