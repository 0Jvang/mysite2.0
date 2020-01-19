from collections import defaultdict

from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from.serializers import *


class PostList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostRetrieve(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CategoryList(APIView):
    def get(self, request, *args, **kwargs):
        category_freq = defaultdict(int)
        for post in list(Post.objects.all()):
            category_freq[post.category.name] += 1

        category_entries = CategorySerializer(Category.objects.all(), many=True).data
        for category in category_entries:
            category['count'] = category_freq.get(category['name'], 0)

        return Response(category_entries)


class TagList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class ArchiveList(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)