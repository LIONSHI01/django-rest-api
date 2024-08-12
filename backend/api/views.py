from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from products.models import Product
from products.serializers import ProductSerializer


# Decorator limit http methods
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if (serializer.is_valid()):
        return Response(serializer.data)

# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by('?').first()
#     data = {}
#     if (instance):
#         data = ProductSerializer(instance).data
    # return Response(data)
