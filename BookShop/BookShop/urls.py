from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls', namespace='order')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('parce', include('parcer.urls')),
    path('', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
