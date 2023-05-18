## <u>01 AWS CLI</u>

---

- AWS 명령줄 인터페이스: 콘솔 명령어를 이용. 명령 쉘 인터페이스
- aws configure를 통한 빠른 구성
  - IAM 사용자 추가 -> 보안 자격 증명 -> 액세스 키

### 실습: AWS CLI

- s3 fullaccess 권한 추가 후 aws s3 mb s3://citron-profiles
  -> asw s3 ls로 확인

- 파일 업로드 명령어: 파일 있는 폴더로 이동 -> aws s3 sync . s3://citron-profiles
  - 파일 삭제 명령어: aws s3 rm s3://citron-profiles --recursive(하위 폴더 삭제 옵션)

<br>
<br>
<br>

## <u>04 콘솔접속</u>

### 실습: AWS CLI

- 예) Citronapp-env: beanstalk(private)
  bastonhost: (public)

- public 서브넷 접속: ssh -i myjoo.pem ec2-user@[ip]
- private 서브넷 접속:
  1. vi myjoo.pem로 키 내용 복사
  2. public 접속 -> sudo su -로 root접속 -> cd /home/ec2-user -> mkdir .ssh
  3. ls -alrt로 폴더 확인
  4. cd .ssh -> vi myjoo.pem 만들고 복사 !wq!
  5. chmod 400 myjoo.pem
  6. Citronapp-env EC2 키 페어 설정 -> myjoo
  7. Citronapp-env의 프라이빗 IP로 접속
  8. ssh -i myjoo.pem ec2-user@[프라이빗 IP]
  9. basthost(public)를 통해서 private안에 있는 beanstalk 접속
  10. netstat -an | grep 5000
  11. log 확인: $ sudo su - -> # cd /var/log -> # tail -200f web.stdout.log

<br>
<br>
<br>

## <u>05 RDS</u>

### 실습: AWS CLI

- RDS 서브넷 그룹 생성 -> 이름 -> 가용 영역: a,c -> 서브넷: private설정
- RDS 데이터베이스 생성 -> Virtual Private Cloud(VPC) 설정 -> DB 서브넷 그룹 설정 -> 기존 VPC 보안 그룹 -> 생성
- 파라미터 그룹: 설정 가능
- private 데이터베이스는 바로 접속 x -> Use SSH turnnel
  ```
  Use SSH turnnel(
    Host: 3.35.54.63(public ip)
    User name: ec2-user
    Authentication type: Key pair
    Private key file: myjoo.pem
  )
  ```
  - bastonhost에 접속한 후 private 데이터베이스 접속

<br>
<br>
<br>

## <u>06 Front</u>

### 실습: AWS CLI

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

| ![ex-image](./img/1.PNG) | ![ex-image](./img/2.PNG) |
| ------------------------ | ------------------------ |

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
