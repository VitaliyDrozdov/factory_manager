from directory.views import EquipmentViewSet, FactoryViewSet, SectionViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "directory"

router_v1 = DefaultRouter()

router_v1.register(r"factories", FactoryViewSet, basename="factories")
router_v1.register(r"sections", SectionViewSet, basename="sections")
router_v1.register(r"equipment", EquipmentViewSet, basename="equipment")

urlpatterns = [
    path("", include(router_v1.urls)),
]
