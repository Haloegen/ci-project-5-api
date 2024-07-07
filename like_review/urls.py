from django.urls import path
from like_review import views

urlpatterns = [
    path('likereview/', views.LikeReviewList.as_view()),
    path('likereview/<int:pk>/', views.LikeReviewDetail.as_view()),
]