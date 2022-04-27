import requests
import json

# This function will make an HTTP request using StackOverflow
# API and the error we get from the 1st function and finally
# returns the JSON file.


def make_request(error):
    resp = requests.get(
        "https://api.stackexchange.com/"
        + "/2.3/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(
            error
        )
    )
    return resp.json()


# This function takes the JSON from the 2nd function, and
# fetches and stores the URLs of those solutions which are
# marked as "answered" by StackOverflow. And then finally
# open up the tabs containing answers from StackOverflow on
# the browser.
def get_urls(json_dict):
    url_list = []
    count = 0

    for i in json_dict["items"]:
        if i["is_answered"]:
            url_list.append(i["link"])
            count += 1
        if count == 3 or count == len(i):
            break

    for i in url_list:
        print(i)


resp = make_request("Python module not found")
get_urls(resp)
