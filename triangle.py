def count_triangle(n):
    left, right = (n**2)-(n-1), (n**2)+(n-1)
    print(left, right)
    res=0
    for i in range (left, right+1, 2):
        res+=i
    return res
print(count_triangle(3))