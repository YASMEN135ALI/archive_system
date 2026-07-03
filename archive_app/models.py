from django.db import models
from django.core.exceptions import ValidationError
import re
# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def clean(self):
        password = self.password

        # طول كلمة المرور
        if len(password) < 8:
            raise ValidationError("كلمة المرور يجب أن تكون 8 أحرف على الأقل.")

        # حرف كبير
        if not re.search(r"[A-Z]", password):
            raise ValidationError("كلمة المرور يجب أن تحتوي على حرف كبير واحد على الأقل.")

        # حرف صغير
        if not re.search(r"[a-z]", password):
            raise ValidationError("كلمة المرور يجب أن تحتوي على حرف صغير واحد على الأقل.")

        # رقم
        if not re.search(r"[0-9]", password):
            raise ValidationError("كلمة المرور يجب أن تحتوي على رقم واحد على الأقل.")

        # رمز
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("كلمة المرور يجب أن تحتوي على رمز واحد على الأقل.")

    def __str__(self):
        return self.name

class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)   
    role = models.CharField(max_length=50)               
    can_add = models.BooleanField(default=False)         
    can_edit = models.BooleanField(default=False)        
    can_delete = models.BooleanField(default=False)      
    can_archive = models.BooleanField(default=False)
    can_restore = models.BooleanField(default=False)    

    def __str__(self):
        return f"صلاحيات الدور: {self.role}"



class GeneralSettings(models.Model):
    setting_id = models.AutoField(primary_key=True)          # رقم الإعداد
    document_types = models.JSONField(default=dict)          # أنواع الوثائق
    security_levels = models.JSONField(default=dict)         # مستويات السرية
    archive_rules = models.JSONField(default=dict)           # قواعد الأرشفة

    def __str__(self):
        return f"إعدادات رقم {self.setting_id}"



class Document(models.Model):
    document_id = models.AutoField(primary_key=True)            
    title = models.CharField(max_length=200)                     
    type = models.CharField(max_length=100)                      
    owner = models.IntegerField()                               
    security_level = models.CharField(max_length=100)            
    created_at = models.DateTimeField(auto_now_add=True)         
    updated_at = models.DateTimeField(auto_now=True)            
    attachment = models.FileField(upload_to='attachments/')      

    def __str__(self):
        return self.title



class DocumentStatus(models.Model):
    status_id = models.AutoField(primary_key=True)              # رقم الحالة
    document_id = models.IntegerField()                        # رقم الوثيقة

    status = models.CharField(max_length=100)                  # حالة الوثيقة
    updated_by = models.IntegerField()                         # من عدل الحالة
    updated_at = models.DateTimeField(auto_now=True)           # وقت التعديل
    notes = models.TextField(null=True, blank=True)            # ملاحظات

    def __str__(self):
        return f"حالة الوثيقة رقم {self.document_id}: {self.status}"



class DocumentFiles(models.Model):
    file_id = models.AutoField(primary_key=True)                 # رقم الملف
    document_id = models.IntegerField()                         # الوثيقة المرتبطة بها الملف
    file_path = models.FileField(upload_to='document_files/')   # مسار الملف المخزن
    uploaded_at = models.DateTimeField(auto_now_add=True)       # تاريخ رفع الملف
    uploaded_by = models.IntegerField()                         # المستخدم الذي رفع الملف

    def __str__(self):
        return f"ملف رقم {self.file_id} للوثيقة {self.document_id}"
