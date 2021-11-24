from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from api.models import Question
from api.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question_serializer = serializer.save()
            return Response(QuestionSerializer(question_serializer).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question_serializer = serializer.save()
            return Response(QuestionSerializer(question_serializer).data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        survey = get_object_or_404(Question, pk=pk)
        survey.delete()
        return Response("Question deleted", status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]
