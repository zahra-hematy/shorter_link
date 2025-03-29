from .models import Link
from django.shortcuts import render, HttpResponse
from . import forms
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, DetailView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views import View
import base64

def url_to_base64(url):
    # Encode the URL to bytes
    url_bytes = url.encode('utf-8')
    # Encode the bytes to Base64
    base64_bytes = base64.b64encode(url_bytes)
    # Convert the Base64 bytes back to a string
    base64_url = base64_bytes.decode('utf-8')
    #print(type(base64_url))
    base64_url_short = base64_url[0:10]
    return base64_url_short



def ConvertView(request):
	if request.method == 'POST':
		form = forms.ConvertForm(request.POST)
		if form.is_valid():
			url_long = form.cleaned_data['url_long']
			url_short = url_to_base64(url_long)

			url_obj = Link(url_long=url_long, 
							url_short=url_short,
							user=request.user if request.user.is_authenticated else None
							)
			url_obj.save()
			return render(request, 'short_link.html', {'url_short': url_short})
	else:
		form = forms.ConvertForm()
	return render(request, 'index.html', {'form': form})
