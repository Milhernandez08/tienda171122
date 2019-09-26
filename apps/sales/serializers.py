from rest_framework import routers, serializers, viewsets
from apps.sales.models import Sale


class SaleSerializers(serializers.ModelSerializer):
    # quantity    = serializers.ReadOnlyField(source='sales.quantity')
    # total       = serializers.ReadOnlyField(source='sales.total')
    # dates       = serializers.ReadOnlyField(source='sales.dates')
    # payment     = serializers.ReadOnlyField(source='sales.payment')
    # status      = serializers.ReadOnlyField(source='sales.status')
    class Meta:
        model = Sale
        fields = ('__all__')