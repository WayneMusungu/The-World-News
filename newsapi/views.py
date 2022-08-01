from unicodedata import category
from django.shortcuts import render, redirect
import requests
from decouple import config
# import newsapi.wayne as wayne


NEWS_API_KEY = config('NEWS_API_KEY')

# Create your views here.

def index(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles=data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "index.html", context)

def china(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles= data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=cn&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=cn&apiKey={NEWS_API_KEY}'
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
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=ae&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=ae&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "uae.html", context)

def argentina(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=ar&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=ar&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "argentina.html", context)


def austria(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=at&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=at&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "austria.html", context)


def australia(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=au&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=au&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "australia.html", context)


def belgium(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=be&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=be&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "belgium.html", context)


def bulgaria(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=bg&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=bg&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "bulgaria.html", context)


def brazil(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=br&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=br&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "brazil.html", context)


def southafrica(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=za&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=za&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "southafrica.html", context)


def canada(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=ca&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=ca&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "canada.html", context)

def nigeria(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=ng&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=ng&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "nigeria.html", context)

def germany(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=de&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=de&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "germany.html", context)


def ukraine(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=ua&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=ua&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "ukraine.html", context)


def netherlands(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=nl&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=nl&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "netherlands.html", context)


def japan(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=jp&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=jp&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "japan.html", context)


def egypt(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=eg&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=eg&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "egypt.html", context)

def morocco(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=ma&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=ma&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "morocco.html", context)

def israel(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=il&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=il&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "israel.html", context)


def southkorea(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=kr&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=kr&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "southkorea.html", context)

def france(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=fr&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=fr&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "france.html", context)


def uk(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=gb&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=gb&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "uk.html", context)

def italy(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=it&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=it&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "italy.html", context)


def portugal(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=pt&category={category}&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=pt&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        
        
    context = {
        'articles' : articles
    }
        
    return render (request, "portugal.html", context)


