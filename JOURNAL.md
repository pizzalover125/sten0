### 05/12: created idea + plan (20 min)
- created idea after seeing StenoKeyboard's outrageous pricing on https://stenokeyboards.com/products/the-uni-v4
- i've seen videos of people typing at crazy speeds with steno
- what if i made a cheap steno keyboard?
- v1 is going to be basic but i want v2 to be hotswap + RGB
- i could still do hotswap with this thing called "mill-max sockets"
  - they basically plug the PCB holes and make a regular MX footprint become hotswappable
  - require kapton tape
  - ok ill decide this later
- created the thing below
- was originally going to copy the StenoKeyboards layout but Taran told me to make it more unique so I tried doing that 
<img width="1003" height="466" alt="image" src="https://github.com/user-attachments/assets/838183e9-1de5-4a4a-b22a-350ab0566fd2" />
- ok ill first design w/o LEDs and then add them in v2
- goal of this project is to be ultra-polished in every way possible
  - want some sick renders  

### 5/13: expanded on plan, created initial BOM, figured out firmware (30 min)
- thought about required costs
- decided to make BOM for some reason

<img width="580" height="507" alt="image" src="https://github.com/user-attachments/assets/439e133b-8376-4244-82cc-56f5eac84dd9" />

- im going to source a lot of parts from Amazon
  - Aliexpress has misdelievered packages
  - lot easier to get parts, replace parts, etc.
- i alr have a bunch of Picos lying around so i'll use one of those
- PCB probably going to be around $20
- realized i need to figure out firmware because it is complex
- found Plover (most popular firmware)
- ok this is a bit weird but basically I can program the keyboard firmware to be like a regular keyboard but Plover will translate the regular keypresses to Steno

<img width="704" height="267" alt="image" src="https://github.com/user-attachments/assets/85eb8337-90c1-4a6a-a060-293325a3d843" />

- (in this image, I would set the top left key on my PCB to be a "W" on QWERTY which would be translate to the "T" sound on Steno
- ok i basically have firmware figured out!
- ill use a 7*4 matrix layout so I can get the 2 rotary encoders and make them keys
- i tried to draw out the matrix but its hard so ill prob just figure which keys are what after schematic done
- nvm ill use 3x10 cause its easier and i have enough keys and it would be easier to route

<img width="970" height="265" alt="image" src="https://github.com/user-attachments/assets/07a71782-ce72-4925-90fe-e771dd74f084" />

### 5/14: redid design + schematic + PCB (140 min)
- before starting the schematic, I wanted to look at other open source Steno boards
- found https://plover.wiki/index.php/DIY_steno_writers
  - they are cool, but none of them have encoders or OLEDs
- omg i just realized my layout is off
- i need another two keys on the left side
- i did not expect almost all steno keyboards to be not aligned?
- thats actually so weird, but ill change my design
- i also need to move the bottom row down by 1 unit
- how did i make all these mistakes wow

<img width="843" height="393" alt="image" src="https://github.com/user-attachments/assets/e3841258-1064-4761-afef-338f018ac056" />

- ok that was ez to fix
- time to hop on KiCad
- watching https://www.youtube.com/watch?v=8WXpGTIbxlQ to learn a little bit
- got matrix done
- using this https://pip-assets.raspberrypi.com/categories/610-raspberry-pi-pico/documents/RP-008309-DS-1-Pico-R3-A4-Pinout.pdf?disposition=inline

<img width="1155" height="764" alt="image" src="https://github.com/user-attachments/assets/33c4b271-5538-496b-a77d-d18f7e05a526" />

- schematic done! it was pretty ez
- assigned footprint
  - spent 5 minutes looking for EC11 + cherry mx footrpints but realized they were built in after alex told me
- time to start PCB!
  
  <img width="1189" height="420" alt="image" src="https://github.com/user-attachments/assets/25746456-65ac-40e2-91fe-779f18e90af8" />

- finished the keys, encoders, and pico placement; need to do diodes + OLED

<img width="959" height="365" alt="image" src="https://github.com/user-attachments/assets/e4f4d496-1cfc-466e-946d-90c648ac7ee9" />

- routing time!
- oops forgot to flip the diodes... ill do that rn!
- routed!

<img width="926" height="320" alt="image" src="https://github.com/user-attachments/assets/e686b3a7-6759-48c3-9f69-02fa45546c78" />

- added 3d models for keys
  - took so long for no reason
- added all the other 3d models... these were shorter!

<img width="697" height="221" alt="image" src="https://github.com/user-attachments/assets/383648ef-e66b-4cd0-ada1-46053d653374" />

- aight going to call it for a day but great progress today!
