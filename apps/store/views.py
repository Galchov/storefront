from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api_view()
def product_list(request: Request) -> Response:
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def product_detail(request: Request, pk: int) -> Response:
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
