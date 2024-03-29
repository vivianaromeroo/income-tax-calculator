# Income Tax Calculator
This project study develops a program that calculates income tax.

INSTRUCTIONS<br />
Request<br />
The customer requests a program that computes a person’s income tax.

Analysis<br />
Analysis often requires the programmer to learn some things about the problem domain, in this case, the relevant tax law. 
For the sake of simplicity, let’s assume the following tax laws:

-All taxpayers are charged a flat tax rate of 20%<br />
-All taxpayers are allowed a $10,000 standard deduction<br />
-For each dependent, a taxpayer is allowed an additional $3,000 deduction<br />
-Gross income must be entered to the nearest penny<br />
-The income tax is expressed as a decimal number<br />

Another part of the analysis determines what information the user will have to provide. 
In this case, the user inputs are gross income and number of dependents. 
The program calculates the income tax based on the inputs and the tax law and then displays the income tax. 
The figure below shows the proposed terminal-based interface. Characters in italics indicate user inputs. 
The program prints the rest. The inclusion of an interface at this point is a good idea because it allows the 
customer and the programmer to discuss the intended program’s behavior in a context understandable to both.

Your output should match the following:

Enter the gross income: 150000.0<br />
Enter the number of dependents: 3<br />
The income tax is $26200.0<br />
