from django.shortcuts import render, render_to_response

def homePage (request):
    return render_to_response('plantilla.html')
