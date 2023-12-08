def calc_temp(time,a,b,c):
    temp=a*(time**2)+(b*time)+c
    return temp

with open("data.txt","r")as file:
    line=file.readline().split()
    time,a,b,c=map(float,line)

temperature=calc_temp(time,a,b,c)
print(f"Temperature at {time} is {temperature} degrees celsius.")
