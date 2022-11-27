from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PrimeNumber
from . import algorithm
# Create your views here.

# getting prime number between two number view 
class PrimeGenerateView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        min = request.data.get('min',1)
        max = request.data.get('max',1)
        algo = request.data.get('method')
        if algo=='optimised':
            lst,execution_time = algorithm.prime_optimised(min,max)
            PrimeNumber.objects.create(user=request.user, range=[min,max], time_elapsed=execution_time,
                prime_numbers=lst,algorithm='Optimised')
        else:
            lst,execution_time = algorithm.prime_algo_1(min,max)
            PrimeNumber.objects.create(user=request.user, range=[min,max], time_elapsed=execution_time,
                prime_numbers=lst)
        return Response({'primeNumber':lst})
             
