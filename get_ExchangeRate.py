import requests

def get_currency_rates():
    # Where USD is the base currency you want to use
    url = 'https://api.exchangerate-api.com/v4/latest/USD'

    # Making our request
    response = requests.get(url)
    data = response.json()

    # Your JSON object
    f = open("ExchangeRate.txt", "w")
    # print(type(data['rates']))
    # print(data['rates'])
    # f.write(data['rates'])
    for i, j in data['rates'].items():
        print(i, j)
        f.write(str(i) + ' : ' + str(j) + "\n")
    f.close()
    # print(type(data))
    return data['rates']

def get_currency_rates2():
    return requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()['rates']

if __name__ == "__main__":
    dict = get_currency_rates2()
    print(dict)