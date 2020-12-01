# django for vue
1. ***기본 준비***

2. mkdir django_for_vue

3. cd django_for_vue

4. python -m venv venv

5. 확인) source venv/Scripts/activate, pip list, python -m pip install --upgrade pip

6. touch .gitignore

7. gitignore.io > venv, django, visualstudiocode

8. 복사 후 .gitignore에 붙여넣기

9. 확인) git status | .gitignore만 보임, venv 음영처리

10. source venv/Scripts/activate

11. pip install django==2.1.15 djangorestframework

12. pip freeze > requirements.txt

13. ***프로젝트 시작***

14. django-admin startproject django_for_vue . | . 의 의미는 현재폴더에 생성하기

15. setting.py > installedapp > 'rest_framework' 등록

16. python manage.py startapp accounts

17. python manage.py startapp articles

18. setting.py > installedapp > 'accounts', 'articles' 등록

19. user model을 굳이 변경하지 않더라도 나중에 확장성을 보장해주기 위해

    ```python
    # accouts > models.py
    from django.contrib.auth.models import AbstractUser
    
    class User(AbstractUser):
        pass
    
    
    # settings.py 맨아래
    AUTH_USER_MODEL = 'accounts.User'
    ```

20. articles > models.py 에 모델 정의

21. python manage.py makemigrations, python manage.py migrate | 모델링 끝

22. touch articles/serializers.py

    ```python
    from rest_framework import serializers
    from .models import Article
    
    class ArticleListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ['id', 'title', 'created_at']
    
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = '__all__'
    ```

23.  articles/urls.py

    ```python
from django.urls import path
    
    app_name = 'articles'
    
    urlpatterns = [
        path('', views.article_list),
        path('create/', views.create_article),
        path('<int:article_pk>', views.article_detail),
    ]
    ```
    
23. articles/views.py

```python
from django.shortcuts import get_object_or_404
    from rest_framework.decorators import api_view, permission_classes
    from rest_framework.permissions import IsAuthenticated
    from rest_framework.response import Response
    
    from .models import Article
    from .serializers import ArticleListSerializer, ArticleSerializer
    
    @api_view(['GET'])
    def article_list(request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def article_detail(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def create_article(request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
    
```

    - raise_exception=True: REST framework에서 제공하는 기본 exception handler => 400에러 반환


​    
​    
​    
​    
​    
​    
​    

## accounts

```bash
pip install django-rest-auth django-allauth
# django-rest-auth는 로그인 로그아웃
# django-allauth는 사인업까지
```

문서는 djanog rest auth



- settings.py

  ```python
  installed apps = [
      #DRF
      'rest_framework.authtoken,' # 토큰베이스로 인증하려면 이거쓰세요
      
      #rest_auth
      'rest_auth'
  ]
  ```

  ```python
  # DRF auth settings.
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.BasicAuthentication',
          'rest_framework.authentication.SessionAuthentication',
      ]
  }
  
  #우리는 토큰어쎈을 쓸것이기 때문에 위 대신 아래를 써준다
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ]
  }
  ```

  여기까지 기본 세팅

- urls.py

  ```python
  # rest-auth
  path('rest-auth/', include('rest_auth.urls'))
  ```

- 로그인은 토큰 발급

### signup(allauth)

- settings.py

  ```python
  # installed apps
      'django.contrib.sites', # registraion
  
      # rest-auth + allauth
      'allauth',
      'allauth.account',
      'rest_auth.registration',
  
  # django sites app setting
  SITE_ID = 1
  
  ```

- urls.py

  ```python
  # path('rest-auth/registration/', include('rest_auth.registration.urls'))
  # signup으로 이름 바꿔도 된다.
  path('rest-auth/signup/', include('rest_auth.registration.urls'))
  ```



### user도 serializer를 해야 한다

- articles에 user를 엮기 위해서

- ```bash
  touch accounts/serializers.py
  ```

- accounts/serializers.py

  ```python
  from django.contrib.auth import get_user_model
  from rest_framework import serializers
  
  User = get_user_model()
  
  class UserSerializer(serializers.ModelSerializer):
      class meta:
          model = User
          fields = ['id', 'username']
  ```

- articles/serializers.py

  ```python
  + from accounts.serializers import UserSerializer
  
  class ArticleSerializer(serializers.ModelSerializer):
      + user = UserSerializer()
      class Meta:
          model = Article
          fields = '__all__'
  ```

- 어떻게 serializer.is_valid를 통과할것인가

  ```python
  user = UserSerializer(required=False)
  # is_valid() 에서 유무검증 pass
  ```

- articles/views.py = create_article

  ```python
  serializer.save(user=request.user)
  괄호안에 아무것도 안넣을 경우 # NOT NULL CONSTRAINT FAILED
  ```

  내가 누군지 인증하는것은 헤더에 있다

  headers - Authorization - Token 토큰값

- html에서 쓰는 login_required 대신 쓰는것 permission_classes | views.py

  ```python
  from rest_framework.decorators import permission_classes
  from rest_framework.permissions import IsAuthenticated
  
  @permission_classes([IsAuthenticated])
  ```




## 프론트로 넘어가기

### axios 요청을 보낼 때 headers에 뭔가를 담아서 보내야 한다

```bash
pip install django-cors-headers
```

- settings.py

  ```python
  installed app =[
      # CORS
      'corsheaders',
  ]
  
  middleware = [
      # 순서가 중요함 commonmiddleware보다 위에 써주자
      'corsheaders.middleware.CorsMiddleware',
  ]
  ```

  브라우저야 얘만 열어줘 whitelist

  ```python
  # CORS Allow
  CORS_ORIGIN_ALLOW_ALL = True
  ```

  



---

토큰 발급이 됐다는 것은 로그인 됐다는 것을 의미

따라서 회원가입 후 토큰이 자동 생성됐다면 자동 로그인 됐다는 것.

userserializer을 만드는 이유 -> article을 생성할 때 유저 필드가 비어있으면 안 되는데

serializer은 form과 다르게 save 할 때 정보를 함께 저장할 수 있다

ArticleSerializer에서 user = UserSerializer(required=False) 옵션을 넣으면 is_valid()에서 유저 유무 검증을 패스한다.

데이터 유무 검증 시, 세 가지를 모두 통과해야 하는데 0.UI HTML파트에서도 Scripts로 검증 1. 장고에서 폼 or 시리어라이저를 통해 걸릴 수도 있고 2. 데이터베이스에서 not null 조건으로 걸릴 수도 있다. 세 가지로 검증 가능한데 어디서 걸리는지 알아야 한다.

장고 서버에서 사용자 인증 관련해서는 토큰베이스로 관리된다.



(drf 규칙에 의해) 내가 누군지 즉, 인증에 대한 정보는 header에 들어간다.

body에는 사용자가 보내고 싶은 정보를 담는다.



request, response의 header와 body는 각각 따로 있다

사용자 인증 정보는 request의 header에 담는다



@login_required는 html 파트에서 사용하는 것이기 때문에 django-rest-framework 에서는 permission_classes와 Isauthenticated 두 개를 사용한다.



세션베이스, 토큰베이스 인증에서 로그아웃 후 재 로그인시 새로운 토큰이 발급된다. 항상 바뀐다.



JWT _  json web token authentication 방식을 요즘 많이 쓰고 있다.  무작위가 아닌 데이터를 담아 놓은 토큰이다. 암호화된 상태가 아니다.

토큰이나 세션은 db를 사용하지만 jwt 는 db 서버에 아무것도 저장하지 않음, 사용하지 않고 그저 해석만 하는 방식이다. 기존 토큰과 다른 방식이니 유념



> 가장 핵심이 되는 것은 토큰 헤더에 토큰값을 넣으면 drf가 request.user를 찾아온다는 것이다. vue에서 장고 서버에 axios.post 요청을 보내면 헤더에 토큰이 있어야 사용자를 인증할 수 있다는 것.

