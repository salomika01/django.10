from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Car, Animal
from .serializers import CarSerializer, AnimalSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(detail=True, methods=['delete'])
    def delete_car(self, request, pk=None):
        car = self.get_object()
        car.delete()
        return Response(status=204)


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    @action(detail=True, methods=['delete'])
    def delete_animal(self, request, pk=None):
        animal = self.get_object()
        animal.delete()
        return Response(status=204)
