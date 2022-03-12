from django.contrib import admin

from graph.models import Group, Node


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ("name", "color")
    list_display = ("name", "color")


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    fields = search_fields = (
        "link",
        "group",
        "title",
        "year",
        "month",
        "authors",
        "summary",
        "description",
    )

    list_display = (
        "summary",
        "year",
        "month",
        "authors",
        "group",
        "title",
    )

    list_filter = ("group",)
