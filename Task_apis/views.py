from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


@api_view(['POST'])
def addUser(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'customerId': serializer.data['customerId']})
    return Response({'error': "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addPurchase(request):
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'purchaseOrderId': serializer.data['purchaseOrderId']})
    return Response({'error': "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addShipping(request):
    serializer = ShippingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'shippingId': serializer.data['shippingId']})
    return Response({'error': "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cityCustomers(request, city):
    customers = UsersSerializer(Users.objects.filter(shipping__city=city).distinct(), many=True).data
    return Response({'data': customers})


@api_view(['GET'])
def getCustomers(request, shipping=False):
    data = []
    customers = UsersSerializer(Users.objects.all(), many=True).data
    for customer in customers:
        purchases = OrdersSerializer(Orders.objects.filter(customerId=customer['customerId']), many=True).data
        if shipping:
            customer['purchaseOrder'] = []
            for purchase in purchases:
                shipments = ShippingSerializer(Shipping.objects.filter(purchaseOrderId=purchase['purchaseOrderId']), many=True).data
                purchase['shipmentDetail'] = shipments
                customer['purchaseOrder'].append(purchase)
        else:
            customer['purchaseOrder'] = purchases
        data.append(customer)
    return Response({'data': data})

