from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path("account/", include("account.urls")),
    path("", include("website.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls")),
]


handler404 = "core.error_views.error_404"  # page_not_found


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
