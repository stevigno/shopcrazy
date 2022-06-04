from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecrazy.urls')),
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('carts/', include('carts.urls')),

    # orders
    path('orders/', include('orders.urls')),

    # customadmin
    path('customadmin/', include('customadmin.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)