#tip and split calculator.
x=input('Enter the bill amount')
y=input('Enter the tip percentage you want to give')
z=input('Enter the number of persons the bill has to be divided with')

tb=(float(x)*(1+float(y)/100))
a=tb/float(z)
ans=round(a,2)
print(f"Each person will give {ans} INR")