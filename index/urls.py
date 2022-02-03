from django.urls import path, include
import index.views as views

urlpatterns = [
    path('', views.getIndexPage, name='index_page'),
    path('maintenance', views.getMaintenancePage, name='maintenance_page')
]