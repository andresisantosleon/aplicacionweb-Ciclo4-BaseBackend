from rest_framework import serializers
from .models import *


class materiaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model=materiaPrima
        #fields="__all__"
        exclude=('materiaPrimaId',)


class proveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedores
        #fields="__all__"
        exclude = ('proveedorId',)


class movimientosSerializer(serializers.ModelSerializer):

    #refMateriaprima=serializers.SlugRelatedField(slug_field='materiaPrimaId', read_only=False, queryset=materiaPrima.objects.all())
    #refProveedor=serializers.SlugRelatedField(slug_field='proveedorId', read_only=False, queryset=proveedores.objects.all())
    refMateriaprima=serializers.PrimaryKeyRelatedField(read_only=False, queryset=materiaPrima.objects.all())
    refProveedor=serializers.PrimaryKeyRelatedField(read_only=False, queryset=proveedores.objects.all())

    class Meta:
        model=movimientos
        fields=('movimientoCantidad','refMateriaprima', 'refProveedor')

    def create(self, validated_data):
        meteriaPrimaObjeto=validated_data.pop('refMateriaprima')
        proveedorObjeto=validated_data.pop('refProveedor')
        movimientoInput=movimientos.objects.create(**validated_data, idMateriaPrima=meteriaPrimaObjeto, movimientoProveedor=proveedorObjeto)
        return movimientoInput

    def to_representation(self, obj):
        materiaPrimaPresentacion=materiaPrima.objects.get(materiaPrimaId=obj.idMateriaPrima_id)
        proveedorPresentacion=proveedores.objects.get(proveedorId=obj.movimientoProveedor_id)
        representacion={'cantidad': obj.movimientoCantidad,
        'materiaPrima': materiaPrimaPresentacion.materiaPrima_descripcion,
        'proveedor': proveedorPresentacion.proveedor_Name}
        return representacion


#movimientos.objects.all().delete()