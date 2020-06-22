#Author : Rushil Kaushal Sanghavi
#Roll No. : B18CSE066

#This file contains data used by main file.

#Admin can modify this dictionary according to govt. rules

dict_maximum_advance_allowed = {
		1: 450,2: 450,3: 450,4: 450,5: 450,
		6: 750,7: 750,8: 750,
		9: 2250, 10: 2250 , 11:2250,
		12: 4500, 13:4500,
		14: 7500,
	}#this dictionary gives the maximum hotel advance amount per day according to payscale.
	#for example, key 6 has value 750, that means if an empolyee has a payscale of 6, he can get maximum upto INR 750 per day for hotel charges.

Allow_message = " Congratulations!. The requested amount is under your limit."
Error_message = "You exceeded the maximum advance amount granted according to your payscale.Keep it below INR "
