
def saferegister(req):
    not_safe = ['/', '\\', '*', '#', '$', '^', ')', '(', '+', '-', '%', '!', '~', '?', '[', ']', '{', '}', '<', '>',
                '=']
    email_need = ['@', '.']
    email = req.json['username']
    password = req.json['password']
    repeate = req.json['repeate']
    if password == repeate:
        if email_need[0] in email:
            if email_need[1] in email:
                for x in not_safe:
                    if x in email:
                        return False
                        break
                    else:
                        if x in password:
                            return False
                            break
                        else:
                            return True
            else:
                return False
        else:
            return False

def safelogin(req):
    not_safe = ['/', '\\', '*', '#', '$', '^', ')', '(', '+', '-', '%', '!', '~', '?', '[', ']', '{', '}', '<', '>',
                '=']
    email_need = ['@', '.']
    email = req.json['username']
    password = req.json['password']
    if email_need[0] in email:
        if email_need[1] in email:
            for x in not_safe:
                if x in email:
                    return False
                    break
                else:
                    if x in password:
                        return False
                        break
                    else:
                        return True
    else:
        return False



