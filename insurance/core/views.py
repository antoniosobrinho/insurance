from rest_framework import viewsets
from .serializers import QuestionTypeSerializer
from .models import QuestionType
# Create your views here.

class QuestionTypeViewSet(viewsets.ModelViewSet):

    serializer_class = QuestionTypeSerializer
    queryset = QuestionType.objects.all()

