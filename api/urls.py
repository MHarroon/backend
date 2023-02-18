from django.urls import path
from .views import  *

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('ApplicationForm',ApplicationView.as_view()),
    path('ApplicationForm/<int:pk>/',ApplicationView.as_view()),
    # path('CustomerAccount',CustAccountView.as_view()),
    # path('CustomerAccount/<int:pk>/',CustAccountView.as_view()),
]
