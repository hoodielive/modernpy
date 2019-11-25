import requests 

def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    parameters = {"q": "stars:>5000"}
    response = requests.get(gh_api_repo_search_url, params=parameters) 

    response_json = response.json()

    print(response_json.keys())

if __name__ == "__main__":
    repos_with_most_stars()
