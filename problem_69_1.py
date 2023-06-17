# Problem 69_1
# Reading from the file
with open(file="problem_69_output.txt", mode="r") as file:
    data = (file.read()).split('\n')
    file.close()
with open(file="problem_69_output.txt", mode='a') as file:
    print(f"Hello {data[0]}! Your age is {data[1]}")
    num1, num2 = input("Enter Number: ").split(' ')
    file.write(f"\nSum of Nums are: {int(num1)+int(num2)}")
    file.close()
