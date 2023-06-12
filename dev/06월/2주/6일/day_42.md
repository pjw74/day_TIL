## <u>1. airflow-day2-1</u>

- 1장 숙제 리뷰 + SQL 트랜잭션 1장 숙제를 같이 리뷰하면서 이해하기
- Contents

1. 1장 숙제 리뷰 + SQL 트랜잭션 이해하기
2. Airflow 설치
3. Airflow 기본 프로그램 실행

- 1장 숙제 - Python ETL 개선하기
- Colab 링크 -> 개선 버전

  - 데이터 웨어하우스에서 테이블 업데이트 방법은 크게 두 가지
    - Full Refresh
      - 단순해서 좋지만 데이터가 커지면 사용불가능
      - 이 숙제는 Full Refresh하는 예라고 보면 됨
    - Incremental Update
      - 데이터가 클 경우 효과적이지만 복잡도 증가
      - 보통 타임스탬프 혹은 일련 번호 등의 필드 필요
      - execution_date 활용

- DELETE FROM(조건 설정 가능, 트랜잭션 준수) vs. TRUNCATE(조건 설정 불가, 트랜잭션 무시)
- **트랜잭션**

  - 중간에 실패하면 불완전 상황에 놓이는 작업들이 있다면?
  - 아래 예에서 인출은 성공했지만 송금에서 문제가 생긴다면?

- Atomic하게 실행되어야 하는 SQL들을 묶어서 하나의 작업처럼 처리하는 방법

  - https://postgresql.kr/docs/9.2/tutorial-transactions.html
  - BEGIN과 END 혹은 BEGIN과 COMMIT 사이에 해당 SQL들을 사용
  - ROLLBACK은 BEGIN의 이전의 상태로 돌아가라는 SQL 명령

    ![this_screenshot](./img/1.PNG)

  - 이 과정 중의 SQL 결과는 임시 상태가 됨. 다른 세션에서는 커밋 전까지 보이지 않음
  - 트랜잭션에 들어가는 SQL을 최소화하는 것이 좋음
  - 위의 경우 auto commit을 사용하는 경우임

<br>

1장 숙제 - 트랜잭션 구현방법 (1)

- 두 가지 종류의 트랜잭션이 존재
  - 레코드 변경/삭제/추가를 바로 반영하는지 여부. autocommit이라는 파라미터로 조절가능
- autocommit=True
  - 기본적으로 모든 SQL statement가 바로 물리 테이블에 커밋됨
  - 이를 바꾸고 싶다면 BEGIN;END; 혹은 BEGIN;COMMIT을 사용 (혹은 ROLLBACK)
- autocommit=False
  - 기본적으로 모든 SQL statement가 커밋되지 않음. 즉 모두 스테이징 상태로 존재
  - 커넥션 객체의 .commit()과 .rollback()함수로 커밋할지 말지 결정

1장 숙제 - 트랜잭션 구현방법 (2)

- auto commit을 사용할 것인지 말지?
  - 이는 개인이나 팀의 선택
- Python의 경우 try/catch와 같이 사용하는 것이 일반적
  - try/catch로 에러가 나면 rollback을 명시적으로 실행. 에러가 안 나면 commit을 실행

불완전한 에러 처리의 위험성!

- except에서 raise를 호출하면 발생한 원래 exception이 위로 전파됨
  - ETL을 관리하는 입장에서 어떤 에러가 감춰지는 것보다는 명확하게 드러나는 것이 더 좋음
  - 위의 경우 cur.execute 뒤에 raise를 호출하는 것이 좋음

```python
try:
cur.execute(create_sql)
cur.execute("COMMIT;")
except Exception as e:
cur.execute("ROLLBACK;")

try:
cur.execute(create_sql)
cur.execute("COMMIT;")
except Exception as e:
cur.execute("ROLLBACK;")
raise
```

<br>
<br>
<br>

## <u>2. airflow-day2-2</u>

### Airflow 설치

Airflow 설치 방법

- 직접 설치하고 운영
  - 우리가 사용할 방법. 뒤에서 설명
- 클라우드 사용 (프로덕션 환경에서 선호됨)
  - AWS: MWAA (Managed Workflows for Apache Airflow) 사용
  - 구글 클라우드: Cloud Composer 사용
  - Microsoft Azure: Azure Data Factory에 Airflow DAGs 기능 존재

직접 설치 방법

1. 개인 랩탑에 도커 설치 후 Airflow 설치
2. AWS EC2 등의 리눅스 서버에 직접 설치
   a. 우분투 20.04 사용

우분투 20.04 사용

- AWS EC2 t3.small나 t3a.small 인스턴스를 사용할 예정
  - 2 CPU, 2 GB Memory, 8GB SSD Disk 사용
- AWS 계정 필요
  - 위 인스턴스 타입은 Free Tier가 아니기에 비용이 발생함을 인지
    - t3.small 인스턴스의 경우 한달 비용이 $18.72
    - t3a.small 인스턴스의 경우 한달 비용이 $16.85
  - **가능하면 실제 개발 실습은 Docker 환경을 사용하고 이 설치 과정은 그냥 시청**

리눅스 이해하기

- 우분투 (ubuntu): 리눅스 타입 중의 하나. 다른 타입은 데비안, 레드햇, 페도라, ...
- ssh: 리눅스 혹은 유닉스 서버에 로그인해주는 프로그램 (터미널)
  - private key와 public key를 사용
- sudo: 보통 슈퍼유저로서 프로그램을 구동할 수 있도록 하는 프로그램이다.
- apt-get: 우분투/데비안 계열의 리눅스에서 프로그램 설치/삭제를 관리해주는 -로그램
  - apt-get update, apt-get install
- su: substitue user의 약자로 현재 사용 중인 사용자 계정을 로그아웃하지 않고 다른 사용자의 권한을 얻을 때 사용한다
- vi: 텍스트 에디터. https://withcoding.com/112

Airflow 2.5.1 설치 과정 (github_feat.max)

- 최신 안정 버전을 찾아서 2.5.1을 적절히 변경해서 실행할 것!
- Airflow 메타데이터베이스로 로컬 서버에 Postgres를 설치할 예정
- Airflow는 /var/lib/airflow/ 밑에 설치됨
- Airflow 서버에 총 3개의 어카운트가 사용됨
  - ubuntu: 메인 어카운트
  - postgres: (postgres 설치시 만들어지는 계정)
    - 이 계정을 이용해 postgres 액세스를 위한 airflow 계정을 별도로 생성
  - airflow: Airflow용 어카운트. Airflow 서비스는 이 계정으로 실행됨

## <u>3. airflow-day2-3</u>

### Airflow 설치 - ec2

실습

- 설치 문서 참고
- AWS EC2 서버 론치
- Airflow 2.5.1 설치
- Airflow 웹 UI 접근
- 터미널 로그인 -> $ ssh -i airflow-dev.pem ubuntu@Public IPv4 DNS
- $ ls -tl airflow-dev.pem 해서 rw인지 확인
  -> (MAC os) $ chmod 600 airflow-dev.pem
  (Windows os) 해당 파일 속성에서 읽기전용으로 할 것

```bash
$ sudo apt-get update
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
$ sudo apt-get install -y python3-pip
$ sudo pip3 install pyopenssl --upgrade
```

Airflow 2.0을 설치하고 필요 기타 모듈을 설치

```bash
sudo apt-get install -y libmysqlclient-dev
sudo pip3 install --ignore-installed "apache-airflow[celery,amazon,mysql,postgres]==2.5.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.1/constraints-3.7.txt"
sudo pip3 install oauth2client gspread numpy pandas
```

airflow:airflow 계정 생성

```bash
sudo groupadd airflow
sudo useradd -s /bin/bash airflow -g airflow -d /var/lib/airflow -m
```

Airflow의 정보가 저장될 데이터베이스로 사용될 Postgres 설치

Postgres 설치

```bash
sudo apt-get install -y postgresql postgresql-contrib
```

Airflow가 Postgres를 접속할 때 사용할 계정을 Postgres위에서 생성

```bash
$ sudo su postgres
$ psql
# psql (10.12 (Ubuntu 10.12-0ubuntu0.18.04.1))
# Type "help" for help.

postgres=# CREATE USER airflow PASSWORD 'airflow';
CREATE ROLE
postgres=# CREATE DATABASE airflow;
CREATE DATABASE
postgres=# \q
$ exit
```

Postgres를 재시작

```bash
sudo service postgresql restart
```

Airflow 첫 번째 초기화

```bash
sudo su airflow
$ cd ~/
$ mkdir dags
$ AIRFLOW_HOME=/var/lib/airflow airflow db init
$ ls /var/lib/airflow
# airflow.cfg  airflow.db  dags   logs  unittests.cfg
```

<br>

- Airflow 환경 파일(/var/lib/airflow/airflow.cfg)을 편집하여 다음 2가지를 바꾼다
- "executor"를 SequentialExecutor에서 LocalExecutor로 수정한다
- DB 연결스트링("sql_alchemy_conn")을 앞서 설치한 Postgres로 바꾼다
  - 이 경우 ID와 PW와 데이터베이스 이름이 모두 airflow를 사용하고 호스트 이름은 localhost를 사용한다

```bash
$ vi airflow.cfg


[core]
...
executor = LocalExecutor
...

# 찾기: /database , 다음: n
[database]
...
sql_alchemy_conn = postgresql+psycopg2://airflow:airflow@localhost:5432/airflow
...
```

- Airflow를 재설정
  - airflow 사용자로 아래 명령을 수행해야 한다

```bash
$ AIRFLOW_HOME=/var/lib/airflow airflow db init

```

<br>

## Airflow 웹서버와 스케줄러 실행

---

Airflow 웹서버와 스케줄러를 백그라운드 서비스로 사용하려면 다음 명령을 따라하여 두 개를 서비스로 등록한다. \
다음 명령들은 ubuntu 계정에서 실행되어야한다. 만일 "[sudo] password for airflow: " 메시지가 나온다면 \
지금 airflow 계정을 사용하고 있다는 것으로 이 경우 "exit" 명령을 실행해서 ubuntu 계정으로 돌아온다

ubuntu 계정으로 아래를 수행

- 웹서버와 스케줄러를 각기 서비스로 등록

```bash
$ sudo vi /etc/systemd/system/airflow-webserver.service
```

```
[Unit]
Description=Airflow webserver
After=network.target

[Service]
Environment=AIRFLOW_HOME=/var/lib/airflow
User=airflow
Group=airflow
Type=simple
ExecStart=/usr/local/bin/airflow webserver -p 8080
Restart=on-failure
RestartSec=10s

[Install]
WantedBy=multi-user.target
```

```bash
$ sudo vi /etc/systemd/system/airflow-scheduler.service
```

```
[Unit]
Description=Airflow scheduler
After=network.target

[Service]
Environment=AIRFLOW_HOME=/var/lib/airflow
User=airflow
Group=airflow
Type=simple
ExecStart=/usr/local/bin/airflow scheduler
Restart=on-failure
RestartSec=10s

[Install]
WantedBy=multi-user.target
```

<br>

- 다음 명령을 실행하여 앞서 서비스들을 활성화 한다

```bash
$ sudo systemctl daemon-reload
$ sudo systemctl enable airflow-webserver
$ sudo systemctl enable airflow-scheduler
```

- 서비스들을 시작한다:

```bash
$ sudo systemctl start airflow-webserver
$ sudo systemctl start airflow-scheduler
```

- 서비스들의 상태를 보고 싶다면 다음 명령을 실행한다:

```bash
$ sudo systemctl status airflow-webserver
# 빠져나오기: 소문자 q
$ sudo systemctl status airflow-scheduler
```

<br>

## 마지막으로 Airflow webserver에 로그인 어카운트를 생성한다

---

이는 airflow계정에서 실행되어야 한다. password의 값을 적당히 다른 값으로 바꾼다

```bash
sudo su airflow
AIRFLOW_HOME=/var/lib/airflow airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin4321
```

만일 실수로 위의 명령을 ubuntu 어카운트에서 실행했다면 admin 계정을 먼저 지워야한다. 지울 때 아래 명령을 사용한다

```bash

AIRFLOW_HOME=/var/lib/airflow airflow users delete --username admin
```

그리고나서 본인 서버를 웹브라우저에서 포트번호 8080을 이용해 접근해보면 아래와 같은 로그인 화면이 실행되어야 한다. \
예를 들어 본인 EC2 서버의 호스트 이름이 ec2-xxxx.us-west-2.compute.amazonaws.com이라면 http://ec2-xxxx.us-west-2.compute.amazonaws.com:8080/을 웹브라우저에서 방문해본다. \
기본적으로 Airflow 연결은 https (SSL)이 아닌데 이를 변경하고 싶다면 https://airflow.apache.org/docs/apache-airflow/1.10.1/security.html?highlight=celery#ssl 참고.

## 이 Github repo를 클론해서 dags 폴더에 있는 DAG들을 /var/lib/airflow/dags로 복사

---

keeyong/airflow-setup repository에 있는 dags 폴더의 내용을 /var/lib/airflow/dags로 복사한다.

```bash
sudo su airflow
cd ~/
git clone https://github.com/keeyong/airflow-setup.git
cp -r airflow-setup/dags/* dags
```

## 이 Github repo의 업데이트가 필요한 경우

---

```bash
sudo su airflow
cd ~/airflow-setup
git pull
cd ..
cp -r airflow-setup/dags/* dags
```

<br>

그리고나서 Airflow 웹서버를 다시 방문해보면 (이 설치 작업을 한 시점에 따라) DAG들이 몇개 보이고 일부 에러도 몇개 보일 수 있다. 이 에러들은 나중에 하나씩 해결한다.

단 여기서 복사한 DAG들이 웹 서버에 나타나는데 시간이 좀 걸릴 수 있는데 그 이유는 Airflow가 기본적으로 5분 마다 한번씩 dags 폴더를 뒤져서 새로운 DAG이 있는지 보기 때문이다. \
이 변수는 dag_dir_list_interval으로 airflow.cfg에서 확인할 수 있으며 기본값은 300초 (5분)이다.

<br>

## Bash 파일(/var/lib/airflow/.bashrc)을 편집

---

airflow 사용자로 로그인시 (sudo su airflow등)

AIRFLOW_HOME 환경변수가 자동설정되게 한다

```bash
airflow@ip-172-31-54-137:~$ vi ~/.bashrc
```

이 파일의 마지막에 다음 3개의 라인을 추가한다:

- i를 누르면 편집모드로 들어간다 (ESC 키를 누르면 명령 모드로 들어간다)
- 파일을 저장하고 나오려면 명령 모드에서 콜론(:)을 누르고 wq!를 입력한다

```bash
AIRFLOW_HOME=/var/lib/airflow
export AIRFLOW_HOME
cd ~/
```

exit을 실행하여 ubuntu 사용자로 나온 다음에 다시 airflow 사용자로 로그인하면 (sudo su airflow) 자동으로 홈디렉토리로 이동하고 AIRFLOW_HOME 환경변수가 설정되어 있음을 확인할 수 있다.

```bash
ubuntu@ip-172-31-54-137:~$ sudo su airflow
airflow@ip-172-31-54-137:~/$ pwd
/var/lib/airflow
airflow@ip-172-31-54-137:~/$ echo $AIRFLOW_HOME
/var/lib/airflow
```

<br>
<br>
<br>

## <u>4. airflow-day2-4</u>

### Airflow 설치 - Docker

[git 설명서]

<br>
<br>
<br>

## <u>5. airflow-day2-5</u>

### Airflow 기본 프로그램 실행

- DAG 설정 예제 (1)

  ![this_screenshot](./img/2.PNG)

<br>

- 여기에 지정되는 인자들은 모든 태스크들에 공통으로 적용되는 설정이 됨
- 뒤에서 DAG 객체를 만들 때 지정함

- DAG 설정 예제 (2)

  ![this_screenshot](./img/3.PNG)

- start_date and end_date specify when this dag starts and stops:
  - can be used to do one-off backfilling
  - **catchup**의 의미를 이해하는 것이 중요 \
    (default: True 과거 데이터 다 불러옴)
- Schedule interval can be defined as cron expression or presets as follows:
  - None, @once, @hourly, @daily, @weekly, @monthly, @yearly

<br>

Bash Operator를 사용한 예제 (1)

- 3개의 태스크로 구성
- t1은 현재 시간 출력
- t2는 5초간 대기 후 종료
- t3는 서버의 /tmp 디렉토리의 내용 출력
- t1이 끝나고 t2와 t3를 병렬로 실행

  ![this_screenshot](./img/4.PNG)

<br>

How to Trigger a DAG - 터미널에서 실행

- 먼저 Airflow 서버에 로그인하고 다음 명령 실행
- airflow dags list
- airflow tasks list DAG이름
- airflow tasks test DAG이름 Task이름 날짜 # test vs. run
  - 날짜는 YYYY-MM-DD
    - start_date보다 과거인 경우는 실행이 되지만 오늘 날짜보다 미래인 경우 실행 안됨
    - 이게 바로 execution_date의 값이 됨 (execution_date은 나중에 설명)

<br>

데모

- 웹 UI 살펴보기
- 터미널로 연결해서 커맨드라인 툴 사용해보기 (EC2와 Docker 버전 모두)
- airflow dags list
- airflow tasks list dag_v1
- airflow tasks test dag_v1 ls 2020-08-09
- airflow dags test dag_v1 2019-12-08
- airflow dags backfill dag_v1 -s 2019-01-01 -e 2019-12-31

- Docker 명령어

```bash
$ docker ps
# $ docker ps -a
$ docker exec -it [CONTAINER ID] sh
$ airflow dags list
$







































<br>
<br>
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

### **Summary**:

<br>
<br>
<br>
<br>
<br>
<br>

## 팀 미팅

8주차 팀 미팅

**Agenda**

- 건의 사항
- QnA
- 미니 세미나 - AWS 전반적인 내용 (EC2, VPC, Security, DB, Monitoring, Storage)
- 팀원 소감

  - 프로젝트 진행 후기
  - **Airflow** 필수
  - raw_data의 중요성

- 데이터

  - 공공 데이터 조회를 위한 오픈소스 파이썬 라이브러리 Github 추천
  - 호락호락하지 않은 공공데이터와의 전쟁 유튭

- QnA

  - 2팀 2조: Github 레포 푸쉬

- Team Rule 개선
- [미니세미나] AWS Network

  - AWS Network - VPC, Subnet, Endpoint, ...
  - VPC - public 차이 ??
    - 사용자가 정의한, 논리적으로 격리된 가상의 프라이빗 네트워크 환경
  - VPC 서브넷
  - Internet gateway 만들고 라우팅 테이블에 타겟팅 경로 설정
  - 프라이빗 서브넷 / 퍼블릭 서브넷: Igw 연결 유무
  - NAT gateway: private 서버에서 나가고 싶다. ip 치환 외부 나감, 외부에선 private 서버 접근 불가능
  - 고정 IP/Public IP 선택
  - VPC 액세스 제어: NACL과 보안그룹
  - VPC Peering 기술
  - AWS Direct Connect
  - EndPoint 타입 종류

- 미니세미나 다음 주제
- 코드리뷰 세미나 질문
```
