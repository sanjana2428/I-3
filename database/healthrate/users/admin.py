from django.contrib import admin
from .models import CustomUser, Review, ProviderResponse, InappropriateReview

admin.site.register(CustomUser)
admin.site.register(Review)
admin.site.register(ProviderResponse)
admin.site.register(InappropriateReview)
