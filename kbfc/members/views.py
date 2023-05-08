from django.shortcuts import render
from django.urls import reverse_lazy
from members.models import MemberList, Expertise


def memberlist(request):
    attack_obj = Expertise.objects.get(name='Attack')
    midfield_obj = Expertise.objects.get(name='Midfield')
    defence_obj = Expertise.objects.get(name='Defence')
    gk_obj = Expertise.objects.get(name='Goalkeeping')
    
    all_members = MemberList.objects.all()
    
    attack_members = all_members.filter(area_of_expertise=attack_obj)
    midfield_members = all_members.filter(area_of_expertise=midfield_obj)
    defence_members = all_members.filter(area_of_expertise=defence_obj)
    gk_members = all_members.filter(area_of_expertise=gk_obj)

    ctx = {
        "attack_members":attack_members,
        "midfield_members":midfield_members,
        "defence_members":defence_members,
        "gk_members":gk_members,
    }
    return render(request, "members/memberlist.html", ctx)