from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model (Extending Django's default User model)
class CustomUser(AbstractUser):
    user_type_choices = [
        ('patient', 'Patient'),
        ('provider', 'Healthcare Provider'),
    ]
    user_type = models.CharField(max_length=20, choices=user_type_choices)

# Review Model
class Review(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="patient_reviews")
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="provider_reviews")
    rating = models.PositiveSmallIntegerField()  # Rating between 1 and 5
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Provider Response Model
class ProviderResponse(models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name="response")
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Inappropriate Review Model
class InappropriateReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="flags")
    flagged_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reason = models.TextField(blank=True, null=True)
    flagged_at = models.DateTimeField(auto_now_add=True)