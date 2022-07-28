from unicodedata import category
from django.shortcuts import render, redirect
import requests
import newsapi.wayne as wayne

# Create your views here.

def index(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={wayne.NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={wayne.NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={wayne.NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "index.html", context)

def china(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={wayne.NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=cn&category={category}&apiKey={wayne.NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=cn&apiKey={wayne.NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "china.html", context)


def uae(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={wayne.NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=ae&category={category}&apiKey={wayne.NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=ae&apiKey={wayne.NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "uae.html", context)
