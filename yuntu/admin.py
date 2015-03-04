from django.contrib import admin
from .models import Index, FeatureMatrix, SubscribedEmail


admin.site.register(Index)
admin.site.register(FeatureMatrix)
admin.site.register(SubscribedEmail)
