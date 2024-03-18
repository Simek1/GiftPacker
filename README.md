# Introduction
GiftPacker is an application designed for the thoughtful gifter, transforms the act of giving into an exciting and personalized experience. Tailored for those who seek to add an extra layer of joy to their presents, GiftPacker allows users to customize puzzle-based challenges, turning the unwrapping process into a fun and memorable adventure.

# Instruction 

<div style="text-align:center">

![Configuration menu](/README_imgs/conf.png)

</div>

Upon the first launch of the application, you will be prompted to perform the initial setup. The configuration involves adding content for messages that will appear after each puzzle, questions and answers for the quiz, and a final message hidden in the safe. Each of these messages conveys one of the three parts of the safe code. The content of the messages is intended to be a riddle, suggesting the sequence for entering each part of the code into the safe. Navigation between individual puzzles (detailed puzzle information can be found [here](#puzzles)) is facilitated through tabs located at the top of the screen. The first tab pertains to the reward within the safe, where you should provide a message (intended to be a message with good wishes) and an optional game key. The game key can then be copied by the gift recipient to activate the game on a chosen platform. Tabs ["Invisible Sheet"](#invisible-sheet) and ["Hidden Sheet"](#hidden-sheet) refer to two puzzles, in both of which you need to fill in a segment of the code obtained by solving them and a message that is intended to suggest which part of the code you received (this is an optional field). In the "Quiz" tab, in addition to the fields that also appeared in the two previous puzzles, you must also specify and confirm the number of questions to appear in the quiz. New tabs will appear at the top of the window, one for each question, where you need to enter the question and three answers. For the correct answer, you should check the checkbox. The last tab is the "Safe Code," where you need to input the code for the safe (intended to be created from the previously provided 3 parts of the code from the previous puzzles), which can be used to open it and receive the reward mentioned in the first tab.

# Puzzles
<details>
  <summary>Puzzles description and their solutions</summary>
  
  ## Open the box

  On the right side of the screen, there are hidden scissors. Grab them and drag them onto the box to open it.

  <div style="text-align:center">

  ![Scisors](/README_imgs/scisors.png)

  </div>

  ## Invisible sheet

  There is a camera app on the tablet. Launch it and move the tablet across the entire desktop to find the hidden sheet.

  ## Hidden sheet

  There is a hidden sheet behind the tablet that moves along with it, sticking out slightly, so you can grab it. Grab It and drag from behind. Double-click it to open, then launch the lantern app and flip the tablet (right-upper corner). Move the sheet above the light to see the message.

  <div style="text-align:center">

  ![Hidden sheet](/README_imgs/hidden_sheet.png)

  </div>

  ## Quiz

  You have to answer all the questions that you or your friend who sent you this program have set before. If you answer incorrectly, the answer will be deleted. Answer all the questions to receive the message.

  ## Safe

  Previous puzzles should provide you with fragments of the safe code. Enter them in the correct order (as should be suggested by the puzzle's reward messages) to claim your reward.

</details>

# Code requirements

In releases tab, there is an exe file that can be launched even without python on your computer but it needs to be in same folder as folder "imgs". Code has been written in Python 3.11. It uses the following libraries:

- PyQt5, graphic rendering.

- os, writing and reading settings file.

- cryptography, settings file encryption so player can't get safe code or any game data without playing game.
