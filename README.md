# MouseKeyDetectionROS
ROS Publisher, Subscriber structure capable of detecting mouse clicks and converting that data into Boolean values to be used in application like Mouse controlled TurtleBot in 2D  space

# Workflow

1. Setup the package till the scripts folder
2. make two programs one subscriber and one publisher
3. Publisher with boolean topic type
4. Three topics for each click
5. subscriber of the same type and listens to the same three topics

# The setup

1. Make a package and set it up till the scripts folder
2. Write the mouse control sub and pub, link to the mouse reading program 
  - Put the detection part inside the continuous repeated loop
  - can make the mouse reading part and the ros part in two separate functions #todo

# The code
1. checked the data type printed using the `type()` function
2. `from std_msgs.msg import Bool`
3. Make separate publisher objects for each type of click and publish it separately in the `.publish` part.
4. In the subscriber part make sure to connect to the three topics and make separate callback functions for each type of click.

# Important takeaways
  - need `sudo` permission for mouse click detection enable terminal wide `sudo` privileges using `sudo -s`
