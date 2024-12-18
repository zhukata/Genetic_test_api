from django.db import models

class Test(models.Model):
    animal_name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    test_date = models.DateField()
    milk_yield = models.FloatField()
    health_status = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.animal_name} ({self.species})"