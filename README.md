# teapot-rasterizer
## A custom 3d model display for an Apple II, written in Applesoft BASIC as a short project. 
Renders wireframes 3d models in Applesoft BASIC for an Apple II. Includes the Utah Teapot model by default.

<img width="557" alt="Screen Shot 2021-06-28 at 9 04 53 PM" src="https://user-images.githubusercontent.com/28445400/123721508-7f540f80-d854-11eb-851e-eac13082efe3.png">

For a quick demo, paste the file basic_program.txt into https://www.calormen.com/jsbasic/, an online Apple II emulator.
By default, it includes the Utah Teapot model. If you would like to change this, teapotdatascraperOFFformat.py is a python program to convert the 3d model format OFF into the format my program uses. OFF is slightly more obscure than something like OBJ, but it was the format of the Utah Teapot model I found.
To use the output of the conversion program, paste the "data" output printed to console in place of lines 7000-onward, and change np and nf (lines 20 and 30) to nverticies and nfaces, respectively. xfst, yfst, and zfst (lines 120-140) can all be adjusted as wished to move the model around. The model can also be rotated by changing xrot, yrot, and zrot (lines 150-170), which are the rotations about the x, y, and z axes, respectively, applied pre-offset. 
