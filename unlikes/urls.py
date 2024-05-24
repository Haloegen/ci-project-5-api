from django.urls import path
from unlikes import views


urlpatterns = [
    path('unlikes/', views.UnlikeList.as_view()),
    path('unlikes/<int:pk>/', views.UnlikeDetail.as_view()),
]