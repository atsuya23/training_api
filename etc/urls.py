from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import DayEtcViewSet, GoalViewSet, MemoViewSet

router = routers.DefaultRouter()
router.register('day-etc', DayEtcViewSet, basename='day-etc')
router.register('goal', GoalViewSet, basename='goal')
router.register('memo', MemoViewSet, basename='memo')

urlpatterns = [
    path('', include(router.urls))
]