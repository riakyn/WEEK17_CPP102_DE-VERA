Test Cases – Simulated Device Monitoring and Alert System

Tested by: Ma. Eleonor A. De Vera
Date of Testing: October 12, 2026

Test Case	Input or Action	Expected Result	Actual Result	Pass/Fail
TC01	Choose 1	Five readings: 28, 31, 35, 37, 29	The program displayed all five initial readings correctly.	Pass*
TC02	Choose 2, enter 33	Reading added successfully	The program displayed "Reading added successfully."	Pass*
TC03	Choose 2, enter abc	Rejected; list unchanged	The program displayed "Invalid input. Enter a whole number only."	Pass*
TC04	Choose 2, enter -5	Rejected; list unchanged	The program displayed "Invalid input. Enter a whole number only."	Pass*
TC05	Choose 2, enter 120	Rejected; list unchanged	The program displayed "Invalid reading. Enter a value from 0 to 100."	Pass*
TC06	Add 30, then choose 3	30 °C -> WARNING	The program should classify 30 °C as WARNING.	Verify
TC07	Choose 3	35 °C -> WARNING	The program should classify 35 °C as WARNING.	Verify
TC08	Choose 4 with initial data	Total 160, average 32.00, minimum 28, maximum 37, status ATTENTION REQUIRED	The summary should display the correct values and overall status.	Verify
TC09	Enter 9	Error message; menu shown again	The program should display an invalid-choice message and show the menu again.	Verify
TC10	Choose 5	Exit message; program ends	The program should display the thank-you message and end.	Verify

* These results match the program behavior shown in the provided code or sample session. Confirm them by running the tests yourself before final submission.

Bugs Found and Fixed

The hardest part was handling invalid temperature inputs correctly. The program uses isdigit() to reject letters, decimal numbers, and negative numbers before converting the input to an integer. It also checks that the reading is between 0 and 100 before adding it to the list.