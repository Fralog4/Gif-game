from PIL import Image
goku=r'C:\Users\Utente\Desktop\Goku.png'
goku1=r'C:\Users\Utente\Desktop\Goku1.png'
image1=Image.open(goku) #open first image
image2=Image.open(goku1) #open second image
gif=[image1,image2] #we need a list to put the two images together
output_gif_path = r'C:\Users\Utente\Desktop\gokuuu.gif' #specify the path where we want to save the gif
image1.save(output_gif_path, save_all=True, append_images=gif, duration=500, loop=0)
#save works only on image so we need to use it on one of the opened images
#first argument is where we want to save it
#append_images is the list of image to use
#duration=500 for long lasting and loop=0 because we want it infinite