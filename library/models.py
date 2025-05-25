from django.db import models

class Book(models.Model):
    id = models.IntegerField(primary_key=id)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    category = models.CharField(max_length=100)
    available_copies = models.PositiveBigIntegerField(default=1)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title

