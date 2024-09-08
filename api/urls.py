from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ResturantViewSet, MenuViewSet, 
    ItemViewSet, CategoryViewSet, 
    ModifierViewSet, OrderViewSet, 
    OrderItemViewSet
)

router = DefaultRouter()
router.register('restaurants', ResturantViewSet)
router.register('categories', CategoryViewSet)
router.register('menus', MenuViewSet)
router.register('items', ItemViewSet)
router.register('modifiers', ModifierViewSet)
router.register('orders', OrderViewSet)
router.register('order-items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
