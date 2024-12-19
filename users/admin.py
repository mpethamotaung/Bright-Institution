from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TutorProfile, StudentProfile

class TutorProfileInline(admin.StackedInline):
    model = TutorProfile
    can_delete = False
    verbose_name_plural = 'Tutor Profile'

class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False
    verbose_name_plural = 'Student Profile'

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_student', 'is_tutor']
    list_filter = ['is_student', 'is_tutor']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_student', 'is_tutor')}),
    )
    search_fields = ['username', 'email']
    ordering = ['username']

    def get_inline_instances(self, request, obj=None):
        inlines = []
        if obj and obj.is_student:
            inlines.append(StudentProfileInline(self.model, self.admin_site))
        if obj and obj.is_tutor:
            inlines.append(TutorProfileInline(self.model, self.admin_site))
        return inlines

class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone', 'subjects']
    search_fields = ['user__username', 'email', 'subjects']
    ordering = ['user__username']

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone', 'grade', 'subjects']
    search_fields = ['user__username', 'email', 'grade', 'subjects']
    ordering = ['user__username']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TutorProfile, TutorProfileAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
