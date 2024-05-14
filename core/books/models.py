from django.db import models
from isbn_field import ISBNField

# Create your models here.


#class Author

class GenderBooks(models.Model):
    name_gender = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name='Gender Book')

    def __str__(self):
        return self.name_gender

    class Meta:
        verbose_name = 'Gender Book'
        verbose_name_plural = 'Genders Book'
        ordering = ['id']
    



class Book(models.Model):
    title = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name='Title Book')
    gender_name = models.ForeignKey(GenderBooks, on_delete=models.PROTECT, verbose_name='Gender Name')
    author = models.CharField(max_length=150, null=False, blank=False, verbose_name='Author')
    isbn = ISBNField("ISBN")
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    review = models.TextField(max_length=20000)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Book'
        ordering = ['id']