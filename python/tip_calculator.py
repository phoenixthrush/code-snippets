# first homework, tip calculator by phoenixthrush

# asking for user input as a float and setting it to the variable "bill" and replacing the dollar sign with nothing
bill = float(input("how much did your meal cost? ").replace("$", ""))

# calculating the taxes with 15, 18 and 20 percent
tax_amount_15 = bill / 100 * 15
tax_amount_18 = bill / 100 * 18
tax_amount_20 = bill / 100 * 20

# printing out the result and rounding the result to the second decimal point
print("recommended tip amounts are: \n ")
print(f"- for 15% of taxes: ${tax_amount_15:.2f}")
print(f"- for 18% of taxes: ${tax_amount_18:.2f}")
print(f"- for 20% of taxes: ${tax_amount_20:.2f}")
