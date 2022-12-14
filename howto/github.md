# GitHube
설정값인 ssh는 넣어줘야 한다
## CI/CD
push 후 자동으로 빌드 및 배포하는 스크립트를 실행시켜주는 것
### branch 만들기
    git branch 이름
- 통합 브랜치 (main(전에는 master였다)) : 배포
- 개발 브랜치 : 다음 버전 준비
- 피쳐 브랜치 : 기능 개발
- 릴리즈 브랜치 : 출시 준비

### branch 이동

    git checkout 이름

### Collaborator 추가

---
## 협업
    git clone <주소>

##### 현재 작업 중인 branch 확인
    git branch

##### branch 바꾸기(작업 시작 전 확인)
    git checkout <branch 이름>

### 작업 전 변경사항 불러오기(택 1)
##### fetch 사용 시 merge도 함께 진행(내 저장소에 변경 내용 반영 참고)
    git pull origin <branch 이름> → 변경 사항 자동 병합<br/>
    git fetch <branch 이름> → 변경 사항 확인 후 직접 병합

##### 내 저장소에 변경 내용 반영
    git checkout <branch 이름><br/>
    git fetch upstream → 변경사항 불러오기<br/>
    git merge upstream/<branch 이름> → 변경사항 병합<br/>
    git push origin <branch 이름> → 내 Fork에 최종 push<br/>
> 99658240f9d6dca12978dbb1078adca3da4ac82f
## 공동사용 중인 깃허브
### 등록 순서
> 권한 받은 후 github에서 fork로 내 깃허브에 팀프로젝트용 레파지토리 생성
> '본인 아이디/프로젝트명'으로 들어온거 확인 후 해당 레파지토리를 클론
> 브랜치 확인 후 

### branch 생성, 삭제(강제 삭제 -D)
##### git branch <branch 이름><br/>
##### git branch -d <branch 이름>

##### upstream 저장소 추가(초기 세팅)
##### Collaborators 에 협업자 등록된 상태
##### origin 은 개인 repository에 위치 → 완료하면 Fork 로 연결되어 있어야 함
##### upstream 은 메인 repository에 위치
    git remote add upstream <메인 repository 주소>

##### remote 저장소 목록 확인(초기 세팅)
    git remote -v


### 매 작업시
##### sync, pull
- 깃허브에서 sync
- git pull

##### 수정 후 add, commit, push

$ git add .<br/>
$ git commit -m "메세지"<br/>
$ git push origin <작업 중인 branch 이름><br/>

##### 업로드 후 git-hub 계정에 Pull Request 생성
##### Pull Request에 작업 내용 작성 후 Merge 클릭





### history 삭제
    git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch 파일명과 위치' --prune-empty -- --all
    -->반드시 파일위치와 파일명 둘 다 적어줘야 작동
    git push origin 브랜치명 --force
##### 브랜치명 확인
    git branch

## 백업
<a href ="https://git-scm.com/book/en/v2/Git-Branching-Branch-Management">링크</a>
    git branch
    git branch hotfix-핫픽스명(주로 날짜)
    git checkout hotfix-2022-12-14 #
    git branch로 확인 

### feature, hotfix, 
