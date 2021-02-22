from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Items', views.ItemViewSet)
router.register(r'Fields', views.FieldViewSet)
router.register(r'Sheets', views.SheetViewSet)
router.register(r'Styles', views.StyleViewSheet)

urlpatterns = [
    path('', include(router.urls)),
    path('request/kanban-structure/<int:table_id>', views.kanban_structure, name='kanban-structure'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]