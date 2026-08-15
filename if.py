tier ="silver"
if tier == "gold":
    discount = 0.20
elif tier == "silver":
    discount = 0.10
else:
    discount = 0.0
print ("Discount for", tier, "tier is", discount * 100, "%") 