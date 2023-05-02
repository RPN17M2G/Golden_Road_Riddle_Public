
\5.

**How can we know the calculator gives us correct answers?** I tested the calculator in 2 different ways:

1. I calculated the formulas myself in different scenarios and checked how close my answers were to the calculator’s answers, because the difference is less than 5% than it means that its fairly accurate.
1. I searched the internet for data about cargo planes take off, firstly I needed to find a similar aircraft to our cargo plane. I found the **Lockheed C-130 Hercules**, which weights 34.38 Ton (Very close to our aircraft which weights 35.0 Ton), This aircraft is also used as a military aircraft. This aircraft used the Allison T56-A-7 turboprop engines which provide 3,336 N of force(3.336 time more than our aircraft). Here is what I found from comparison:
1. Payload(without passengers and aircraft weight): From my calculations the cargo can be loaded with 7,857 KG of cargo. Meanwhile the Locakheed C-130 Hercules can be loaded with 19,000 KG of cargo.
1. Take off distance(when unloaded):  For our cargo plane the runway must be 3.43 KM. For the Locakheed C-130 Hercules the runway must be at least 1.093 KM.
1. Take off speed: Our aircraft takes off at a speed of 140 M/S, the Locakheed C-130 Hercules takes off at a speed of 167 M/S.
1. Take off time(when unloaded): Our aircraft needs at least 49 seconds for taking off. Locakheed C-130 Hercules needs 30 seconds(Inaccurate information, I didn’t find a data about it online so I watched a video of the Locakheed C-130 Hercules taking off and timered the process from starting the movement to the moment the aircraft does not touch the ground).

From this comparison I can see that the Locakheed C-130 Hercules can carry                                                                              around 2.5 times as much as our aircraft and reach a little higher take off speed with 19 seconds less. Those results are acceptable because the Locakheed C-130 Hercules is equipped with 3.336 times stronger engines, , and because the difference in the results is not marginally bigger or smaller than 3.336 times, which is the engine’s force gap(also we need to consider that the Locakheed C-130 Hercules weights less), we can see that the answers are approximately correct.


From those methods I used to determine if the calculator gives correct answers I can see that the calculations of the calculator are mostly correct.

**What are some edge cases in the calculator? How can we deal with them?** Some edge cases are situations when the user inputs a negative** number or a value which isn’t a number, I dealt with those input issues by checking the input and raising an exception when the input is incorrect. A negative input can cause division by 0 error.

6 - Bonus.

The calculator does not consider the thrust and drag of the plane, the air pressure, the difference between above and below the aircraft air pressure and not the wind resistance. It does not consider the shape of the cargo aircraft as well. We can realistically improve the calculator accuracy if we consider the wind speed, that’s because there is an accurate and approachable real time data and because it can change the taking off conditions including the aircraft acceleration(which resolves changes in the distance required for take off and in the time required for take off), the difficulty of the take off from the pilot perspective and even how well will the remaining cargo will burn(in a strong wind it may be difficult to light the cargo on fire, and if the direction of the wind is in a specific angle the smoke from the burning can block the pilots view and resolve a dangerous take off condition).

