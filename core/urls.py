from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategoryView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='marketplace-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('search/', views.search, name='search-posts'),
    path('about/', views.about, name='marketplace-about'),
    
]

