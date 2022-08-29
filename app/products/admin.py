from django.contrib import admin

from .models import Claim


class ClaimAdmin(admin.ModelAdmin):
    """Admin model for claims treatment."""

    # Options for list view
    list_display = (
        "date",
        "status",
        "name",
        "code",
        "brand",
    )
    list_display_links = ("name",)
    list_filter = ("date", "status")
    ordering = ("date",)
    # Options for edit view
    readonly_fields = ("name", "brand", "code", "user_comment")
    fieldsets = (
        (
            "Produit demandé",
            {"fields": ("name", "brand", "code", "user_comment")},
        ),
        ("Réponse", {"fields": ("admin_comment", "status")}),
    )


admin.site.register(Claim, ClaimAdmin)
