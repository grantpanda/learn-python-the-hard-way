print(True and True)
print(False and True)
print(1 == 1 and 2 == 1)

print("test" == "test", 1 == 1 or 2 != 1, True and 1 ==1)

a = False and 0 != 0
b = True or 1 ==1
c = "test" == "testing"
d = 1 != 0 and 2 == 1
print(a,b,c,d)

a11 = "test" != "testing"
a12 = "test" == 1
a13 = not (True and False)
a14 = not (1 == 1 and 0 != 1)
a15 = not (10 == 1 or 1000 == 1000)
print(a11, a12, a13, a14, a15)

a16 = not (1 != 10 or 3 == 4)
a17 = not ("testing" == "testing" and "Zed" == "cool guy")
a18 = 1 == 1 and not ("testing" == 1 or 1 == 0)
a19 = "chunky" == "bacon" and not (3 == 4 or 3 == 3)
a20 = 3 == 3 and not ("testing" == "testing" or "python" == "Fun")