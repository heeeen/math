import numpy as np

# 행렬 A를 출력하는 함수
def pprint(msg, A):
    print("---", msg, "---")
    (n,m) = A.shape
    for i in range(0, n):
        line = ""
        for j in range(0, m):
            line += "{0:.2f}".format(A[i,j]) + "\t" # 그대로 + 소숫점 2자리
            if j == n-1:
                line += "| "
        print(line)
    print("")

# 가우스 소거법을 수행하는 함수
def gauss(A):
    (n,m) = A.shape # n * m

    for i in range(0, min(n,m)): #  range (0 ~ x) => (0, 1, 2, .. x) ==> 결과값 무시하기 위함
        # i번째 열에서 절댓값이 최대인 성분의 행 선택  ==> 열의 짱 선택. pivot 아래로만 비교
        minEl = abs(A[i,i]) # abs = 절댓값 함수 ==> pivot
        print("MinEl:",minEl)
        minRow = i
        print("MinRow:",minRow)
        for k in range(i+1, n): # find a max row
            if minEl != 0 and abs(A[k,i]) < minEl:
                minEl = abs(A[k,i])
                print("Final MinEl:",minEl)
                minRow = k
                print("Final MinRow:",minRow)
            elif minEl == 0:
                minEl = abs(A[k,i])
                print("Final MinEl:",minEl)
                minRow = k

        pprint("처음", A) # 중간 과정 출력

        # 현재 i번째 행과 최댓값을 갖는 행 maxRow의 교환
        for k in range(i, m): # pivoting by using the max row
            tmp = A[minRow,k] # Max가 있는 행의 가로로 pivot 오른쪽으로해서 싹 훑어봄 (4,3,2,1번씩)
            A[minRow,k] = A[i,k]
            A[i,k] = tmp
pprint("pivoting", A) # 중간 과정 출력

        # 양수로 만들기!
        piv = A[i,i]
        for k in range(i, m):
            if (piv<0 and A[i,k] != 0):
                A[i,k] = -A[i,k] # pivot이 음수라면 양수로

        pprint("무지성 1로 만들기", A) # 중간 과정 출력

        # 현재 i번째 열의 i번째 행을 제외한 모두 성분을 0으로 만들기
        for k in range(i+1, n):
            c = A[k,i]/A[i,i] # i행외 행들도 무지성 i행 pivot으로 나누기
            for j in range(i, m): # 가로로 훑어봄
                #print("c =",c)
                #print("A[i,j] = ",A[i,j])
                #print("First (%.0f, %.0f) = %.2f"%(k,j,A[k,j]))
                if i == j:
                    A[k,j] = 0
                else:
                    A[k,j] = A[k,j] - c * A[i,j]

                    #print("Second (%.0f, %.0f) = %.2f"%(k,j,A[k,j]))

        pprint(str(i+1)+"번째 반복", A) # 중간 과정 출력

    # Ax=b의 해 반환
    x = np.zeros(m-1)
    for i in range(0,m-1):
        x[i] = A[i,m-1]
    return x

# 주어진 문제
#       
#       
#       

# 주어진 연립선형방정식에 대한 첨가행렬



A = np.array([[2., 2., 4., 18.], [1., 3., 2., 13.], [3., 1., 3., 14.]])
#A = np.array([[1., 3., -2., 5.], [3., 5., 6., 7.], [2., 4., 3., 8.]])

pprint("주어진 문제", A) # 첨가행렬 출력
x = gauss(A) # 가우스-조단 소거법 적용

# 출력 생성
(n,m) = A.shape


lt=[0 for i in range(n)]

for i in range(n-1,-1,-1):
    tnum = A[i][m-1]
    for j in range(n-1,i-1,-1):
        if lt[j] == 0:
            lt[j] = tnum / A[i][j]
        else:
            tnum -= A[i][j] * lt[j]


line = "해:\t"

for i in range(0, m-1):
    line += "{0:.2f}".format(lt[i]) + "\t"
print(line)
