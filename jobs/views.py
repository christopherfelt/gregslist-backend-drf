from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Job
from .serializers import JobSerializer


class JobList(APIView):
    def get(self, request, format=None):
        job = Job.objects.all()
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetail(APIView):
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            Http404

    def get(self, request, pk, format=None):
        job = self.get_object(pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        job = self.get_object(pk=pk)
        serializer = JobSerializer(job, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job = self.get_object(pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

