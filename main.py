import get_item_data
import image_recognition
import outputs

if __name__ == "__main__":

    while(True):
        menu = input("Press enter to start, or 'q' to quit. ")
        if(menu != 'q'):
            ammount_of_players = 4

            outputs.get_outputs(image_recognition.screenshot_magic(ammount_of_players))

        else:
            quit()
    