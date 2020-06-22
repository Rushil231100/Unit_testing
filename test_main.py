#Author : Rushil Kaushal Sanghavi
#Roll No. : B18CSE066
import pytest
import main
print("\n\n\t\t\t\t\t\t==============================")
print("\t\t\t\t\t\t//\tUNIT TEST START...  //")
print("\t\t\t\t\t\t==============================")

test_case_list = [	("Rushil", 10 , 2000, True), #Under maximum limit testing	
		("Chandrakant", 11 , 5000, False),		 #Over Maximum limit testing	
		("Venketesh", 15, 7500 , True),		 	 #level >14 testing
		("Amar Ghosh", 0 , 100 , False),		 #invalid payscale tesing
		("Jay Agarwal", 4 , -300 ,False),	 	 #negative amount testing
		("Jyoti Sinha" , 7 ,"hh3h" ,False),		 #string instead of number testing
		("Elexendra", "4dd",5100,False), 		 #string instead of number in payscale tesing
		("Johnson", 5, 4944, "False"),	 		 #non boolean data type tesing

	]

@pytest.mark.parametrize('name, payscale, requested_advance_amount, expected_output' ,test_case_list)
def test_request_advance(name, payscale, requested_advance_amount, expected_output):
	
	User_test = main.User(name, payscale)
	flag = User_test.request_advance(requested_advance_amount)
	if not (isinstance(expected_output,bool)):
		print("\n\n\t\t\tFault in test case. Enter a valid expected output\n\n")
	else:
		assert flag == expected_output






