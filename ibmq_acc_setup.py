#get new api from ibmq if there is an account load error and set it as a string value of api
#if you dont have an api or an ibmq account, go to https://quantum-computing.ibm.com/ to create one
#your api will be on your account dashboard

from qiskit import *

api = ""
IBMQ.save_account(api)
