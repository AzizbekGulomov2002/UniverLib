from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.app.views import *
from apps.users.views import *
from apps.app.views import *
from .views import *

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('director', DirectorViewset, basename='director')
router.register('user', UserViewset, basename='user')

# path('trade/<int:trade_id>/', TradeAPIView.as_view(), name='trade-api'),

router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('trade',TradeViewSet)
router.register('payments',PaymentsViewSet)

router.register('alltrade', AllTradeViewSet, basename='alltrade')

urlpatterns = [
    path('', include(router.urls)),
    path('auth-token/', obtain_auth_token, name='api_token_auth'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)