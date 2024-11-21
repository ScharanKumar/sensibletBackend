from django.urls import path
from .views import UserCreateView, LoginView
# , LogoutView

urlpatterns = [
    path('api/users/', UserCreateView.as_view(), name='user-create'),
    path('api/login/', LoginView.as_view(), name='login'),
    # path('api/logout/', LogoutView.as_view(), name='logout'),
]
