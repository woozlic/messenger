#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import subprocess
import sys

import redis.exceptions
from redis import Redis


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messenger.settings')
    try:
        from django.core.management import execute_from_command_line
        redis_host = '127.0.0.1'
        redis_port = '6379'
        r = Redis(redis_host, redis_port)
        try:
            r.ping()
        except redis.exceptions.ConnectionError:
            subprocess.call(['docker', 'run', '-p', '6379:6379', '-d', 'redis:5'])
        if not r.ping():
            raise ValueError('Can not connect to Redis')
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
