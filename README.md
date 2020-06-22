# Unit_testing
For Software engg. project, CPDA Allowance system

Use case : Maximum advance amount allowed for hotel charges per day , according to payscale of the employee.

Main.py contains stub class User, with attributes name, and payscale.
Other attributes are abstracted.
It also contains methods for checking the Use case validity, i.e. the method check if the requested amount by an employee is valid(within limit) according to his/her payscale.

data.py contains the data used in main.py code. 
This is separated from main code, as it might change once govt. changes the rules for the same.

>>>Payscales of an employee are ranging from 1 to 20.

test_main.py file contains the methods that tests the main code.
It also contains, pre-written unit test cases written by developer himself.

>>>To run these files in your computer , 
    1. clone the repository ,
    2. Open the terminal
    3. run >>> pytest test_main.py -s"
    
Test reults:
![alt text](https://github.com/Rushil231100/Unit_testing/blob/master/Result_Screenshot/Annotation%202020-06-22%20130543.png?raw=true)


