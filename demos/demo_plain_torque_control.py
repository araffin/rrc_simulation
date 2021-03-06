#!/usr/bin/env python3
"""Demonstrate how to run the simulated finger with torque control."""
import time
import numpy as np

from rrc_simulation import sim_finger


if __name__ == "__main__":
    time_step = 0.001

    finger = sim_finger.SimFinger(
        finger_type="fingerone",
        time_step=time_step,
        enable_visualization=True,
    )
    # set the finger to a reasonable start position
    finger.reset_finger_positions_and_velocities([0, -0.7, -1.5])

    # Send a constant torque to the joints, switching direction periodically.
    torque = np.array([0.0, 0.3, 0.3])
    while True:
        time.sleep(time_step)

        action = finger.Action(torque=torque)
        t = finger.append_desired_action(action)
        observation = finger.get_observation(t)

        # invert the direction of the command every 100 steps
        if t % 100 == 0:
            torque *= -1
