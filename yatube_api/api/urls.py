from django.urls import include, path
from rest_framework import routers

from api.views import (CommentsViewSet,
                       FollowViewSet,
                       GroupsViewSet,
                       PostsViewsSet)

v1_router = routers.DefaultRouter()
v1_router.register(
    'posts',
    PostsViewsSet,
    basename='posts'
)
v1_router.register(
    'groups',
    GroupsViewSet,
    basename='groups'
)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
v1_router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
