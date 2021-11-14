from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, RegisterView, ProfileView, AddCommentView, GetCommentView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

app_name = 'blog_api'


urlpatterns = [
    path("", include(router.urls), name='posts_api'),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path("comments/<slug:post_slug>/", GetCommentView.as_view()),
    path("addcomment/", AddCommentView.as_view()),
]