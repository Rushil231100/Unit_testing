#Author : Rushil Kaushal Sanghavi
#Roll No. : B18CSE066
import os
import sys
import data


#							================================
#Advance amount eligible for HOTEL ACCOMODATION PER DAY    ||
#							================================


#this function returns the maximum advance amount a user can get according to his/her payscale
def payscale_allowance_chart(payscale):
	if (payscale > 14 and payscale < 20):
		return 7500 
	return data.dict_maximum_advance_allowed.get(payscale,None)



#The below function verifies if the requested amount is in the limit allowed according to the payscale
def amount_request_verification(payscale,amount_requested):

	

	if not (isinstance(payscale,int)):
		print("\n\n\t\t\tYou entered an invalid payscale. Kindly enter a number.\n\n")
		return False
	if not (isinstance(amount_requested,int)):
		print("\n\n\t\t\tYou requested an invalid amount. Kindly enter a number.\n\n")
		return False
	if(amount_requested < 0):
		print("\n\n\t\t\tYou requested an invalid amount. Kindly enter a positive value.\n\n")
		return False

	Maximum_advance_permitted = payscale_allowance_chart(payscale)

	if (Maximum_advance_permitted == None):
		print("\n\n\t\t\tYou entered an invalid payscale. Kindly enter the payscale range from 1 - 20.\n\n")
		return False	
	#checking for the maximum condition
	if(amount_requested <= Maximum_advance_permitted):
		print("\n\n\t\t\t"+data.Allow_message+"\n\n")
		return True
		
	else:
		print("\n\n\t\t\t"+ data.Error_message+ str(Maximum_advance_permitted) + "\n\n")
		return False

#Stub class
class User:
	#default constructor , helps in creating a new object for User
	def __init__ ( self, name, payscale): #other attributes are abstracted
		self.name =  name
		#self.position = position
		self.payscale = payscale #the range of allowance depends on the payscale of the user
		#self.balance = balance

	def get_payscale(self):
		return self.payscale

	def request_advance(self, amount_requested):
		flag = amount_request_verification(self.get_payscale(),amount_requested)
		return flag






