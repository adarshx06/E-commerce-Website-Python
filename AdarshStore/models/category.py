from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    # description = models.CharField(max_length=255, default='')
    # image = models.ImageField(upload_to='uploads/categories/')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name