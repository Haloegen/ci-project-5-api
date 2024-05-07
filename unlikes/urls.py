from django.urls import path
from likes import views


urlpatterns = [
    path('unlikes/', views.LikeList.as_view()),
    path('unlikes/<int:pk>/', views.LikeDetail.as_view()),
]