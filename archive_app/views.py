from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import (
    User,
    Permission,
    GeneralSettings,
    DocumentCategory,
    Document,
    DocumentStatus,
    DocumentFiles,
    ActivityLog
)

from .serializers import (
    UserSerializer,
    PermissionSerializer,
    GeneralSettingsSerializer,
    DocumentCategorySerializer,
    DocumentSerializer,
    DocumentStatusSerializer,
    DocumentFilesSerializer,
    ActivityLogSerializer
)


# ============================
# User ViewSet
# ============================
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# ============================
# Permission ViewSet
# ============================
class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]


# ============================
# General Settings ViewSet
# ============================
class GeneralSettingsViewSet(viewsets.ModelViewSet):
    queryset = GeneralSettings.objects.all()
    serializer_class = GeneralSettingsSerializer
    permission_classes = [IsAuthenticated]


# ============================
# Document Category ViewSet
# ============================
class DocumentCategoryViewSet(viewsets.ModelViewSet):
    queryset = DocumentCategory.objects.all()
    serializer_class = DocumentCategorySerializer
    permission_classes = [IsAuthenticated]


# ============================
# Document ViewSet
# ============================
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    # فلترة حسب النوع أو الحالة أو مستوى السرية
    def get_queryset(self):
        queryset = Document.objects.all()

        category = self.request.query_params.get('category')
        status = self.request.query_params.get('status')
        security = self.request.query_params.get('security_level')

        if category:
            queryset = queryset.filter(category__name=category)

        if status:
            queryset = queryset.filter(status=status)

        if security:
            queryset = queryset.filter(security_level=security)

        return queryset


# ============================
# Document Status ViewSet
# ============================
class DocumentStatusViewSet(viewsets.ModelViewSet):
    queryset = DocumentStatus.objects.all()
    serializer_class = DocumentStatusSerializer
    permission_classes = [IsAuthenticated]


# ============================
# Document Files ViewSet
# ============================
class DocumentFilesViewSet(viewsets.ModelViewSet):
    queryset = DocumentFiles.objects.all()
    serializer_class = DocumentFilesSerializer
    permission_classes = [IsAuthenticated]


# ============================
# Activity Log ViewSet
# ============================
class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    permission_classes = [IsAuthenticated]
