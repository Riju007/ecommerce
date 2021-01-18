from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from products.models import Product


class ProductListView(ListView):
	"""Display all the products."""

	queryset = Product.objects.all()
	template_name = 'products/list.html'

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context


def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, 'products/list.html', context=context)


class ProductDetailView(DetailView):
	"""Display a product with details."""
	# queryset = Product.objects.all()
	context_object_name = 'product'
	template_name = 'products/detail.html'

	def get_queryset(self):
		product = Product.objects.all()
		return product

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		context['extra_context'] = "This is an extra context."
		return context


def product_detai_view(request, pk=None, *args, **kwargs):
	# product = Product.objects.get(pk=pk)
	product = get_object_or_404(Product, pk=pk)
	context = {
		'product': product,
		'extra_context': "This is an extra context."
	}
	return render(request, 'products/detail.html', context=context)
