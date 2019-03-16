from rent import views

from django.urls import path


urlpatterns = [
    path('', views.ServeReactApp.as_view(), name='homepage')
]
