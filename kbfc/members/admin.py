from django.contrib import admin
from members.models import Company, Profession, FieldPosition, Club, Player, MemberList, Expertise, Foot

# Register your models here.
class MemberListAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "area_of_expertise", "preferred_field_position")

admin.site.register(Foot)
admin.site.register(Company)
admin.site.register(Profession)
admin.site.register(FieldPosition)
admin.site.register(Club)
admin.site.register(Player)
admin.site.register(Expertise)
admin.site.register(MemberList, MemberListAdmin)