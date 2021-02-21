from rest_framework import routers
from .views import QuestionTypeViewSet

router = routers.SimpleRouter()
router.register(r'question_type', QuestionTypeViewSet)

urlpatterns = router.urls
