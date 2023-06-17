from django.urls import path
from .views import home, about, portfolio, PostListView, PostDetailView

urlpatterns = [
    path("", home),
    path("about/", about),
    path("portfolio/", portfolio),
    path("blog/", PostListView.as_view()),
    path('blog/<int:pk>/', PostDetailView.as_view())
]
