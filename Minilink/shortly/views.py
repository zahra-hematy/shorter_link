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


import hashlib  # Import hashlib to generate a hash for the long URL

# Dictionary to store the mapping between long URLs and short URLs
url_mapping = {}

def shorten_url(long_url):
    """Generate a short URL by hashing the long URL."""
    # Generate a unique hash using SHA-256 and take the first 6 characters for short URL
    short_url_hash = hashlib.sha256(long_url.encode()).hexdigest()[:6]
    short_url = f"https://short.url/{short_url_hash}"
    
    # Store the mapping in the dictionary
    url_mapping[short_url] = long_url
    
    return short_url

def ConvertView(request):
	if request.method == 'POST':
		form = forms.ConvertForm(request.POST)
		if form.is_valid():
			url_long = form.cleaned_data['url_long']
			url_short = shorten_url(url_long)

			url_obj = Link(url_long=url_long, 
							url_short=request.build_absolute_uri(f'/{url_short}'),
							user=request.user if request.user.is_authenticated else None
							)
			url_obj.save()
			return render(request, 'short_link.html', {'url_short': url_short})
	else:
		form = forms.ConvertForm()
	return render(request, 'index.html', {'form': form})
