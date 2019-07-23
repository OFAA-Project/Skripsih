import numpy as daud
import docker
import logging
import psutil
import json

api_docker_low = docker.APIClient(base_url='unix://var/run/docker.sock')
api_docker_top = docker.from_env()

#container_list = api_docker_top.containers.list()
#json_container_list = json.dumps(container_list)
#print (json_container_list)
#print (container_list)

#container_list1 = api_docker_low.containers()
#print (container_list1())

#a = api_docker_low.version()
#print (a)

#b = json.dumps(a, indent=4,sort_keys=True)
#print (b)
a = []
for a in api_docker_top.containers.list():
    print (a)

print (type(api_docker_top.containers.list()))

list_container = api_docker_top.containers.list()
#json_list_container = json.dumps(api_docker_top.containers.list())

#print (json_list_container)
def convert(list): 
      
    # Converting integer list to string list 
    s = [str(i) for i in list] 
      
    # Join list items using join() 
    res = int("".join(s)) 
      
    return(res)
#list1 = api_docker_top.containers.list()

#for a in api_docker_top.containers.list():
#    ' '.join(str(e) for e in a)
#str1 = ' '.join(str(e) for e in api_docker_top.containers.list())
#print (str1)
#json_str1 = json.dumps(str1)
#print (json_str1)

out_arr = daud.asarray(list_container)
print (out_arr)
print (out_arr[1])

images = api_docker_top.images.list()
#print (images)
y = daud.asarray(images)
print (y)