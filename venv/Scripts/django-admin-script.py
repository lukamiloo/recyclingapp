#!C:\Users\lmilo\PycharmProjects\recyclingapp\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'kivy-django==1.9.1','console_scripts','django-admin'
__requires__ = 'kivy-django==1.9.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('kivy-django==1.9.1', 'console_scripts', 'django-admin')()
    )
