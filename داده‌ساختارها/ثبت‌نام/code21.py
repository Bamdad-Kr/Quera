def check_registration_rules(**rules):
    result = []
    for mohtava in rules:
        result.append(mohtava)

    for user, password in rules.items():

        if len(user) < 4 or len(password) < 6:
            result.remove(user)
            continue

        if user == 'codecup' or user == 'quera':
            result.remove(user)
            continue
        
        if password.isdigit():
            result.remove(user)

    return result
