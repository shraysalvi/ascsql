from django.urls import path, include
from rest_framework import routers
from .views import OrganizationViewSet, CustomUserModelViewSet, loging, ProductViewSet, OrgUserModelViewSet, SuperUserModelViewSet, product_upload, RequestUserViewSet, TestSubmissionViewSet
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'organization', OrganizationViewSet)
router.register(r'user', CustomUserModelViewSet)
router.register(r'superadminlist',
                SuperUserModelViewSet,
                basename='superadminlist')
router.register(r'orgadminlist', OrgUserModelViewSet, basename='orgadminlist')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'requestusers', RequestUserViewSet, basename='requestusers')
router.register(r'testsubmission', TestSubmissionViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path("login/", loging),
  path("productup/", product_upload),
]
