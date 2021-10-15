from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

#Auto URL Generator for multiple different tags
router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
