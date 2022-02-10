from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import DayViewSet, DayListView, DayRetrieveView, \
    TrainingViewSet, TrainingRetrieveView, TrainingListView, \
    MeasurementViewSet, MeasurementRetrieveView, MeasurementListView, CreateUserView

router = routers.DefaultRouter()
router.register('day', DayViewSet, basename='day')
router.register('training', TrainingViewSet, basename='training')
router.register('measurement', MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('list-day/', DayListView.as_view(), name='list-day'),
    path('detail-day/<str:pk>/', DayRetrieveView.as_view(), name='detail-day'),
    path('list-trainig/', TrainingListView.as_view(), name='list-training'),
    path('detail-training/<str:pk>/', TrainingRetrieveView.as_view(), name='detail-training'),
    path('list-measurement/', MeasurementListView.as_view(), name='list-measurement'),
    path('detail-measurement/<str:pk>/', MeasurementRetrieveView.as_view(), name='detail-measurement'),

    path('register/', CreateUserView.as_view(), name='register'),
    path('auth', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
