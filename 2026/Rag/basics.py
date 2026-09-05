from decimal import Decimal

tax_rate = Decimal('7.25') / Decimal(100)
purchase_amount = Decimal('2.95')
sumit = tax_rate * purchase_amount

print(sumit)
