## <u>1강. Day 1-0</u>

- 과정 소개

1. 다양한 데이터 웨어하우스 옵션
2. Redshift 소개와 기능 소개
3. Redshift 설치와 고급 기능 소개
4. Snowflake 설치와 관리
5. 대시보드 옵션 리뷰와 데이터 웨어하우스의 미래/트랜드

<br>
<br>
<br>

## <u>2강. Day 1-1</u>

- Contents

1. 데이터 팀의 역할
2. 데이터 조직 구성원
3. 데이터 웨어하우스와 ETL/ELT
4. 데이터 웨어하우스 옵션들
5. 실리콘밸리 회사들의 데이터 스택 트랜드

- 비전, 회사의 발전/성장에 어떻게 기여??

  - 신뢰할 수 있는 데이터 바탕으로 부가 가치 생성
  - 데이터 직접 매출x, 간접 매출o

- **데이터 조직이 하는 일(1)**

  - **결정과학(Decision Science)**
  - 고품질 데이터 기반으로 의사 결정권자에게 입력 제공
  - 데이터를 고려한(data informed) 결정 vs 데이터 기반(data driven) 결정
  - 데이터 기반 지표 정의, 대시보드와 리포트 생성 등 수행

- **데이터 조직이 하는 일(2)**

  - **Product Science**
  - 사용자 서비스 경험 개선 or 프로세스 최적화
    - ML 알고리즘을 통해 개인화를 바탕으로 한 추천과 검색 기능 제공
  - 공장이라면 공정 과정에서 오류를 최소화

- 데이터의 흐름과 데이터 팀의 발전 단계

  - 이상적:
    1. 데이터 인프라 구축 ->
    2. 데이터 분석(지표 정의, 시각화, ...) ->
    3. 데이터 과학 적용(사용자 경험 개선(추천, 검색 등의 개인화, ...))

  1. 인프라

  - 서비스에서 직접 생기는 데이터와 써드파티를 통해 생기는 간접 데이터
  - 데이터 인프라: ETL -> 데이터 웨어하우스

- 프로덕션 데이터베이스 vs 데이터 웨어하우스

  - OLTP: Online **Transaction** Processing(프로덕션)
  - OLAP: Online **Analytical** Processing(DW)

- **ETL(Extract, Transform, Load)** 이란? (1)

  - 다른 곳에 존재하는 데이터를 가져다가 데이터 웨어하우스에 로드하는 작업

    - Extract: 외부 데이터 소스에서 데이터를 추출
    - Transform: 데이터의 포맷을 원하는 형태로 변환
    - Load: 변환된 데이터를 최종적으로 데이터 웨어하우스로 적재
    - 데이터 파이프라인이라고 부르기도 함

  - 관련하여 가장 많이 쓰이는 프로임웍은 **Airflow**

    - 오픈소스 프로젝트, 파이썬 3 기반, Airbnb에서 시작
    - AWS, 구글 클라우드에서도 지원

  - ETL 관련 **SaaS**(Software as a Service) 출현하기 시작
    - 흔한 데이터 소스의 경우 FiveTran, Stitch Data와 같은 SaaS를 사용하는 것도 가능

- **시각화 대시보드** 란?

  - 보통 중요한 지표를 시간의 흐름과 함께 보여주는 것이 일반적
    - 지표의 경우 3A(Accessible, Actionable, Auditable)가 중요
    - 중요 지표의 예: 매출액, 월간/주간 액티브 사용자수, ...
  - 가장 널리 사용되는 대시보드:
    - 구글 클라우드의 룩커(Looker)
    - 세일즈포스의 태블로(Tableau)
    - 마이크로소프트의 파워 BI(Power BI)
    - 오픈소스 아파치 수퍼셋(Superset)

- 머신 러닝(Machine Learning)이란?
  - (프로그래밍 없이) 배움이 가능한 알고리즘 -> 블랙박스
    - 'A field of study that gives computers the ability to learn \
      without being explicitly programmed'(Arthur Samuel)
  - 데이터로부터 패턴을 찾아 학습
    - 데이터의 품질과 크기가 중요
    - 데이터로 인한 왜곡(bias) 발생 가능
      - AI 윤리
    - 내부동작 설명 가능 여부도 중요
      - ML Explainability

<br>
<br>
<br>

## <u>3강. Day 1-2</u>

- 데이터 팀에는 누가 있는가?

  - 데이터 엔지니어(Data Engineer)
    - 데이터 인프라(데이터 웨어하우스와 ETL) 구축
  - 데이터 분석가(Data Analyst)
    - 데이터 웨어하우스의 데이터를 기반으로 지표를 만들고 시각화(대시보드)
    - 내부 직원들의 데이터 관련 질문 응답
  - 데이터 과학자(Data Scientist)
    - 과거 데이터를 기반으로 미래를 예측하는 머신러닝 모델을 만들어 \
      고객들의 서비스 경험을 개선(개인화 혹은 자동화 혹은 최적화)

- 데이터 엔지니어의 역할

  - 기본적으로 SW 엔지니어
    - 파이썬이 대세, 자바 혹은 스칼라와 같은 언어도 아는 것이 좋다.
  - 데이터 웨어하우스 구축
    - 데이터 웨어하우스를 만들고 이를 관리. 클라우드로 가는 것이 추세
      - AWS의 Redshift, 구글클라우드의 BigQuery, 스노우플레이크
    - 관련해서 중요한 작업중의 하나는 ETL 코드 작성, 주기적으로 실행
      - ETL 스케줄러 혹은 프레임웍이 필요(Airflow라는 오픈소스가 대세)
  - 데이터 분석가와 과학자 지원
    - 데이터 분석가, 데이터 과학자들과의 협업을 통해 필요한 툴이나 데이터를 \
      제공해주는 것이 데이터 엔지니어의 중요한 역할 중의 하나

- 데이터 엔지니어가 알아야하는 기술(1)

  - SQL: 기본 SQL, Hive, Presto, SparkSQL, ...
  - 프로그래밍 언어: 파이썬, 스칼라, 자바
  - 데이터 웨어하우스
    - Redshift/Snowflake/BigQuery
  - ELT/ELT 프레임웍: Airflow, ...
  - 대용량 데이터 처리 플랫폼: Spark/YARN

- 데이터 엔지니어가 알아야하는 기술(2)

  - 컨테이너 기술: Docker/K8s
  - 클라우드 컴퓨팅
    - AWS, GCP, Azure
  - 도움이 되는 기타 지식
    - 머신 러닝 일반
    - A/B 테스트, 통계
  - 데이터 엔지니어 스킬 로드맵
    - https://github.com/datastacktv/data-engineer-roadmap
    - MLOps 혹은 ML Engineer가 다음 스텝이 많이 됨

- 데이터 분석가의 역할

  - 비지니스 인텔리전스를 책임짐
    - 중요 지표를 정의하고 이를 대시보드 형태로 시각화
      - 대시보드로는 태블로(Tableau)와 룩커(Looker)등의 툴이 가장 흔히 사용됨
      - 오픈소스로는 수퍼셋(Superset)이 많이 사용됨
    - 비지니스 도메인에 대한 깊은 지식이 필요함
  - 회사내 다른 팀들의 데이터 관련 질문 대답
    - 임원, 팀리드들이 데이터 기반 결정 내릴 수 있도록 도와줌
    - 질문들이 굉장히 많고 반복적이기 때문에 어떻게 **셀프서비스**로 만들 수 있느냐가 관건

- 데이터 분석가가 알아야하는 기술

  - SQL: 기본 SQL, Hive, Presto, SparkSQL, ...
  - 대시보드
    - 룩커, 태블로, 파워 BI, 수퍼셋
    - 엑셀, 구글 스프레드시트, 파이썬
  - 데이터 모델링
  - 통계 지식
    - AB테스트 분석 혹은 다양한 데이터 분석에서 통계 지식은 아주 유용함
  - 좋은 지표를 정의하는 능력
  - 보통 코딩을 하지는 않음

- MLOps란 무슨 일을 하는가?

  - DevOps가 하는 일은?
    - 개발자가 만든 코드를 시스템에 반영하는 프로세스(CI/CD, deployment)
    - 시스템이 제대로 동작하는지 모니터링 그리고 이슈 감지시 escalation 프로세스
      - On-call 프로세스
  - MLOps가 하는 일은?
    - 앞의 DevOps가 하는 일과 동일. 차이점은 서비스 코드가 아니라 ML모델이 대상
    - 모델을 계속적으로 빌딩하고 배포하고 성능을 모니터링
      - ML모델 빌딩과 프로덕션 배포를 자동화할 수 있을까? 계속적인 모델 빌딩(CT)과 배포!
      - 모델 서빙 환경과 모델의 성능 저하를 모니터링하고 필요시 escalation 프로세스 진행

- MLOps 엔지니어가 알아야 하는 기술

  - 데이터 엔지니어가 알아야 하는 기술
    - 파이썬/스칼라/자바
    - 데이터 파이프라인과 데이터 웨어하우스
  - DevOps 엔지니어가 알아야 하는 기술
    - CI/CD, 서비스 모니터링, ...
    - 컨테이너 기술(K8S, 도커)
    - 클라우드(AWS,GCP,Azure)
  - 머신러닝 관련 경험/지식
    - 머신러닝 모델 빌딩과 배포
    - ML 모델 빌딩 프레임웍 경험
      - SageMaker, Kubeflow, MLflow

- 프라이버시 엔지니어

  - 전체 시스템에서 개인정보 보호를 위한 가이드라인/툴을 제공
  - 이는 데이터 시스템에서 더욱 중요
  - 개인 정보 보호 법안의 징벌 조항이 점점 강화되는 추세
    - GDPR, HIPAA, CCPR

- 데이터 디스커버리(Data Discovery)란?
  - 별도 직군은 아니지만 데이터 팀이 커지면 꼭 필요한 서비스
  - 데이터가 커지면 테이블과 대시보드 수 증가!
    - 정보 과잉 문제가 심해지는 악순환!
    - 주기적인 테이블과 대시보드 클린업이 필수!
  - 테이블과 대시보드 관련 검색 서비스!
    - https://www.amundsen.io/
    - https://github.com/datahub-project/datahub
    - https://www.selectstar.com/

<br>
<br>
<br>

## <u>4강. Day 1-3</u>

- 데이터 웨어하우스 옵션별 장단점

  - 데이터 웨어하우스는 기본적으로 클라우드가 대세
  - 데이터가 커져도 문제가 없는 확장가능성(Scalable)과 적정한 비용이 중요한 포인트
  - Redshift 고정비용 옵션, BigQuery, Snowflake 가변비용
  - 오픈소스 기반(Presto, Hive)을 사용하는 경우도 클라우드 버전 존재
  - 데이터가 작다면 굳이 빅데이터 기반 데이터베이스 사용할 필요 x

- 데이터 레이크
  - 구조화 데이터 + 비구조화 데이터(로그 파일)
  - 보존 기한이 없는 모든 데이터를 원래 형태대로 보존하는 스토리지에 가까움
  - 보통은 데이터 웨어하우스보다 몇 배는 더 크고 더 경제적인 스토리지
  - 보통 클라우드 스토리지가 됨
    - AWS라면 S3가 대표적인 데이터 레이크라 볼 수 있음
  - 데이터 레이크와 데이터 웨어하우스 바깥에서 안으로 데이터를 가져옴: ETL
  - 데이터 레이크와 데이터 웨어하우스 안에 있는 데이터를 처리: ETL

◆ Airflow (ETL 스케줄러) 소개

- ETL 관리 및 운영 프레임웍의 필요성
  - 다수의 ETL이 존재할 경우 이를 스케줄해주고 이들간의 의존관계(dependency)를 \
    정의해주는 기능 필요
  - 특정 ETL이 실패할 경우 이에 관한 에러 메세지를 받고 \
    재실행해주는 기능도 중요해짐 (Backfill)
- 가장 많이 사용되는 프레임웍은 Airflow

  - Airflow는 오픈소스 프로젝트로 파이썬 3 기반이며 에어비앤비, 우버, 리프트, 쿠팡등에서 사용
    - AWS와 구글클라우드와 Azure에서도 지원
  - Airflow에서는 ETL을 DAG라 부르며 웹 인터페이스를 통한 관리 기능 제공
  - 크게 3가지 컴포넌트로 구성됨: 스케줄러, 웹서버, 워커 (Worker)

- **ELT**

  - ETL: 데이터를 데이터 웨어하우스 외부에서 내부로 가져오는 프로세스
  - ELT: 데이터 웨어하우스 내부 데이터를 조작해서 (보통은 좀더 추상화되고
    요약된) \
     새로운 데이터를 만드는 프로세스 - 이런 프로세스 전용 기술들이 있으며 dbt가 가장 유명: Analytics Engineering

- **빅데이터 처리 프레임웍**

  - 분산 환경 기반 (1대 혹은 그 이상의 서버로 구성)
    - 분산 파일 시스템과 분산 컴퓨팅 시스템이 필요
  - Fault Tolerance
    - 소수의 서버가 고장나도 동작해야함
  - 확장이 용이해야함
    - Scale Out이 되어야함

- 대표적 빅데이터 프로세싱 시스템
  - 1 세대 -> 하둡 기반의 Mapreduce, Hive/Presto
  - 2 세대 -> Spark (SQL, DataFrame, Streaming, ML, Graph)

<br>
<br>
<br>

## <u>5강. Day 1-4</u>

### 데이터 웨어하우스 옵션들

- 살펴볼 옵션들

  - AWS Redshift
  - Snowflake
  - Google Cloud BigQuery
  - Apache Hive
  - Apache Presto
  - Apache Iceberg
  - Apache Spark

- 이 옵션들의 공통점은?

  - Iceberg를 제외하고는 모두 **SQL을** 지원하는 **빅데이터** 기반 데이터베이스

- **AWS Redshift**

  - 2012년에 시작된 AWS 기반의 데이터웨어하우스로 PB 스케일 데이터 분산처리 가능
    - Postgresql과 호환되는 SQL로 처리 가능하게 해줌
    - Python UDF (User Defined Function)의 작성을 통해 기능 확장 가능
    - 처음에는 고정비용 모델로 시작했으나 이제는 가변비용 모델도 지원 (Redshift Serverless)
    - 온디맨드 가격 이외에도 예약 가격 옵션도 지원
  - CSV, JSON, Avro, Parquet 등과 같은 다양한 데이터 포맷을 지원
  - AWS내의 다른 서비스들과 연동이 쉬움
    - S3, DynamoDB, SageMaker 등등
  - 배치 데이터 중심이지만 실시간 데이터 처리 지원
  - 웹 콘솔 이외에도 API를 통한 관리/제어 가능

- **Snowflake**

  - 2014년에 클라우드 기반 데이터웨어하우스로 시작됨 (2020년 상장)
    - 지금은 데이터 클라우드라고 부를 수 있을 정도로 발전
    - 데이터 판매를 통한 매출을 가능하게 해주는 Data Sharing/Marketplace 제공
    - ETL과 다양한 데이터 통합 기능 제공
  - SQL 기반으로 빅데이터 저장, 처리, 분석을 가능하게 해줌
    - 비구조화된 데이터 처리와 머신러닝 기능 제공
  - CSV, JSON, Avro, Parquet 등과 같은 다양한 데이터 포맷을 지원
    - S3, GC 클라우드 스토리지, Azure Blog Storage도 지원
  - 배치 데이터 중심이지만 실시간 데이터 처리 지원
  - 웹 콘솔 이외에도 API를 통한 관리/제어 가능

- **Google Cloud Bigquery**

  - 2010년에 시작된 구글 클라우드의 데이터 웨어하우스 서비스
    - 구글 클라우드의 대표적인 서비스
    - BigQuery SQL이란 SQL로 데이터 처리 가능 (Nested fields, repeated fields 지원)
    - 가변 비용과 고정 비용 옵션 지원
  - CSV, JSON, Avro, Parquet 등과 같은 다양한 데이터 포맷을 지원
  - 구글 클라우드 내의 다른 서비스들과 연동이 쉬움
    - 클라우드 스토리지, 데이터플로우, AutoML 등등
  - 배치 데이터 중심이지만 실시간 데이터 처리 지원
  - 웹 콘솔 이외에도 API를 통한 관리/제어 가능

- **Apache Hive**

  - Facebook이 2008년에 시작한 아파치 오픈소스 프로젝트
  - 하둡 기반으로 동작하는 SQL 기반 데이터 웨어하우스 서비스
    - HiveQL이라 부르는 SQL 지원
    - MapReduce위에서 동작하는 버전과 Apache Tez를 실행 엔진으로 동작하는 버전 두 가지가 존재
    - 다른 하둡 기반 오픈소스들과 연동이 쉬움 (Spark, HBase 등등)
    - 자바나 파이썬으로 UDF 작성 가능
  - CSV, JSON, Avro, Parquet 등과 같은 다양한 데이터 포맷을 지원
  - 배치 빅데이터 프로세싱 시스템
    - 데이터 파티셔닝과 버킷팅과 같은 최적화 작업 지원
    - 빠른 처리속도 보다는 처리할 수 있는 데이터 양의 크기에 최적화
  - 웹 UI와 커맨드라인 UI (CLI라고 부름) 두 가지를 지원
  - 점점 Spark에 의해 밀리는 분위기임

- **Apache Presto**

  - Facebook이 2013년에 시작한 아파치 오픈소스 프로젝트
  - 다양한 데이터소스에 존재하는 데이터를 대상으로 SQL 실행 가능
    - HDFS (Hadoop Distributed File System), S3, Cassandra, MySQL 등등
    - PrestoSQL이란 부르는 SQL 지원
  - CSV, JSON, Avro, ORC, Parquet 등과 같은 다양한 데이터 포맷을 지원
  - 배치 빅데이터 프로세싱 시스템
    - Hive와는 다르게 빠른 응답 속도에 좀더 최적화 (메모리 기반)
  - 웹 UI와 커맨드라인 UI (CLI라고 부름) 두 가지를 지원
  - AWS Athena가 바로 Presto를 기반으로 만들어짐

- **Apache Iceberg**

  - Netflix가 2018년에 시작한 아파치 오픈소스 프로젝트로 데이터 웨어하우스
    기술이 아님
  - 대용량 SCD (Slowly-Changing Datasets) 데이터를 다룰 수 있는 테이블 포맷
    - HDFS, S3, Azure Blob Storage 등의 클라우드 스토리지 지원
    - ACID 트랙잭션과 타임여행 (과거 버전으로 롤백과 변경 기록 유지 등등)
    - 스키마 진화 (Schema Evolution) 지원을 통한 컬럼 제거와 추가 가능 (테이블 재작성 없이)
  - 자바와 파이썬 API를 지원
  - Spark, Flink, Hive, Hudi 등의 다른 Apache 시스템과 연동 가능

- **Apache Spark**

  - UC 버클리 AMPLab이 2013년에 시작한 아파치 오픈소스 프로젝트
  - 빅데이터 처리 관련 종합선물세트
    - 배치처리(API/SQL), 실시간처리, 그래프처리, 머신러닝 기능 제공
  - 다양한 분산처리 시스템 지원
    - 하둡(YARN), AWS EMR, Google Cloud Dataproc, Mesos, K8s 등등
  - 다양한 파일시스템과 연동 가능
    - HDFS, S3, Cassandra, HBase 등등
  - CSV, JSON, Avro, ORC, Parquet 등과 같은 다양한 데이터 포맷을 지원
  - 다양한 언어 지원: 자바, 파이썬, 스칼라, R

<br>
<br>
<br>

## <u>6강. Day 1-5</u>

### 실리콘밸리 회사들의 데이터 스택 살펴보기

- 데이터 플랫폼의 발전단계

  - 초기 단계: 데이터 웨어하우스 + ETL
    - 이미 앞에서 살펴봄
  - 발전 단계: 데이터 양 증가
    - Spark과 같은 빅데이터 처리시스템 도입
    - 데이터 레이크 도입
  - 성숙 단계: 데이터 활용 증대
    - 현업단의 데이터 활용이 가속화
    - ELT 단이 더 중요해지면서 dbt 등의 analytics engineering 도입
    - MLOps 등 머신러닝 관련 효율성 증대 노력 증대

- 발전 단계:
  - 데이터 소스 -> 데이터 파이프라인 -> 데이터 웨어하우스
  - 데이터 소스 -> 데이터 파이프라인 -> 데이터 레이크
  - 데이터 레이크 -> 데이터 파이프라인 -> 데이터 웨어하우스
    - 이때 Spark/Hadoop 등이 사용됨
    - Hadoop: Hive/Presto등이 기반됨

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

### 특강: [유데미 데이터 거버넌스 여정, ] (feat. max)

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
<br>
<br>
<br>
<br>
<br>
