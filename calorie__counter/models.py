from django.db import models
from django.core.validators import MinValueValidator


class Profile(models.Model):
    CHOOSE_GENDER = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    age = models.SmallIntegerField(blank=True, null=True)
    gender = models.CharField(
        choices=CHOOSE_GENDER, max_length=10, null=True, blank=True
    )
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    bmr = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        
        self.full_clean(exclude=['bmr'])
        
        gender, age, weight, height = self.gender, self.age, self.weight, self.height
        
        if gender and all(v is not None and v > 0 for v in [age, weight, height]):
            if gender.lower() == 'male':
                bmr_val = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age) # type: ignore
            else:
                bmr_val = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age) # type: ignore
                
            self.bmr = round(bmr_val, 2)
        else:
            self.bmr = 0
            
        super().save(*args, **kwargs)


class Calorie(models.Model):
    user = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE
    )
    item_name = models.CharField(max_length=200, null=True, blank=True)
    calorie_consumed = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.item_name}"
