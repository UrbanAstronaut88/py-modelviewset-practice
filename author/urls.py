from django.urls import path, include
from rest_framework.routers import SimpleRouter
from author.views import AuthorViewSet


app_name = "author"
router = SimpleRouter()
router.register(r"authors", AuthorViewSet, basename="author")


urlpatterns = [
    path("", include(router.urls)),
]
