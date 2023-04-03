from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('article', ArticleGenericViewSet, basename='article')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    path('function/article/', article_list),
    path('function/detail/<int:pk>/', article_detail),

    path('article/', ArticleAPIVIEW.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),

    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),

    path('api/v2/', ApiGenericView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v2/<int:pk>', ApiGenericView.as_view({'get': 'retrieve', 'put': 'update', 'delete': "destroy"}))

]
