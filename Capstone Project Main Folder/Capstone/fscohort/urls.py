from django.urls import path, include

from .views import (
    PostViews,
    PostView_View,
    LikesView,
    CommentView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('likes', LikesView)
router.register('post', PostViews)
router.register('comment', CommentView)
router.register('views', PostView_View)

urlpatterns = [

] + router.urls
