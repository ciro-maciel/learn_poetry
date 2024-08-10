import requests

def fetch_github_user(username):
    """
    Function to fetch a user's information from GitHub.

    Args:
        username (str): Username on GitHub.

    Returns:
        dict: User information in JSON format.
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Unable to fetch information for user {username}."}

def main():
    user = input("Enter your GitHub username: ")
    user_info = fetch_github_user(user)

    if "error" in user_info:
        print(user_info["error"])
    else:
        print(f"Name: {user_info['name']}")
        print(f"Bio: {user_info['bio']}")
        print(f"Public Repositories: {user_info['public_repos']}")

if __name__ == "__main__":
    main()
