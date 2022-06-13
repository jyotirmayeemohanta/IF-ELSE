water=int(input("enter water quantity"))
if water<1l:
    print("pani or bharna hai")
elif water>1l and<=10l:
    print("pani nehi bharna hai")
else:
    print("pani overflow")