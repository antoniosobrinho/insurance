from rest_framework import serializers
from .models import QuestionType, Question

class QuestionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionType
        fields = ['id', 'name']

    def to_representation(self, instance):

        representation = super().to_representation(instance)

        representation.update({
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

    def to_representation(self, instance):

        representation = super().to_representation(instance)

        representation.update({
            'question_type_name': instance.question_type.name
        })

        return representation
