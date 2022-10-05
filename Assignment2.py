import logging
logging.basicConfig(filename="Assignment2.log",level=logging.INFO,format=("%(levelname)s %(asctime)s %(name)s %(message)s"))
import calendar
import cmath
class Assignment2:
    logging.info("This is Assignment2 program ")
    def Convent_kilometer_miles(self):
        try:
            logging.info("we are in Convent_kilometer")
            kms = int(input("Enter the lenth of Kms :-"))
            miles = kms/1.609
            logging.info("the lenth of Kms %s ", miles)
            return miles
        except Exception as e:
            logging.exception(e)


    def convert_Celsius_to_Fahrenheit(self):
        try:
            logging.info("we are in  convert_Celsius_to_Fahrenheit")
            celsius_1 = float(input("Temperature value in degree Celsius: "))
            Fahrenheit_1 = (celsius_1 * 9 / 5) + 32
            logging.info("convert_Celsius_to_Fahrenheit %s ",Fahrenheit_1  )
            return Fahrenheit_1
        except Exception as e:
            logging.exception(e)

    def showCalender(self):
        logging.info("showCalender")
        try:
            year = int(input("Enter calender year: "))
            logging.info("Calender %s ", calendar.calendar(year))
            return calendar.calendar(year)
        except Exception as e:
            logging.exception(e)

    def swap_two_variables(self):
        logging.info(" swap two variables without temp variable ")
        try:
            num1 = int(input("Enter the first num"))
            num2 = int(input("Enter the secoun num"))
            logging.info("swap two variables " , num1 , num2)
            print("swap two variables " , num1 , num2)
            num1 = num1 + num2
            num2 = num1 - num2
            num1 = num1 - num2
            logging.info("swap two variables ", num1, num2)
            return num1, num2
        except Exception as e:
            logging.exception(e)

    def solve_quadratic_equation(self):
        logging.info("solve_quadratic_equation")
        try:
            a = int(input("enter value of a"))
            b = int(input("enter value of b"))
            c = int(input("enter value of c"))
            d = (b ** 2) - (4 * a * c)

            s1 = (-b - cmath.sqrt(d)) / (2 * a)
            s2 = (-b + cmath.sqrt(d)) / (2 * a)
            logging.info("solve_quadratic_equation %s ".format(s1, s2))
            print('The solution are {0} and {1}'.format(s1, s2))

        except Exception as e:
            logging.exception(e)







a =  Assignment2
a.Convent_kilometer_miles
print(a.Convent_kilometer_miles("miles"))
a.convert_Celsius_to_Fahrenheit
print(a.convert_Celsius_to_Fahrenheit("Fahrenheit_1"))
a.showCalender
print(a.showCalender("year"))
a.swap_two_variables
print(a.swap_two_variables)
a.solve_quadratic_equation
print(a.solve_quadratic_equation("format(s1, s2)"))



