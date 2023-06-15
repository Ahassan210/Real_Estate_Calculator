from House import House
from Person import Person

#list to store the houses
houses = []
pay_off_months = 0
#instanitating 3 persons
person_1 = Person("John", 1000, 0, 0)
person_2 = Person("ALex", 1000, 0, 0)
person_3 = Person("Mathew", 1000, 0, 0)

#Menu to print first
def menu():
    print("Please select one of the following options: ")
    print("1: To check how long it takes Pay off a new house press 1")
    print("2: To Check how long it takes for Houses to start "
          "buying themselves press 2")
    print("3: To Quit the menu press 3 or type `quit`")



#method to create a new house(aka create a new instance)
def create_new_house():
    return House(340000,(person_1,person_2,person_3),1800)

#Method to calculate how long it takes to pay off 1 house
def pay_off_house(house: House):
    global pay_off_months
    #variale to store the total money of payments until a house is paid
    payments = 0

    #check how many months it takes
    number_of_months = 0

    #store the total amount of payments each person can contribute to the new house
    person_one_payment = person_1.active_income + person_1.passive_income
    person_two_payment = person_2.active_income + person_2.passive_income
    person_three_payment = person_3.active_income + person_3.passive_income

    #check how much they all pay together yearly
    total_amount_that_year = ((person_one_payment +
                               person_two_payment +
                               person_three_payment)*12)

    #loop to iterate until it's been paid off
    while payments <= 340000:
        #make all the payments
        payments += (person_one_payment + person_two_payment + person_three_payment)
        number_of_months += 1
    #number of payments it took
    print("It took {} number of Payments and {} years".format(number_of_months, number_of_months/12))
    #Payment details of each person
    print("{} paid {} active income and {} passive income monthly,"
          " {} in total that year".format(person_1.name,
          person_1.active_income,person_1.passive_income,
          person_one_payment*12))
    print()
    print("{} paid {} active income and {} passive income monthly,"
          " {} in total that year".format(person_2.name,
          person_2.active_income,person_2.passive_income,
          person_two_payment*12))
    print()
    print("{} paid {} active income and {} passive income monthly,"
          " {} in total that year".format(person_3.name,
          person_3.active_income,person_3.passive_income,
          person_three_payment*12))
    print()
    print("A total of {} That Year.".format(total_amount_that_year))
    person_1.passive_income += (house.rent/3)
    person_2.passive_income += (house.rent/3)
    person_3.passive_income += (house.rent/3)
    #store how long it took
    pay_off_months += number_of_months
    houses.append(house)


#function to check how long it takes for house to pay themselves off
def check_to_riches_time():
    full_house_payment = 340000
    total_yearly_passive_payments = 0
    number_of_months = 0
    can_pay_itself = False
    while not can_pay_itself:
        house = create_new_house()
        pay_off_house(house)

        total_yearly_passive_payments = ((person_1.passive_income +
        person_2.passive_income + person_3.passive_income)*12)
        if total_yearly_passive_payments >= full_house_payment:
            can_pay_itself = True

    return print("It took {} months and {} years".format(pay_off_months,pay_off_months/12))


choice = ""
while choice != "3":
    menu()
    choice = input()

    match choice:
        case "1":
            new_house = create_new_house()
            pay_off_house(new_house)

        case "2":
            check_to_riches_time()

        case "3":
            break








