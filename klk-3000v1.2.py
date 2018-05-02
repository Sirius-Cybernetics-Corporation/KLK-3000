#David Grey. May 5, 2015
#Edited by SGR May 1, 2018
#Program for Bluetooth Presense to play WWE-Style Intro Songs.  
#To add a device:
#1) Lookup mac address using hcitool scan OR Pair devices using bluetooth manager
#2) Copy the address to the #Mac address varaibles
#3) Create a new "if chunk" for the device in the code below
#4) Add variables to #Variables (below) and a song to the SongFiles if you haven't done so already

import bluetooth
import time
import os
import pygame
pygame.mixer.init()

#Variables: Indicates if song has been played (1) or not (0)
cmb = atr = laf = ems = pbs = ixf = sgr = rjc = 0

#Mac address variables:

cmb_mac = '00:00:00:00:00:00'
atr_mac = '00:00:00:00:00:00'
laf_mac = '00:00:00:00:00:00'
ems_mac = '00:00:00:00:00:00'
pbs_mac = '00:00:00:00:00:00'
ixf_mac = '00:00:00:00:00:00'
sgr_mac = '00:00:00:00:00:00'
rjc_mac = '00:00:00:00:00:00'


#While loops forever. Resets variables at time 'hora' (midnightish)        
while True:
    hora = time.strftime("%H:%M", time.localtime())
    print (time.strftime("%H:%M:%S", time.localtime()) + " Searching...")
    if (hora == '02:45'):
        print ("Restarting Raspberry Pi...")
        os.system("sudo shutdown -r now")
    else:
        pass
    

#cmb
    if (cmb == 0):
        result = bluetooth.lookup_name(cmb_mac, timeout=3)
        if (result != None):
            print ("Person 1 has arrived!")
            pygame.mixer.music.load("/home/pi/SongFiles/cmb.wav")
            pygame.mixer.music.play()
            cmb = cmb + 1
    else:
        pass

#atr
    if (atr == 0):
        result = bluetooth.lookup_name(atr_mac, timeout=3)
        if (result != None):
                print ("Person 2 has arrived!")
                pygame.mixer.music.load("/home/pi/SongFiles/atr.wav")
                pygame.mixer.music.play()
                atr = atr + 1     
    else:
        pass

#laf
    if (laf == 0):
        result = bluetooth.lookup_name(laf_mac, timeout=3)
        if (result != None):
                print ("Person 3 has arrived")
                pygame.mixer.music.load("/home/pi/SongFiles/laf.wav")
                pygame.mixer.music.play()
                laf = laf + 1     
    else:
        pass
#ems
    if (ems == 0):
        result = bluetooth.lookup_name(ems_mac, timeout=3)
        if (result != None):
                print ("Person 4 has arrived!")
                pygame.mixer.music.load("/home/pi/SongFiles/ems.wav")
                pygame.mixer.music.play()
                ems = ems + 1
    else:
        pass
#pbs
    if (pbs == 0):
        result = bluetooth.lookup_name(pbs_mac, timeout=3)
        if (result != None):
                print ("Person 5 has arrived!")
                pygame.mixer.music.load("/home/pi/SongFiles/pbs.wav")
                pygame.mixer.music.play()
                pbs = pbs + 1
    else:
        pass



#ixf
    if (ixf == 0):
        result = bluetooth.lookup_name(ixf_mac, timeout=3)
        if (result != None):
                print ("Person 6 has arrived!")
                pygame.mixer.music.load("/home/pi/SongFiles/ixf.wav")
                pygame.mixer.music.play()
                ixf = ixf + 1     
    else:
        pass    

#sgr
    if (sgr == 0):
        result = bluetooth.lookup_name(sgr_mac, timeout=3)
        if (result != None):
                print ("Person 7 has arrived!")
                pygame.mixer.music.load("/home/pi/SongFiles/sgr.wav")
                pygame.mixer.music.play()
                sgr = sgr + 1     
    else:
        pass

#rjc
    if (rjc == 0):
        result = bluetooth.lookup_name(rjc_mac, timeout=3)
        if (result != None):
                print ("Person 8 have arrived!")
                pygame.mixer.music.load("/home/pi/SongFiles/rjc.wav")
                pygame.mixer.music.play()
                rjc = rjc + 1
    else:
        pass

#tbii
#    if (tbii == 0):
#        result = bluetooth.lookup_name(tbii_mac, timeout=3)
#        if (result != None):
#               print "Future entry!"
#               pygame.mixer.music.load("/home/pi/SongFiles/tbii.wav")
#               pygame.mixer.music.play()
#               tbii = tbii + 1
#    else:
#        pass


