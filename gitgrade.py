import requests
def analyze_repo(repo_url):
    parts = repo_url.replace("https://github.com/", "").split("/")
    owner = parts[0]
    repo = parts[1]
    repo_api = f"https://api.github.com/repos/{owner}/{repo}"
    commits_api = f"{repo_api}/commits"
    contents_api = f"{repo_api}/contents"
    languages_api = f"{repo_api}/languages"
    repo_data = requests.get(repo_api).json()
    commits = requests.get(commits_api).json()
    contents = requests.get(contents_api).json()
    languages = requests.get(languages_api).json()
    has_readme = False
    file_count = 0
    for item in contents:
        file_count += 1
        if item["name"].lower().startswith("readme"):
            has_readme = True
    commit_count = len(commits)
    language_list = list(languages.keys())
    score = 0
    if has_readme:
        score += 20
    if commit_count >= 10:
        score += 20
    elif commit_count >= 5:
        score += 10
    if file_count >= 5:
        score += 20
    if len(language_list) >= 1:
        score += 20
    score = min(score, 100)
    if score >= 80:
        level = "Advanced"
    elif score >= 50:
        level = "Intermediate"
    else:
        level = "Beginner"
    if commit_count >= 15:
        consistency = "Consistent Developer"
    elif commit_count >= 5:
        consistency = "Moderately Consistent"
    else:
        consistency = "Inconsistent Commit History"
    summary = f"This is a {level} level project with {consistency.lower()}."
    if score >= 75:
        verdict = "This project is strong enough to catch a recruiter's attention."
    elif score >= 50:
        verdict = "This project shows potential but needs improvements before recruiter review."
    else:
        verdict = "This project reflects early learning and needs significant improvement."
    roadmap = []
    if not has_readme:
        roadmap.append("Add a detailed README with project explanation and setup steps")
    if commit_count < 10:
        roadmap.append("Improve commit consistency with meaningful commit messages")
    roadmap.append("Add unit tests to improve maintainability")
    roadmap.append("Refactor folder structure for better readability")
    print("\n====== GitGrade AI Report ======")
    print("Score:", score, "/ 100")
    print("Project Level:", level)
    print("Developer Consistency:", consistency)
    print("\nSummary:")
    print(summary)
    print("\nRecruiter Verdict:")
    print(verdict)
    print("\nPersonalized Roadmap:")
    for step in roadmap:
        print("-", step)
repo_link = input("Enter GitHub Repository URL: ")
analyze_repo(repo_link)