"""
Given the structure of a company, your task is to calculate for each employee the number of their subordinates.

Input:
The first input line has an integer n: the number of employees. The employees are numbered 1,2,...,n, and employee 1 is the general director of the company.
After this, there are n-1 integers: for each employee 2,3,...,n their direct boss in the company.

Output:
Print n integers: for each employee 1,2,...,n the number of their subordinates.


Constraints:
1 <= n <= 2 * 10^5

Example:
Input:
5
1 1 2 3

Output:
4 1 1 0 0
"""