## <u>16. 뷰(Views)와 템플릿(Templates)</u>

- ### 실습 진행(VScode)

- polls/views.py

```python
from .models import *
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'first_question': latest_question_list[0]}
    return render(request, 'polls/index.html', context)
```

<br>

- Django Shell

```python
>>> from polls.models import *
>>> Question.objects.order_by('-pub_date')[:5]
>>> print(Question.objects.order_by('-pub_date')[:5].query)
SELECT "polls_question"."id", "polls_question"."question_text", "polls_question"."pub_date" FROM "polls_question" ORDER BY "polls_question"."pub_date" DESC LIMIT 5
```

<br>

- polls/templates/polls/index.html

```html
<ul>
  <li>{{first question}}</li>
  <ul></ul>
</ul>
```

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>17. 템플릿(Templates)에서 제어문 사용하기</u>

- ### 실습 진행(VScode)

- polls/templates/polls/index.html

```html
{% if questions %}
<ul>
  {% for question in questions %}
  <li>{{question}}</li>
  {% endfor %}
</ul>
{% else %}
<p>no questions</p>
{% endif %}
```

<br>

- polls/views.py

```python
from .models import *
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    #context = {'questions': []}
    return render(request, 'polls/index.html', context)
```

<br>

- git bash로 업로드 -> src refspec main does not match any 오류
- [참고1](https://star992411.tistory.com/54)
- [참고2](https://daily50.tistory.com/334)

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>18. 상세(detail) 페이지 만들기</u>

- ### 실습 진행(VScode)

- polls/views.py

```python
...
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

<br>

- polls/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('some_url', views.some_url),
    path('<int:question_id>/', views.detail, name='detail'),
]
```

<br>

- polls/templates/polls/detail.html

```html
<h1>{{ question.question_text }}</h1>
<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }}</li>
  {% endfor %}
</ul>
```

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>19. 상세(detail) 페이지로 링크 추가하기</u>

- ### 실습 진행(VScode)

- polls/urls.py

```python
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('some_url', views.some_url),
    path('<int:question_id>/', views.detail, name='detail'),

]
```

<br>

- polls/templates/polls/index.html

```html
{% if questions %}
<ul>
  {% for question in questions %}
  <li>
    <a href="{% url 'polls:detail' question.id %}"
      >{{ question.question_text }}</a
    >
  </li>

  {% endfor %}
  <ul>
    {% else %}
    <p>no questions</p>
    {% endif %}
  </ul>
</ul>
```

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>20. 404 에러 처리하기</u>

- ### 실습 진행(VScode)

- polls/views.py

```python
from models.py import *
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render , get_object_or_404

...
def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>21. 폼(Forms)</u>

- ### 실습 진행(VScode)

- polls/views.py

```python
...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': '선택이 없습니다.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:index'))
```

<br>

- polls/urls.py

```python
...
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

<br>

- polls/templates/polls/detail.html

```html
<form action="{% url 'polls:vote' question.id %}" method="post">
  {% csrf_token %}
  <h1>{{ question.question_text }}</h1>
  {% if error_message %}
  <p><strong>{{ error_message }}</strong></p>
  {% endif %} {% for choice in question.choice_set.all %}
  <input
    type="radio"
    name="choice"
    id="choice{{ forloop.counter }}"
    value="{{ choice.id }}"
  />
  <label for="choice{{ forloop.counter }}"> {{ choice.choice_text }} </label>
  <br />
  {% endfor %}

  <input type="submit" value="Vote" />
</form>
```

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>22. 에러 방어하기 1</u>

- ### 실습 진행(VScode)

- polls/views.py

```python
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': f"선택이 없습니다. id={request.POST['choice']}"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>23. 에러 방어하기 2</u>

- ### 실습 진행(VScode)

- polls/views.py

```python
from django.urls import reverse
from django.db.models import F

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': f"선택이 없습니다. id={request.POST['choice']}"})
    else:
        # A서버에서도 Votes = 1
        # B서버에서도 Votes = 1
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:index'))
```

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>24. 결과(result) 조회 페이지</u>

- ### 실습 진행(VScode)

- polls/views.py

```python
from django.shortcuts import get_object_or_404, render

...
def vote(request, question_id):
...
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})
```

<br>

- polls/templates/polls/result.html

```html
<h1>{{ question.question_text }}</h1>
<br />
{% for choice in question.choice_set.all %}

<label> {{ choice.choice_text }} -- {{ choice.votes }} </label>
<br />
{% endfor %}
```

<br>

- polls/urls.py

```python
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/result/', views.result, name='result'),
]
```

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>25. Django Admin의 편집 페이지 커스터마이징</u>

- ### 실습 진행(VScode)

- polls/admin.py

```python
from django.contrib import admin
from .models import Choice, Question

admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 섹션', {'fields': ['question_text']}),
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
```

<br>

- **Keyword**:

<br>
<br>
<br>

## <u>26. Django Admin의 목록 페이지 커스터마이징</u>

- ### 실습 진행(VScode)

- polls/models.py

```python
import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose='질문')
    pub_date = models.DateTimeField(auto_now_add=True, verbose='생성일')

    @admin.display(boolean=True, description='최근생성(하루기준)')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f'제목: {self.question_text}, 날짜: {self.pub_date}
```

<br>

- polls/admin.py

```python
from django.contrib import admin
from .models import Choice, Question

admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 섹션', {'fields': ['question_text']}),
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text', 'choice__choice_text']

admin.site.register(Question, QuestionAdmin)
```

<br>

- **Keyword**:

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

---

**1. 이론 강의 추가할 부분 추가 진행**

- 추가할 부분: day 02 ~ 12까지 확인

**2. 선택 강의 문제 풀이 진행**
