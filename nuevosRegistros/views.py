from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request

from rest_framework.views import APIView
from .serializerNuevosRegistros import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def materiaPrimaAPIView(request):
    if request.method=='GET':
        materiasPrimasBD=materiaPrima.objects.all()
        materiasPrimasBD_serialilizada=materiaPrimaSerializer(materiasPrimasBD, many=True)
        return Response(materiasPrimasBD_serialilizada.data)
    
    if request.method == 'POST':
        print(request.data)
        entrada_serilizada=materiaPrimaSerializer(data=request.data)
        if entrada_serilizada.is_valid():
            entrada_serilizada.save()
            return Response(entrada_serilizada.data)
        return Response(entrada_serilizada.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def materiaPrima_detailsAPIView(request, pk=None):
    if request.method == 'GET':
        materia_Prima = materiaPrima.objects.filter(materiaPrima_codigo=pk).first()
        materia_Prima_serializer = materiaPrimaSerializer(materia_Prima)
        return Response(materia_Prima_serializer.data)
 #Para modificar/Actualizar
    elif request.method == 'PUT':
        materia_Prima = materiaPrima.objects.filter(materiaPrima_codigo=pk).first()
        materia_Prima_serializer = materiaPrimaSerializer(materia_Prima, data=request.data)
        if materia_Prima_serializer.is_valid():
            materia_Prima_serializer.save()
            return Response(materia_Prima_serializer.data)
        return Response(materia_Prima_serializer.errors)
    # Para eliminar
    elif request.method == 'DELETE':
        materia_Prima = materiaPrima.objects.filter(materiaPrima_codigo=pk).first()
        materia_Prima.delete()
        return Response("Materia prima eliminada")


@api_view(['GET', 'POST'])
def movimientosAPIView(request):
    if request.method=='GET':
        movimietosBD=movimientos.objects.all()
        movimietosBD_serialilizada=movimientosSerializer(movimietosBD, many=True)
        return Response(movimietosBD_serialilizada.data)

    if request.method == 'POST':
        print(request.data)
        movimiento_serilizado=movimientosSerializer(data=request.data)
        print(request.data)
        if  movimiento_serilizado.is_valid():
            movimiento_serilizado.save()
            return Response(movimiento_serilizado.data)
        return Response( movimiento_serilizado.errors)


@api_view(['GET', 'POST'])
def proveedoresAPIView(request):
    if request.method == 'GET':
        proveedoresBD = proveedores.objects.all()
        proveedoresBD_serialilizada = proveedorSerializer(proveedoresBD, many=True)
        return Response(proveedoresBD_serialilizada.data)

    if request.method == 'POST':
        print(request.data)
        entrada_serilizada = proveedorSerializer(data=request.data)
        if entrada_serilizada.is_valid():
            entrada_serilizada.save()
            return Response(entrada_serilizada.data)
        return Response(entrada_serilizada.errors)

@api_view(['GET','PUT','DELETE'])
def proveedores_detail_APIView(request, pk=None, proveedoresBD_serialiada=None):

    if request.method == 'GET':
        proveedoresBD = proveedores.objects.filter(proveedorId=pk).first()
        proveedoresBD_serializada = proveedorSerializer(proveedoresBD)
        return Response(proveedoresBD_serializada.data)

    elif request.method == 'PUT':
        print(request.data)
        proveedoresBD = proveedores.objects.filter(proveedorId=pk).first()
        proveedoresBD_serializada = proveedorSerializer(proveedoresBD, data=request.data)
        if proveedoresBD_serializada.is_valid():
            proveedoresBD_serializada.save()
            return Response(proveedoresBD_serializada.data)
        return Response(proveedoresBD_serializada.errors)

    elif request.method == 'DELETE':
        proveedoresBD = proveedores.objects.filter(proveedorId=pk).first()
        proveedoresBD.delete()
        return Response('Eliminado')









