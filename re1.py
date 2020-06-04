def tree(n):
    a = 0 
    while True:
        a += 1
        print("나무를 {0}번 찍었습니다".format(a))
        if a == n:
            print("나무가 넘어갑니다.")
            break

tree(100)
