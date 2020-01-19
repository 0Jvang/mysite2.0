from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('post/', PostList.as_view()),
    path('post/<int:pk>/', PostRetrieve.as_view()),
    path('category/', CategoryList.as_view()),
    path('tag/', TagList.as_view()),
    # path('archive/', ArchiveList.as_view()),
]
