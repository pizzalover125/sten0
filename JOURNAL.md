# journal

17.75 hrs total

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

### 5/15: part 1: firmware (50 minutes)
- new day; no school!
- wanted to fully figure out the firmware aspect
- found the NKRO layout for https://nolltronics.com/product/picosteno/
  - NKRO is basically a setting you can change on your QWERTY keyboard to actually register all the keys you press at the same time

<img width="1164" height="359" alt="image" src="https://github.com/user-attachments/assets/360618a4-5249-4299-90e4-315ea0ac84c4" />

- basically, ill code firmware w/ regular QMK/KMK and itll be normal keyboard firmware.
- user runs Plover software on their computer
- Plover converts each regular key press to steno
- this way, I can have the OLED + rotary encoders be super easy to code up
- i removed the labels from the front + back silkscreen to make it look better / cleaner
- ill do only firmware today
- i created the keymap:
  
column 1: Q W E R T Y U I Y P [
column 2: A S D F T O J K L ; '
column 3: 2 C V [mute/unmute] [video on/off] N M 8 '

- this looks super simple but it isn't bc i messed up in schematic / placement and some of the keys were swapped around; instead of rerouting, imo fixing it in firmware is better and faster and thats what I did
- wait nvm i messed up; this should be good:

column 1: Q W E R T Y U I Y P 
column 2: A S D F T O J K L ; 
column 3: 2 C V [mute/unmute] [video on/off] N M 8 ' [

- im creating firware w help of Claude (pretty hard to do firmware w/o parts)

### 5/15: part 2: mounting holes (15 minutes)
- adding the mounting holes
- watching https://www.youtube.com/watch?v=TDL3USgDEM0
- realized I only have to press "a" and add M2 hole
- need to position it properly

<img width="703" height="274" alt="image" src="https://github.com/user-attachments/assets/aa62082c-2fbd-481b-92ae-bba00febe910" />

- i want to make the PCB black (or white i haven't chosen yet)

<img width="883" height="313" alt="image" src="https://github.com/user-attachments/assets/178d99cb-a5b0-478e-a760-d07093cea560" />

- looks pretty mid ngl
- okay time to do case
- idk what software to use
- ehhh ill just design a logo today
- time to hop on figma
- nvm my internet went out??????????? why did this happen to me
- uhhhh ig i can't do much so ill end it here for today... unless it comes back

### 5/16: render + polish (120 minutes)
- BRUHHHH MY WHOLE JOURNAL for today GOT DELETED
- basically, I was learning how to Render KiCad
- It was this crazy thing where I had to downgrade KiCAD to 9.0 and then upgrade to 10.0
- I downloaded Blender and Fusion and tried to Render but it wasn't working
- I watched like 5 YT videos trying to figure it out
- So I ultimately decided to have no render
- I added mounting holes + logos

<img width="706" height="323" alt="image" src="https://github.com/user-attachments/assets/9f2b8c7d-9d3d-4f0b-a84e-f4906890a788" />

- made back panel

<img width="728" height="493" alt="image" src="https://github.com/user-attachments/assets/b35eb90c-1faf-449a-a6cc-acec0179cc6f" />

- tried to export from KiCAD as STEP but it doesn't work?
- ok that was a weird bug; i just had to redraw the outline

<img width="1211" height="519" alt="image" src="https://github.com/user-attachments/assets/143825d8-5359-4867-beaf-38b63598382a" />

- pretty basic, ngl
- idk where to add polish
- first im going to add keycaps to make it look better
- nvm no keycaps bc very tedious
- asked for help on Slack: https://hackclub.slack.com/archives/C0B0CADUV3P/p1778990312121819

<img width="1035" height="341" alt="image" src="https://github.com/user-attachments/assets/c53ed315-2d9c-4a1b-b074-c4b5e44e6160" />

- what do we think? it looks pretty sick ngl
- idk what else to add for polish
- will look at approved keebs on hardware.hackclub.com
- liked https://github.com/KaiPereira/PR1SM, https://github.com/sudo-apt-install-tap/TaoTeChing, https://github.com/code2344/SplitCodeBoard, https://github.com/meepodeep/ErgoDecks
- ok all of them are pretty standard and i lowk didn't gain much inspiration
- note to self: need to split the keyboard in half to print it
- wait I can just do that in the Bambu Slicer; ok ill just do that
- ok i think plan now is to finalize and then submit
- start w/ BOM

<img width="1265" height="450" alt="image" src="https://github.com/user-attachments/assets/4352d4af-7238-42e1-8907-a6870afe64ca" />

- im genuinely shocked by this
- time to see JLC.. doesn't work?
- ok time to sleep; will see tmrw

### 5/17: polish + BOM (180 minutes)
- started off with a BOM
- wait if I get some more switches I can build 2 keyboards
- ok $6 more for +1 keyboard is not bad
- soooooo that comes down to $67.64 for two keebs or $33.82 for two
  - doesn't include 3d printed case but thats not too bad
- acon told me to look at other keyboard companies
- polish #1: logo on back

<img width="739" height="401" alt="image" src="https://github.com/user-attachments/assets/7cfe024f-0eb3-49cf-86c7-3a385ad443b7" />

- watched https://www.youtube.com/watch?v=YR1xkOp5U1g
- just realized I forgot screws in BOM
- ok apparently i can just use M2x3 without any hex nuts.
- adding to BOM
- ok $80.43 now; still cheaper than an Asterik
- ok going to scroll more on hardware.hackclub.com
- wait b4 that I wanted to round all corners

<img width="1435" height="566" alt="image" src="https://github.com/user-attachments/assets/756ba424-0802-4c3a-93cb-77553fbdc409" />

- wait i don't need mounting holes if tolerance is tight enough
- idk ill still keep them

<img width="1045" height="577" alt="image" src="https://github.com/user-attachments/assets/9197a7cf-7fb0-48a9-a898-d0842114895a" />

- rounded literally every corner
- idk what else to make this polished
- ok ive seen so many other keyboards and don't see how mine isn't as polished...
- made PCB shorter
- ok im going to reroute everything to make routing better
- moving two diodes below encoders bc they seem kinda weird
- looks better

<img width="266" height="351" alt="image" src="https://github.com/user-attachments/assets/3105cc9c-f4a2-43e7-8b88-8c8f589a9603" />

- rerouted everything!

<img width="1167" height="471" alt="image" src="https://github.com/user-attachments/assets/b9df68bc-9061-45a8-beb3-102deffbe778" />

- ok imma make a 3d model of the key + keycap
- WHY ALL KEYCAPS ARE SLANTED OMG MGOMOGMOGMOGM
- looks pretty slick NGL

<img width="742" height="370" alt="image" src="https://github.com/user-attachments/assets/2cbbbdab-2898-4c0f-bce6-1eee1ba9efa9" />
<img width="741" height="295" alt="image" src="https://github.com/user-attachments/assets/91527503-1562-47f0-b3a3-256ca54fefeb" />

- ill create a rotary encoder w/ cap as well

<img width="725" height="383" alt="image" src="https://github.com/user-attachments/assets/9ca9a0b3-c3d9-4414-86cc-812ce0f19df3" />

- time for render!
- not working on render?
- ok its fine 
- added README... ready to submit!

### 5/17: part 2: fixing CAD (15 minutes)
- after I uploaded the thing on Slack, Taran told me I needed some sort of support for the pins
- after a lot of help by him, I made the thing below:

<img width="343" height="279" alt="image" src="https://github.com/user-attachments/assets/aa1dae57-6e44-41e9-abb0-78e5b7880b27" />

- Taran said it looks good so :yay:
- okay he said to extrude something on bottom
- ill do that later
- ok turns out i also need standoffs for OLED
- will do
- wait i can't extrude a logo or something on bottom bc im splitting it in half

### 5/21: project rejected (1 hr)
- project got rejected... 😭
- got rejected for design which i can understand
- need to make design more cohesive
- no exposed PCB ig
- ok ill make basic face plate then ill spice it up
- nvm ill just create a cool render
- the encoder keeps bugging out; need a fix
- tried like 5 diff models and tweaked a bunch of settings and it worked!

<img width="731" height="259" alt="image" src="https://github.com/user-attachments/assets/e3ed03e8-3ad0-433b-8ca0-defdd115289c" />
<img width="1197" height="267" alt="image" src="https://github.com/user-attachments/assets/513995c3-f446-498f-af5c-2953eea99808" />
<img width="850" height="324" alt="image" src="https://github.com/user-attachments/assets/0535d998-d9b1-49d6-88a9-c3221efee283" />
<img width="590" height="399" alt="image" src="https://github.com/user-attachments/assets/a8d1d40f-a583-4556-8639-b64b67ae01d0" />

### 5/22: CAD CAD CAD nvm i switched to designing quality PCB (3hr)
- ok time to make a better CAD!
- im thinking i'll do a simpler backplate design with a cool frontplate so its basically a sandwich
- nvm this is too hard
- im switching to exposed PCB style
- time to look for inspo
- watching https://www.youtube.com/watch?v=82yD0RMeEw8
- i came up with the following but it doesn't seem like enough

<img width="1078" height="600" alt="image" src="https://github.com/user-attachments/assets/2ba26202-b663-4582-820d-7f38fa4f720b" />

- OMG IVE BEEN TRYING TO MAKE A CUTOUT FOR USB AND ITS NOT WORKING AHHHHH
- going to redo the PCB layout
- making it low profile now
- removing encoders; bulky and don't look good
- hotswap also cause why not
- nvm no hotswap cause i don't really need it personally

<img width="1036" height="385" alt="image" src="https://github.com/user-attachments/assets/9fc2ff81-ef35-4fb7-bf30-390277d1c5c5" />

- using only what i need

<img width="1138" height="402" alt="image" src="https://github.com/user-attachments/assets/69014b11-b78c-47ba-8b1d-0fe9f4b68fe3" />

- routed but just realized its not symetrical 😭
- ok figuring out how to round corners
- figured it out! you just use arcs and move the lines
- acon was right; this feels super nice
- ok time for routing!
- OMG I DID IT WITH 0 VIAS

<img width="1382" height="432" alt="image" src="https://github.com/user-attachments/assets/0e904f86-ce26-4d38-bf47-9078e8fa6f81" />

- im going to create a cool render now
- first i added back silkscreen art

<img width="668" height="365" alt="image" src="https://github.com/user-attachments/assets/8ef9adc0-038f-422d-9085-663f47a56327" />

- renders are awesome

<img width="842" height="297" alt="image" src="https://github.com/user-attachments/assets/4f81e6b6-27b1-46fa-8bf9-0b1534e311c9" />
<img width="863" height="294" alt="Screenshot 2026-05-22 at 8 03 14 PM" src="https://github.com/user-attachments/assets/86f5d0e5-0527-4330-96ce-c5dd262c8ab3" />

- there were these random "K"s next to the diodes, so I removed them
- need to figure out where mounting holes go
- wait i dont need them cause i can just press fit with supports
- created dimensions

<img width="1380" height="490" alt="image" src="https://github.com/user-attachments/assets/d7860d81-8021-4b05-afd5-ed14f82b2811" />

- according to my calculations, i need two rectangles; one that is 252x35 and another that is 147x26. 1mm filets

<img width="1233" height="383" alt="image" src="https://github.com/user-attachments/assets/f71b9514-fc57-4120-9045-580edcddd933" />

- idk if this will work
- added things in middle:

<img width="1206" height="338" alt="image" src="https://github.com/user-attachments/assets/8258f147-8040-4d55-9669-d842c3ce7f31" />

- added cutout!

<img width="211" height="170" alt="image" src="https://github.com/user-attachments/assets/8bb05cdf-01ee-4eb5-b6b1-0a8e612ed10a" />

- going to render this

<img width="863" height="396" alt="image" src="https://github.com/user-attachments/assets/b9d89b97-4096-4dc4-8b13-a8bc81232aef" />

- keys may not be able to be pressed

### 5/23: day of shipment (4hr)
- added 1mm more of spacing

<img width="982" height="330" alt="image" src="https://github.com/user-attachments/assets/7b25a9a8-7044-47c1-9c3b-bca090d2e9e3" />

- but now i can't 3d print it.
- im thinking to reduce space between Pico and rest

<img width="1394" height="519" alt="image" src="https://github.com/user-attachments/assets/3d73f2fa-9e93-4a11-b62d-bee94ffcb2b4" />

- made it smaller + moved diodes to back
- only 249mm wide
- dimensions: 249x37, 141x26
- 3d modeling time

<img width="802" height="113" alt="image" src="https://github.com/user-attachments/assets/183f4d7c-41c1-4d3f-89ce-9ba6ac0f947e" />

- w cutout
- and i made a render!

<img width="859" height="296" alt="image" src="https://github.com/user-attachments/assets/fa804dc0-2d8c-4bd5-acb3-5b5d286186ef" />

- nvm i need screws apparently
- ahhhhhh have to redesign it again
- wait let me create BOM

<img width="437" height="136" alt="image" src="https://github.com/user-attachments/assets/42ef6f4e-5d31-45ca-8e37-a97062dcbea0" />
<img width="1052" height="775" alt="image" src="https://github.com/user-attachments/assets/01cd5379-e908-449d-ae32-e934b075b149" />

- $53 flat is pretty good ngl
- ok back to case design
- watching this https://www.youtube.com/watch?v=cLz7wpwAEoI
- learned a lot about how to make it exposed PCB
- but ill just have a front panel ig

<img width="892" height="405" alt="image" src="https://github.com/user-attachments/assets/f8cd2cdb-48fc-4519-9916-02e182dbdf7a" />

- going to use https://kbplate.ai03.com/ for cutouts
- ok i have no idea on how to do this
- idk what dimensions to use
- i have all of it imported; asked on Slack on how to do it; will continue work after
- actually let me fully prepare the BOM
- lets ring up the PCB cost on JLC
- $21.08... nice!
- let me create BOM.csv
- ok going to upload all PCB files through a Codespace
- added everything except the CAD and CAD images in README
- time to go back to doing CAD! (started 220)
- watching https://www.youtube.com/watch?v=7azQkSu0m_U
- not helpful at all
- manually did it

<img width="992" height="466" alt="image" src="https://github.com/user-attachments/assets/95e4b81b-5aac-4724-8482-05e5be61b17e" />

- cool section view
- ok i made it so the holes are invis
- cutout in middle also
- going to test out micro-usb cable
- it fits!

<img width="1035" height="337" alt="image" src="https://github.com/user-attachments/assets/95ddc964-23e8-417c-b6b4-7a4c681b0d9a" />

- voila!
- ok preparing for submission again

### 06/02: updating README (15 min)
- Raygen told me to update it with more details on my exact layout
- sounds like a great idea so ill do it!
- experimenting with https://stenokeyboards.com/products/the-uni-v4 and https://opensteno.org/demo/

<img width="926" height="625" alt="image" src="https://github.com/user-attachments/assets/3cb6465d-ec42-4dce-8ae4-fbaf1d7b7a0f" />

- done!
- i have both QWERTY and STENO
- will update README with more info

# BUILD
Jun 25: 5 hours

### soldering
- Recieved all the parts today
- Was NOT expecting to get the PCBs this quick
- But very excited nonetheless
- Got straight to building
- Recorded my soldering cause why not
- Started with diodes
- Diodes were pretty simple, just pretty sharp
- switches slotted right in; no frills
- Pico was pretty hard to solder
- I moved Pico to a breadboard to solder headers
- there were bridges, but easy to remove
- but when i put them on the board, something went wrong
- THERE WERE SO MANY SOLDER BRIDGES
- I thought I could just remove the bridges like normal... right?
- NOPE! They just wouldn't come off
- I WAS SO MAD
- I had to switch the soldering iron tip a couple of times
- and eventually, they worked!

### firmware
- when I plugged it in; nothing lit up
- i was devestated; did I mess up something?
- did I fry the pico?
- i frantically connected and reconnected the cable
- nothing happened
- i remembered... this pico doesn't like my USB-C port and needs a USB-A cable
- the pico lit up!
- i was really happy but also nervous about the firmware not working
- i uploaded the firmware
- and it didn't work
- oh wait i just needed to add the missing folder
- i added the kmk folder
- still nothing
- seems like my firmware was broken
- i used the getting started guide by KMK
- one key worked!
- it was time to figure out the other keys
- i manually added the other GPIO pins and the keys
- it was a tedious process, but i eventually got all but 3 working properly
- these three were confusing cause they just didn't register
- i tried changing some values aruond but nothing seemed to work
- after a long time, i realized i had entered 20, 21 instead of 19, 20
- when i made that super simple fix, it worked!
- i was actually so thrilled
- this was my first built hardware project other than my hackpad
- i was also happy because i don't need to worry about ordering another PCB cause this one works
- I have a 3D printer so I can tweak the design as needed

### 3d print
- I wasn't sure if my white filament was enough
- so i switched it to black
- but it didn't end up working after multiple failed prints
- so im moving back to black
- ok it printed
- but it doesn't fit
- need to tweak the model
- i printed a keycap
- it fits!
- didn't like the design tho
- going to use this simple one: https://www.printables.com/model/700878-simple-choc-v1-flat-keycaps/files

<img width="142" height="322" alt="image" src="https://github.com/user-attachments/assets/17210c9f-7f5c-4be4-95c5-28e1abe137d8" />

- printed! looks super clean
- redesigning the thing now
- wait nvm i can just cutout the pins
- it fits!
- WHAAAT THE KEEB DOESN'T WORK ANYMORE
- NOOOOOOOOOOO
- fixed it!
- it was a messy solder connectionm
- shoutout to @Naytik on slack for the help
