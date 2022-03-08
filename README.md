# DRF
1. install `djangorestframework` using 
```shell 
pip install djangorestframework
```
2. Add this to our project settings
3. create a `serializer.py` file - converts a model to json and vice versa
4.  create a class serializer for a model
   

# Authentication for API

1. We first add `rest_framework.authtoken` to our INSTALLED_APPS settings. Remember to migrate the database to add any changes.

2. We then define the DEFAULT_AUTHENTICATION_CLASSES for the `rest_frameworkpackage`. Now we can define the URLConf to allow us to get the token.
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
```

3. in `urls.py` add the authentication urls

```py
from rest_framework.authtoken.views import obtain_auth_token
#.......
urlpatterns = [
#.......
    url(r'^api-token-auth/', obtain_auth_token)
]
```
