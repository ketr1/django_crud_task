from django.urls import path
from .views import AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', AuthorListCreateAPIView.as_view(), name='author_list_create'),
    path('<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author_detail'),
]
