# Test 2 - Retrieve a list of users and verify that there is at a minimum one user whose name
# starts with the letter C. The test fails either when a response is not returned, or no usernames
# match the set criteria.

import json
import requests


#API url - correct
url = "https://gorest.co.in/public/v2/users"

# url to be used for test failing due to unexpected response
#url = "https://www.elementive.com/web-analytics/"

response = requests.get(url)
text = str(json.loads(response.text))
print('###############################################\n','Content of created GET request is: \n', text)
C_name = []
def status_code_extended(url):
    response = requests.get(url)
    if 200 <= response.status_code <= 299: #accepts all possible status codes from range 200 <= and <= 299
        print('###############################################\nStatus code is as expected - extended range determined!')
    else:
        raise Exception("The status code is not in predetermined range! FINAL VERIDICT -  FAILED for status code!")
    print("Detected status code is '{}'! FINAL VERIDICT - PASSED for status code!\n###############################################".format(response.status_code))


def test(text, C_name):
    for i in text:
        if i.startswith("C"):#to confirm this function works as expected and throws an exception - change this letter from C to A for example
            C_name.append(i)
    if C_name:
        print("###############################################\nTotal number of names starting with letter 'C' is ", len(C_name), '! \nTest is finished!\n FINAL VERIDICT - PASSED!')
    else:
        raise Exception("No names starting with letter 'C' are detected!\nFINAL VERIDICT -  FAILED!\nPlease try another letters - different then 'C'.\nYou can pick any from names that are listed above  in logs!")

status_code_extended(url)
test(text, C_name)


