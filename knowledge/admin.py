from django.contrib import admin
from.models import Skill,Category, Tag

# Register your models here.


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "category",
        "slug",
        "profile",
        "published",
        "updated_at",
        )

    list_filter= ["category", "published"]
    prepopulated_fields = {"slug": ["title"]}
    list_editable= ['category']
    ordering = ["-updated_at"]
    search_fields= ["title"]
    filter_horizontal=["tags"]
    autocomplete_fields= ["profile"]
    list_per_page: 5

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'label', 'slug'
    )


admin.site.register([Tag])