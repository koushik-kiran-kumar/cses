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

class CompanyStructure:
    def __init__(self, n: int) -> None:
        self.num_employees = n
        self.hierarchy = [[] for _ in range(n)]
    
    def add_employee(self, emp_id: int, boss_id: int) -> None:
        self.hierarchy[boss_id].append(emp_id)

    def get_subordinate_counts(self) -> str:
        subordinate_counts = [0 for _ in range(self.num_employees)]
        visited = [False for _ in range(self.num_employees)]
        processing_order = []
        stack = [0]
        
        while stack:
            current = stack[-1]
            
            if not visited[current]:
                visited[current] = True
                for subordinate in self.hierarchy[current]:
                    if not visited[subordinate]:
                        stack.append(subordinate)
            else:
                stack.pop()
                processing_order.append(current)
        
        for employee in processing_order:
            for subordinate in self.hierarchy[employee]:
                subordinate_counts[employee] += 1 + subordinate_counts[subordinate]
        
        return " ".join(map(str, subordinate_counts))

def main():
    n = int(input())
    hierarchy = CompanyStructure(n)
    bosses = list(map(int, input().split()))
    for i in range(1, n):
        boss_id = bosses[i-1]
        hierarchy.add_employee(i, boss_id-1)
    
    print(hierarchy.get_subordinate_counts())


if __name__ == "__main__":
    main()
