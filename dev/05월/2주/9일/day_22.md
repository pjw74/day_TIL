## <u>SQL_Analysis_Day 2-1</u>

- ### <u>SQL - SELECT</u>

- #### Redshift 클러스터 정보
  - 1 x dc2.large instance
    - 160GB
  - Host
    - learnde.
  - Port number:
    - 5439
  - Database name:
    - dev

- #### 예제 테이블
  - 관계형 데이터베이스 예제 - 웹서브 사용자/세션 정보(1)
    - 사용자 ID: 보통 웹서비스에서는 등록된 사용자마다 부여하는 유일한 ID
    - 세션 ID: 세션마다 부여되는 ID
      - 세션: 사용자의 방문을 논리적인 단위로 나눈 것
        - 사용자가 외부 링크(광고)를 타고 오거나 직접 방문해서 올 경우 세션을 생성
        - 사용자가 방문 후 30분간 interaction이 없거나 뭔가를 하는 경우 새로 세션을 생성
      - 즉 하나의 사용자는 여러 개의 세션을 가질 수 있음
      - 보통 세션의 경우 세션을 만들어낸 접점(경유지)를 채널이란 이름으로 기록해둠 
        - 마케팅 관련 기여도 분석을 위함
      - 또한 세션이 생긴 시간도 기록
      - 



- ### <u>Redshift 론치 데모</u>

  - 관계형 데이터베이스는 2단계로 구성됨
    - 가장 밑단에는 테이블들이 존재 (테이블 엑셀의 시트에 해당)
    - 테이블들은 데이터베이스(혹은 스키마)라는 폴더 밑으로 구성(엑셀에서는 파일)
      ![ex-image](./img/1.PNG)

<br>

- 테이블을 보고 짐작할 수 있다.
  - raw(날 것의) data

<br>

- 테이블의 구조(테이블 스키마라고도 함)

  - 테이블은 레코드들로 구성(행)
  - 레코드는 하나 이상의 필드(컬럼)로 구성(열)
  - 필드(컬럼)는 이름과 타입과 속성(primary key)으로 구성됨

    ![ex-image](./img/2.PNG)
    <br>

  - pk가 동일하면 리젝(유일해야 한다)

<br>

- ### <u>SQL</u>

  - Structured Query Language
    - 관계형 데이터베이스에 있는 데이터(테이블)를 질의하거나 조작해주는 언어
    - SQL은 1970년대 초반에 IBM이 개발한 구조화된 데이터 질의 언어
    - 두 종류의 언어로 구성됨
      - DDL(Data Definition Laguage):
        - 테이블의 구조를 정의하는 언어
      - DML(Data Manipulation Language):
        - 테이블에서 원하는 레코드들을 읽어오는 질의 언어
        - 테이블에 레코드를 추가/삭제/갱신해주는데 사용하는 언어
    - 구조화된 데이터를 다루는 한 SQL은 데이터 규모와 상관없이 쓰임
    - 모든 대용량 데이터 웨어하우스는 SQL기반
      - Redshift, Snowflake, BigQuery, Hive
    - Spark나 Hadoop도 예외 x
      - SparkSQL과 Hive라는 SQL언어 지원됨
    - 데이터 분야에서 일하고자 한다면 반드시 익혀야 함

<br>
<br>
<br>
<br>

- [git push 사용법/팁](https://www.daleseo.com/git-push/)
- [git 입문](https://backlog.com/git-tutorial/kr/stepup/stepup2_4.html)
- [git branch 팁](https://www.freecodecamp.org/korean/news/git-clone-branch-how-to-clone-a-specific-branch/)
- [원하는 파일만 git push](https://velog.io/@lov012726/git%EC%9B%90%ED%95%98%EB%8A%94-%ED%8C%8C%EC%9D%BC%EB%93%A4%EB%A7%8C-git-push-%ED%95%98%EB%8A%94-%EB%B2%95)
- [branch생성 후 push](https://velog.io/@clubmed2/Git-branch%EC%83%9D%EC%84%B1-%ED%9B%84-push%ED%95%98%EA%B8%B0)
- [git main](https://blog.outsider.ne.kr/1598)

<br>
<br>
<br>
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
<br>
<br>
<br>
<br>

### **Summary**:

<br>

- [실습 링크](https://github.com/pjw74/DjangoProject/tree/main/mysite)

- 전체 코드 복습할 것

<br>
<br>
<br>
<br>
<br>
<br>

---

**1. 이론 강의 추가할 부분 추가 진행**

- 추가할 부분: day 02~06까지 확인
- 보충: day 07~13

**2. 선택 강의 문제 풀이 진행**
