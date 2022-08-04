## Description 

This is a Django News App that integrates with the NewsApi (newsapi.org) and displays articles/news to the user(s)

##### Link to Live Site

[Link](https://twnews.herokuapp.com/)
 
#### Website Screenshot
![LANDING PAGE](theworldnews.png)


#### Technologies used
    - Python 3.8
    - News API
    - HTML
    - Bootstrap 5
    - Heroku


# Installation

### Requirements

Go to [The News API](https://newsapi.org/) and sign up for an account 
Go to get started then get an API KEY






#### Install dependencies
First, create a `.env` file inside this file you need to store your API Key. Below is how the `.env` file should look like:
`NEWS_API_KEY="your_news_api_key"`
`SECRET_KEY='django_secret_key'`

Install dependencies that will create an environment for the app to run
`pip install -r requirements.txt`


#### Run the app
```bash
python manage.py runserver
```

# License

Copyright (c) 2022 WayneMusungu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.