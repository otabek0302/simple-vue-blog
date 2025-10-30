from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return JsonResponse({"message": "Welcome to Blog API"})

urlpatterns = [
    path('', home),
    path("admin/", admin.site.urls),
    path("api/v1/", include("blog.urls")),
    
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
