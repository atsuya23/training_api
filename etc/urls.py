from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import GoalViewSet, MemoViewSet, MeasurementViewSet, MeasurementRetrieveView, MeasurementListView

router = routers.DefaultRouter()
router.register('goal', GoalViewSet, basename='goal')
router.register('memo', MemoViewSet, basename='memo')
router.register('measurement', MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('', include(router.urls)),
    path('list-measurement/', MeasurementListView.as_view(), name='list-measurement'),
    path('detail-measurement/<str:pk>/', MeasurementRetrieveView.as_view(), name='detail-measurement'),

]