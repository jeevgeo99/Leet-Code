def is_happy(n):
    def sum_of_squares(num):
        return sum(int(digit ** 2 for digit in str(num)))
    
    seen_numbers = set()

    while n!=1 and n not in seen_numbers:
        seen_numbers.add(n)
        n=sum_of_squares(n)

    return n == 1


n1 = 19
print(f"Is {n1} a happy number? {is_happy(n1)}")  

n2 = 2
print(f"Is {n2} a happy number? {is_happy(n2)}")  