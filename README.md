[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SkD24yV8)
# 1.1.4Spirographs

*Complete the following.*

1. Compare and contrast zero-iteration conditions and infinite loops.
2. A link to your code where you solve the following problem. Take the screen size of 800px. Create code or algorithm that always places the object(s), up to 5, in the center an equal distance from one another and from the edges of the screen.
3. Concentric Squares -- Add a screenshot of your result and the code to create it on your repo.
Objective: Write a Python program using the turtle module to draw a pattern of concentric squares. The pattern should be created using nested loops.

Instructions:

Setup the Turtle Environment:
Import the turtle module.
Create a turtle object.
Set the turtle speed to the fastest setting.
Draw Concentric Squares:
Use a nested loop to draw multiple squares.
The outer loop should control the number of squares.
The inner loop should draw each square.
Each square should be slightly larger than the previous one.
Customize the Pattern:
Use different colors for each square.
Ensure the squares are centered on the screen.
Example Output:

The turtle should draw a series of squares, each one larger than the last, creating a pattern of concentric squares.

Hints:

Use the penup() and pendown() methods to move the turtle without drawing.
Use the color() method to change the turtle’s color.
Use the forward() and right() methods to draw the sides of the squares.


4. Complete the steps 17, 18 and 19 from [mypltw use clever to sign on](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/728c751a6c4145bea0ea83c5058fb9f9#44b0003a2ee14fcc9865e7bb5faec747)
5. Answer to step 21
6. Insert a screenshot or picture of the algorithm you used for your tokenizer on the previous activity.
7. Give an example of an undecidable problem, and attach code.



|0 iteration condition|infinite loop condition|
|--|--|
|A 0 iteration loop is a loop that never runs and contains a value of 0. It is used when you need something to check all of your requirements but you don't want to change anything. Many video games use this to store data. "for i in range(0): print(I)". This is an example of it and we can see the number 0 is being used. 0 indicates to the for loop that the function will not output anything because of that 0. This is what the 0 iteration does.| An infinite loop is when a loop keeps on going and never stops. This will continue to happen if the loop is True. Once it becomes false, the loop will break. "while True: print("This will print forever")". This is an example of an infinite loop that goes until the boolean becomes false. If it is false the code will stop, but if it is true - the code will continue. |

|Equidistant code|<img width="1392" alt="Screenshot 2024-09-11 at 4 31 05 PM" src="https://github.com/user-attachments/assets/1dadff25-480f-4217-bf40-b6b380cec919">|
|--|--|
|Another example| <img width="1346" alt="Screenshot 2024-09-11 at 4 39 39 PM" src="https://github.com/user-attachments/assets/3e3a88b8-85fd-4a3c-9aff-7c325fb317d1">|
|Explain| Both of these screenshots show examples from my code and you can see what happens when the user inputs 3 or 5. One key point to notice is the shapes are all equidistant from each other meaning they are the same distance apart from all of the values. This was the goal and I have achieved it. The way I did this was using nested for loops. I had a main for loop and then kept multiple indented in the main. This let me create the number of shapes needed and most importantly let me position it in a way where I could satisfy the user with any number 1-5.|
|![Screenshot 2024-09-11 at 4 43 33 PM](https://github.com/user-attachments/assets/9f45ada2-2e76-4dfc-972d-87f72c109033)| This is of the many nested for loops I had. To explain more, the beginning of the loop was added so I could determine how many squares I would need to make this code work. Then the for loop (nested) was there to create the actual square. I set the nested for loops range to 4 so it could repeat and this would help create a square.|











|Cocentric squares Project|![image](https://github.com/user-attachments/assets/e0eaec5f-87a8-47dd-b56e-10722c35471f)| 
|--|--|
|Explain|The co-centric squares project was difficult at first but I realized it is just math. I just added to add 10 to every time my code made a 90-degree turn. This would lead my squares to keep on increasing and this is how the line was created. I used a while loop to let this be possible. A while loop allowed my code to keep on going forever. When the square reached the top, I made a function to break the code. This is how I stopped the while loop. After finding out what to do, this assignment became fairly easy and it's cool how much math can contribute to coding.  |
|Code|![Screenshot 2024-09-11 at 4 51 44 PM](https://github.com/user-attachments/assets/4bcb9e10-667b-41dd-848b-dfcccef782ee)|


