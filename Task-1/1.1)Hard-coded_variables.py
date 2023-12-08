def calc_temp(time,a,b,c):
    temp=a*(time**2)+(b*time)+c
    return temp

a=0.6
b=1.8
c=26

time=2
temperature=calc_temp(time,a,b,c)
print(f"Temperature at {time} is {temperature} degrees celsius.")
