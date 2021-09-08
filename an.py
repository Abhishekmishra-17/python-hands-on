n=int(input())
arr=list(map(int,input().split()))
if(((arr[3]-arr[1])/(arr[2]-arr[0]))==((arr[5]-arr[1])/(arr[4]-arr[0]))):
    print(str(int((arr[3]-arr[1])/(arr[2]-arr[0])))+"x-"+str(int((arr[3]-arr[1])/(arr[2]-arr[0])))+"y=0")
else:
    print("0")
