# teapot-rasterizer
Renders wireframes 3d models in Applesoft BASIC for an apple 2. Includes the Utah Teapot model by default.
Custom 3d model display for an Apple 2, written in Applesoft Basic as a short project. 
For a quick demo, paste the file basic_program.txt into https://www.calormen.com/jsbasic/, and online apple 2 emulator.
By default, it includes the utah teapot model. If you would like to change this, teapotdatascraperOFFformat.py is the python program I made to convert the 3d model formats OFF into the format my program uses. The format is slightly more obscure than something like OBJ, but I needed it because that was the format of the utah teapot model I found.
To use the output of that program, paste the "data" output printed to console in place of lines 7000-onward, and change np and nf (lines 20 and 30) to nverticies and nfaces, respectively. xfst, yfst, and zfst (lines 120-140) can all be adjusted as wished to move the model around. The model can also be rotated by changing xrot, yrot, and zrot (lines 150-170), which are the rotations about the x, y, and z axis, respectively, applied pre-offset. 
