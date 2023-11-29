from validate_email import validate_email

is_valid1 = validate_email('allankiprop174332323@gmail.com', verify=True)
is_valid2 = validate_email('allankiprop@gmail.com', verify=True)
is_valid3 = validate_email('allan@allan.com', verify=True)


if is_valid1:
    print('Valid')
else:
    print('Invalid')

if is_valid2:
    print('Valid')
else:
    print('Invalid')

if is_valid3:
    print('Valid')
else:
    print('Invalid')