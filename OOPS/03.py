#WAP TO CREATE A CLASS ZOO WITH MINIMUM 3 CLASS PROPERTIES AND CREATE MINIMUM 2 OBJECTS.......

#class zoo:
#    a='anaconda'
#    b='buffalo'
#    c='cat'
#sonu=zoo()
#naina=zoo()
#print(zoo.a,zoo.b,zoo.c)
#print(sonu.a,sonu.b,sonu.c)
#print(naina.a,naina.b,naina.c)
#
#zoo.a='alligator'
#sonu.b='bear'
#
#print(zoo.a,zoo.b,zoo.c)
#print(sonu.a,sonu.b,sonu.c)
#print(naina.a,naina.b,naina.c)
#
#naina.c='cow'
#print(zoo.a,zoo.b,zoo.c)
#print(sonu.a,sonu.b,sonu.c)
#print(naina.a,naina.b,naina.c)


import winsound
import time

# Frequencies of notes (in Hz)
note_freqs = {
    'E': 330,   # E note
    'F': 349,   # F note
    'G': 392,   # G note
    'A': 440,   # A note
}

# Tune for "Ek Haseena Thi, Ek Deewana Tha"
tune = ['E', 'E', 'G', 'E', 'G', 'A', 'G',  # Ek Haseena Thi
        'E', 'E', 'G', 'E', 'G', 'F', 'E']  # Ek Deewana Tha

# Play the tune
for note in tune:
    winsound.Beep(note_freqs[note], 900)  # Play each note for 400 ms
    time.sleep(0.1)  # Short pause between notes
