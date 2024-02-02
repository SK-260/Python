# python script to demonstrate integration with github to fetch the
# details of users who created Pull requests(Active) on Kubernetes Github repo.

import requests
# https://api.github.com/repos/OWNER/REPO/pulls This is the format for the URL

# URL to fetch the pull requests from github api
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

# Make a GET request to fetch pull request data from the github API
response = requests.get(url)

# Convert the response from JSON format to dictionaries
complete_detail = response.json()

# Create an empty dictionary to store the details for pull request creator and their counts
pr_creators = {}

# Iterate through the complete data to get the PR creators
for pulls in complete_detail:
    creator = pulls["user"]["login"]
    # print(creator)
    if creator in pr_creators:
        pr_creators[creator]+= 1
    else:
        pr_creators[creator] = 1

# Print the PR creators and their count.
print(f"The pull requestor and the number of pull request are: ")
for creator , pulls in pr_creators.items():
    print(f"{creator} : {pulls}")
