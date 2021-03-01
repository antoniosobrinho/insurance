from rest_framework import viewsets
from .serializers import (
                            QuestionTypeSerializer,
                            QuestionSerializer,
                            InsuredSerializer
                        )
from .models import (
                        QuestionType,
                        Question,
                        Insured
                    )
# Create your views here.

class QuestionTypeViewSet(viewsets.ModelViewSet):

    serializer_class = QuestionTypeSerializer
    queryset = QuestionType.objects.all()

class QuestionViewSet(viewsets.ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class InsuredViewSet(viewsets.ModelViewSet):

    serializer_class = InsuredSerializer
    queryset = Insured.objects.all()
