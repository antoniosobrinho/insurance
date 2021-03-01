from rest_framework import viewsets
from .serializers import QuestionTypeSerializer, QuestionSerializer
from .models import QuestionType, Question
# Create your views here.

class QuestionTypeViewSet(viewsets.ModelViewSet):

    serializer_class = QuestionTypeSerializer
    queryset = QuestionType.objects.all()

class QuestionViewSet(viewsets.ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
