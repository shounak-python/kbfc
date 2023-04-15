from django.shortcuts import render
from django.urls import reverse_lazy
from member.models import MemberList


def memberlist(request):
    member_obj = MemberList.objects.all()
    print(member_obj)
    for item in member_obj:
        print(item)
    ctx = {"obj": member_obj}
    return render(request, "member/memberlist.html", ctx)