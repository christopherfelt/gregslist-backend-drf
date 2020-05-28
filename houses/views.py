from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import House
from .serializers import HouseSerializer


class HouseList(APIView):
    def get(self, request):
        house = House.objects.all()
        serializer = HouseSerializer(house, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class HouseDetail(APIView):
    def get_object(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        house = self.get_object(pk=pk)
        serializer = HouseSerializer(house)
        return Response(serializer.data)

    def put(self, request, pk):
        house = self.get_object(pk)
        serializer = HouseSerializer(house, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        house = self.get_object(pk=pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)