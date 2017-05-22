import sys
import glob 
import subprocess
import os

args = sys.argv

# include args
files_path = glob.glob(args[1]+"/*")
files_name = os.listdir(args[1])

# set scale
scale = args[2]

if subprocess.call( "test -e save_picture", shell=True  ):
    # make directory
    subprocess.call( "mkdir save_picture", shell=True  )
    print "1"
else:
    # remove save_picture directory
    subprocess.call( "rm -r save_picture", shell=True  )
    # make directory
    subprocess.call( "mkdir save_picture", shell=True  )    

for (file_path,file_name) in zip(files_path,files_name):
    cmd = "convert -geometry "+scale+"%"+" "+file_path+" "+file_name
    subprocess.call( cmd, shell=True  )

    # move pictures
    subprocess.call( "mv "+file_name+" save_picture/", shell=True  )


