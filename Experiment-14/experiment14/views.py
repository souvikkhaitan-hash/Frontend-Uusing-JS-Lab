from django.shortcuts import render


def base_layout_demo(request):
    return render(request, "layout.html")