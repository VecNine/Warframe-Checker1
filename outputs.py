import get_item_data

def get_outputs(extracted_list):
    max_outcome = 0
    most_optimal_buy = ""

    for i in extracted_list:
        try:
            prices = get_item_data.item_data(i)
            print(i, ": ", prices, "\n")

            if (max_outcome < int(prices[0])):
                max_outcome = int(prices[0])
                most_optimal_buy = i

        except:
            pass

    print("MOST OPTIMAL: - ", most_optimal_buy, " -\n")

    return
    