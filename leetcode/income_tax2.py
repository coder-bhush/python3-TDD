

# annual_income = int(input("Enter your anual income Here : "))

def calculate_income(annual_income):

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
        return tax_5per(taxable_income)

    elif taxable_income >= 500001 and taxable_income <= 1000000:
            tax_slab1 = tax_20per(second_sal)
            tax_slab2 = tax_5per(taxable_income - second_sal)
            
            total = tax_slab1 + tax_slab2 
            
            return total

    elif taxable_income >= 1000001:
            tax_slab1 = tax_20per(taxable_income - third_sal)
            tax_slab2 = tax_5per(taxable_income - second_sal)
            # d = taxable_income - third_sal
            tax_slab3 = tax_30per(third_sal)
            total = tax_slab1 + tax_slab2 + tax_slab3 
            
            return total

    else:
            return 0
    
calculate_income(800000)