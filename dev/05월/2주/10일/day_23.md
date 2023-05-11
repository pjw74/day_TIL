## <u>SQL_Analysis_Day 3-1</u>

- ### <u>SQL - GROUP BY, CTAS</u>

- #### GROUP BY & Aggregate 함수 (1)

  - 테이블의 레코드를 그룹핑하여 그룹별로 다양한 정보를 계산
  - 두 단계로 이뤄짐

    - 먼저 그룹핑을 할 필드를 결정(하나 이상의 필드가 될 수 있음)
      - GROUP BY로 지정(필드 이름을 사용하거나 필드 일련번호를 사용)
    - 다음 그룹별로 계산할 내용을 결정

      - 여기서 Aggregate함수를 사용
      - COUNT, SUM, AVG, MIN, MAX, LISTAGG, ...
        - 보통 필드 이름을 지정하는 것이 일반적 (alias)

- #### GROUP BY & Aggregate 함수 (2)

  - 월별 세션수를 계산하는 SQL
    - raw_data.session_timestamp를 사용(sessionId와 ts필드)

  ```SQL
  SELECT
    LEFT(ts, 7) AS mon, --2023-05
    COUNT(1) AS session_count
  FROM raw_data.session_timestamp
  GROUP BY 1 -- GROUP BY mon, GROUP BY LEFT(ts,7) 같은 의미
  ORDER BY 1;
  ```

- #### GROUP BY로 다음 문제를 풀어보자

  - 가장 많은 사용된 채널은 무엇인가? (1)

    - 가장 많이 사용되었다는 정의는?
      - 사용자 기반 아니면 세션 기반?
    - 필요한 정보 - 채널 정보, 사용자 정보 혹은 세션 정보
    - 먼저 어느 테이블을 사용해야하는지 생각!
      - **user_session_channel** ?
      - session_timestamp ?
      - 혹은 이 2개의 테이블을 조인해야하나?
      ```SQL
      SELECT
        channel,
        COUNT(1) AS session_count,
        COUNT(DISTINCT userId) AS user_count
      FROM raw_data.user_session_channel
      GROUP BY 1
      ORDER BY 2 DESC;
      ```

<br>

- 가장 많은 세션을 만들어낸 사용자 ID는 무엇인가?

  - 필요한 정보 - 세션 정보, 사용자 정보
  - 먼저 어느 테이블을 사용해야하는지 생각!

    - **user_session_channel** ?
    - session_timestamp ?
    - 혹은 이 2개의 테이블을 조인해야하나?

    ```SQL
    SELECT
      userId,
      COUNT(1) AS count
      COUNT(DISTINCT userId) AS user_count
    FROM raw_data.user_session_channel
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 1;
    ```

<br>

- 월별 유니크한 사용자 수(MAU - Monthly Active User)

  - 한 사용자는 한번만 카운트되어야 함
  - MAU에 해당
  - 필요한 정보 - 세션 정보, 사용자 정보
  - 먼저 어느 테이블을 사용해야하는지 생각!

    - user_session_channel(userId, **sessionId**, channel) ?
    - session_timestamp(**sessionId**, ts) ?
    - 혹은 이 2개의 테이블을 조인해야하나?

    ```SQL
    SELECT
      TO_CHAR(A.ts, 'YYYY-MM') AS month,
      COUNT(DISTINCT B.userid) AS mau
    FROM raw_data.session_timestamp A
    JOIN raw_data.user_session_channel B ON A.sessionid = B.sessionid
    GROUP BY 1
    ORDER BY 1 DESC;
    ```

    - TO_CHAR(A.ts, 'YYYY-MM')
      - LEFT(A.ts, 7)
      - SUBSTRING(A.ts, 1, 7)
      - DATE_TRUNC('month', A.ts) --ts 형식

<br>

- 월별 채널별 유니크한 사용자 수
  - 필요한 정보 - 세션 정보, 사용자 정보
  - 먼저 어느 테이블을 사용해야하는지 생각!
    - user_session_channel(userId, **sessionId**, **channel**) ?
    - session_timestamp(**sessionId**, ts) ?
    - 혹은 이 2개의 테이블을 조인해야하나?
    ```SQL
    SELECT
      TO_CHAR(A.ts, 'YYYY-MM') AS month,
      channel,
      COUNT(DISTINCT B.userid) AS mau
    FROM raw_data.session_timestamp A
    JOIN raw_data.user_session_channel B ON A.sessionid = B.sessionid
    GROUP BY 1, 2
    ORDER BY 1 DESC, 2;
    ```

<br>
<br>
<br>

## <u>SQL_Analysis_Day 3-2</u>

## 실습진행 Colab

<br>
<br>

- ![ex-image](./img/1.PNG)

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
