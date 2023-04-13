# -- Markdown --

# 0. 더보기

[참조 링크1]: https://heropy.blog/2017/09/30/markdown/

더보기 [참조 링크1]를 그대로 사용할 수도 있습니다.

# 1. 글씨크기

## 2

### 3

#### 4 ~ 6

# 2. 글씨 색

- <span style="color:red"> 빨강 글씨 </span>

red
yellow
blue
brown
orange
green
violet
black
yellowgreen
blueviolet
white
greenyellow
indigo
gray

# 3. 띄어쓰기

    <br>

# 4. 강조

_기울게_ _기울게_
**굵게** **굵게**
**_기울고 굵게_** **_기울고 굵게_**
~~취소선~~
<u>밑줄</u>

# 5. 간선

---

---

# 6. 이미지 추가

![this_screenshot](./img/??.PNG)

# 7. 목록

       1. 순서가 필요한 목록
       2. 순서가 필요한 목록
        - 순서가 필요하지 않은 목록(서브)
        - 순서가 필요하지 않은 목록(서브)
       3. 순서가 필요한 목록
        1. 순서가 필요한 목록(서브)
        2. 순서가 필요한 목록(서브)
       4. 순서가 필요한 목록

       - 순서가 필요하지 않은 목록에 사용 가능한 기호
        - 대쉬(hyphen)
        * 별표(asterisks)
        + 더하기(plus sign)

# 8. 링크

[GOOGLE](https://google.com)

[NAVER](https://naver.com "링크 설명(title)을 작성하세요.")

[상대적 참조](../users/login)

[Dribbble][dribbble link]

[GitHub][1]

문서 안에서 [참조 링크]를 그대로 사용할 수도 있습니다.

다음과 같이 문서 내 일반 URL이나 꺾쇠 괄호(`< >`, Angle Brackets)안의 URL은 자동으로 링크를 사용합니다.
구글 홈페이지: https://google.com
네이버 홈페이지: <https://naver.com>

[dribbble link]: https://dribbble.com
[1]: https://github.com
[참조 링크]: https://naver.com "네이버로 이동합니다!"

# 9. 이미지에 링크

[![Vue](/images/vue.png)](https://kr.vuejs.org/)
