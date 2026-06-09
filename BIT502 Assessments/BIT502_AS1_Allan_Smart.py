# Import libraries
from colorama import Fore, Style, init
import time
import os
import sys

init(autoreset=True)

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Task 1: Main menu
def main_menu():
    
    # Print differnt main menu options
    print(Fore.BLUE + "1. Membership Plans\n")
    print(Fore.BLUE + "2. Optional Extras\n")
    print(Fore.BLUE + "3. Reading Challenge\n")
    print(Fore.BLUE + "4. Aurora-Picks Rental Calculator\n")
    print(Fore.BLUE + "5. Exit the program\n")

# Task 2: Membership plans function
def membeship_plans():

    while True:

        #Clear screen
        clear_screen()

        #Opening message
        print('Welcome to Membership Plans\n')

        # Print membership plans sub-menu
        print(Fore.BLUE + "Membership plan options:")
        print(Fore.BLUE + "1. Standard\n")
        print(Fore.BLUE + "2. Premium\n")
        print(Fore.BLUE + "3. Kids\n")
        print(Fore.BLUE + "4. Return to main menu\n")
        print(Fore.BLUE + "5. Exit\n")

        membership_plan_option = 0
        try:
            
            membership_plan_option = int(input("Select option: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please select an option from 1 - 5")

        match membership_plan_option:
            case 1:
                standard_price = 10
                standard_price_annual = (standard_price * 12)
                standard_price_annual_discount = standard_price_annual - standard_price
                print('You have selected the Standard Plan\n')
                print('The Standard Plan provides basic membership\n')
                print(f'The monthly cost for the Standard Plan is: ${standard_price}\n')
                print(f'The annual cost for the Standard Plan is ${standard_price_annual}\n')
                print(f'The annual cost receives one month free, the total annual premium is ${standard_price_annual_discount}\n')
                print('Please note that prices are subject to change in the future\n')

            case 2:
                premium_price = 15
                premium_price_annual = (premium_price * 12)
                premium_price_discount = premium_price_annual - premium_price
                print('You have selected the Premium Plan\n')
                print('The Premium Plan provides access to book discounts and special sales\n')
                print(f'The monthly cost for the Premium Plan is: ${premium_price}\n')
                print(f'The annual cost for the Premium Plan is: ${premium_price_annual}\n')
                print(f'The annual cost receives one month free, the total annual premium is ${premium_price_discount}\n')
                print('Please note that prices are subject to change in the future\n')

            case 3:
                kids_price = 5
                kids_price_annual = (kids_price * 12)
                kids_price_annual_discount = kids_price_annual - kids_price
                print('You have selected the Kids Plan\n')
                print('This plan is only available for kids 12 or younger\n')
                print(f'The monthly cost for the Kids Plan is ${kids_price}\n')
                print(f'The annual cost for the Kids Plan is ${kids_price_annual}\n')
                print(f'The annual cost receives one month free, the total annual premium is ${kids_price_annual_discount}\n')
                print('Please note that prices are subject to change in the future\n')


            case 4:
                print('You have selected to return back to the main menu\n')
                time.sleep(1)
                return
            
            case 5:
                print('You have selected to exit the program\n')
                print('From Aurora we thank you, and we hope to see you again\n')
                print('Exiting......\n')
                time.sleep(1)
                sys.exit()

            case _:
                print(Fore.RED + 'Invalid input. Please enter an option between 1 - 5\n')
                input(Fore.RED + 'Press enter to try again....\n')

        print('Exiting Membership Plan options\n')
        input('Press any key to conintue.....\n')


# Task 3 - Optional extras
def optional_extras():

        clear_screen()
    
        # Opening message
        print('Welcome to Optional Extras\n')
        print('Optional extras are a monthly cost and separate from the base membership cost\n')
        input('Press Enter to continue...\n')

        extra_total = 0
        selected_extras = []

        # Book rental
        EXTRA_1_PRICE = 5
        while True:
            extra_1 = input('Would you like book rental ($5/month) - borrow one book at a time (yes/no): ').lower()
            if extra_1 in ('yes', 'y'):
                print('Thank you for choosing book rental\n')
                extra_total += EXTRA_1_PRICE
                selected_extras.append(f'Book Rental: ${EXTRA_1_PRICE}')
                break
            elif extra_1 in ('no', 'n'):
                print('You have selected no\n')
                break
            else:
                print(Fore.RED + 'Invalid response. Please enter yes or no\n')

        # Private area access
        EXTRA_2_PRICE = 15
        while True:
            extra_2 = input('Would you like private area access ($15/month) - access to quiet reading area (yes/no): ').lower()
            if extra_2 in ('yes', 'y'):
                print('Thank you for choosing private area access\n')
                extra_total += EXTRA_2_PRICE
                selected_extras.append(f'Private Area Access: ${EXTRA_2_PRICE}')
                break
            elif extra_2 in ('no', 'n'):
                print('You have selected no\n')
                break
            else:
                print(Fore.RED + 'Invalid response. Please enter yes or no\n')

        # Monthly booklet
        EXTRA_3_PRICE = 2
        while True:
            extra_3 = input('Would you like the monthly booklet ($2/month) - news, events and upcoming releases (yes/no): ').lower()
            if extra_3 in ('yes', 'y'):
                print('Thank you for choosing the monthly booklet\n')
                extra_total += EXTRA_3_PRICE
                selected_extras.append(f'Monthly Booklet: ${EXTRA_3_PRICE}')
                break
            elif extra_3 in ('no', 'n'):
                print('You have selected no\n')
                break
            else:
                print(Fore.RED + 'Invalid response. Please enter yes or no\n')

        # Online ebook rental
        EXTRA_4_PRICE = 5
        while True:
            extra_4 = input('Would you like online ebook rental ($5/month) - borrow ebooks for up to 7 days (yes/no): ').lower()
            if extra_4 in ('yes', 'y'):
                print('Thank you for choosing online ebook rental\n')
                extra_total += EXTRA_4_PRICE
                selected_extras.append(f'Online Ebook Rental: ${EXTRA_4_PRICE}')
                break
            elif extra_4 in ('no', 'n'):
                print('You have selected no\n')
                break
            else:
                print(Fore.RED + 'Invalid response. Please enter yes or no\n')

        # Display results
        clear_screen()
        print('Your selected extras:\n')
        if selected_extras:
            for extra in selected_extras:
                print(f'- {extra}')
        else:
            print('No extras selected')
        print(f'\nTotal monthly cost for extras: ${extra_total}')
        input('\nPress any key to return to the main menu...')

# Task 4 - Kid's reading challenge
def reading_challenge():
    
    # Clear screen and opening message
    clear_screen()
    print('Welcome to the kids reading challenge. Please enter the number pages read each day')
    input('Press Enter to start....')

    total_pages_read = 0

    # Monday
    while True:
        try:
            monday_pages_read = float(input('Enter the number of pages read on Monday: '))
            if monday_pages_read < 0:
                print(Fore.RED + 'Negative numbers not allowed\n')
                input(Fore.RED + 'Press Enter to try again....\n')
                continue
            print(f'You have read {monday_pages_read} pages')
            total_pages_read += monday_pages_read
            break
        except ValueError:
            print(Fore.RED + 'Invalid input. Please enter a numerical value\n')
            input(Fore.RED + 'Press Enter to try again....\n')
            continue

    # Tueday
    while True:
        try:
            tuesday_pages_read = float(input('Enter the number of pages read on Tuesday: '))
            if tuesday_pages_read < 0:
                print(Fore.RED + 'Negative numbers not allowed\n')
                input(Fore.RED + 'Press Enter to try again....\n')
                continue
            print(f'You have read {tuesday_pages_read} pages')
            total_pages_read += tuesday_pages_read
            break
        except ValueError:
            print(Fore.RED + 'Invalid input. Please enter a numerical value\n')
            input(Fore.RED + 'Press Enter to try again....\n')
            continue

    # Wednesday
    while True:
        try:
            wednesday_pages_read = float(input('Enter the number of pages read on Wednesday: '))
            if wednesday_pages_read < 0:
                print(Fore.RED + 'Negative numbers not allowed\n')
                input(Fore.RED + 'Press Enter to try again....\n')
                continue
            print(f'You have read {wednesday_pages_read} pages')
            total_pages_read += wednesday_pages_read
            break
        except ValueError:
            print(Fore.RED + 'Invalid input. Please enter a numerical value\n')
            input(Fore.RED + 'Press Enter to try again....\n')
            continue

    #Thursday
    while True:
        try:
            thursday_pages_read = float(input('Enter the number of pages read on Thursday: '))
            if thursday_pages_read < 0:
                print(Fore.RED + 'Negative numbers not allowed\n')
                input(Fore.RED + 'Press Enter to try again....\n')
                continue
            print(f'You have read {thursday_pages_read} pages')
            total_pages_read += thursday_pages_read
            break
        except ValueError:
            print(Fore.RED + 'Invalid input. Please enter a numerical value\n')
            input(Fore.RED + 'Press Enter to try again....\n')
            continue

    # Friday
    while True:
        try:
            friday_pages_read = float(input('Enter the number of pages read on Friday: '))
            if friday_pages_read < 0:
                print(Fore.RED + 'Negative numbers not allowed\n')
                input(Fore.RED + 'Press Enter to try again....\n')
                continue
            print(f'You have read {friday_pages_read} pages')
            total_pages_read += friday_pages_read
            break
        except ValueError:
            print(Fore.RED + 'Invalid input. Please enter a numerical value\n')
            input(Fore.RED + 'Press Enter to try again....\n')
            continue


    print(f'Total pages read: {total_pages_read}')
    average_per_day = total_pages_read / 5
    print(f'Average pages per day: {average_per_day}')

    if total_pages_read <= 25:
        print('You ranked Bronze')
        to_silver = 26 - total_pages_read
        print(f'You need {to_silver} pages more to reach silver rank')
    elif total_pages_read > 25 and total_pages_read <= 50:
        print('You ranked Silver')
        to_gold = 51 - total_pages_read
        print(f'You need {to_gold} pages more to reach gold rank')
    elif total_pages_read > 50 and total_pages_read <= 100:
        print('You ranked Gold')
        to_platinum = 101 - total_pages_read
        print(f'You need {to_platinum} pages more to reach platinum rank')
    else:
        print('You ranked Platinum')

    days = {

        'Monday': monday_pages_read,
        'Tuesday': tuesday_pages_read,
        'Wednesday': wednesday_pages_read,
        'Thursday': thursday_pages_read,
        'Friday': friday_pages_read
    }

    max_pages = max(days.values())
    for key, value in days.items():
        if value == max_pages:
            print(f'Your biggest reading was {key} with {value} pages')

    if total_pages_read > 150:
        print('You have broken current record for pages read in a week')

    input('\nPress any key to return to the main menu...')

# Task 5 - Aurora-Picks Rental Calculator
def rental_calculator():

    clear_screen()
    while True:

        print('Welcome to the Aurora-Picks Rental Calculator\n')
        print('Please select from the following options:\n')
        print('1. Enter rental period')
        print('2. return to main menu')

        try:
            aurora_rental_option = int(input('Please select option 1 or 2: '))
        except ValueError:
            print(Fore.RED + 'Invalid input. Please enter a numerical value\n')
            input(Fore.RED + 'Press Enter to try again....\n')
            continue

        match aurora_rental_option:
            case 1:
                while True:
                    clear_screen()
                    number_of_rental_days = 0
                    try:
                        number_of_rental_days = int(input('Enter the number of rental days: '))
                        if number_of_rental_days < 3:
                            print(Fore.RED + 'Number of rental days, must be at least three days\n')
                            input(Fore.RED + 'Press Enter to try again....')
                            continue
                        if number_of_rental_days > 21:
                            print(Fore.RED + 'Maximum rental period is 21 days.')
                            input(Fore.RED + 'Press Enter to try again....')
                            continue
                    except ValueError:
                        print(Fore.RED + 'Invalid input. Must enter a number\n')
                        input(Fore.RED + 'Press Enter to try again')
                    
                    COST_PER_DAY = 1
                    COST_AFTER_3_DAYS = 0.80
                    COST_AFTER_8_DAYS = 0.50
                    FIXED_COST_21_DAYS = 12
                    if number_of_rental_days == 21:
                        total_cost = FIXED_COST_21_DAYS
                    elif number_of_rental_days == 3:
                        total_cost = number_of_rental_days * COST_PER_DAY
                    elif number_of_rental_days > 3 and number_of_rental_days < 8:
                        days_differnce = number_of_rental_days - 3
                        total_cost = (3 * COST_PER_DAY) + (days_differnce * COST_AFTER_3_DAYS)
                    elif number_of_rental_days > 8 and number_of_rental_days < 21:
                        days_differnce = 21 - 8
                        total_cost = (3*COST_PER_DAY) + (5*COST_AFTER_3_DAYS) + (days_differnce * COST_AFTER_8_DAYS)

                    print(f'The total cost for {number_of_rental_days} is ${total_cost}')
                    break
            case 2:
                print('You have chosen to return back to the main menu')
                time.sleep(1)
                return
            case _:
                print(Fore.RED + 'Invalid input. Please enter either option 1 - 2')
                input(Fore.RED + 'Please Enter to try again....')

        
# Main function
def main():

    # Opening message
    clear_screen()
    print(Fore.GREEN + Style.BRIGHT + "Welcome to Aurora Archive")  
    input('\nPress Enter to open the Main Menu...')


    while True:

        # Clear screen each time
        clear_screen()

        # Printing main menu function
        main_menu()

        # Obtain user input and check for errors
        try:
            main_menu_choice = int(input("Please select an option from 1 - 5: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please select an option from 1 - 5\n")
            input(Fore.RED + 'Press Enter to try again...\n')
            continue
        
        # Matching case to choice
        match main_menu_choice:
            case 1:
                print('You have selected Membership plans')
                membeship_plans()

            case 2:
                print('You have selected optional extras')
                optional_extras()

            case 3:
                print('You have selected reading challenge')
                reading_challenge()

            case 4:
                print('You have selected Aurora-Picks Rental Calculator')
                rental_calculator()

            case 5:
                print('You have selected to exit the program')
                print('From Aurora we thank you, and we hope to see you again')
                print('Exiting......')
                time.sleep(1)
                sys.exit()

            case _:
                print(Fore.RED + 'Invalid input. Please enter an option between 1 - 5')
                input(Fore.RED + 'Press enter to try again....')


# Executing main function
if __name__ == "__main__":
    main()

