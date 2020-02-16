from django.urls import path
from . import views


app_name = 'index'

urlpatterns = [
    path('main/', views.HomeListView.as_view(), name='main'),
    path('liveRoom/', views.liveRoomView.as_view(), name='liveRoom'),
    path('zhubo/', views.anchor.as_view(), name='zhubo'),
    




]
