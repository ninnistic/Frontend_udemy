
# **20230112 - Today I learnt** 

## **1. CLI** 
Command Line Interface  ⇒ 명령어를 통해 사용자와 컴퓨터가 상호작용 하는 방식
### **[ Command Line ]**


| commands     |                                            |
| ------------ | ------------------------------------------ |
| ls           | 목록확인                                   |
| clear        | 내용 지우기(화면 지우기)                   |
| mkdir        | make directory = 폴더생성                  |
| mkdir 폴더명 |
| cd           | change directory = 디렉토리 이동(폴더열기) |
cd 위치
cd .. : 상위 폴더 이동 |
| pwd | print working directory = 현재위치 보여주기  |
| rmdir | remove directory 
rmdir 폴더명 |
| find -name  | find -name 이름  |
| rm -d | == rmdir
rm -d 이름  = 비어있는 폴더 지우기  |
| rm -r | rm -r 이름 (recursive)  비어있지 않은 폴더 지우기  |
| rm -f | rm -f 이름 (force) 문제가 있어도 물어보지 않고 지움 (추천x) |
| touch | 파일을 생성함  |
| ./ | 현재 작업하는 폴더 |
| ../ | 현재 작업하고 있는 폴더의 부모 폴더  |
| -a | all |
| . | 자기자신 |
|  |  |

![Command Lines](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/242dc71c-a2e6-45ef-99a8-5eb662f88fd7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230112T063239Z&X-Amz-Expires=86400&X-Amz-Signature=17ec020e17b0c88c7be3996c98f71a619e4c43900021f80fab5b6855d19ac76f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)<br>



## **2. Git Commands**


| git commands         |                                                                     |
| -------------------- | ------------------------------------------------------------------- |
| git init             | git initialize / 로컬저장소 생성                                    |
| .git                 | hidden file (.의 의미는 숨김파일)                                   |
| git status           | 현재 상태 확인                                                      |
| git add              | Working directory → Staging area (어떤 파일을 커밋할지 고르는 단계) |
| git commit           | Staging → Repository (커밋)                                         |
| git commit -m ""     | commit할 때 메세지 붙임                                             |
| git remote -v        | git repository의 주소를 알 수 있다.                                 |
| git dff              | 달라진 내용 확인 가능                                               |
| git push origin main | main에 push함                                                       |
| git log              | git log (commit 내역들 확인 가능)                                   |
| q                    | 누르면 end 탈출 가능                                                |

## **3. Git**
working directory → Staging Area → Repository<br> 
git branch -M main (Master에서 Main으로 바꿔줌)

### **Git Area Overview**
![GitAreaOverview](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/63f1d338-fd63-40a9-97d9-87d4c845d377/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230112T063651Z&X-Amz-Expires=86400&X-Amz-Signature=cd138e29df7db589df34d2696921edf4c1dc88a950d6b5c23c8faf112db37945&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)