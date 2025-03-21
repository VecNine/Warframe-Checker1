import requests
import re

def destrip_info(json_file):
    list_of_prices = []

    for i in json_file["payload"]["orders"]:
        if(i["user"]["status"] == "ingame" and i["order_type"] == "sell"):
            list_of_prices.append(i["platinum"])
    
    sorted_list_of_prices = sorted(list_of_prices)
    return(sorted_list_of_prices)
    

def request_conversion(item_name):
    
    match = re.match(r"(Prime(?: \w+)+) (.+)", item_name)
    if match:
        item_name = f"{match.group(2)} {match.group(1)}"
            
    item_name = item_name.lower().replace(' ', '_')

    return item_name

def item_data(item_url):
    if(item_url != ("Forma Blueprint" or "2 X Forma Blueprint")):
        item_url = request_conversion(item_url)
        base_url = "https://api.warframe.market/v1/items/"

        full_url = base_url+item_url+"/orders"
        
        response = requests.get(full_url)

        # print ("------------------\n", full_url,"\n" )
        
        if response.status_code == 200:
            return destrip_info(response.json())
        else:
            return {"error": f"Failed to retrieve data: {response.status_code}"}
    else:
        return "0 - Can't buy forma from the market!"

# if __name__ == "__main__":
#     item_url = "Dual zoren prime blade"  # Replace with the desired item URL name
#     data = get_item_data(item_url)
#     print(data)