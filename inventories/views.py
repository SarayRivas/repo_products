
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id_product')
    serializer_class = ProductSerializer

def _no_store(response):
    response['Cache-Control'] = 'no-store'
    return response

@require_http_methods(["GET", "HEAD"])
def health_check(request):

    res = JsonResponse({"status": "ok"})
    return _no_store(res)
