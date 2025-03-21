import pyautogui as pg
import easyocr

def screenshot_analyser(ammount_of_players, counter):
    
    extracted_list = []

    if(ammount_of_players == 4):
        for i in range(4):
            print("Computing image ", i, "\n")
            reader = easyocr.Reader(['en'], gpu=True) 

            image_path = f"items_analyser/{str(counter-i-1)}.png"

            # Perform OCR
            results = reader.readtext(image_path)

            # Extract text from results
            extracted_text = " ".join([res[1] for res in results])
            extracted_list.append(extracted_text)
        
        return(extracted_list)
    else:
        return 0


def screenshot_magic(ammount_of_players):
    
    f = open("items_analyser/counter.txt", "r")

    try: 
        counter = int(f.read())

    except ValueError:
        print("ERROR:\n\nWrong item in counter.txt file!")
        return 0

    img_size_x = 236
    img_size_y = 48

    if(ammount_of_players == 4):
        rl = { #resolution list
            "0img_x": 479,
            "1img_x": 721,
            "2img_x": 963,
            "3img_x": 1205,
            "all_img_y": 412
        }

        for i in range(4):
            im = pg.screenshot(f'items_analyser/{str(counter)}.png', region=(rl[f"{i}img_x"], rl["all_img_y"], img_size_x, img_size_y))
            counter = counter + 1
            
        f.close()

        f = open("items_analyser/counter.txt", "w")
        f.write(str(counter))
        f.close()

    else:
        print("Other ammounts of players not implemented yet.")
        return 0

    return screenshot_analyser(ammount_of_players, counter)
