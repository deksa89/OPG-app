from rest_framework import views, response, permissions, exceptions
from .serializers import FarmSerializer
from .services import create_user, user_email_selector, create_token
from .authentication import CustomUserAuthentication

class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = FarmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        serializer.instance = create_user(user_dc=data)
        
        
        return response.Response(data=serializer.data)

# we want to authenticate a user and store user's session inside a cookie
# so that way validation and authentification are done in backend 
class LoginAPI(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        
        user = user_email_selector(email=email)
        
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed('Invalid Password')
        
        token = create_token(user_id=user.id)
        
        resp = response.Response()
        resp.set_cookie(key="jwt", value=token, httponly=True)
        
        return resp


# this endpoint will be used if user is authenticated
class UserApi(views.APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        user = request.user
        
        serializer = FarmSerializer(user)
        
        return response.Response(serializer.data)
    

class LogoutAPI(views.APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message":"vidimo se uskoro!"}
        
        return resp