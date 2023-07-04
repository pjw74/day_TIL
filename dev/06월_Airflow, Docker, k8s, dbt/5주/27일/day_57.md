## <u>3차 프로젝트 1일차</u>

### Crontab -> airflow Dags 작성

gcp -> instance1 -> ssh -> docker ps \
docker exec -it <your_airflow_container_id> sh \
docker exec -u root -it <your_airflow_container_id> sh

<br>

dags 폴더: \
/root/learn-airflow/dags/dags

<br>

[파일 이동] \
mv file1.txt backup/

<br>

[ssh키로 접근] \
ssh -i <key_pwd> <id>@<해당 인스턴스 외부 ip>

<br>

[파일 복사] \
cp [source] [destination] \
cp file1.txt copy/

디렉토리를 재귀적으로 복사하려면 -r 옵션 \
cp -r [source_directory] [destination_directory]

<br>

Vi 에디터는

- 명령 모드(command mode),
- 입력 모드(insert mode),
- Visual 모드 등 여러 가지 모드를 사용하는데, 명령 모드에서는 Vi의 명령어들을 사용해야 합니다.

[Vi 에디터 사용에 있어 기본적인 명령어]

- 입력 모드로 전환: 편집하려는 위치에서 i 를 누르면, 입력 모드로 전환되어 텍스트 입력이 가능합니다.

- 명령 모드로 전환: 입력 모드에서는 esc 키를 누르면 명령 모드로 되돌아갑니다.

- 저장 및 종료: 명령 모드에서 :wq 를 입력하고 엔터를 누르면 변경사항을 저장한 후 종료됩니다.

- 저장하지 않고 종료: 명령 모드에서 :q! 를 입력하고 엔터를 누르면 변경사항을 저장하지 않고 종료됩니다.

- 검색: 명령 모드에서 /검색어를 입력하고 엔터를 누르면 해당 검색어를 찾습니다. n 과 N 을 사용하여 검색 결과를 탐색합니다.

- Vi 에디터에서 명령을 취소하려면, 주로 입력 모드에서 되돌리는 방법을 사용합니다.

- 입력 모드에서 문자를 지우려면 Backspace 키 또는 Ctrl + h 를 사용하여 이전 문자를 지울 수 있습니다.

- 명령 모드에서 가장 최근의 명령을 취소하려면 u를 누릅니다.

- 일반적으로 nano 에디터나 다양한 기능을 갖춘 vim 에디터를 사용하면 명령어 입력에 있어 더 다양한 옵션과 편리한 기능을 사용할 수 있습니다.

<br>

docker-compose up --build 명령 # 생략

scheduler에서 exec -it 에서 pip3 install [모듈]

<br>

[로그 확인] \
/learn-airflow/dags/logs/scheduler/

[CLI 테스트]

airflow tasks test <dag_id> <task_id> <execution_date>

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
