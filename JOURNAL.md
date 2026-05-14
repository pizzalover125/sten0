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
