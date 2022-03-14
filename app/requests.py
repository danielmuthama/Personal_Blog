import urllib.request, json





def get_quotes():        
        quotes_api_endpoint = 'http://quotes.stormconsultancy.co.uk/random.json'
        

        with urllib.request.urlopen(quotes_api_endpoint) as url:
            get_quotes_data = url.read()
            randomquotes = json.loads(get_quotes_data)

            return randomquotes

def get_quotes1():        
        quotes_api_endpoint = 'http://quotes.stormconsultancy.co.uk/random.json'
        

        with urllib.request.urlopen(quotes_api_endpoint) as url:
            get_quotes_data = url.read()
            randomquotes = json.loads(get_quotes_data)

            return randomquotes

def get_quotes2():        
        quotes_api_endpoint = 'http://quotes.stormconsultancy.co.uk/random.json'
        

        with urllib.request.urlopen(quotes_api_endpoint) as url:
            get_quotes_data = url.read()
            randomquotes = json.loads(get_quotes_data)

            return randomquotes


def get_quotes3():        
        quotes_api_endpoint = 'http://quotes.stormconsultancy.co.uk/random.json'
        

        with urllib.request.urlopen(quotes_api_endpoint) as url:
            get_quotes_data = url.read()
            randomquotes = json.loads(get_quotes_data)

            return randomquotes


def get_quotes4():        
        quotes_api_endpoint = 'http://quotes.stormconsultancy.co.uk/random.json'
        

        with urllib.request.urlopen(quotes_api_endpoint) as url:
            get_quotes_data = url.read()
            randomquotes = json.loads(get_quotes_data)

            return randomquotes


