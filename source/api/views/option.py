from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from api.models import Option
from api.serializers import OptionSerializer


class OptionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request):
        queryset = Option.objects.all()
        serializer = OptionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        question = get_object_or_404(Option, pk=pk)
        serializer = OptionSerializer(question)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        option = get_object_or_404(Option, pk=pk)
        serializer = OptionSerializer(option, data=request.data, partial=True)
        if serializer.is_valid():
            option_serializer = serializer.save()
            return Response(OptionSerializer(option_serializer).data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            option = serializer.save()
            return Response(OptionSerializer(option).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        option = get_object_or_404(Option, pk=pk)
        option.delete()
        return Response("Option deleted", status.HTTP_204_NO_CONTENT)
