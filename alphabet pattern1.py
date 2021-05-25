i=1
ascii=65
while ascii<=90:
    if i%5==0:
        print()
    print(chr(ascii),end=" ")
    ascii=ascii+1
    i=i+1