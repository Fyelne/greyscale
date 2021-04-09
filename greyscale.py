from PIL import Image
import glob, os, shutil, errno, math
i=0 #Progress index
dirnumber=0

infile = 'Example : C:\\Users\\myuser\\Desktop\\' #Source folder (don't forget \\ at the end)
outfile= 'Example : C:\\Users\\myuser\\Desktop\\New folder\\' #Destination folder (It need to didn't exist)

def ig_f(dir, files): #Copy folder hierarchy
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

try : 
  shutil.copytree(infile, outfile, ignore=ig_f)
except:
  print("Folder already exist")


for root, dirs, files in os.walk(infile, topdown=False): #Check the number of folder for progress
  dirnumber+=len(dirs)

for root, dirs, files in os.walk(infile, topdown=False):
  i+=1
  outcurrent=outfile + root.replace(infile,'')
  progress=math.floor(100 *(i-1) / dirnumber) #Progress
  print("Loading ... " + str(progress) + "%") #Progress
  for name in files:
    file, ext = os.path.splitext(name)
    if(ext in [".png",".jpg"]): #Supported extensions (you can add more if you want)
      with Image.open(root + "\\"+name) as im:
        image=im.convert('L') #Convert into greyscale
        image.save(outcurrent+"\\"+name, "PNG") #Save at dest copy