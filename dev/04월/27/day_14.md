## <u>1. User 추가하기</u>

- polls/models.py

```python
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='질문')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    owner = models.ForeignKey('auth.User', related_name='questions', on_delete=models.CASCADE, null=True)

    @admin.display(boolean=True, description='최근생성(하루기준)')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f'제목: {self.question_text}, 날짜: {self.pub_date}'
    ...
```

<br>

- Django Shell

```python
>>> from django.contrib.auth.models import User
>>> User
<class 'django.contrib.auth.models.User'>
>>> User._meta.get_fields()
>>> User.objects.all()
<QuerySet [<User: admin>]>

>>> from polls.models import *
>>> user = User.objects.first()
>>> user.questions.all()
>>> print(user.questions.all().query)
SELECT "polls_question"."id", "polls_question"."question_text", "polls_question"."pub_date", "polls_question"."owner_id" FROM "polls_question" WHERE "polls_question"."owner_id" = 1
```

<br>
<br>
<br>

## <u>2. User 관리하기</u>

- polls_api/serializers.py

```python
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'questions']
```

<br>

- polls_api/views.py

```python
from django.contrib.auth.models import User
from polls_api.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

<br>

- polls_api/urls.py

```python
from django.urls import path
from .views import *

urlpatterns = [
    path('question/', QuestionList.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('users/', UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view()),
]
```

<br>
<br>
<br>

## <u>3. Form을 사용하여 User 생성하기</u>

- polls/views.py

```python
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('user-list')
    template_name = 'registration/signup.html'
```

- polls/templates/registration/signup.html

```HTML
<h2>회원가입</h2>
 <form method="post">
   {% csrf_token %}
   {{ form.as_p }}
   <button type="submit">가입하기</button>
</form>
```

- polls/urls.py

```python
from django.urls import path
from . import views
from .views import *

app_name = 'polls'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('signup/', SignupView.as_view(), )
]
```

- Django Shell

```python
>>> from django.urls import reverse_lazy
>>> reverse_lazy('user-list')
'/rest/users/'
```

<br>
<br>
<br>

## <u>4. Serializer를 사용하여 User 생성하기</u>

- polls_api/serializers.py

```python
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "두 패스워드가 일치하지 않습니다."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['username', 'password','password2']
```

- polls_api/views.py

```python
from polls_api.serializers import RegisterSerializer

class RegisterUser(generics.ListCreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
```

- polls_api/urls.py

```python
from django.urls import path
from .views import *

urlpatterns = [
    path('question/', QuestionList.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('users/', UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('register/', RegisterUser.as_view()),

]
```

<br>
<br>
<br>

## <u>5. User 권한 관리</u>

- polls_api/urls.py

```python
from django.urls import path,include
from .views import *

urlpatterns = [
    path('question/', QuestionList.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('users/', UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('register/', RegisterUser.as_view()),
    path('api-auth/', include('rest_framework.urls'))

]
```

<br>

- mysite/settings.py

```python
from django.urls import reverse_lazy
LOGIN_REDIRECT_URL = reverse_lazy('question-list')
LOGOUT_REDIRECT_URL = reverse_lazy('question-list')
```

<br>

- polls_api/serializers.py

```python
class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'owner']
```

<br>

- polls_api/permissions.py

```python
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
```

<br>

- polls_api/views.py

```python
from rest_framework import generics,permissions
from .permissions import IsOwnerOrReadOnly

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
```

<br>
<br>
<br>

## <u>6. perform_create()</u>

- **perform_create()의 동작원리**
- QuestionList

  - generics.ListCreateAPIView
    - mixins.CreateModelMixin

- QuestionList안에 정의된 메소드들

  - def get(self, request, \*args, \*\*kwargs):
    - 출처: generics.ListCreateAPIView
  - def create(self, request, \*args, \*\*kwargs):
    - 출처: mixin.CreateModelMixin
  - def perform_create(sefl, serializer):
    - **지워짐**: mixins.CreateModelMixin(상속)
    - **동작함**: QuestionList(자식에 자식에 자식에서 만든 메소드)

- 구현하다 중복, 모르겠으면 ${\color{red}부모\space 클래스들을\space 들여다\space 볼\space 것}$

<br>
<br>

- Django Shell

```python
>>> from polls_api.serializers import QuestionSerializer
>>> question_serializer = QuestionSerializer(data={"question_text": "some text","owner" :"someone"})
>>> question_serializer.is_valid()
True
>>> question_serializer.validated_data
OrderedDict([('question_text', 'some text')])
>>> question = question_serializer.save(id=10000)
>>> question.id
10000
>>> question.question_text
'some text'
```

<br>

<br>
<br>
<br>

## <u>7. Postman 설치하기 for Windows</u>

- **POSTMAN**은 RESTful API 테스트를 위한 플랫폼
  1. 다양한 HTTP 요청을 보내고 응답 결과를 쉽게 확인할 수 있도록 도와줌.
  2. API 요청과 응답 결과를 저장하고 공유할 수 있는 기능 제공.

<br>
<br>
<br>

## <u>8. </u>

- polls_api/urls.py

```python


```

<br>
<br>
<br>

**<특강>** - ppt 참고 작성(github)

- ㅇㅇ

<br>
<br>
<br>

## <u>상속(Inheritance) 과 오버라이딩(Overriding )</u>

- 자신의 메소드와 속성을 물려주는 클래스를 **부모 클래스(Parent Class)** 또는 **상위 클래스(Super class)** 라고 지칭
- 반대로 그것을 물려받아서 사용하는 클래스는 **자식 클래스(Child Class)** 또는 **하위 클래스(Sub Class)** 라고 부릅니다.

- 파이썬에서 상속을 구현하기 위한 방법은
  - 자식 클래스의 괄호 안에 부모 클래스를 명시하는 것 입니다.

1. 자식 클래스에서는 부모 클래스의 모든 메서드와 속성을 자유롭게 사용 가능하며,
2. 새로운 메서드를 추가하거나 기존 메서드의 내용을 변경 가능.

ex) 다음은 부모 클래스인 Animal 클래스를 정의하고, 자식 클래스인 Dog 클래스가 Animal 클래스를 상속받도록 구현하는 예시코드입니다.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "동물이 울음소리를 냅니다"

class Dog(Animal):
    def speak(self):
        return "멍멍!"

my_dog = Dog("초코")
print(my_dog.name)  # 출력: 초코
print(my_dog.speak())  # 출력: 멍멍!
```

<br>
<br>
<br>

<br>
<br>
<br>

<br>
<br>
<br>
<br>
<br>
<br>

### **Summary**: 회원 추가, 관리, Serializer, 상속&오버라이딩 학습

<br>

- [실습 링크](https://github.com/pjw74/DjangoProject/tree/main/mysite)

- [상속&오버라이딩 링크](https://heytech.tistory.com/109)
- 전체 코드 복습할 것

<br>
<br>
<br>
<br>
<br>
<br>

---

**1. 이론 강의 추가할 부분 추가 진행**

- 추가할 부분: day 02 ~ 11까지 확인

**2. 선택 강의 문제 풀이 진행**
