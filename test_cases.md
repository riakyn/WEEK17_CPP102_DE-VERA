# Test Cases - Simulated Device Monitoring and Alert System

Tested by: Ma. Eleonor A. De Vera

Date of testing: October 12, 2026

| Test Case| Input or Action | Expected Result | Actual Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| TC01 | Choose 1 | Shows readings 28, 31, 35, 37, 29 | Five readings displayed correctly | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | Reading added successfully | Pass |
| TC03 | Choose 2, enter abc | Input rejected and list unchanged | Invalid input message displayed | Pass |
| TC04 | Choose 2, enter -5 | Reading rejected | Invalid reading message displayed | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged. | Invalid reading message displayed | Pass |
| TC06 | Add 30, then choose 3 | 30 C -\> WARNING | 30 C classified as WARNING | Pass |
| TC07 | Choose 3 | 35 C -\> WARNING | 35 C classified as WARNING | Pass |
| TC08 | Choose 4 with initial data | Total 160, average 32.00, minimum 28, maximum 37, status ATTENTION REQUIRED | Summary values match the expected results | Pass |
| TC09 | Enter 9 | Error message displayed and menu repeats | Invalid choice message displayed and menu shown again | Pass |
| TC10 | Choose 5 | Exit message displayed and program ends | Thank-you message appears; program ends. | Pass |

# Bugs Found and Fixed

The hardest part was validating user input. The program uses isdigit() to reject letters, decimal numbers, and negative numbers. It also checks that readings are within the allowed range of 0 to 100 before adding them to the list.