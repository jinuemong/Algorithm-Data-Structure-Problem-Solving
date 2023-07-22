

# 쿼드 압축 후 개수 세기

# 0,1 로만 이루어진 2차원 정수 2^n * 2^n
# 압축하고자 하는 영역 S
# S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축
# 그렇지 않다면 S를 정확히 4개의 균일한 정사각형 영역으로 쪼갠 뒤,
# 각 정사각형 영역에 같은 방식으로 압축 시도

# 더이상 압축이 불가능 하다면 갯수 출력
# 방법 구상
# 역으로 생각 ! 가장 작은 4개 단위부터 합치기 시도
# 4개씩 수를 센 다음 하나로 합치기
# 3개씩 세었을 때, 같은 수만 있다면 개수를 1로 변경
# 점차적으로 늘려나가기

# ** **  ** **
# ** **  ** **
#
# ** **  ** **
# ** **  ** **

def solution(arr):
    answer = []

    return zip_reversed(arr)
def zip_reversed(arr):
    new_arr = [[[0,0]]*(len(arr)//2) for i in range((len(arr)//2))]
    if len(new_arr)<=1:
        return arr
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]==0:
                new_arr[i//2][j//2][0]+=1
            elif arr[i][j]==1:
                new_arr[i//2][j//2][1]+=1
    print(new_arr)

# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))