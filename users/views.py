from rest_framework.authtoken.views import ObtainAuthToken
from users.serializers import MyAuthTokenSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.views import LoginView
from rest_framework.response import Response


# i want to  inherit from ObtainAuthToken class and customize the serializer
class AdminLoginView(ObtainAuthToken):
    serializer_class = MyAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class GenerateTokenView(LoginView):
    def form_valid(self, form):
        # Generate AuthToken if it doesn't exist
        user = form.get_user()
        if not Token.objects.filter(user=user).exists():
            Token.objects.create(user=user)

        return super().form_valid(form)
