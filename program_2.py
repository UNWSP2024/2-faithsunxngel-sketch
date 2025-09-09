# program 2

def main():
    # ages of five friends
    age1 = int(input('Enter the age of friend 1: '))
    age2 = int(input('Enter the age of friend 2: '))
    age3 = int(input('Enter the age of friend 3: '))
    age4 = int(input('Enter the age of friend 4: '))
    age5 = int(input('Enter the age of friend 5: '))

    # average calcuation
    average_age = (age1 + age2 + age3 + age4 + age5) / 5

    # making sure the average is printed
    print("The average age is:", average_age)

# running code
main()
