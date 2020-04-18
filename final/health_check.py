#!/usr/bin/env python3
"""Health Check.

Checks for various system problems, and notifies the administrator to check
the condition of the machine.
"""

import psutil
import emails
import socket


email_list = []
sender = 'automation@example.com'
recipient = '<username>@example.com'
body = 'Please check your system and resolve the issue as soon as possible.'


def chk_cpu():
    """Check CPU."""
    cpu = psutil.cpu_percent()
    assert (cpu < 80), 'high cpu alert!'
    print("cpu looks good!")


def chk_storage():
    """Check storage."""
    usage = psutil.disk_usage('/')
    assert (usage[3] < 80), "low storage space!"
    print("disk usage is fine!")


def chk_memory():
    """Check RAM."""
    memory = psutil.virtual_memory()
    assert (memory[1] / 1024000 > 500), "excessive RAM usage!"
    print("sufficient available RAM!")


def chk_server():
    """Check localhost resolves to loopback IP."""
    resolution = socket.gethostbyname('localhost')
    assert (resolution != '127.0.0.1'), "check your '/etc/hosts' file!"
    print("localhost resolves to correct IP!")


def main():
    """Make it do what it do."""
    chk_cpu()
    chk_storage()
    chk_memory()
    chk_server()
    for message in email_list:
        emails.send_email(message)


if __name__ == "__main__":
    main()
