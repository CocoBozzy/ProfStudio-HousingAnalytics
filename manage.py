#!/usr/bin/env python
<<<<<<< HEAD
"""HousingAnalytics's command-line utility for administrative tasks."""
=======
"""Django's command-line utility for administrative tasks."""
>>>>>>> origin/Joel-Test-Env
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HousingAnalytics.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'housing_analytics.settings')
>>>>>>> origin/Joel-Test-Env
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
<<<<<<< HEAD
            "Couldn't import HousingAnalytics. Are you sure it's installed and "
=======
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
