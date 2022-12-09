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





### history 삭제
    git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch 파일명과 위치' --prune-empty -- --all
    -->반드시 파일위치와 파일명 둘 다 적어줘야 작동
    git push origin 브랜치명 --force
##### 브랜치명 확인
    git branch