from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import permissions
from rest_framework import status
from base.models import *
from .serializers import *

class Clientes(APIView):
    def get(self, request, cliente_id):
        cliente = Cliente.objects.filter(id=cliente_id)
        serializer = ClienteSerializer(cliente, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    

class Cuentas(APIView):
    def get(self, request, cliente_id):
        cuenta = Cuenta.objects.filter(customer_id=cliente_id).order_by('id')
        serializer = CuentaSerializer(cuenta, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    

class Prestamos(APIView):
    def get(self, request, cliente_id):
        prestamo = Prestamo.objects.filter(customer_id=cliente_id).order_by('id')
        serializer = PrestamoSerializer(prestamo, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)                    

class PrestamosSucursal(APIView):
    def get(self, request, branch_id):
        prestamos = []
        clientes = Cliente.objects.filter(branch_id = branch_id).order_by('id')
        for cliente in clientes:
            prestamos += Prestamo.objects.filter(customer_id = cliente)
        serializer = PrestamoSerializer(prestamos, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)                    

class Tarjetas(APIView):
    def get(self, request, cliente_id):
        tarjeta = Tarjeta.objects.filter(customer_id=cliente_id).order_by('id')
        serializer = TarjetaSerializer(tarjeta, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    

class Sucursales(APIView):
    def get(self, request):
        sucursales = Branch.objects.all().order_by('id')
        serializer = SucursalSerializer(sucursales, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)                    
