# GitHube

### history 삭제
    git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch 파일명과 위치' --prune-empty -- --all
    -->반드시 파일위치와 파일명 둘 다 적어줘야 작동
    git push origin 브랜치명 --force
##### 브랜치명 확인
    git branch