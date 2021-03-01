from rest_framework import routers
from .views import QuestionTypeViewSet, QuestionViewSet, InsuredViewSet

router = routers.SimpleRouter()
router.register(r'question_type', QuestionTypeViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'insured', InsuredViewSet)

urlpatterns = router.urls
