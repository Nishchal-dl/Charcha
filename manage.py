#!/usr/bin/env python
import os
import re
import sys


def read_env():
    """
    See https://wellfire.co/learn/easier-12-factor-django/
    Pulled from Honcho code with minor updates, reads local default
    environment variables from a .env file located in the project root
    directory.

    """



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "charcha.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    read_env()
    execute_from_command_line(sys.argv)
