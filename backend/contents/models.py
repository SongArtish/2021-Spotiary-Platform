from django.db import models
from django.conf import settings

class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='contents')
    # address - province/city/district
    province = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=10, blank=True)
    district = models.CharField(max_length=10, blank=True)
    # location value: x & y
    location_x = models.IntegerField(blank=True)
    location_y = models.IntegerField(blank=True)

    name = models.CharField(max_length=50)
    contents = models.TextField()
    date = models.DateField()

    # category: Travel or Food
    Travel = 'Travel'
    Food = 'Food'
    category_choices = [
        (Travel, 'Travel'),
        (Food, 'Food'),
    ]
    category = models.CharField(
        max_length=10,
        choices=category_choices,
    )

    photo = models.ImageField(blank=True)
    rating = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)