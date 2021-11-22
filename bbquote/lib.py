import requests

def get_quote():
    url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"
    result = requests.get(url).json()
    
    return f"{result[0]['quote']} \nsaid: {result[0]['author']}"

# if __name__ == "__main__":
#     quote = get_quote()
#     print(quote)
