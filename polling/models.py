from django.db import models
'''
*after creating data model, run:
1.  python manage.py makemigrations
2.  python manage.py migrate
3.  **remember to register data model in admin.py


'''
# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length = 128)#will create a single line text field to enter data
    text = models.TextField(blank=True)#will create a multi-line text field to enter data
    score = models.IntegerField(default=0)#will create a single line field to enter an integer

    def __str__(self) -> str:
        return self.title