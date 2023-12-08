def calc_temp(time,a,b,c):
    temp=a*(time**2)+(b*time)+c
    return temp

num_sets=int(input("Enter the number of sets: "))

for x in range(num_sets):
    print(f"\nSet {x+1}:")
    a=float(input("Enter coefficient a: "))
    b=float(input("Enter coefficient b: "))
    c=float(input("Enter coefficient c: "))

    time=float(input("Enter time: "))
    temperature=calc_temp(time,a,b,c)
    print(f"Temperature at {time} is {temperature} degrees celsius.")
