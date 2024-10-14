def count_password_strength(password):
    criteria_count = 0

    if any(c.islower() for c in password):
        criteria_count += 1

    if any(c.isupper() for c in password):
        criteria_count += 1

    if any(c.isdigit() for c in password):
        criteria_count += 1

    special_symbols = "!\"#$%&'()*+"
    if any(c in special_symbols for c in password):
        criteria_count += 1

    if len(password) >= 8:
        criteria_count += 1

    return criteria_count


password = input()
result = count_password_strength(password)
print(result)
