import requests
import json


def main():
    """
    Returns dict with information about COVID-19 from over the world.
    All to have another information such as history or countries you should
    change the url to
    https://covid-193.p.rapidapi.com/statistics \n or to
    https://covid-193.p.rapidapi.com/countries

    """
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "Paste API key from rapidAPI"
        }
    
    if headers['x-rapidapi-key'] == "Paste API key from rapidAPI":
        print("YOU FORGOT TO ENTER API KEY")
        return None

    response = requests.request("GET", url, headers=headers)

    with open('results_hw1.json', 'a') as fp:
        json.dump(response.json(), fp, indent=2)
    fp.close()


if __name__ == "__main__":
    main()