from django.urls import path

from users.views import AdminLoginView, GenerateTokenView

urlpatterns = [
    path('generate_token/', GenerateTokenView.as_view(), name='generate'),
    path('login/', AdminLoginView.as_view(), name='loging'),
]