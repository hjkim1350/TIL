from django.urls import path
from .views import StudentsViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register('students', StudentsViewSet)


urlpatterns = router.urls