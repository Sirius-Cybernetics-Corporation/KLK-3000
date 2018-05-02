# KLK-3000

Program that searches for known bluetooth devices (by MAC address) and plays a song once that device is found. 

## TODO (immediate next steps and ownership)
  - DRG: Upload "new" multi-threading program. I will call it v2.x.x (as opposed to the old sequental program v1.x)
  - Implement feature requests (see below)

## Getting Started

Results may vary. Development and testing done using the following system:
  - Raspberry Pi 3 Model B v1.2
  - Raspbian 9 (stretch) installed using N00BS v2_4_4 
  
Other test systems:
  -

### Prerequisites & Installation


This might be more information than you need, but these are all the steps from a fresh pi installation done during testing/development. 

  -sudo apt-get update
  -sudo apt-get upgrade
  -sudo apt-get install python bluetooth
  
Set Timezone: 
  - sudo raspi-config
  -> Localization Options
  -> Change Time Zone
  -> Select Geographical Area
  -> Select city or region
  -> Finish
  
(optional) Enable VNC Server to view from another computer
  - sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer (already included in distro, oh well)
  - sudo raspi config
  -> Interfacing Options
  -> VNC -> Yes -> OK -> Finish
  - In terminal, run vncserver
  - Write down the address (e.g., 192.168.1.20:1)
  - On another computer install and run VNC Viewer (you may need to create an account)
  - Enter the address into the seach bar and press enter
  -> Continue
  -> Enter credentials (the default is pi, raspberry)
  
(optional) Enable SSH (helpful for running terminal remotely from another computer)
  - sudo raspi config
  -> Interfacing Options
  -> SSH
  -> Yes -> OK -> Finish
  -> Good idea to change password at this time too. 
  -> ifconfig (in terminal) to get ip address
  - Install Putty on another computer and open a connection using ip address (Eg., pi@192.168.1.20)
  -> Yes
  
  
## Running the program

Explain how to run the program & features

### Break down into each feature

Explain 

```
Give an example
```

## File Descriptions

  - KLK-3000.py - Main program. Includes GUI and functions. 
  - config.ini - Settings file with variables for end-user to edit. 
  - mac_addr.csv - File to store mac addresses and names of known devices. 
  - SongFiles - folder to store song files for devices. IMPORTANT: song name needs to match name in the csv file. For example, 
    the song file should be ford_prefect.wav for the device ford_prefect.
  - log.txt - log file for recording arrival activity

## Built With



## Contributing

Please contact <email> for contributing
  
## Feature Requests

Late Timer
 - When someone is late, instead of playing their song, play another file to shame them.

Time to Leave
 - Set a time to remind people it is time to leave for the day. 

## Versioning

develop versioning system

## Authors

David Grey

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

Select License?

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

