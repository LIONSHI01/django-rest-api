from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    Combine Get List View and Create Item View
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_delete_view = ProductDeleteAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     """
#     Not use
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# product_detail_view = ProductDetailAPIView.as_view()

# For Demo Use Only(Not Recommended)
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method
#     if method == 'GET':
#         # Detail view
#         if pk is not None:
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)

#         # List view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == 'POST':
#         # Create view
#         serializer = ProductSerializer(data=request.data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)
#         return Response(serializer.data)
#     return Response({"invalid": "not good data"}, status=400)
