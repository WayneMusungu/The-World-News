from django.shortcuts import render, redirect
import requests
import newsapi.wayne as wayne

# Create your views here.

def index(request):
    
    # url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={wayne.NEWS_API_KEY}'
    
    country = request.GET.get('country')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={wayne.NEWS_API_KEY}'
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
