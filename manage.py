#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

        raise

    # This allows easy placement of apps within the interior
    # deepopinion_backend_challenge directory.
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

    # current_path = Path(__file__).parent.resolve()
    # sys.path.append(str(current_path / "deepopinion_backend_challenge/" "deepopinion_backend_challenge"))

    current_path = (os.path.join(BASE_DIR, "deepopinion_backend_challenge/", "deepopinion_backend_challenge"))
    FIXTURE_DIR_PATH = (os.path.join(ROOT_DIR, "backend-coding-challenge/", "fixtures"))


    sys.path.append(str(current_path))



    execute_from_command_line(sys.argv)
