## <u>1. streaming-day4-1-Kafka-Cli-Tools</u>

### 4. Kafka 기본 프로그래밍

Contents

1. Client tool 사용
2. Topic 파라미터 설정
3. Consumer 옵션 살펴보기
4. ksqlDB 사용해보기
5. 숙제

<br>

### Client Tool 사용

Kafka CLI Tools 접근 방법

- docker ps를 통해 Broker의 Container ID 혹은 Container 이름 파악
- 해당 컨테이너로 로그인
  - docker exec -it Broker_Container_ID sh
- 거기서 다양한 kafka 관련 클라이언트 툴을 사용 가능
  - kafka-topics
  - kafka-configs
  - kafka-console-consumer
  - kafka-console-producer
  - …

<br>

```sh
# kafka-topics

$ kafka-topics --bootstrap-server kafka1:9092 --list
$ kafka-topics --bootstrap-server kafka1:9092 --delete --topic topic_test


# kafka-console-producer
# Command line을 통해 Topic 만들고 Message 생성 가능

$ kafka-console-producer --bootstrap-server kafka1:9092 --topic test_console


# kafka-console-consumer
# Command line을 통해 Topic에서 Message 읽기 가능
# --from-beginning 옵션이 있으면 처음부터 읽음 (earliest). 아니면 latest로 동작

$ kafka-console-consumer --bootstrap-server kafka1:9092 --topic test_console --from-beginning


# 두 Console 프로세스들의 Side-by-side 실행
# 터미널을 하나 열고 동일 Broker 로그인 후 console-producer로 메세지 발생

```

### Kafka CLI Tools 데모:

```sh
$ clear -> ctrl + l
```

<br>
<br>
<br>

## <u>2. streaming-day4-2-Kakfa-Topic</u>

### Topic 파라미터 설정

Topic 생성시 다수의 Partition이나 Replica를 주려면

- 먼저 KafkaAdminClient 오브젝트를 생성하고 create_topics 함수로 Topic을 추가
- create_topics의 인자로는 NewTopic 클래스의 오브젝트를 지정

```python

client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
topic = NewTopic(
  name=name,
  num_partitions=partitions,
  replication_factor=replica)
client.create_topics([topic])
```

<br>

NewTopic 클래스

| 파라미터           | 의미             | 기본 값 |
| ------------------ | ---------------- | ------- |
| name               | Topic의 이름     |         |
| num_partitions     | Partition의 수   | 1       |
| replication_factor | Replication의 수 | 1       |

<br>

KafkaProducer 파라미터

| 파라미터                             | 의미                                                                                                               | 기본 값                  |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| bootstrap_servers                    | 메세지를 보낼 때 사용할 브로커 리스트 (host:port)                                                                  | localhost:9092           |
| client_id                            | Kafka Producer의 이름                                                                                              | 'kafka-python-{version}' |
| key_serializer, value_serializer     | 메세지의 키와 값의 serialize 방법 지정 (함수)                                                                      |                          |
| enable_idempotence                   | 중복 메세지 전송을 막을 것인지?                                                                                    | False (안 막음)          |
| acks: 0, 1, ‘all’                    | consistency level. 0: 바로 리턴. 1: 리더에 쓰일 때까지 대기. ‘all’: 모든 partition leader/follower에 적용까지 대기 | 0                        |
| retries                              | 메세지 실패시 재시도 회수                                                                                          | 2147483647               |
| delivery.timeout.ms                  | 메세지 전송 최대 시간                                                                                              | 120000ms                 |
| linger_ms, batch_size                | Replication의 수                                                                                                   | 1                        |
| max_in_flight_request_per_connection | 다수의 메세지를 동시에 보내기 위함 (배치 전송)                                                                     | 1                        |
| replication_factor                   | Replication의 수                                                                                                   | 1                        |
| replication_factor                   | Replication의 수                                                                                                   | 1                        |
| replication_factor                   | Replication의 수                                                                                                   | 1                        |

파라미터

bootstrap_servers

client_id

key_serializer, value_serializer

enable_idempotence

acks: 0, 1, ‘all’

retries
delivery.timeout.ms

linger_ms, batch_size

max_in_flight_request_per_connection

<br>

### 데모: CLI:

- Topic 생성 데모

<br>
<br>
<br>

## <u>1. Spark 데이터 처리</u>

### Spark 데이터 처리

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
