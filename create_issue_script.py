from github import Github

# GitHub 액세스 토큰 설정
access_token = 'YOUR_ACCESS_TOKEN'
repo_name = 'YOUR_REPOSITORY_NAME'

# GitHub 저장소 및 이슈 생성
g = Github(access_token)
repo = g.get_repo(repo_name)

# 이전 스크립트에서 출력된 내용 가져오기
result_text = "축구토토 승무패 10회차 [02월 22일 목요일] - 2회 연속 이월 : 1,596,036,750 원(746,858,000 원)"

# GitHub 이슈 생성
issue_title = f"Automatic Issue: {result_text}"
issue_body = result_text
repo.create_issue(title=issue_title, body=issue_body)
