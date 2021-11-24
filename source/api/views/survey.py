from datetime import date

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Survey
from api.serializers import SurveySerializer, SurveySerializerPATCH


class SurveyViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Survey.objects.all()
        serializer = SurveySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        question = get_object_or_404(Survey, pk=pk)
        serializer = SurveySerializer(question)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        survey = get_object_or_404(Survey, pk=pk)
        serializer = SurveySerializerPATCH(survey, data=request.data, partial=True)
        if serializer.is_valid():
            survey_serializer = serializer.save()
            return Response(SurveySerializer(survey_serializer).data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            survey = serializer.save()
            return Response(SurveySerializer(survey).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        survey = get_object_or_404(Survey, pk=pk)
        survey.delete()
        return Response("Survey deleted", status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]


class GetActiveSurveyView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Survey.objects.filter(end_date__gte=date.today())
        survey_serializer = SurveySerializer(queryset, many=True)
        return Response(survey_serializer.data)
