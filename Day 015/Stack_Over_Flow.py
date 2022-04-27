import requests
import json

# response = requests.get(
#     "https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow"
# )

response = requests.get(
    "https://api.stackexchange.com/"
    + "/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(
        "ModuleNotFoundError: No module named 'tkinter'"
    )
)


for data in response.json()["items"]:
    if data["answer_count"] != 0:
        print(data)
        break
