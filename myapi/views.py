from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HumanSerializer
from .models import Human
# Create your views here.
class HumanViewSet(viewsets.ModelViewSet):
    queryset = Human.objects.all().order_by('fname')
    serializer_class = HumanSerializer