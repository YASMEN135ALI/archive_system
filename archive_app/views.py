from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request, user_id):
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Document
from .serializers import DocumentSerializer

@api_view(['GET'])
def get_documents(request):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_document(request, document_id):
    try:
        document = Document.objects.get(document_id=document_id)
    except Document.DoesNotExist:
        return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = DocumentSerializer(document)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_document(request):
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_document(request, document_id):
    try:
        document = Document.objects.get(document_id=document_id)
    except Document.DoesNotExist:
        return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = DocumentSerializer(document, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_document(request, document_id):
    try:
        document = Document.objects.get(document_id=document_id)
    except Document.DoesNotExist:
        return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)

    document.delete()
    return Response({"message": "Document deleted successfully"}, status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import DocumentFiles
from .serializers import DocumentFilesSerializer

@api_view(['GET'])
def get_all_files(request):
    files = DocumentFiles.objects.all()
    serializer = DocumentFilesSerializer(files, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_files_by_document(request, document_id):
    files = DocumentFiles.objects.filter(document_id=document_id)
    serializer = DocumentFilesSerializer(files, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_file(request):
    serializer = DocumentFilesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_file(request, file_id):
    try:
        file = DocumentFiles.objects.get(file_id=file_id)
    except DocumentFiles.DoesNotExist:
        return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)

    file.delete()
    return Response({"message": "File deleted successfully"}, status=status.HTTP_200_OK)


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import DocumentStatus
from .serializers import DocumentStatusSerializer

@api_view(['GET'])
def get_all_status(request):
    statuses = DocumentStatus.objects.all()
    serializer = DocumentStatusSerializer(statuses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_status_by_document(request, document_id):
    statuses = DocumentStatus.objects.filter(document_id=document_id)
    serializer = DocumentStatusSerializer(statuses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_status(request):
    serializer = DocumentStatusSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_status(request, status_id):
    try:
        status_obj = DocumentStatus.objects.get(status_id=status_id)
    except DocumentStatus.DoesNotExist:
        return Response({"error": "Status not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = DocumentStatusSerializer(status_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_status(request, status_id):
    try:
        status_obj = DocumentStatus.objects.get(status_id=status_id)
    except DocumentStatus.DoesNotExist:
        return Response({"error": "Status not found"}, status=status.HTTP_404_NOT_FOUND)

    status_obj.delete()
    return Response({"message": "Status deleted successfully"}, status=status.HTTP_200_OK)

from .models import Permission
from .serializers import PermissionSerializer
@api_view(['GET'])
def get_permissions(request):
    permissions = Permission.objects.all()
    serializer = PermissionSerializer(permissions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_permission_by_role(request, role):
    permissions = Permission.objects.filter(role=role)
    serializer = PermissionSerializer(permissions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_permission(request):
    serializer = PermissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_permission(request, permission_id):
    try:
        permission = Permission.objects.get(permission_id=permission_id)
    except Permission.DoesNotExist:
        return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PermissionSerializer(permission, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_permission(request, permission_id):
    try:
        permission = Permission.objects.get(permission_id=permission_id)
    except Permission.DoesNotExist:
        return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)

    permission.delete()
    return Response({"message": "Permission deleted successfully"}, status=status.HTTP_200_OK)

from .models import GeneralSettings
from .serializers import GeneralSettingsSerializer

@api_view(['GET'])
def get_settings(request):
    settings = GeneralSettings.objects.all()
    serializer = GeneralSettingsSerializer(settings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_setting(request, setting_id):
    try:
        setting = GeneralSettings.objects.get(setting_id=setting_id)
    except GeneralSettings.DoesNotExist:
        return Response({"error": "Setting not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = GeneralSettingsSerializer(setting)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_setting(request):
    serializer = GeneralSettingsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_setting(request, setting_id):
    try:
        setting = GeneralSettings.objects.get(setting_id=setting_id)
    except GeneralSettings.DoesNotExist:
        return Response({"error": "Setting not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = GeneralSettingsSerializer(setting, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_setting(request, setting_id):
    try:
        setting = GeneralSettings.objects.get(setting_id=setting_id)
    except GeneralSettings.DoesNotExist:
        return Response({"error": "Setting not found"}, status=status.HTTP_404_NOT_FOUND)

    setting.delete()
    return Response({"message": "Setting deleted successfully"}, status=status.HTTP_200_OK)
