from django.shortcuts import render

def embedded_railway_view(request):
    return render(request, 'certibridge_core/embedded_railway.html')