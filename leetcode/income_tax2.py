

annual_income = int(input("Enter your anual income Here : "))
taxable_income = annual_income - 250000
second_sal = taxable_income - 500000
third_sal = second_sal - 1000000


def tax_5per(taxable_income):
    tax = int(taxable_income * 0.05)
    return tax
def tax_20per(taxable_income):
    tax = int(second_sal * 0.2)
    return tax
def tax_30per(taxable_income): 
    tax = int(third_sal * 0.3)
    return tax

if taxable_income >= 250001 and taxable_income <= 500000:
    print("You have to pay 5% tax on your taxable amount ",tax_5per(taxable_income))

elif taxable_income >= 500001 and taxable_income <= 1000000:
        a = tax_20per(second_sal)
        b = taxable_income - second_sal
        c = tax_5per(b)
        total = a + c  
        print("One")
        print("Your Taxable amount is : " , total)

elif taxable_income >= 1000001:
        a = tax_20per(second_sal)
        b = taxable_income - second_sal
        c = tax_5per(b)
        d = taxable_income - third_sal
        e = tax_30per(third_sal)
        total = a + c + e
        print("Two")
        print("Your Taxable amount is : " , total)

else:
     print("You do not have pay any tax..!!")