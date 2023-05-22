# Test 3 - Retrieve a list of users and display it in the console. The test fails when a response is
# not returned, or the list contains zero users.

import json
import requests

#url address for userId=1
url = "https://gorest.co.in/public/v2/users"
# url to be used for test failing due to unexpected response
#url = "https://www.elementive.com/web-analytics/"



#Make get request
response=requests.get(url)
print('###############################################\n','Content of created GET request is: \n', response.content)
data = json.loads(response.text)

#determination of the loop range for collecting all elements from a list
length_list = range(len(data))
#length_list = 0#set to make test failing - returning TypeError: 'int' object is not iterable
def test3():
    print('Retrieved list of users is:')
    for i in length_list:
    #prints the first name from the list

        print(data[i]['name'])
    print('\n###############################################\nTest is finished.\nFival veridict - PASSED!\n###############################################')

def status_code_get(url):
    response = requests.get(url)
    if 200 <= response.status_code <= 299:#accepts all possible status codes from range 200 <= and <= 299
        print('###############################################\nStatus code is as expected - extended range determined!')
    else:
        raise Exception("###############################################\nThe status code is not in predetermined range! FINAL VERIDICT -  FAILED!\n###############################################")
    print("Detected status code is '{}'! FINAL VERIDICT - PASSED!\n".format(response.status_code))

def length_list_get(url):
    response = requests.get(url)
    # parse response to a JSON formated list
    json_response = list(json.loads(response.text))
    #json_response = []#just to test if we are failing with an empty response
    length_list = len(json_response)
    if length_list != 0:
            print("###############################################\nA returned list is not empty!")
    else:
        raise Exception("###############################################\nThe response is empty. FINAL VERIDICT -  FAILED!\n###############################################")
    print("Its length of '{}' elements is assigned to a list 'json_response'! FINAL VERIDICT - PASSED!\n###############################################".format(length_list))

status_code_get(url)
length_list_get(url)
test3()
