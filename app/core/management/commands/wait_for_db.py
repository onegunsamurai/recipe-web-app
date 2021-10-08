import time

from django.db import connections
#If you are using more than one database you can use django.db.connections
#to obtain the connection (and cursor) for a specific database.
#django.db.connections is a dictionary-like object that allows you to
#retrieve a specific connection using its alias:

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django Command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['test']
            except OperationalError:
                self.stdout.write('Db is unavailable waiting for 1 second')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
