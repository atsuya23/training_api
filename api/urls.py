from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TrainingViewSet, TrainingRetrieveView, TrainingListView, \
    MeasurementViewSet, MeasurementRetrieveView, MeasurementListView, CreateUserView,\
    BenchAllViewSet, BenchNormalViewSet, BenchLowWeightViewSet, BenchHighWeightViewSet

router = routers.DefaultRouter()
router.register('training', TrainingViewSet, basename='training')
router.register('measurement', MeasurementViewSet, basename='measurement')
router.register('bench-all', BenchAllViewSet, basename='bench-all')
router.register('bench-normal', BenchNormalViewSet, basename='bench-normal')
router.register('bench-high', BenchHighWeightViewSet, basename='bench-high')
router.register('bench-low', BenchLowWeightViewSet, basename='bench-low')


urlpatterns = [
    path('list-trainig/', TrainingListView.as_view(), name='list-training'),
    path('detail-training/<str:pk>/', TrainingRetrieveView.as_view(), name='detail-training'),
    path('list-measurement/', MeasurementListView.as_view(), name='list-measurement'),
    path('detail-measurement/<str:pk>/', MeasurementRetrieveView.as_view(), name='detail-measurement'),

    path('register/', CreateUserView.as_view(), name='register'),
    path('auth', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
