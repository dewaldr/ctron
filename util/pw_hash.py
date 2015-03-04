from werkzeug import check_password_hash, generate_password_hash


a = raw_input('Enter the password: ')
b = raw_input('Re-enter to confirm: ')


if a == b:
    pw_hash = generate_password_hash(a)
    print pw_hash

else:
    print "Passwords did not match"
