"""
Django command to wait for database to be avaialble. 
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from typing import Any, Optional
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write("waiting for databse")
        db_up = False
        while db_up is False:
            try:
                self.check(databases = ['default'])
                db_up = True
            except(Psycopg2OpError,OperationalError):
                self.stdout.write("databse is unable, waiting 1 second")
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database Avaialble'))
        

    