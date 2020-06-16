from urllib import request


def connect(host='http://google.com'):
    try:
        request.urlopen(host)
        return True
    except:
        return False


print('Conectado' if connect() else 'Offline')
