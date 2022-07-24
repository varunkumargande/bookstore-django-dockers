from rest_framework.routers import DefaultRouter
from .views import BookViewset

router = DefaultRouter()
router.register(r"book", BookViewset),

urlpatterns = router.urls
