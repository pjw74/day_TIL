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

### 실습: AWS 콘솔: RDS

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

### 실습: AWS CLI: 버킷

1. 도메인 이름 맞추고, 정적 웹 사이트 호스팅 편집 활성화
2. npx create-react-app ciron-app
3. npm start
4. npm run build
5. npm install -g serve
6. serve -s build
7. 업로드 -> build 안에 있는 것 모두
8. 관리 -> 편집 -> 퍼블릭 액세스 차단 해제
9. 버킷 정책 편집 -> Pricipal: \*
10. ARN 복사 후 + /\*
11. JSON 정책 복붙
12. 버킷 웹 사이트 앤드포인트로 접속

<br>
<br>
<br>

## <u>07 CI/CD</u>

### 실습: AWS CLI: CodePipeline

1. 파이프라인 생성 -> ciron-prod-pipeline -> Github 연동
2. 리포지토리, 브랜치 선택
3. AWS CodeBuild
4. 프로젝트 빌드 -> Buildspec 내

   ```
   phases:
   ...
     build:
       command:
         - ./gradlew build
   ...
   artifacts:
     files:
       - '**/*'
   ```

5. 배포 공급자 - private -> AWS CodeDeploy, ELB
6. 개발자 도구 -> CodeDeploy -> 애플리케이션 -> ELB 생성
7. 역할 선택
8. root에 appspec.yml 추가
   ```
   version: 0.0
   os: linux
   files:
     - source: /
       destination: /home/ec2-user/build/
   ```

<br>
<br>
<br>

## <u>08 Route53</u>

### 실습: AWS CLI: Route53

1. 도메인 등록 -> 다른 데서 구입했으면 DNS: 호스팅 영역 생성
2. NS(Name Server 교체)
3. CloudFront 설정
4. SSL 인증서 요청
5. Route53 레코드 생성

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
