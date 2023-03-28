from django.urls import path
from base.views import users_veiws as views

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register/', views.registerUser, name='register'),

    path('profile/', views.getUserProfile, name='user-profile'),
    path('', views.getUsers, name='users'),

]
