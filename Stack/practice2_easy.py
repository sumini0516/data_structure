#pop 간단 구현
stack=["커피","꿀물","녹차",None,None]
top=2

print("스택상태:")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])

print("==========================")
data=stack[top]
stack[top]=None
top-=1
print("pop--->", data)

data=stack[top]
stack[top]=None
top-=1
print("pop--->",data)

data=stack[top]
stack[top]=None
top-=1
print("pop--->",data)

print("스택상태:")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])