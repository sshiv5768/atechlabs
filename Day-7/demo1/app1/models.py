from django.db import models

# Create your models here.
class Books(models.Model):
    auth_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254)
    book_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.auth_name + " " + self.book_name

