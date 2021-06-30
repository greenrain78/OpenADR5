from django.shortcuts import render


# Create your views here.
from app_collect.models import equipments_info


def equipments_list(request):
    posts = equipments_info.objects.all()

    if 'page' in request.GET:
        p = int(request.GET['page'])
        posts = posts[(p - 1) * 10, p * 10]
    return render(request, 'equipments_list.html', {'equipments_list': posts})

#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/detail.html', {'post': post})
