from rest_framework import serializers
from .models import QuestionType, Question

class QuestionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionType

    def to_representation(self, instance):

        representation = dict()
        representation.update( {
           'id': instance.id,
           'name': instance.name,
           'questions': list()
        })

        for question in instance.question_set.all():

            representation['questions'].append(
               {
                   'id': question.id,
                   'question': question.question
               }
           )

        return representation

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'
