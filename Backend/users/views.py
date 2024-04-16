from django.shortcuts import render
from rest_framework import generics,status,views,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from .models import HealthcareWorker
import jwt, datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer,LoginSerializer,LogoutSerializer


# Create your views here.

class HealthcareWorkerView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms= 'HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        
        user = HealthcareWorker.objects.get(payload['id'])
        serializer = RegisterSerializer(user)


        return Response(serializer.data)
    


class RegisterView (APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterSerializer(data = request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# class HealthcareWorkerLoginView(APIView):
#     def post(self, request):
#         user_id = request.data['user_id']
#         password = request.data['password']

#         user = HealthcareWorker.objects.filter(user_id =user_id).first()

#         if user is None:
#             raise AuthenticationFailed('User not found')
        
#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorect password')
        
#         payload = {
#             'id': user.id,
#             'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat':datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secrete', algorithm='HS256').decode('utf-B')
        
#         response = Response()

#         response.set_cookie(key='jwt',value=token,httponly=True)

#         response.data = {
#             "jwt": token
#             }
        
#         return response
    
#         #return Response({"jwt": "token"})
        
#         #return Response({"message": "User Logedin successfully."}, status=status.HTTP_201_CREATED)


# class HealthcareWorkerLogoutView(APIView):
#     def post(self, request):
#         response =Response()
#         response.delete_cookie('jwt')
#         response.data= {
#              "message":"success"
#         }
#         return response

