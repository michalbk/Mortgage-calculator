"""
This interactive script calculates monthly mortgage repayments.

TODO: file export
"""


def main():
    # input values - loan, monthly interest rate, number of months
    loan, r, n = get_user_input()

    # fixed values
    monthly_payment = calc_m_payment(loan, r, n)
    total_payment = monthly_payment * n
    total_interest = total_payment - loan

    print_header(loan, r, n, total_interest, monthly_payment)
    print_monthly_payments(loan, r, n)


def calc_m_payment(loan, monthly_rate, months):
    return loan * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)


def get_user_input():
    try:
        loan = float(input('How much would you like to borrow? '))
        r = (float(input('Enter an yearly interest rate in %: ')) / 100) / 12  # monthly interest rate
        n = int(input('How many years would you like to pay instalments? ')) * 12  # in months
    except ValueError:
        print('Invalid input. Only numbers accepted. Exiting now.')
        quit()
    else:
        return loan, r, n


def print_header(loan, r, n, total_interest, monthly_payment):
    print()
    print('{:20}{:,.0f} for {:.0f} year(s)'.format('Loan: ', loan, n/12))
    print('{:20}{:.2f} % yearly ({:.2f} % monthly)'.format('Interest rate: ', r*100*12, r*100))
    print('{:20}{:,.0f}'.format('Total interest: ', total_interest))
    print('{:20}{:,.0f}'.format('Total paid: ', monthly_payment * n))
    print('{:20}{:,.0f}'.format('Monthly payment: ', monthly_payment))


def print_monthly_payments(loan, monthly_rate, months):
    # table header
    print('=' * 76)
    print('|{:^11}|{:^20}|{:^20}|{:^20}|'.format(
        'Payment', 'Interest', 'Principal', 'Loan remaining'))
    print('=' * 76)

    monthly_payment = calc_m_payment(loan, monthly_rate, months)
    loan_remaining = loan  # initial value

    for month in range(1, months + 1):
        monthly_interest = monthly_rate * loan_remaining
        monthly_principal = monthly_payment - monthly_interest
        loan_remaining -= monthly_principal
        print('|{:^11}|{:^20,.0f}|{:^20,.0f}|{:^20,.0f}|'.format(
            month, monthly_interest, monthly_principal, loan_remaining))


main()
