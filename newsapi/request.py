'''
Import request module
'''
import requests
import wayne

'''
Making a get request
'''
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={wayne.NEWS_API_KEY}'
response = requests.get(url)
data = response.json()

'''
Print data that has json content
'''
print(data)


    
    
    
   
