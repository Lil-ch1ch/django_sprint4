from django.contrib import admin

# Register your models here.
from .models import Category, Location, Post, Comment
<<<<<<< HEAD
=======
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model 

User = get_user_model()
if not admin.site.is_registered(User):
    admin.site.register(User, UserAdmin)
>>>>>>> 3ba034c (Initial commit)

class PostInline(admin.StackedInline):
    model = Post
    extra = 0
    readonly_fields = ("created_at","image_preview")

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return "Нет изображения"
    image_preview.allow_tags= True
    image_preview.short_description="Предпросмотр"

<<<<<<< HEAD
=======

>>>>>>> 3ba034c (Initial commit)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "slug")
    list_editable = ("is_published",)
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = (PostInline,)

<<<<<<< HEAD
=======

>>>>>>> 3ba034c (Initial commit)
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "created_at")
    list_editable = ("is_published",)
    list_filter = ("is_published", "created_at")
    search_fields = ("name",)
    inlines = (PostInline,)

<<<<<<< HEAD
=======

>>>>>>> 3ba034c (Initial commit)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_published",
        "pub_date",
        "author",
        "location",
        "category",
        "created_at",
    )
    list_editable = ("is_published",)
    list_filter = ("is_published", "category",
                   "location", "pub_date", "author")
    search_fields = ("title", "text")
    list_display_links = ("title",)
    readonly_fields = ("created_at","image_preview")
    date_hierarchy = "pub_date"

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("title", "text", "author", "category", "location")},
        ),
        (
            "Публикация",
            {
                "fields": ("is_published", "pub_date", "created_at"),
                "classes": ("collapse",),
            },
        ),
    )

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return "Нет изображения"
    image_preview.allow_tags = True
    image_preview.short_description = "Предпросмотр"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Показываем все посты в админке, даже будущие
        return qs

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)

<<<<<<< HEAD
admin.site.register(Comment)
=======
admin.site.register(Comment)
>>>>>>> 3ba034c (Initial commit)
