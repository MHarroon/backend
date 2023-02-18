from django.shortcuts import render
from .serializers import *
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import *
import jwt, datetime
from rest_framework.parsers import JSONParser
from rest_framework import status
# from .serializers import * 
# Create your views here.
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response




# view of ApplicationForum 
    # Here i created the customer
class ApplicationView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = ApplicationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   
    # geting meaning reading data 
    def get_C_ApplicatioInfo(self, pk):
        try:
            customer =ApplicationModel.objects.get(applicationID=pk)
            return customer
        except ApplicationSerializer.ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
             data = self.get_C_ApplicatioInfo(pk)
             serializer = ApplicationSerializer(data)
        else:
              data = ApplicationModel.objects.all()
              serializer = ApplicationSerializer(data, many=True)
        return Response(serializer.data)
    
    # for updation of date 
    def put(self, request, pk=None):
           customer_to_update = ApplicationModel.objects.get(applicationID=pk)
           serializer = ApplicationSerializer(instance=customer_to_update, data=request.data, partial=True)
           if serializer.is_valid():
               serializer.save()
               return JsonResponse("Application Data updated Successfully", safe=False)
           return JsonResponse("Application Data Failed To Update CustomerInfo")
       
    def delete(self,request, pk):
          customer_to_delete = ApplicationModel.objects.get(applicationID=pk)
          customer_to_delete.delete()
          return JsonResponse("Application Data Deleted Successfully", safe=False) 



# # Customer Account View 
# class CustAccountView(APIView):
       
#     def post(self, request):
#         data = request.data
#         serializer = CustAccountSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Customer Account Data Added Successfully", safe=False)
#         return JsonResponse("Failed to Add Customer Account ", safe=False)
   
   
#     # geting meaning reading data 
#     def get_C_Account(self, pk):
#         try:
#             customer =CustAccountSerializer.objects.get(CAccountID=pk)
#             return customer
#         except CustAccountSerializer.DoesNotExist:
#             raise Http404

#     def get(self, request, pk=None):
#         if pk:
#              data = self.get_C_Account(pk)
#              serializer = CustAccountSerializer(data)
#         else:
#               data = CustAccountSerializer.objects.all()
#               serializer = CustAccountSerializer(data, many=True)
#         return Response(serializer.data)
    
#     # for updation of date 
#     def put(self, request, pk=None):
#            customer_to_update = CustAccountSerializer.objects.get(CAccountID=pk)
#            serializer = CustAccountSerializer(instance=customer_to_update, data=request.data, partial=True)
#            if serializer.is_valid():
#                serializer.save()
#                return JsonResponse("Customer Account Data updated Successfully", safe=False)
#            return JsonResponse("Customer Account Data Failed To Update CustomerInfo")
       
#     def delete(self,request, pk):
#           customer_to_delete = CustAccountSerializer.objects.get(CAccountID=pk)
#           customer_to_delete.delete()
#           return JsonResponse("Customer Account Data Deleted Successfully", safe=False) 


