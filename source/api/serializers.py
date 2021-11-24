from rest_framework import serializers
from api.models import Survey, Question, Option, Answer


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class SurveySerializerPATCH(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['title', 'describe', 'end_date']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(AnswerDetailSerializer, self).to_representation(instance)
        representation['question'] = instance.question.text
        representation['option'] = instance.option.text
        representation['survey'] = instance.survey.title
        return representation
