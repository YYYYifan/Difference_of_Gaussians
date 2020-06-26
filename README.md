# Difference_of_Gaussians
 
input grayscale image, get 3 different level of DoG

original image:

![image](./images/BMW_1.png)

DoG_1:

![image](./images/DOG_Layer1.png)

DoG_2:

![image](./images/DOG_Layer2.png)

DoG_3:

![image](./images/DOG_Layer3.png)


the result will be an array by [3 * y * x]

use **PIL.Image.fromarray(np.uint8(t1[0, :, :])).show()** to check