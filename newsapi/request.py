'''
Import request module
'''
from distutils.command.config import config
import requests
from decouple import config
# import newsapi.wayne as wayne

NEWS_API_KEY = config('NEWS_API_KEY')

'''
Making a get request
'''
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
response = requests.get(url)
data = response.json()

'''
Print data that has json content
'''
print(data)


    
    
    
   
