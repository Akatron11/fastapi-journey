1. What is the size of your image? Is it large or small — and why do you think that is?
size of my image is 93.5MB and its small. because i consider my others images, some others size 1.9GB. thats why its small.

2. How many layers does your image have? What does each major layer add?
my image has 8 layers. ADD alpine-minirootfs is operating system layer

3. What operating system and architecture does your image use? (from `docker inspect`)
operating system linux, architecture is amd64

4. **Image-specific question:**
   - 🌐 Nginx: What does the port mapping `-p 8080:80` actually mean? What would happen if you used `-p 9090:80` instead?
  
  I connected my computer's outside world port (8080) to Nginx's container port (80). 
  Nothing would happen. I just need to change the addresses.

5. In one paragraph: what surprised you most about this lab?
during the cleanup phase, I accidentally deleted the image and I thought I'd have to start over, but when I checked again with the `list` command, I realized I had actually deleted a container, not the image. It was funny to me. I also didn't give it a name in step 5, but I learned that Docker automatically assigns names in this cases. 
