from .models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserRegestrationSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# regiter user
class Signup(CreateAPIView):
    serializer_class = UserRegestrationSerializer

# login user
class Login(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

# logout and blacklist token
class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        token = RefreshToken(request.data.get('refresh_token'))
        token.blacklist()
        return Response({'message':"You are logout"})