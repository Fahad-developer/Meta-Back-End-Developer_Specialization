#Using Control Flow

http_status = 501

if http_status == 200 or http_status == 201:
    print('success')
elif http_status == 400:
    print('Bad request')
elif http_status == 404:
    print('Not found')
elif http_status == 500 or http_status == 501:
    print('server error')
else:
    print('Unknown')


#Using Match
match http_status:
    case 200 | 201:
        print('success')
    case 400:
        print('Bad request')
    case 404:
        print('Not found')
    case 500 | 501:
        print('server error')
    case _:
        print('Unknown')