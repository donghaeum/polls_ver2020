from .models import *
from rest_framework import serializers
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
class QuestionSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'
