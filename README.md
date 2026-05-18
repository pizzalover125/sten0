# sten0: the best stenography keyboard
sten0 is a minimalist, cheap steno board. it was meant to defeat the industry standard Uni v4. it uses a 2-layer PCB and KMK firmware that converts to stenography with Plover. 

<img width="1035" height="341" alt="image" src="https://github.com/user-attachments/assets/9dbfd9b3-72da-4909-82cf-9539d38a1004" />

### what is steno?
traditional stenography keyboards are keyboards used by transcribers at justices to type extremely fast. hobbyists and now companies have created their own versions of steno keyboards. one can easily get 200 wpm using steno, demonstrated in the video here: https://www.youtube.com/watch?v=l8SWkR5y774. 

the company, stenokeyboards.com, is the leader of the steno industry with products that are pretty cool, but extremely expensive and lacking features. there are other steno keyboards, but they are either super expensive or do not have any features other than steno. i wanted to build a feature-packed stenography keyboard that is still cheap. 

### features
- 28x MX keys
- 0.96" OLED display
- 2x rotary encoders to control everything
- ~$50/full keyboard with 3D-printed keycaps and case

### PCB + Schematic
I used KiCad for the PCB design. The silkscreen art was created using https://www.fontspace.com/ and inputted to KiCad using the built-in Image Convertor tool.

<img width="712" height="502" alt="image" src="https://github.com/user-attachments/assets/17c78bb6-1210-4e29-b60e-f2de2616d9a8" />
<img width="811" height="361" alt="image" src="https://github.com/user-attachments/assets/2250a4b4-c687-41cd-9d28-4649a590f690" />
<img width="725" height="383" alt="image" src="https://github.com/user-attachments/assets/6cb3fec4-ae82-48f8-ad84-396f5681bf3c" />

### CAD
I used Onshape for the entire CAD. It's pretty basic, as I wanted to have an exposed PCB. To achieve this, the design only features a backplate. The case uses M2x3 screws to hold everything in (including OLED!). Split in half in Slicer to print on a regular sized printer bed.  

<img width="1451" height="574" alt="image" src="https://github.com/user-attachments/assets/63cf98a7-1206-4cbf-a3d4-17cdc3985e31" />

### Firmware
There is a matrix that links to QWERTY layout which will be converted to Steno layout with Plover. 

### BOM
A detailed Bill of Materials can be found at https://docs.google.com/spreadsheets/d/1TjUF5DwXCz-duM485mYQtrJNJa8_saizqugbLS9kPO8/edit?gid=0#gid=0!

### Credits
Big thanks to Hack Club for funding the project + providing a LOT of help!
