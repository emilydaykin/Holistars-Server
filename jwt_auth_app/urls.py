from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('credentials/', CredentialsView.as_view()),
    path('', UserList.as_view()),
    path('<int:pk>', UserRetriveUpdateDelete.as_view()),
]
