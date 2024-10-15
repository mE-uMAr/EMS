from django.urls import path , include
from . import views
urlpatterns = [
    path('' , views.home , name="home"),
    path('payments/' , views.payments , name='payments'),
    path('tasks/' , views.tasks , name='tasks'),
    path('profile/' , views.profile , name="profile"),
    path('login/' , views.handlelogin , name='login'),
    path('logout/' ,views.handlelogout , name='logout'),
    path('signup/', views.register , name='signup'),
]