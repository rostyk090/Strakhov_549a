# 1. Парне чи непарне
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# 2. Помножити число на 4 або 5
def multiply_by_condition(number):
    return number * 4 if number % 2 == 0 else number * 5

# 3. Зробити число негативним
def make_negative(number):
    return number if number < 0 else -number

# 4. Століття за роком
def century_from_year(year):
    return (year + 99) // 100

# 5. Найменше число в списку
def find_smallest(numbers):
    return min(numbers)

# 6. Два найбільших числа
def two_largest(numbers):
    numbers = sorted(numbers)
    return [numbers[-2], numbers[-1]]

# 7. Порахувати позитивні та суму негативних
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    positives = sum(1 for x in arr if x > 0)
    negatives = sum(x for x in arr if x < 0)
    return [positives, negatives]

# 8. Порахувати голосні
def count_vowels(s):
    vowels = "aeiouyAEIOUY"
    return sum(1 for char in s if char in vowels)

# 9. Знайти середній символ
def get_middle(s):
    n = len(s)
    if n % 2 == 0:
        return s[n//2-1:n//2+1]
    else:
        return s[n//2]

# 10. Таблиця множення NxN
def multiplication_table(n):
    return [[(i+1)*(j+1) for j in range(n)] for i in range(n)]



num1 = 5
num2 = 6

print(even_or_odd(num1))
print(even_or_odd(num2))

print(multiply_by_condition(num1))
print(multiply_by_condition(num2))

print(make_negative(1))
print(make_negative(-5))

print(century_from_year(1705))
print(century_from_year(1900))

print(find_smallest([34, 15, 88, 2]))

print(two_largest([1, 5, 87, 45, 8, 8]))

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([]))

print(count_vowels("hello world"))

print(get_middle("test"))
print(get_middle("student"))
print(get_middle("A"))

table = multiplication_table(3)
for row in table:
    print(row)