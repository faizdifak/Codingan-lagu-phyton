from time import sleep
import time
import os
import sys

def print_lirik():
    lyrics = (
        "Aku yang jatuh cinta",
        "Haruskah kau yang kuberi kesempatan",
        "Ingin aku jadi kekasih yang baik",
        "Berikan aku kesempatan oh",
        "Tahukah dirimu?, tahukah hatimu?",
        "Berulang kuketuk, aku mencintamu",
        "Tapi dirimu tak pernah sadari",
        "Aku yang jatuh cinta <-_->",
    )
    delays = [7.2, 3, 2.5, 7.5, 3.5, 4, 3.5, 3.5]
    delay_per_karakter = 0.05  # delay per karakter dalam detik

    os.system('cls' if os.name == 'nt' else 'clear')

    for lyric, delay in zip(lyrics, delays):
        for karakter in lyric:
            sys.stdout.write(karakter)
            sys.stdout.flush()
            time.sleep(delay_per_karakter)
        print()  # Print newline setelah setiap lirik
        time.sleep(delay)  # Add a delay before printing the next line

print_lirik()