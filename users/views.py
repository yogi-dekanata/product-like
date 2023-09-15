from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserLoginSerializer, UserRegisterSerializer


@api_view(['POST'])
def login(request):
    """
    Authenticate a user and return an access token if successful.
    """
    serializer = UserLoginSerializer(data=request.data)

    if serializer.is_valid():
        user = authenticate(username=request.data['username'], password=request.data['password'])

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    """
    Register a new user.
    """
    serializer = UserRegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
