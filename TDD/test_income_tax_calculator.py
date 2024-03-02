""" 
Calculate taxes have to pay on annual income :

  1)  Anual Income < 2.50 Lakhs 
         0

  2)  Anual Income > 2.50 and <  5 Lakhs
         5% tax on taxable amt

  3)  Anual Income > 5 Lakh and < 10 Lakhs
         20% tax On Taxable amt

  4)  Anual Income more than 10 Lakhs 
         30% tax On Taxable amt            """




def income_tax_calculator(annual_income):
    taxable_income = annual_income - 250000

    # Declare some functions to calculate taxes :
    def tax_5per(taxable_income):
        tax = int(taxable_income * 0.05)
        return tax

    def tax_20per(second_sal):
        tax = int(second_sal * 0.2)
        return tax

    def tax_30per(third_sal):
        tax = int(third_sal * 0.3)
        return tax

    # filtering taxable amount by annual income :
    if annual_income <= 250000:
        return 0

    elif annual_income >= 250001 and annual_income <= 500000:
        return tax_5per(taxable_income)

    elif annual_income >= 500001 and annual_income <= 1000000:
        if taxable_income >= 500001:
            second_sal = taxable_income - 500000
            first_sal = taxable_income - second_sal
            return tax_20per(second_sal) + tax_5per(first_sal)
        else:
            return tax_5per(taxable_income)

    elif annual_income >= 1000001:
        if taxable_income >= 500001 and taxable_income <= 1000000:
            second_sal = taxable_income - 500000
            first_sal = taxable_income - second_sal
            return tax_20per(second_sal) + tax_5per(first_sal)
        elif taxable_income >= 1000001:
            second_sal = taxable_income - 500000
            first_sal = taxable_income - second_sal
            third_sal = second_sal - 1000000

            if third_sal > 0:
                return (
                    tax_20per(second_sal) + tax_5per(first_sal) + tax_30per(third_sal)
                )
            else:
                return tax_20per(second_sal) + tax_5per(first_sal)


# Test cases :


def test_taxfree_income():
    expected_res = income_tax_calculator(200000)
    assert expected_res == 0


def test_income_is_more_than_two_lakh():
    expected_res = income_tax_calculator(300000)
    assert expected_res == 2500


def test_income_is_more_than_five_lakh():
    expected_res = income_tax_calculator(700000)
    assert expected_res == 22500


def test_income_is_more_than_five_lakh():
    expected_res = income_tax_calculator(900000)
    assert expected_res == 55000


def test_income_is_ten_lakh():
    expected_res = income_tax_calculator(1000000)
    assert expected_res == 75000


def test_income_is_more_than_ten_lakh():
    expected_res = income_tax_calculator(1300000)
    assert expected_res == 135000


def test_income_is_more_than_ten_lakh():
    expected_res = income_tax_calculator(1800000)
    assert expected_res == 250000
