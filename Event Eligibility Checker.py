person_age = 20 
has_vip_pass = (True)

if person_age >= 18 and has_vip_pass:
    print("Eligible")
elif person_age >= 65 or not has_vip_pass:
    print("Eligible")
else:
    print("Rejected")