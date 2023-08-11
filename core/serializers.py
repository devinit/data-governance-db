from django.urls import path, include
from rest_framework import permissions, routers, serializers, viewsets
# from .models import ...



class CoreSerializer(serializers.HyperlinkedModelSerializer):
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CoreSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'lookup_field', None):
            return expanded_fields + [self.Meta.lookup_field]
        else:
            return expanded_fields


# class ClientSerializer(CoreSerializer):
#     class Meta:
#         model = Client
#         fields = '__all__'
#         lookup_field = 'code'


# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


router = routers.DefaultRouter()
# router.register(r'clients', ClientViewSet)
