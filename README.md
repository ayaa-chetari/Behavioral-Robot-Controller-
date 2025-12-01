Behavioral Robot Controller – Webots Simulation 

==> Project Overview :

This project creates a multi-robot convoy in the Webots simulator.
The system consists of three robots:

- Leader robot (main_controller.py): controlled with the keyboard (forward, turn, stop).

- Two follower robots (controller1.py and controller2.py ): they automatically follow the leader.

- The follower robots do not receive direct commands. They rely only on their proximity sensors to react to the leader’s movement:

- They move forward when the leader moves forward.

- They slow down or stop when they get too close.

- They adjust their direction when the leader turns.

- Each follower robot continuously reads its sensors and adjusts its motors to maintain a safe distance while staying behind the leader. The convoy emerges from this simple, reactive principle.

==> Simulation Context :

The robots used in this system are differential-drive platforms simulated in Webots.
Each robot is equipped with:

- Two wheel motors (motor.left and motor.right)

- Seven horizontal proximity sensors (prox.horizontal.0 to prox.horizontal.6)

- A keyboard interface (used only by the leader)

The proximity sensors return raw distance values that allow the robots to detect objects ahead, behind, and on the sides.
Based on these readings, each robot selects its motion in a fully reactive manner, without communication or predefined trajectories.
