from django.urls import path

from .views import ( get_users, add_user, update_user, delete_user,
    get_documents,
    get_document,
    add_document,
    update_document,
    delete_document,
    get_all_files,
    get_files_by_document,
    add_file,
    delete_file,
    get_all_status,
    get_status_by_document,
    add_status,
    update_status,
    delete_status,
    get_permissions,
    get_permission_by_role,
add_permission,
update_permission,
delete_permission,
get_settings, get_setting,add_setting,update_setting,delete_setting
)

urlpatterns = [
    path('users/', get_users),
    path('users/add/', add_user),
    path('users/update/<int:user_id>/', update_user),
    path('users/delete/<int:user_id>/', delete_user),
     path('documents/', get_documents),
    path('documents/<int:document_id>/', get_document),
    path('documents/add/', add_document),
    path('documents/update/<int:document_id>/', update_document),
    path('documents/delete/<int:document_id>/', delete_document),
    
    path('files/', get_all_files),
    path('files/document/<int:document_id>/', get_files_by_document),
    path('files/add/', add_file),
    path('files/delete/<int:file_id>/', delete_file),
     path('status/', get_all_status),
    path('status/document/<int:document_id>/', get_status_by_document),
    path('status/add/', add_status),
    path('status/update/<int:status_id>/', update_status),
    path('status/delete/<int:status_id>/', delete_status),
path('permissions/', get_permissions),
path('permissions/role/<str:role>/', get_permission_by_role),
path('permissions/add/', add_permission),
path('permissions/update/<int:permission_id>/', update_permission),
path('permissions/delete/<int:permission_id>/', delete_permission),
path('settings/', get_settings),
path('settings/<int:setting_id>/', get_setting),
path('settings/add/', add_setting),
path('settings/update/<int:setting_id>/', update_setting),
path('settings/delete/<int:setting_id>/', delete_setting),


]


