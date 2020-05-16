# SPACESHIP GAME

In **Alien Invasion**, the player controls a spaceship that appears at the bottom center of the screen. The player can move the spaceship to the **right** and **left**, **up** and **down** using the arrow keys and to shoot using the **space bar**. When the game starts, a fleet of aliens fills the sky and shifts sideways and down the screen. The player shoots the aliens and destroys them. If the player reaches all the aliens, a new fleet, which will move faster than the previous fleet, will appear. If an alien hits the player's spaceship or reaches the bottom of the screen, the player will lose a ship. If the player loses three spaceships, the game is over.

## FIRST STAGE OF THE GAME

In the **first phase** of development, we will create a **spaceship** capable of moving **left** and **right**, **up** and **down**. The ship must be able to fire when the player presses the **space bar**. After providing this behavior, we can turn our attention to the aliens and refine the gameplay.

## SECOND STAGE OF THE GAME

We will add aliens to the Alien Invasion. We will initially add an alien near the top of the screen and then we will generate a complete fleet of them. We will move the fleet forward and down and get rid of any aliens hit by a projectile. Finally, we will limit the number of spaceships a player can have and end the game when he runs out of spaceships.

 When starting a new phase of development on a large project, it is always a good idea to review your plan and make it clear what you want to accomplish with the code you are about to write. Let's go then:

    * Analyze our code and determine if we need to refactor it before implementing new features.
    * Add a single alien in the upper left corner of the screen, with appropriate spacing around it.
    * Use the spacing around the first alien and the size of the screen as a whole to determine how many aliens will fit on the screen. We will write a loop to create aliens in order to fill the top of the screen.
    * Make the fleet move sideways and down until the entire fleet is hit or an alien strikes the spaceship or the ground. If the entire fleet is reached, we will create a new fleet. If an alien hits the spaceship or the ground, we will destroy the spaceship and create a new fleet.
    * Limit the number of spaceships the player can use and end the game when he has used his batch of spaceships.

We will refine this plan as the features are implemented, but that is enough to get started.

## THIRD AND LAST STAGE OF THE GAME

We’ll add a Play button to start the game on demand or restart it after it’s finished. We will also change the game to make it faster when the player moves to the next level and implement a scoring system.
