from django.urls import path
from .views import TransactionListView, UserPurchasesView, ProductPurchasesView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Bog Api",
        default_version='v1',
        description="Bog API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('user-purchases/<int:user_id>/', UserPurchasesView.as_view(), name='user-purchases'),
    path('product-purchases/<int:item_code>/', ProductPurchasesView.as_view(), name='product-purchases'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
