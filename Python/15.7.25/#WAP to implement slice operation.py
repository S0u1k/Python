#WAP to implement slice operation
x=['Arisha','is','a','good','student','I','must','say','that','you','chucho?']
y=slice(2,6)  # y=[2:5]
print(x[y])
y=slice(2)  
print(x[y])
y=slice(2,len(x),2)  
print(x[y])