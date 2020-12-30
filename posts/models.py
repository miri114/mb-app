from django.db import models

# My code here


class Post(models.Model):                 # new database model called Post
    text = models.TextField()             # field 'text' and type of content TextField()

    def __str__(self):
        return self.text[:50]
