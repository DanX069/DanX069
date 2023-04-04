import os
import requests
from requests.structures import CaseInsensitiveDict

REPO_NAME = os.environ['GITHUB_REPOSITORY']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

def get_stats_card(username):
    url = f"https://github-readme-stats.vercel.app/api?username={DanX069}&show_icons=true&theme=radical"
    return f"![{username}'s GitHub stats]({url})"

def update_readme(stats_card):
    with open("README.md", "r") as file:
        content = file.read()

    new_content = f"<!--stats_start-->\n{stats_card}\n<!--stats_end-->"

    start_index = content.index("<!--stats_start-->")
    end_index = content.index("<!--stats_end-->") + len("<!--stats_end-->")
    content = content[:start_index] + new_content + content[end_index:]

    with open("README.md", "w") as file:
        file.write(content)

def main():
    username = REPO_NAME.split('/')[0]
    stats_card = get_stats_card(username)
    update_readme(stats_card)

if __name__ == "__main__":
    main()
