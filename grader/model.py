import os

from peewee import Model, CharField, FloatField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///grade_database.db'))

class Grade(Model):
    
    student = CharField(max_length=255 )
    assignment = CharField(max_length=255)
    grade = CharField(max_length=10)

    class Meta:
        database = db
