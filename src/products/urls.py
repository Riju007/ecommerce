from django.urls import path

from products.views import (
	ProductListView, product_list_view, ProductDetailView, product_detai_view
)

app_name = 'products'

urlpatterns = [
	path('list-cbv/', ProductListView.as_view(), name='product_list_cbv'),
	path('list-fbv/', product_list_view, name='product_list_fbv'),
	path('detail-cbv/<int:pk>/', ProductDetailView.as_view(), name='product_detail_cbv'),
	path('detail-fbv/<int:pk>/', product_detai_view, name='product_detail_fbv'),
]
