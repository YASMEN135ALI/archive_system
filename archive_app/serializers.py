from rest_framework import serializers
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


# ============================
# User Serializer
# ============================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'role',
            'is_active',
            'created_at'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }


# ============================
# Permission Serializer
# ============================
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


# ============================
# General Settings Serializer
# ============================
class GeneralSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSettings
        fields = '__all__'


# ============================
# Document Category Serializer
# ============================
class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = '__all__'


# ============================
# Document Serializer
# ============================
class DocumentSerializer(serializers.ModelSerializer):

    # عرض اسم المستخدم بدل رقمه
    owner = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    # عرض اسم التصنيف بدل رقمه
    category = serializers.StringRelatedField()

    class Meta:
        model = Document
        fields = [
            'id',
            'reference_number',
            'title',
            'description',
            'category',
            'security_level',
            'status',
            'owner',
            'created_by',
            'archive_date',
            'attachment',
            'created_at',
            'updated_at'
        ]


# ============================
# Document Status Serializer
# ============================
class DocumentStatusSerializer(serializers.ModelSerializer):

    document = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()

    class Meta:
        model = DocumentStatus
        fields = '__all__'


# ============================
# Document Files Serializer
# ============================
class DocumentFilesSerializer(serializers.ModelSerializer):

    document = serializers.StringRelatedField()
    uploaded_by = serializers.StringRelatedField()

    class Meta:
        model = DocumentFiles
        fields = '__all__'


# ============================
# Activity Log Serializer
# ============================
class ActivityLogSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    document = serializers.StringRelatedField()

    class Meta:
        model = ActivityLog
        fields = '__all__'
