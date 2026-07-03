from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'name',
            'email',
            'password',
            'role',
            'is_active'
        ]

from .models import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            'permission_id',
            'role',
            'can_add',
            'can_edit',
            'can_delete',
            'can_archive',
            'can_restore'
        ]

from .models import GeneralSettings

class GeneralSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSettings
        fields = [
            'setting_id',
            'document_types',
            'security_levels',
            'archive_rules'
        ]

from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'document_id',
            'title',
            'type',
            'owner',
            'security_level',
            'created_at',
            'updated_at',
            'attachment'
        ]

from .models import DocumentStatus

class DocumentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentStatus
        fields = [
            'status_id',
            'document_id',
            'status',
            'updated_by',
            'updated_at',
            'notes'
        ]

from .models import DocumentFiles

class DocumentFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentFiles
        fields = [
            'file_id',
            'document_id',
            'file_path',
            'uploaded_at',
            'uploaded_by'
        ]
