from django.urls import path, include
from rest_framework import permissions, routers, serializers, viewsets
from .models import (
    Document,
    Institution,
    InstitutionType,
    Category,
    DocumentType
)


class CoreSerializer(serializers.HyperlinkedModelSerializer):
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CoreSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'lookup_field', None):
            return expanded_fields + [self.Meta.lookup_field]
        else:
            return expanded_fields


class DocumentSerializer(CoreSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        lookup_field = 'id'


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


class InstitutionSerializer(CoreSerializer):
    class Meta:
        model = Institution
        fields = '__all__'
        lookup_field = 'id'


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


class InstitutionTypeSerializer(CoreSerializer):
    class Meta:
        model = InstitutionType
        fields = '__all__'
        lookup_field = 'id'


class InstitutionTypeViewSet(viewsets.ModelViewSet):
    queryset = InstitutionType.objects.all()
    serializer_class = InstitutionTypeSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


class CategorySerializer(CoreSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'id'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


class DocumentTypeSerializer(CoreSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'
        lookup_field = 'id'


class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'institutions', InstitutionViewSet)
router.register(r'institution-types', InstitutionTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'document-types', DocumentTypeViewSet)
