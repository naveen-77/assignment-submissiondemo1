altitude=int(input("alitude= "))
if altitude<1000:
    print("Land the plane")
elif altitude>1000 and altitude<5000:
    print("come down to 1000")
else:
    print("go around and try later")
