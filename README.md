<h1> BatteryMonitor </h1>
<h2> How it works ?</h2>
It says the battery level for certain battery levels.
<h2>Customization</h2>
Almost all important settings are inside src/constants.py file ( if you think more should be added open an issue :P )

- BATTERY_LEVEL_CHECK_INTERVAL - interval in seconds of checking battery level
    - Default 30 seconds - battery will be checked every 30 seconds
- BATTERY_LEVEL_TRIGGERS - which battery levels should trigger speaker
  - Default - 20%, 15%, 10%-1%
  - Battery level will be said once it hits given trigger
  - Multiple triggers can be triggered at once ( if triggers are 10 and 9 but battery level will jump from 11% to 8%, battery level will be said once ) 
  - Trigger is reseted when battery level is greater from it
<h2>Why it is needed ?</h2>
It's hard to tell what the battery level is sometimes, and system warning can be not enough / too late
<h2>What is needed ?</h2>

  - python3
    - On Arch / SteamOs  - sudo pacman -S python3
  - espeak
    - On Arch / SteamOs  - It needs to be installed from AUR
<h2>How to run it ?</h2>
  
  - ./start.sh <- starts program
  - ./start.sh ut <- starts uts
  - ./start.sh it <- starts its ( not much here for now )
  - ./start.sh all <- starts uts and its
