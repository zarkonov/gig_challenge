# Test 1 - Fetching content from url and checking if response status code is 200 and if response is not empty

import json
import requests

#API url - correct
url = "https://gorest.co.in/public/v2/users"

# url to be used for test failing due to unexpected response
#url = "https://www.elementive.com/web-analytics/"

def status_code(url):
    response = requests.get(url)
    if response.status_code == 200:#accepts status code 200
        print('Status code is  as expected!')
    else:
        raise Exception("The status code is not in predetermined range! FINAL VERIDICT -  FAILED!")
    print("Detected status code is '{}'\!".format(response.status_code))


def length_list(url):
    response = requests.get(url)
    # parse response to a JSON formated list
    json_response = list(json.loads(response.text))
    #json_response = []#just to test if we are failing with an empty response
    length_list = len(json_response)
    if length_list != 0:
            print("A returned list is not empty!")
    else:
        raise Exception("The response is empty. FINAL VERIDICT -  FAILED!")
    print('json_response content is:\n', json_response)
    print("Its length of '{}' elements is assigned to a list 'json_response'!\nTest is finished!\nFINAL VERIDICT - PASSED!".format(length_list))

status_code(url)
length_list(url)
