#WAP TO CHECK IF A NO TAKEN AS ITSELF FROM USER IS EVEN OR NOT, IF YES THEN PRINT SQUARE OF THE NO.

num=int(input("Enter a number:- "))

if num%2==0:
    print(num, "The number is even")
    num=num**2
    print(num)