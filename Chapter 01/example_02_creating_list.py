import numpy as np

# 기본 리스트 선언
l = [1,2,3,4]

# convert to numpy array
a = np.array(l)

print(a)
print(f"type(a) : {type(a)}")

# python tuple
t = (1,2,3,4)

# convert to numpy array
b = np.array(t)

print(b)
print(f"type(b) : {type(b)}")

# 메모리에 저장된 레퍼런스(주소) 확인하기
print(f"a.data : {a.data}")

# a.data의 obj를 출력하면 다차원 배열의 값을 보여준다. 
print(f"a.data.obj : {a.data.obj}")

# 속성 base는 다차원 배열의 메모리를 공유할 때 원본 레퍼런스를 저장한다.
c = b
print(f"c.base is b.base : {c.base is b.base}")

# 새로운 변수 c에 저장된 첫 번째 원소를 변경하면 내부에 저장된 원본 배열을 변경하다.
# 모든 변수를 조회하면 다차원 배열의 변경된 것을 볼 수 있다.
c[0] = 100
print(f"c : {c}")
print(f"b : {b}")

# 배열 복사1!
d = np.array(b)
print(f"d : {d}")