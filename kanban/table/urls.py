from django.urls import path

from . import views

urlpatterns = [
    # ex: /table
    path('', views.index, name='index'),
    # ex: /table/3
    path('<int:table_id>/', views.view_table, name='view_table')
]
