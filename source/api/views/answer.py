from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Answer
from api.serializers import AnswerSerializer, AnswerDetailSerializer


class AnswerViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Answer.objects.all()
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        question = get_object_or_404(Answer, pk=pk)
        serializer = AnswerSerializer(question)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        answer = get_object_or_404(Answer, pk=pk)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            answer_serializer = serializer.save()
            return Response(AnswerSerializer(answer_serializer).data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            survey = serializer.save()
            return Response(AnswerSerializer(survey).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        survey = get_object_or_404(Answer, pk=pk)
        survey.delete()
        return Response("Answer deleted", status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]


class GetAswerByUserId(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        queryset = Answer.objects.filter(user=pk)
        survey_serializer = AnswerDetailSerializer(queryset, many=True)
        return Response(survey_serializer.data)
