This Python script shall help to create new custom Decks for Warno. You can input a list of Units(From your Devision.ndf) and tries to find the corresponding DevisionRule for that Unit.
Note: Currently only tries to match the Name of the Unit regardless from which batallion it comes from.

---------
HOW IT WORKS:
---------
1. Insert your Units(From Devision.ndf) from which you want to have the Corresponding DevisionRule into the "Unit.txt"
2. (OPTIONAL): If you want to modify which DevisionRules shall be used to match against, you can modify the Unit "Descriptor.txt". Currently I have every Unit in there and removed the Placeholder Devisionrules with like 999Units etc. (13.09.23 - If new Units were added this needs to be updated)
3. Run the "UnitMatcher.py" If nothing is written into the Console... GREAT! Otherwise it prints the unsucessful matches, where the script was not able to find any match. You can find the DevisionRules in the "result" file. Just copy it over to the DevisionRule.ndf