from rest_framework import routers
from .views import QuestionTypeViewSet, QuestionViewSet

router = routers.SimpleRouter()
router.register(r'question_type', QuestionTypeViewSet)
router.register(r'question', QuestionViewSet)

urlpatterns = router.urls
