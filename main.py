# TODO: easygui/tkinter
from time import sleep
from bs4 import BeautifulSoup
from requests import get
from os.path import exists
from os import system
from re import search

of = "output.txt"
def loop():
    counter = 0
    while 1:
        try:
            counter += 1
            print("Starting crawl #", counter)
            html = get("https://www.simulatorvibes.com/songhistory").content
            soup = BeautifulSoup(html, "html.parser")
            links = soup.find_all("a")

            outputfile = open(of, "a")
            for item in links:
                if "<a href=\"https://open.spotify.com/track/" in str(item):
                    track = search("(?<=[^>]>)([^<]*)", str(item)).group().replace("&amp;", "&")
                    spotify = search("https:\/\/open.spotify.com\/track\/[^\"]*", str(item)).group()
                    outputfile.write("%s - %s\n" % (spotify, track))

            outputfile.write("\n")
            outputfile.close()
            print("Waiting 3000s...")
            sleep(3000)
        except KeyboardInterrupt:
            print("Good bye!")
            sleep(1)
            break
        except:
            print("Error!")
            sleep(5)
            break



if __name__ == "__main__":
    if not exists(of):
        with open(of, "w"): pass
    system("title SimulatorVibes Crawler ^| STRG+C to close | iZer000")
    system("cls||clear")
    print("@@@@@@@@@@@@@@@@@@@%((%#((##@@#%%%%%%%%%%%%%%%%%%%\n@@@@@@@@@@@@@##(((((((#%&&&%((((((((%%%%%%%%%%%%%&\n@@@@@@@@@#(((((@@@@@@@@@@@@@@@&@@@@@((((%%%%%%%@@@\n@@@@@@@#(((@@@@@@@&@@@@@@@@&@@@@@@@@@@@&(((*&@@@@@\n@@@@%(((%@@@@@@@@@@@&@@@@@@&@@@@@@&@%&&&@&(((&%@@@\n@@@@((#@@@@@@,.......,@@@@@@@@&%(@@@@@@(#%@@@&%%@@\n@@(((&@@@..............@@((((((((@@@@@((((((((#(%@\n@#((@@@...............@@@((((((((@@@@((((((((@&((&\n(((&@@.......#@@@@@@@(&@&&(((((((@&&((((((((&@&(((\n(((&&@..............@@(@#%(((((((@#(((((((#%#%%&((\n(((((&@...............(%*/(((((((&(((((((%##,*((((\n(((%&((#&@@@@#........&/*(@(((((((((((((@%((%%&#((\n@((@@,,,,,.,.,,,,,,,,,&&&@@((((((((((((@@@@@@&@(((\n%#((,,,,,,,,,,,,,,,,@@@@@@@(((((((((((@@@@@@@@&((@\n%##,,,,,,,,,,,,,,,@@@&@@@&@@(((((((((@@@@@@@@#((%%\n%%#%((&@@@@@@@@@@@@@@@@@&@@&@@@@@@@@@&&&&&&&(((##%\n%%%%##(((@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@(((#%##%\n%%%%%%%%(((%@@@@@@@&@&@@@@@@@@@@@@@@@@@#(((*#####%\n%%%%%%%%%&#((((@@@@@@@@@@@@@@@@@@@@%((((@%#######%\n%%%%%%%%%%%%##%(((((((((###(((((((((%%%##########%\n")
    sleep(2)
    system("cls||clear")
    loop()