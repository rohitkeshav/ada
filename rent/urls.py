from rent import views

from django.urls import path


urlpatterns = [
    path('', views.ServeReactApp.as_view(), name='homepage'),
    path('login/', views.sign_in, name='sign_in'),
    path('logout/', views.sign_out, name='sign_out'),
    path('sign_up/', views.sign_up, name='sign_up')
]
