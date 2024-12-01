from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


# class CustomUserAdmin(UserAdmin):
#     """
#     Custom admin panel for user management with add and change forms plus password
#     """

#     model = User
#     list_display = ("id", "email","is_verified")
#     list_filter = ("email", "is_verified")
#     searching_fields = ("email",)
#     ordering = ("email",)
#     fieldsets = (
#         (
#             "Authentication",
#             {
#                 "fields": ("email", "password"),
#             },
#         ),
#         (
#             "permissions",
#             {
#                 "fields": (
#                     "is_superuser",
#                     "is_staff",
#                     "is_verified",
#                 ),
#             },
#         ),
#         (
#             "group permissions",
#             {
#                 "fields": ("groups", "user_permissions","user_type"),
#             },
#         ),
#         (
#             "important date",
#             {
#                 "fields": ("last_login",),
#             },
#         ),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "email",
#                     "password1",
#                     "password2",
#                     "is_superuser",
#                     "is_verified",
#                     "is_staff",
#                     "user_type",
#                 ),
#             },
#         ),
#     )

# admin.site.register(Profile)
admin.site.register(User)