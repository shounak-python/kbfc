from django.contrib import admin
from member.models import Company, Profession, FieldPosition, Club, Player, MemberList

# Register your models here.
admin.site.register(Company)
admin.site.register(Profession)
admin.site.register(FieldPosition)
admin.site.register(Club)
admin.site.register(Player)
admin.site.register(MemberList)