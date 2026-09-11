"""Lesson content for the Lumixa.

Holds all lesson, step, and final-project data in one place so
learn_python_gui.py stays focused on application logic. The data
includes small lambda checkers used to evaluate learner code.
"""


def build_lesson_sets():
    sets = {
                "Beginner": [
                    {
                        "title": "Built-in functions",
                        "unit": "Core tools",
                        "topic": "Python built-ins",
                        "summary": "Python gives you ready-made tools like print(), len(), and type() right away. These are called built-in functions because they are always available without importing anything.",
                        "example": "name = 'Ada'\nprint(name)\nprint(len(name))\nprint(type(name))",
                        "challenge": "Use print() and len() to show the length of your own name.",
                        "why_it_matters": "Built-in functions help you inspect values quickly while you learn. They are the first tools every Python programmer uses.",
                        "key_takeaways": "\u2022 print() sends output to the console\n\u2022 len() counts characters in strings or items in lists\n\u2022 type() tells you what kind of value something is\n\u2022 Combining them helps you debug and understand your data",
                        "review_question": "Which function tells you how many characters are in a string?",
                        "review_answer": "len() returns the number of characters in a string.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Meet Python's built-in tools",
                                "content": "Python gives you ready-made tools called built-in functions.\nThey're always available without importing anything.\n\nprint() sends output to the console.\nlen() counts characters in strings.\ntype() tells you what kind of value something is.",
                                "example": "name = 'Ada'\nprint(name)       # Ada\nprint(len(name))   # 3\nprint(type(name))  # <class 'str'>",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use print() to display the text 'Hello World'.",
                                "starter_code": "# Your code here\n",
                                "check": lambda code: "print(" in code and ("Hello" in code or "hello" in code),
                                "hint": "Try: print('Hello World')",
                                "success_msg": "print() sends text to the console. You'll use it constantly!",
                            },
                            {
                                "type": "concept",
                                "title": "len() and type()",
                                "content": "len() returns the number of characters in a string or items in a list.\ntype() tells you what category a value belongs to \u2014 string, integer, list, etc.",
                                "example": "word = 'Python'\nprint(len(word))    # 6\nprint(type(word))   # <class 'str'>\n\nnum = 42\nprint(type(num))    # <class 'int'>",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a variable called name, then use print(), len(), and type() to show its info.",
                                "starter_code": "# Create your variable\nname = 'Python'\n\n# Print the value, its length, and its type\n",
                                "check": lambda code: "print(" in code and "len(" in code and "type(" in code,
                                "hint": "Use print(name), print(len(name)), and print(type(name))",
                                "success_msg": "Excellent! You combined print(), len(), and type() to inspect data.",
                            },
                            {
                                "type": "review",
                                "question": "Which function tells you how many characters are in a string?",
                                "options": ["len()", "count()", "size()", "length()"],
                                "answer": "len()",
                            },
                        ],
                        "final_project": {
                            "title": "Number Analyzer",
                            "description": "Write a program that analyzes a number and displays information about it using print() and len().",
                            "scenario": "Your friend is building a quiz app and needs to inspect a player's answer before validating it. "
                                         "Write a small helper that analyzes 42 both as a real number and as its text form, so they can see exactly what they're working with.",
                            "start_hints": [
                                "Just make the first step work: create num and num_str, then print(num). One line working beats five lines guessed.",
                                "Add len(num_str) inside a print() \u2014 the exact function you practiced. It counts the 2 characters in '42'.",
                                "Finish with print(type(num)). Three print() calls one after another is the whole program.",
                            ],
                            "starter_snippet": "num = 42\nnum_str = '42'\n\n# Step 3: print the number first\nprint(num)",
                            "steps": [
                                "1. Create a variable called num with the value 42",
                                "2. Create a variable called num_str with the value '42'",
                                "3. Print the number itself",
                                "4. Use len() on num_str and print the result",
                                "5. Use type() on num and print the result",
                                "Expected: You should see 42, 2, and <class 'int'>",
                            ],
                            "starter_code": "# Build your Number Analyzer\nnum = 42\nnum_str = '42'\n\n# Step 3: Print the number\n\n# Step 4: Print the length of num_str\n\n# Step 5: Print the type of num\n",
                            "check": lambda code: (
                                True, "Great work! You used print(), len(), and type() to analyze data."
                            ) if ("print(" in code and "len(" in code and "type(" in code) else (
                                False, "Make sure you use print(), len(), and type() in your code."
                            ),
                        },
                    },
                    {
                        "title": "Python keywords",
                        "unit": "Control flow",
                        "topic": "Control flow",
                        "summary": "Keywords such as for, while, if, and def guide how Python structures your code. A for loop repeats an action for each item in a sequence, which is one of the most common patterns in Python.",
                        "example": "for item in ['one', 'two', 'three']:\n    print(item)",
                        "challenge": "Write a short loop that prints three numbers.",
                        "why_it_matters": "Loops let you repeat actions without rewriting the same code over and over. They are the foundation of almost every program.",
                        "key_takeaways": "\u2022 for loops repeat code for each item in a sequence\n\u2022 range() generates numbers to loop through\n\u2022 Indentation matters \u2014 it shows what is inside the loop\n\u2022 You can loop over lists, strings, and ranges",
                        "review_question": "What keyword starts a loop over a sequence?",
                        "review_answer": "for starts a loop over a sequence.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Loops repeat work",
                                "content": "A for loop repeats an action for each item in a sequence.\nInstead of writing the same code over and over, a loop does it automatically.\n\nIndentation (4 spaces) shows what is inside the loop.",
                                "example": "for item in ['one', 'two', 'three']:\n    print(item)\n\n# Output:\n# one\n# two\n# three",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write a for loop that prints three numbers using a list.",
                                "starter_code": "# Create a list and loop through it\n",
                                "check": lambda code: "for " in code and "print(" in code,
                                "hint": "Try: for i in [1, 2, 3]:\\n    print(i)",
                                "success_msg": "Perfect! Your for loop repeats code automatically for each item.",
                            },
                            {
                                "type": "concept",
                                "title": "range() generates numbers",
                                "content": "range(n) creates a sequence of numbers from 0 to n-1.\nThis is the most common way to repeat something a specific number of times.",
                                "example": "for i in range(5):\n    print(i)\n\n# Output: 0, 1, 2, 3, 4",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use a for loop with range() to print numbers 0 through 4.",
                                "starter_code": "# Loop with range()\n",
                                "check": lambda code: "for " in code and "range(" in code and "print(" in code,
                                "hint": "Try: for i in range(5):\\n    print(i)",
                                "success_msg": "Great! range() makes it easy to repeat something a set number of times.",
                            },
                            {
                                "type": "review",
                                "question": "What keyword starts a loop over a sequence?",
                                "options": ["for", "while", "loop", "repeat"],
                                "answer": "for",
                            },
                        ],
                        "final_project": {
                            "title": "Pattern Printer",
                            "description": "Use for loops and print() to create a repeating pattern of symbols.",
                            "scenario": "Your club is making printable banners and the president asks you to generate a divider pattern with code \u2014 "
                                         "5 rows of stars over 3 rows of dashes. You could copy and paste by hand, but a loop does it instantly and you can change the size anytime.",
                            "start_hints": [
                                "Start with one row only: print('*****'). Get that working before adding loops.",
                                "Wrap it in a loop: for i in range(5): then indent the print so it repeats five times.",
                                "Add the second loop right after the first: for j in range(3): print('---').",
                            ],
                            "starter_snippet": "# Step 1: get a single row to print first\nprint('*****')",
                            "steps": [
                                "1. Use a for loop with range(5) to repeat 5 times",
                                "2. Inside the loop, print a row of stars like '*****'",
                                "3. After that loop, create a second loop with range(3)",
                                "4. Inside the second loop, print '---'",
                                "Expected: 5 rows of stars followed by 3 rows of dashes",
                            ],
                            "starter_code": "# Build your Pattern Printer\n# Loop 1: Print 5 rows of stars\n\n\n# Loop 2: Print 3 rows of dashes\n\n",
                            "check": lambda code: (
                                True, "Excellent! You used multiple for loops to build a pattern."
                            ) if ("for " in code and code.count("print(") >= 2 and "range(" in code) else (
                                False, "Use two for loops with range() and print() inside each."
                            ),
                        },
                    },
                    {
                        "title": "Strings and methods",
                        "unit": "Core tools",
                        "topic": "String methods",
                        "summary": "Python strings come with useful methods like .upper(), .lower(), and .replace(). Methods are functions attached to an object. String methods return new strings without changing the original.",
                        "example": "word = 'python'\nprint(word.upper())\nprint(word.replace('p', 'P'))",
                        "challenge": "Turn a word into uppercase and replace one letter with another.",
                        "why_it_matters": "String methods are essential for cleaning up user input, formatting output, and processing text data.",
                        "key_takeaways": "\u2022 .upper() makes all letters uppercase\n\u2022 .lower() makes all letters lowercase\n\u2022 .replace() swaps one part of a string for another\n\u2022 Methods return new strings \u2014 the original is unchanged",
                        "review_question": "Which method makes a string all uppercase?",
                        "review_answer": ".upper() changes a string to uppercase letters.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Strings have superpowers",
                                "content": "Python strings come with built-in methods \u2014 functions that are attached to the string itself.\n\n.upper() makes all letters uppercase.\n.lower() makes all letters lowercase.\nMethods return new strings \u2014 the original is unchanged.",
                                "example": "word = 'python'\nprint(word.upper())   # PYTHON\nprint(word.lower())   # python\nprint(word.title())   # Python",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a variable with a lowercase word, then use .upper() to print it in uppercase.",
                                "starter_code": "# Create a variable and transform it\nword = 'python'\n\n# Print the uppercase version\n",
                                "check": lambda code: ".upper(" in code and "print(" in code,
                                "hint": "Try: print(word.upper())",
                                "success_msg": "Great! .upper() transforms text to uppercase.",
                            },
                            {
                                "type": "concept",
                                "title": "Replace and combine",
                                "content": ".replace(old, new) swaps one part of a string for another.\nYou can chain methods together: word.upper().replace('X', 'Y')\nEach method returns a new string, so chaining works cleanly.",
                                "example": "sentence = 'I like cats'\nprint(sentence.replace('cats', 'dogs'))\n# I like dogs\n\nprint(sentence.upper().replace('LIKE', 'love'))\n# I LOVE CATS",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a sentence, then use .replace() to swap one word for another and print the result.",
                                "starter_code": "# Create and transform a sentence\nsentence = 'I am learning Python'\n\n# Replace a word and print\n",
                                "check": lambda code: ".replace(" in code and "print(" in code,
                                "hint": "Try: print(sentence.replace('learning', 'mastering'))",
                                "success_msg": "Awesome! .replace() lets you modify text without changing the original.",
                            },
                            {
                                "type": "review",
                                "question": "Which method makes a string all uppercase?",
                                "options": [".upper()", ".capitalize()", ".uppercase()", ".toUpper()"],
                                "answer": ".upper()",
                            },
                        ],
                        "final_project": {
                            "title": "Word Statistics",
                            "description": "Build a program that analyzes and transforms a sentence using string methods.",
                            "scenario": "Your internship asks you to clean up a product title before it goes on the site: an uppercase version for the header, "
                                         "a lowercase one for the URL, a character count, and one word swapped. Write the program that produces all four.",
                            "start_hints": [
                                "Print the sentence as-is first (print(sentence)) to confirm your variable is there.",
                                "Add print(sentence.upper()) and print(sentence.lower()) \u2014 chain a method straight onto the variable.",
                                "Finish with print(len(sentence)) and print(sentence.replace('learning', 'mastering')).",
                            ],
                            "starter_snippet": "sentence = 'I am learning Python'\n\n# Step 2: print the uppercase version\nprint(sentence.upper())",
                            "steps": [
                                "1. Create a variable sentence with any sentence you like",
                                "2. Print it in all uppercase using .upper()",
                                "3. Print it in all lowercase using .lower()",
                                "4. Print the character count using len()",
                                "5. Use .replace() to swap one word for another and print the result",
                                "Expected: The sentence in upper, lower, its length, and a modified version",
                            ],
                            "starter_code": "# Build your Word Statistics\nsentence = 'I am learning Python'\n\n# Print uppercase version\n\n# Print lowercase version\n\n# Print character count\n\n# Replace a word and print\n",
                            "check": lambda code: (
                                True, "Great job! You used string methods to transform and analyze text."
                            ) if (".upper(" in code and ".lower(" in code and ".replace(" in code) else (
                                False, "Make sure you use .upper(), .lower(), and .replace() on your sentence."
                            ),
                        },
                    },
                    {
                        "title": "Variables and numbers",
                        "unit": "Core tools",
                        "topic": "Values and math",
                        "summary": "Variables are named boxes that store values, and Python can do arithmetic with numbers. You use a single '=' to store a value and refer to it later by name.",
                        "example": "age = 25\nprint(age)\nage = age + 1\nprint(age)",
                        "challenge": "Create two number variables, add them, and print the result.",
                        "why_it_matters": "Almost every program stores data in variables and does math with numbers. Getting comfortable with '=' and arithmetic is the foundation for everything that follows.",
                        "key_takeaways": "\u2022 = stores a value into a variable (it is not 'equals')\n\u2022 Variables let you reuse a value by name instead of retyping it\n\u2022 +, -, *, / are arithmetic operators\n\u2022 You can use a variable's old value to compute its new value",
                        "review_question": "What does the single '=' symbol do in Python?",
                        "review_answer": "A single '=' stores a value into a variable. It does not mean 'is equal to'.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Storing values in variables",
                                "content": "A variable is a named box for a value.\nYou create one with a single '=' sign.\nOnce stored, you can print it or use it in math.\n\nVariables make code readable and let you change one value in one place.",
                                "example": "name = 'Ada'      # store text\nage = 25          # store a number\nprint(name)       # Ada\nprint(age)        # 25",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a variable called score with the value 100, then print it.",
                                "starter_code": "# Store 100 in a variable called score\n\n# Print the score\n",
                                "check": lambda code: "score" in code and "=" in code and "print(" in code,
                                "hint": "Type: score = 100  then  print(score)",
                                "success_msg": "You stored a value in a variable and printed it. Variables save and reuse values by name.",
                            },
                            {
                                "type": "concept",
                                "title": "Doing math with numbers",
                                "content": "Python uses familiar math symbols for arithmetic.\n+ add, - subtract, * multiply, / divide.\nYou can compute and store the result in a new variable.\nYou can also update a variable using its own value.",
                                "example": "price = 10\ncount = 3\ntotal = price * count\nprint(total)      # 30\nprice = price + 5\nprint(price)      # 15",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create two variables, a is 7 and b is 3. Print a + b and a * b.",
                                "starter_code": "a = 7\nb = 3\n\n# Print the sum\n# Print the product\n",
                                "check": lambda code: bool(__import__("re").search(r"\ba\s*=\s*7", code) and __import__("re").search(r"\bb\s*=\s*3", code) and "print(" in code and ("+" in code) and ("*" in code)),
                                "hint": "Try: print(a + b)  and  print(a * b)",
                                "success_msg": "Nice! Arithmetic works on numbers and you printed both results.",
                            },
                            {
                                "type": "review",
                                "question": "Which operator multiplies two numbers in Python?",
                                "options": ["*", "x", "&", "!"],
                                "answer": "*",
                            },
                        ],
                        "final_project": {
                            "title": "Budget Helper",
                            "description": "Use variables and math to total up a small budget and print a summary.",
                            "scenario": "You're helping a friend track a small trip budget. Write a program that stores the cost of three items in variables, totals them, splits the total evenly between two people, and prints each line clearly.",
                            "start_hints": [
                                "Start simple: create three cost variables (e.g. hotel, food, travel) and print their total first.",
                                "Add a second line that divides the total by 2 using / and prints it.",
                                "Finally, print a friendly summary that labels what each number means.",
                            ],
                            "starter_snippet": "hotel = 120\nfood = 60\ntravel = 40\n\n# Step 1: print the total\ntotal = hotel + food + travel\nprint(total)",
                            "steps": [
                                "1. Create three variables for costs (for example hotel, food, travel)",
                                "2. Add them into a total variable and print it",
                                "3. Split the total between two people and print a per-person amount",
                                "4. Print a labeled summary like 'Total budget:' and 'Per person:'",
                                "Expected: the total, then each amount shown with a label",
                            ],
                            "starter_code": "# Build your Budget Helper\nhotel = 120\nfood = 60\ntravel = 40\n\n# Total the costs\n\n# Split evenly between two people\n\n# Print labeled summary\n",
                            "check": lambda code: (
                                True, "Great job! You used variables and arithmetic to build a working budget helper."
                            ) if ("=" in code and "+" in code and "print(" in code and "/" in code) else (
                                False, "Make sure you add the costs with +, split with /, and print() each result."
                            ),
                        },
                    },
                    {
                        "title": "Conditionals and decisions",
                        "unit": "Control flow",
                        "topic": "Making choices",
                        "summary": "Python programs can make decisions with if, elif, and else. Comparisons like ==, >, and < test whether a condition is True or False, and the right block of code runs.",
                        "example": "age = 18\nif age >= 18:\n    print('You can vote')\nelse:\n    print('Too young')",
                        "challenge": "Write an if statement that checks a number and prints one of two messages.",
                        "why_it_matters": "Decision-making is what lets programs respond differently to different input. Learning if/elif/else turns scripts into real, responsive programs.",
                        "key_takeaways": "\u2022 if runs its block only when the condition is True\n\u2022 else runs when the condition is False\n\u2022 Use == to compare for equality, and >, <, >=, <= for size\n\u2022 Indentation marks which code lives inside the if",
                        "review_question": "When does the else block run?",
                        "review_answer": "The else block runs when the if (and any elif) condition is False.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Making decisions with if",
                                "content": "if checks a condition, and if it's True, runs the indented block below it.\nComparisons give a True or False result:\n== equal, != not equal, > greater, < less, >= greater or equal, <= less or equal.\nIf the condition is False, Python moves past the block.",
                                "example": "temperature = 30\nif temperature > 25:\n    print('It is hot')\n\nif 5 == 5:\n    print('Equal!')",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use an if statement to check if a number called age is greater than 18, and print 'Adult' if it is.",
                                "starter_code": "age = 20\n\n# Write an if statement\n",
                                "check": lambda code: "if " in code and "age" in code and "print(" in code,
                                "hint": "Type: if age > 18: then on a new indented line print('Adult')",
                                "success_msg": "Your if statement runs the block only when age is greater than 18.",
                            },
                            {
                                "type": "concept",
                                "title": "Adding else and elif",
                                "content": "else runs a fallback block when the if is False.\nelif lets you check several conditions in order.\nOnly one branch runs: the first whose condition is True.\nThis lets programs handle many different situations.",
                                "example": "score = 85\nif score >= 90:\n    print('A')\nelif score >= 80:\n    print('B')\nelse:\n    print('Keep studying')",
                            },
                            {
                                "type": "practice",
                                "instruction": "Extend the age check: print 'Adult' if age is 18 or more, otherwise print 'Minor'.",
                                "starter_code": "age = 15\n\n# Use if and else\n",
                                "check": lambda code: "if " in code and "age" in code and "else" in code and "print(" in code,
                                "hint": "Add an else: line and print a different message in its indented block.",
                                "success_msg": "Now your program handles both cases: adult or minor.",
                            },
                            {
                                "type": "review",
                                "question": "Which operator checks that two values are equal?",
                                "options": ["=", "==", "!=", "=>"],
                                "answer": "==",
                            },
                        ],
                        "final_project": {
                            "title": "Grade Checker",
                            "description": "Write a program that takes a score and prints a grade using if/elif/else.",
                            "scenario": "Your teacher wants a quick tool to turn a 0-100 score into a letter grade. Write a program with a score variable that prints an A for 90+, B for 80+, C for 70+, and otherwise 'Needs work'.",
                            "start_hints": [
                                "Start with one score variable and a single if that prints 'A' for 90 or more.",
                                "Add elif branches for 80 and 70 so each range falls through correctly.",
                                "Finish with an else that prints 'Needs work' for anything below 70.",
                            ],
                            "starter_snippet": "score = 85\n\n# Step 1: top grade\nif score >= 90:\n    print('A')",
                            "steps": [
                                "1. Create a variable called score with a number from 0 to 100",
                                "2. Print 'A' when score is 90 or more",
                                "3. Add an elif printing 'B' when score is 80 or more",
                                "4. Add an elif printing 'C' when score is 70 or more",
                                "5. Add an else that prints 'Needs work' for anything below",
                                "Expected: a single grade line printed for the given score",
                            ],
                            "starter_code": "# Build your Grade Checker\nscore = 85\n\n# Grade with if / elif / else\n",
                            "check": lambda code: (
                                True, "Great job! Your Grade Checker uses if/elif/else to turn a score into a grade."
                            ) if ("if " in code and "elif " in code and "else" in code and "print(" in code and ">=" in code) else (
                                False, "Make sure you use if, elif, and else with >= comparisons and print() each grade."
                            ),
                        },
                    },
                    {
                        "title": "Reading and fixing code",
                        "unit": "Thinking like a programmer",
                        "topic": "Debugging basics",
                        "summary": "Real programming is mostly reading and fixing code, not typing fresh code from scratch. You'll practice spotting errors, reading error messages, and repairing broken programs until they run.",
                        "example": "# error message: name 'nane' is not defined\nnane = 'Ada'\nprint(name)",  "challenge": "Fix a small script so it prints a name without crashing.",
                        "why_it_matters": "Every programmer spends most of their time debugging. Being able to read an error and fix it quickly is the single most useful skill for real Python work.",
                        "key_takeaways": "\u2022 Read the error message \u2014 it names the line and the problem\n\u2022 A typo in a variable name causes 'is not defined'\n\u2022 Indentation errors crash the program instantly\n\u2022 print() is your friend for inspecting what's happening",
                        "review_question": "What does 'NameError: name x is not defined' usually tell you?",
                        "review_answer": "It means you used a variable named x before it was created, or you misspelled it.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Reading error messages",
                                "content": "Python tells you exactly where it got confused.\n\nNameError: name 'nane' is not defined\n\nThis says you used 'nane' but you never created that name.\nThe fix is usually a typo \u2014 the real variable is 'name'.\n\nTraceback gives the file and line number, so look there first.",
                                "example": "nane = 'Ada'\n\n# Traceback (most recent call last):\n#   File \"(your code)\", line 1, in <module>\n#     nane = 'Ada'\n# NameError: name 'nane' is not defined\n\n# Fix: spell it the same everywhere\nname = 'Ada'\nprint(name)",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write code that creates a variable called greeting with the text 'Hello' and prints it. Make sure every use is spelled exactly the same.",
                                "starter_code": "# Create the variable and print it\n",
                                "check": lambda code: "greeting" in code and "print(" in code,
                                "hint": "Try: greeting = 'Hello' then print(greeting)",
                                "success_msg": "Correct! Consistency in spelling is the #1 fix for NameErrors.",
                            },
                            {
                                "type": "debug",
                                "instruction": "This code crashes with a NameError. Fix it so it prints 'Hello, Ada'.",
                                "broken_code": "grerting = 'Hello'\nname = 'Ada'\nprint(greeting + name)\n",
                                "goal_hint": "greeting is spelled wrong in the first line but used correctly below. Match the spelling.",
                                "bug_notes": "The variable is defined as 'grerting' but used as 'greeting' later. Python can't find 'greeting'.",
                                "check": lambda code: "grerting" not in code and "greeting" in code and "print(" in code,
                                "success_msg": "Debugged! You found and fixed the misspelled variable.",
                                "hint": "Change grerting to greeting.",
                            },
                            {
                                "type": "concept",
                                "title": "Indentation errors",
                                "content": "Python uses indentation to know what belongs inside a block.\n\nprint(a)\n  print(b)   # unexpected indent\n\nToo much (or too little) indentation raises:\nIndentationError: unexpected indent\n\nThe fix is usually small \u2014 line up each block consistently (4 spaces).",
                                "example": "if True:\n    print('inside')\nprint('outside')   # one tab = error\n\n# Fix: keep every line in the block at the same 4-space indent",
                            },
                            {
                                "type": "debug",
                                "instruction": "Fix the indentation error so this loops through each letter and prints it (only one error).",
                                "broken_code": "word = 'cat'\nfor letter in word:\n  print(letter)\n   print(letter)\n",
                                "goal_hint": "One line is indented with a different number of spaces. Make all three lines in the loop match.",
                                "bug_notes": "The two print() lines use different heights of indentation. Python's IndentationError appears when a block isn't consistent.",
                                "check": lambda code: "for " in code and "print(letter)" in code,
                                "success_msg": "Fixed! Consistent indentation makes Python happy.",
                            },
                            {
                                "type": "review",
                                "question": "Which line does a Traceback point you to first?",
                                "options": ["The line with the bug", "The last line of the file", "The first import", "A random line"],
                                "answer": "The line with the bug",
                            },
                        ],
                        "final_project": {
                            "title": "Debug the Number Reporter",
                            "description": "A helper script with three bugs hides inside it. Find and fix every bug so it prints clean output.",
                            "scenario": "A teammate wrote a small script that should report facts about the number 12, but it crashes and also prints a wrong value. Fix all three bugs.",
                            "start_hints": [
                                "Start by finding the NameError \u2014 the variable spelled differently in one spot. Fix that first, then re-run.",
                                "Next look for a wrong math operation that makes the total incorrect.",
                                "Finally, the type() output is missing because one print uses the wrong parentheses. Even it out.",
                            ],
                            "starter_snippet": "num = 12\nname = 'twelve'\n\n# Bug 1: spelling\nprint(nmae)\n\n# Bug 2: math\nprint(num + num)\n\n# Bug 3: missing print\nprint(type(num)",
                            "steps": [
                                "1. Find and fix the NameError (a misspelled variable)",
                                "2. Correct the addition so it sums two numbers correctly",
                                "3. Add the closing parenthesis to the last print",
                                "4. You should see 'twelve', then 24, then <class 'int'>",
                            ],
                            "starter_code": "# Your code starts with bugs. Fix them!\nnum = 12\nname = 'twelve'\n\n# Bug 1: spelling\nprint(nmae)\n\n# Bug 2: math\nprint(num + num)\n\n# Bug 3: missing print\nprint(type(num)",
                            "check": lambda code: (
                                True, "Great debugging! You fixed all three bugs."
                            ) if (code.count('print') == 3 and 'nmae' not in code and 'num + num' not in code) else (
                                False, "Look for: (1) a misspelled variable, (2) adding num to itself instead of a different value, (3) the final print missing its parenthesis."
                            ),
                        },
                    },
                    {
                        "title": "Getting input and type conversion",
                        "unit": "User interaction",
                        "topic": "Input and casting",
                        "summary": "Real programs ask the user for values. input() always returns a string, so you convert that text to a number with int() or float() to do math, and back to text with str() when you need to show it.",
                        "example": "value = \"42\"\nnum = int(value)\nprint(num * 2)  # 84\nprice = \"19.99\"\nprint(float(price) + 5)",
                        "challenge": "Convert the text '19' to an integer and print double its value.",
                        "why_it_matters": "Every form, game score, or price a user types starts as text. Converting lets your code compute, compare, and then show a polished message.",
                        "key_takeaways": "\u2022 input() always returns a string (we simulate it with a variable)\n\u2022 int(\"42\") \u2192 42, float(\"3.14\") \u2192 3.14\n\u2022 str(42) \u2192 \"42\" for showing numbers in messages\n\u2022 Converting non-numeric text like int(\"abc\") raises ValueError",
                        "review_question": "What does int('42') return?",
                        "review_answer": "The integer 42 \u2014 the text '42' converted to a real number you can do math with.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "input() is always text",
                                "content": "When a program asks 'How old are you?' the answer comes back as a string, even if the user typed digits.\n\nIn the playground we simulate this with a preset variable:\n  value = \"42\"   # this stands in for input(\"Age: \")\n\nThe string \"42\" looks like a number but you can't do math until you convert it.\nTry it: \"42\" + 1 crashes, int(\"42\") + 1 is 43.",
                                "example": "value = \"42\"      # pretend this came from input()\nprint(value)            # \"42\" (still text)\nprint(int(value) + 1)   # 43 (now a real number)\nprint(type(value), type(int(value)))",
                            },
                            {
                                "type": "practice",
                                "instruction": "You have value = '19' (a string). Convert it to an integer with int(), store it in num, and print(num * 2).",
                                "starter_code": "value = '19'\n\n# Convert value to int and print double\n",
                                "check": lambda code: "int(" in code and "value" in code and "print(" in code and ("* 2" in code or "*2" in code),
                                "hint": "Try: num = int(value) then print(num * 2)",
                                "success_msg": "You turned text into a real integer and did math \u2014 exactly what input handling requires!",
                            },
                            {
                                "type": "concept",
                                "title": "float() and str() round trip",
                                "content": "int() handles whole numbers. float() handles decimals.\nstr() goes the other way: number \u2192 text so you can concatenate or f-string it.\n\nIf the text isn't numeric, Python raises ValueError \u2014 that's where try/except later helps.",
                                "example": "price = \"19.99\"\nprint(float(price) + 5)   # 24.99\nnum = 42\nprint(\"Answer: \" + str(num))  # Answer: 42\n# int(\"abc\")  # ValueError: invalid literal",
                            },
                            {
                                "type": "practice",
                                "instruction": "Convert price = '19.99' to a float, add 5, and print the result. Then convert the number 7 to a string and print('Score: ' + str(num)).",
                                "starter_code": "price = '19.99'\nnum = 7\n\n# Convert price to float, add 5, print\n\n# Print 'Score: 7' using str(num)\n",
                                "check": lambda code: "float(" in code and "price" in code and "str(" in code and code.count("print(") >= 2,
                                "hint": "Use float(price) for the decimal and str(num) inside the concatenation.",
                                "success_msg": "float() handled decimals and str() turned a number back into text for messages.",
                            },
                            {
                                "type": "review",
                                "question": "What does int('42') return?",
                                "options": ["42 as an integer you can do math with", "\"42\" as text", "42.0 as a float", "An error"],
                                "answer": "42 as an integer you can do math with",
                            },
                        ],
                        "final_project": {
                            "title": "Age in Months",
                            "description": "Build a helper that takes an age written as text, converts it, and reports months and days lived.",
                            "scenario": "A kids' museum wants a kiosk: a visitor types their age as text (e.g. '25'), and the screen shows that age in months and in days. Convert the string once, then compute both values.",
                            "start_hints": [
                                "Start with age_str = '25' and convert: age = int(age_str). Print age to confirm.",
                                "Compute months = age * 12 and days = age * 365, printing each with a label.",
                                "Wrap the prints in f-strings for polish: print(f'{age} years is {months} months').",
                            ],
                            "starter_snippet": "age_str = '25'\n\n# Step 1: convert to int\nage = int(age_str)\nprint(age)",
                            "steps": [
                                "1. Start with age_str = '25' (text)",
                                "2. Convert it with int(age_str) into age",
                                "3. Print months = age * 12",
                                "4. Print days = age * 365",
                                "5. Make both prints labeled (e.g. 'Months: 300')",
                                "Expected: the numeric age, then months and days on labeled lines",
                            ],
                            "starter_code": "# Build your Age in Months\nage_str = '25'\n\n# Convert to int\n\n# Months and days\n\n# Labeled prints\n",
                            "check": lambda code: (
                                True, "Great! You converted text to a number and computed derived values."
                            ) if ("int(" in code and "age_str" in code and "print(" in code and "*" in code) else (
                                False, "Convert age_str with int(), multiply for months and days, and print each result."
                            ),
                        },
                    },
                    {
                        "title": "While loops",
                        "unit": "Control flow",
                        "topic": "Looping with while",
                        "summary": "for loops count through a known sequence; while loops keep going as long as a condition stays True. They shine when you don't know in advance how many steps you'll need.",
                        "example": "n = 3\nwhile n > 0:\n    print(n)\n    n = n - 1\nprint('Go!')",
                        "challenge": "Countdown from 3 to 1 using a while loop.",
                        "why_it_matters": "while is how you retry until success, wait for a condition, or read until there is nothing left. It's the counterpart to for in every language.",
                        "key_takeaways": "\u2022 while condition: repeats while the condition is True\n\u2022 You must change a variable inside or the loop never ends\n\u2022 break exits immediately, continue skips to the next check\n\u2022 Use a counter like n = n - 1 to move toward termination",
                        "review_question": "What stops a while loop?",
                        "review_answer": "When its condition becomes False (or a break is hit).",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "while repeats while True",
                                "content": "for is for a fixed sequence. while is for 'keep going until...'.\n\nThe structure:\n  while condition:\n      # body\n      # update something so condition can become False\n\nIf you never update, the loop is infinite and the playground times out.",
                                "example": "n = 3\nwhile n > 0:\n    print(n)\n    n = n - 1   # update toward 0\nprint('Go!')\n# 3, 2, 1, Go!",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write a while loop that prints the numbers 3, 2, 1 using n starting at 3. Don't forget to decrement n inside.",
                                "starter_code": "n = 3\n\n# while n > 0: print and decrement\n",
                                "check": lambda code: "while" in code and "print(" in code and "n" in code and ("n =" in code or "n-=" in code),
                                "hint": "Use while n > 0: then print(n) and n = n - 1 on indented lines.",
                                "success_msg": "Countdown with while \u2014 you controlled termination with a counter!",
                            },
                            {
                                "type": "concept",
                                "title": "Summing until a limit",
                                "content": "while is great for accumulating until a threshold.\nKeep a total and a counter; each iteration adds and moves the counter.\nThis replaces 'do 5 times' with 'do until total >= 100'.",
                                "example": "total = 0\nn = 1\nwhile total < 20:\n    total = total + n\n    n = n + 1\nprint(total)  # 21",
                            },
                            {
                                "type": "practice",
                                "instruction": "With total = 0 and n = 1, use while total < 10 to keep adding n to total and incrementing n, then print total.",
                                "starter_code": "total = 0\nn = 1\n\n# while total < 10: add and increment\n\nprint(total)",
                                "check": lambda code: "while" in code and "total" in code and "print(" in code and ("+ n" in code or "+= n" in code or "total +" in code),
                                "hint": "Inside while: total = total + n and n = n + 1 (both indented).",
                                "success_msg": "You grew the total until the condition flipped \u2014 classic while pattern!",
                            },
                            {
                                "type": "review",
                                "question": "What must you do inside a while loop that counts?",
                                "options": ["Change a variable so the condition can become False", "Never change anything", "Always use break", "Print without updating"],
                                "answer": "Change a variable so the condition can become False",
                            },
                        ],
                        "final_project": {
                            "title": "Streak Counter",
                            "description": "Use a while loop to simulate a daily streak until a skip day appears.",
                            "scenario": "You're modeling a habit streak: each day is 'done' or 'skip'. Walk the list with a while index until you hit 'skip' or run out of days, counting how many consecutive 'done' days you had.",
                            "start_hints": [
                                "Start with days = ['done','done','skip','done'] and i=0, streak=0. Print days[0] to check indexing.",
                                "Loop while i < len(days) and days[i] == 'done': inside, streak += 1; i += 1.",
                                "After the loop, print(f'Streak: {streak}').",
                            ],
                            "starter_snippet": "days = ['done', 'done', 'skip', 'done']\ni = 0\nstreak = 0\n\n# Step 2: while condition\nwhile i < len(days) and days[i] == 'done':\n    streak += 1\n    i += 1\nprint(streak)",
                            "steps": [
                                "1. Create days list with at least one 'skip' in the middle",
                                "2. Set i = 0 and streak = 0",
                                "3. While i < len(days) and days[i] == 'done', increment both",
                                "4. Print the final streak count labeled",
                                "Expected: the count of leading 'done' days before the first 'skip'",
                            ],
                            "starter_code": "# Build your Streak Counter\ndays = ['done', 'done', 'skip', 'done']\ni = 0\nstreak = 0\n\n# While consecutive 'done'\n\n# Print labeled streak\n",
                            "check": lambda code: (
                                True, "You modeled a real streak with while and a compound condition!"
                            ) if ("while" in code and "streak" in code and "print(" in code and "len(" in code) else (
                                False, "Use while i < len(days) and days[i] == 'done':, update streak and i, then print."
                            ),
                        },
                    },
                    {
                        "title": "Booleans and logic",
                        "unit": "Logic & decisions",
                        "topic": "Boolean logic",
                        "summary": "Booleans are the two values True and False. Comparisons produce them, and and/or/not combine them to make nuanced decisions.",
                        "example": "is_adult = True\nhas_id = False\nprint(is_adult and has_id)  # False\nprint(is_adult or has_id)   # True\nprint(not is_adult)          # False",
                        "challenge": "Combine two booleans with and/or and print the result.",
                        "why_it_matters": "Every permission check, login, and game rule is a boolean formula. Mastering and/or/not turns flat if statements into precise logic.",
                        "key_takeaways": "\u2022 Comparisons like age >= 18 give True/False\n\u2022 and is True only if both sides are True\n\u2022 or is True if at least one side is True\n\u2022 not flips True\u2194False\n\u2022 Truthiness: \"\", 0, None, [] are falsy",
                        "review_question": "What does True and False evaluate to?",
                        "review_answer": "False \u2014 and needs both sides True.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Booleans from comparisons",
                                "content": "A comparison doesn't print by itself \u2014 it yields True or False.\nThose two values have type bool.\nYou can store them: is_adult = age >= 18.\nYou can print them: print(age >= 18) shows True.",
                                "example": "age = 20\nis_adult = age >= 18\nprint(is_adult)        # True\nprint(age == 20)       # True\nprint(age < 18)        # False\nprint(type(is_adult))  # <class 'bool'>",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create is_adult = (age >= 18) for age = 19 and print it. Then change age to 15 and print the new value.",
                                "starter_code": "age = 19\nis_adult = age >= 18\nprint(is_adult)\n\n# Now try age = 15 and print again\n",
                                "check": lambda code: "is_adult" in code and ">=" in code and code.count("print(") >= 2,
                                "hint": "Assign is_adult = age >= 18 and print it. Then reassign age = 15, is_adult = age >= 18, print again.",
                                "success_msg": "Comparisons produce booleans you can store and reuse!",
                            },
                            {
                                "type": "concept",
                                "title": "Combining with and/or/not",
                                "content": "and \u2014 True only if both sides True (strict).\nor \u2014 True if at least one side True (lenient).\nnot \u2014 flips the value.\nParentheses clarify: (a or b) and not c.",
                                "example": "is_adult = True\nhas_ticket = False\nprint(is_adult and has_ticket)  # False\nprint(is_adult or has_ticket)   # True\nprint(not has_ticket)            # True\n# (is_adult or has_ticket) and not has_ticket",
                            },
                            {
                                "type": "practice",
                                "instruction": "With is_adult = True and has_ticket = False, print is_adult and has_ticket, is_adult or has_ticket, and not has_ticket (three prints).",
                                "starter_code": "is_adult = True\nhas_ticket = False\n\n# Print and, or, not combinations\n",
                                "check": lambda code: "and" in code and "or" in code and "not" in code and code.count("print(") >= 3,
                                "hint": "Three prints: print(is_adult and has_ticket), print(is_adult or has_ticket), print(not has_ticket)",
                                "success_msg": "You wielded and/or/not \u2014 the core of decision logic!",
                            },
                            {
                                "type": "review",
                                "question": "What does True and False evaluate to?",
                                "options": ["True", "False", "Error", "None"],
                                "answer": "False",
                            },
                        ],
                        "final_project": {
                            "title": "Access Checker",
                            "description": "Use booleans and logic to decide if a person can enter a venue.",
                            "scenario": "A venue requires you to be 18+ AND have a ticket, OR be a VIP. Given age, has_ticket, and is_vip, compute can_enter and print whether access is granted.",
                            "start_hints": [
                                "Compute is_adult = age >= 18 first and print it to sanity-check.",
                                "Then can_enter = (is_adult and has_ticket) or is_vip. Recall and binds tighter than or, parentheses help.",
                                "Print a clear line: print(f'Can enter: {can_enter}') and test with vip True vs False.",
                            ],
                            "starter_snippet": "age = 17\nhas_ticket = True\nis_vip = False\n\n# Step 2: adult check\nis_adult = age >= 18\nprint(is_adult)",
                            "steps": [
                                "1. Set age, has_ticket, is_vip (try 17, True, False)",
                                "2. Compute is_adult = age >= 18",
                                "3. Compute can_enter = (is_adult and has_ticket) or is_vip",
                                "4. Print can_enter with a label",
                                "Expected: False for 17 with ticket but not VIP; True if VIP is True",
                            ],
                            "starter_code": "# Build your Access Checker\nage = 17\nhas_ticket = True\nis_vip = False\n\n# Adult check\n\n# Can enter logic\n\n# Labeled print\n",
                            "check": lambda code: (
                                True, "Perfect logic! You combined comparisons and boolean operators correctly."
                            ) if ("and" in code and "or" in code and ">=" in code and "print(" in code) else (
                                False, "Use is_adult = age >= 18 and can_enter = (is_adult and has_ticket) or is_vip, then print."
                            ),
                        },
                    },
                ],
                "Intermediate": [
                    {
                        "title": "Lists and ranges",
                        "unit": "Collections",
                        "topic": "Collections",
                        "summary": "Lists hold multiple values in order, and range() helps you step through numbers cleanly. Together they let you store and process groups of data.",
                        "example": "numbers = [1, 2, 3]\nfor n in range(3):\n    print(numbers[n])",
                        "challenge": "Create a list of three favorite foods and print each one with a loop.",
                        "why_it_matters": "Lists and ranges are common when you need to work through a group of values. Almost every real program uses them.",
                        "key_takeaways": "\u2022 Lists use [square brackets] and start counting at 0\n\u2022 range(n) creates numbers from 0 to n-1\n\u2022 for loops + lists let you process many items\n\u2022 lists[index] accesses each item by position",
                        "review_question": "What does range(3) produce?",
                        "review_answer": "range(3) produces the numbers 0, 1, and 2.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Lists organize data",
                                "content": "Lists hold multiple values in order, using [square brackets].\nEach item has a position (index) starting at 0.\nYou can mix types, but usually lists contain the same kind of data.",
                                "example": "fruits = ['apple', 'banana', 'cherry']\nprint(fruits[0])   # apple\nprint(fruits[2])   # cherry\nprint(len(fruits)) # 3",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a list of three items and print the second item using its index.",
                                "starter_code": "# Create a list\nitems = ['first', 'second', 'third']\n\n# Print the second item (index 1)\n",
                                "check": lambda code: "[" in code and "print(" in code and ("1]" in code or "[1" in code),
                                "hint": "Lists start at index 0, so the second item is items[1]",
                                "success_msg": "Lists use zero-based indexing. items[1] gets the second element.",
                            },
                            {
                                "type": "concept",
                                "title": "Loop through lists",
                                "content": "The most common pattern is combining a for loop with a list.\nrange(len(list)) gives you indices to access items by position.\nOr you can loop directly over the list items.",
                                "example": "colors = ['red', 'green', 'blue']\nfor color in colors:\n    print(color)\n\n# Also works with range:\nfor i in range(len(colors)):\n    print(colors[i])",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a list of three numbers and use a for loop to print each one.",
                                "starter_code": "# Create a list of numbers\nnumbers = [10, 20, 30]\n\n# Loop through and print each number\n",
                                "check": lambda code: "for " in code and "[" in code and "print(" in code,
                                "hint": "Try: for n in numbers:\\n    print(n)",
                                "success_msg": "Awesome! Lists + loops let you process many items cleanly.",
                            },
                            {
                                "type": "review",
                                "question": "What does range(3) produce?",
                                "options": ["0, 1, 2", "1, 2, 3", "0, 1, 2, 3", "1, 2"],
                                "answer": "0, 1, 2",
                            },
                        ],
                        "final_project": {
                            "title": "Shopping Cart",
                            "description": "Build a shopping cart that stores items, calculates a total, and displays a receipt.",
                            "scenario": "A friend runs a small lunch stand and wants to see the receipt before checkout: each item with its price, then the grand total. "
                                         "The item and price lists already exist \u2014 write the code that prints the receipt and adds everything up.",
                            "start_hints": [
                                "Verify your data works first: print(cart[0]) and print(prices[0]).",
                                "Loop with for i in range(len(cart)): and print cart[i] and prices[i] together inside the loop.",
                                "Make total = 0 before the loop, add each price inside it (total = total + prices[i]), then print the total after the loop.",
                            ],
                            "starter_snippet": "cart = ['Apple', 'Bread', 'Milk']\nprices = [1.50, 2.00, 3.25]\n\n# Step 3: print the first item with its price\nprint(cart[0], prices[0])",
                            "steps": [
                                "1. Create a list called cart with 3-4 item names",
                                "2. Create a list called prices with matching prices",
                                "3. Use a for loop to print each item and its price",
                                "4. Use range(len(cart)) to iterate through both lists",
                                "5. Calculate and print the total of all prices",
                                "Expected: A list of items with prices and a total at the bottom",
                            ],
                            "starter_code": "# Build your Shopping Cart\ncart = ['Apple', 'Bread', 'Milk']\nprices = [1.50, 2.00, 3.25]\n\n# Loop through and print each item with its price\n\n# Calculate and print the total\n",
                            "check": lambda code: (
                                True, "Awesome! You used lists and loops to build a shopping cart."
                            ) if ("for " in code and "[" in code and "print(" in code) else (
                                False, "Create two lists and use a for loop to print items and prices."
                            ),
                        },
                    },
                    {
                        "title": "Functions and returns",
                        "unit": "Reusable code",
                        "topic": "Reusable logic",
                        "summary": "Functions bundle repeated logic into a single reusable block. Use def to create a function, parameters to customize behavior, and return to send back a result.",
                        "example": "def greet(name):\n    return f'Hello {name}'\n\nprint(greet('Ada'))",
                        "challenge": "Write a function that doubles a number and returns the result.",
                        "why_it_matters": "Functions help you organize code into reusable pieces. They are the building blocks of every well-structured program.",
                        "key_takeaways": "\u2022 def defines a function\n\u2022 Parameters go in parentheses and act like variables\n\u2022 return sends a value back to the caller\n\u2022 Reusing functions saves time and reduces errors",
                        "review_question": "What keyword sends a value back from a function?",
                        "review_answer": "return sends a value back from a function.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Functions bundle logic",
                                "content": "A function is a reusable block of code defined with def.\nYou give it a name, optional parameters, and it runs when you call it.\nFunctions keep your code organized and avoid repetition.",
                                "example": "def greet(name):\n    print(f'Hello, {name}!')\n\ngreet('Ada')   # Hello, Ada!\ngreet('Bob')   # Hello, Bob!",
                            },
                            {
                                "type": "practice",
                                "instruction": "Define a function called greet that takes a name parameter and prints a greeting.",
                                "starter_code": "# Define your function\ndef greet(name):\n    # Add your print statement\n    pass\n\n# Test it\ngreet('Python')",
                                "check": lambda code: "def " in code and "print(" in code,
                                "hint": "Use def greet(name): then print a greeting inside",
                                "success_msg": "Functions let you reuse code by calling it with different inputs.",
                            },
                            {
                                "type": "concept",
                                "title": "Parameters and return",
                                "content": "Parameters are variables a function receives.\nreturn sends a value back to whoever called the function.\nWithout return, a function returns None by default.",
                                "example": "def add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)  # 8",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write a function called double that takes a number and returns it multiplied by 2.",
                                "starter_code": "# Define your function\ndef double(n):\n    # Return n multiplied by 2\n    pass\n\n# Test it\nprint(double(5))   # Should print 10\nprint(double(12))  # Should print 24",
                                "check": lambda code: "def " in code and "return" in code,
                                "hint": "Use return n * 2 inside your function",
                                "success_msg": "Perfect! return sends a value back so you can use it elsewhere.",
                            },
                            {
                                "type": "review",
                                "question": "What keyword sends a value back from a function?",
                                "options": ["return", "send", "output", "yield"],
                                "answer": "return",
                            },
                        ],
                        "final_project": {
                            "title": "Calculator App",
                            "description": "Build a calculator that uses functions for add, subtract, multiply, and divide.",
                            "scenario": "A classmate is building a budgeting tool and asked you for the math core: four small functions they can call from their menu. "
                                         "You'll write add, subtract, multiply, and divide, then prove each one works with a printed test.",
                            "start_hints": [
                                "Write one function first: def add(a, b): return a + b. Then test it: print(add(5, 3)).",
                                "Copy the same shape for subtract and multiply \u2014 only the operator changes.",
                                "Add divide (return a / b), then print a test for each of the four functions.",
                            ],
                            "starter_snippet": "def add(a, b):\n    return a + b\n\n# Test just this one before adding more\nprint(add(5, 3))",
                            "steps": [
                                "1. Define a function add(a, b) that returns a + b",
                                "2. Define a function subtract(a, b) that returns a - b",
                                "3. Define a function multiply(a, b) that returns a * b",
                                "4. Define a function divide(a, b) that returns a / b",
                                "5. Call each function with sample values and print the results",
                                "Expected: Results of add, subtract, multiply, and divide operations",
                            ],
                            "starter_code": "# Build your Calculator App\ndef add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n\n# Define multiply and divide\n\n# Test your functions with print()\n",
                            "check": lambda code: (
                                True, "Perfect! You built reusable functions for common math operations."
                            ) if ("def " in code and "return" in code and code.count("def ") >= 3) else (
                                False, "Define at least 3 functions with def and return."
                            ),
                        },
                    },
                    {
                        "title": "Dictionaries",
                        "unit": "Collections",
                        "topic": "Mapping values",
                        "summary": "Dictionaries store data as key-value pairs, which is useful for lookup tables. Unlike lists which use numeric indices, dictionaries let you access data by meaningful labels.",
                        "example": "student = {'name': 'Ada', 'age': 37}\nprint(student['name'])",
                        "challenge": "Create a dictionary with your name and one hobby, then print the hobby.",
                        "why_it_matters": "Dictionaries are one of the most versatile data structures. They are used everywhere from configs to databases to APIs.",
                        "key_takeaways": "\u2022 Dictionaries use {curly braces} and key: value pairs\n\u2022 Keys are labels (usually strings) for looking up values\n\u2022 Access data with dict['key']\n\u2022 Great for organizing related information",
                        "review_question": "What do dictionaries store?",
                        "review_answer": "Dictionaries store data as key-value pairs.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Dictionaries map keys to values",
                                "content": "Dictionaries store data as key: value pairs inside {curly braces}.\nKeys are labels (usually strings) you use to look up values.\nUnlike lists, you access data by meaningful names, not numbers.",
                                "example": "student = {'name': 'Ada', 'age': 37}\nprint(student['name'])  # Ada\nprint(student['age'])   # 37",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a dictionary called pet with keys 'name' and 'species', then print the name.",
                                "starter_code": "# Create your pet dictionary\npet = {\n    'name': 'Max',\n    'species': 'dog'\n}\n\n# Print the name\n",
                                "check": lambda code: "{" in code and ":" in code and "[" in code and "print(" in code,
                                "hint": "Use print(pet['name']) to access a value by key",
                                "success_msg": "Dictionaries let you access data by meaningful labels instead of positions.",
                            },
                            {
                                "type": "concept",
                                "title": "Organizing real-world data",
                                "content": "Dictionaries shine when modeling real objects with multiple attributes.\nYou can nest them, add new keys, and loop through them.\nThey're used everywhere: configs, user profiles, API responses.",
                                "example": "contact = {\n    'name': 'Ada Lovelace',\n    'phone': '555-0101',\n    'email': 'ada@example.com'\n}\n\nfor key, value in contact.items():\n    print(f'{key}: {value}')",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a dictionary called car with at least 3 keys (like 'make', 'model', 'year'), then print each key-value pair.",
                                "starter_code": "# Build your car dictionary\ncar = {\n    'make': 'Toyota',\n    'model': 'Camry',\n    'year': 2024\n}\n\n# Print each piece of info\n",
                                "check": lambda code: "{" in code and ":" in code and code.count("print(") >= 2,
                                "hint": "Use print(car['make']), print(car['model']), etc.",
                                "success_msg": "Excellent! Dictionaries organize related information in one place.",
                            },
                            {
                                "type": "review",
                                "question": "What do dictionaries store?",
                                "options": ["Key-value pairs", "Only numbers", "Only strings", "Ordered sequences"],
                                "answer": "Key-value pairs",
                            },
                        ],
                        "final_project": {
                            "title": "Contact Book",
                            "description": "Build a simple contact book that stores names, phone numbers, and emails using dictionaries.",
                            "scenario": "The robotics club needs a directory of members. Each contact keeps a name, phone, and email stored under clear labels, "
                                         "so anyone can look things up without remembering positions. Build two contacts and print them out for the officers.",
                            "start_hints": [
                                "contact1 is already given \u2014 access it by label: print(contact1['name']).",
                                "Create contact2 with your own info in the same shape, then print its name and email.",
                                "Combine parts into one formatted line using an f-string with your keys inside curly braces, like f'{key} - {value}' for a name and phone.",
                            ],
                            "starter_snippet": "contact1 = {\n    'name': 'Ada Lovelace',\n    'phone': '555-0101',\n    'email': 'ada@example.com'\n}\n\n# Step 3: print one value by its key\nprint(contact1['name'])",
                            "steps": [
                                "1. Create a dictionary called contact with keys 'name', 'phone', 'email'",
                                "2. Assign values to each key",
                                "3. Print each piece of information using its key",
                                "4. Create a second contact dictionary",
                                "5. Print both contacts in a formatted way",
                                "Expected: Two contacts displayed with all their information",
                            ],
                            "starter_code": "# Build your Contact Book\ncontact1 = {\n    'name': 'Ada Lovelace',\n    'phone': '555-0101',\n    'email': 'ada@example.com'\n}\n\n# Create contact2 with your own info\n\n# Print each contact's info\n",
                            "check": lambda code: (
                                True, "Excellent! You used dictionaries to organize and access structured data."
                            ) if ("{" in code and ":" in code and "[" in code and code.count("'") >= 8) else (
                                False, "Create at least two dictionaries with key-value pairs and print them."
                            ),
                        },
                    },
                    {
                        "title": "Sets and tuples",
                        "unit": "Collections",
                        "topic": "More collection types",
                        "summary": "Tuples hold ordered values you shouldn't change, and sets hold unique values with fast membership checks. Both are compact alternatives to lists that make your code clearer and safer.",
                        "example": "point = (3, 4)\nunique = {1, 2, 2, 3}\nprint(point[0])\nprint(unique)\nprint(2 in unique)",
                        "challenge": "Create a tuple for a point and a set of unique numbers, then check membership.",
                        "why_it_matters": "Choosing the right collection type makes your code safer and faster. Tuples protect data that shouldn't change; sets make 'is this value present?' checks easy.",
                        "key_takeaways": "\u2022 Tuples use (round brackets) and can't be changed once created\n\u2022 Sets use {curly braces} with no duplicates\n\u2022 Sets automatically remove repeats\n\u2022 'in' checks whether a value is in a set or tuple",
                        "review_question": "Which collection type can never be changed after it's created?",
                        "review_answer": "A tuple. Its items are fixed once you create it.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Tuples are fixed lists",
                                "content": "A tuple is like a list you can't modify.\nUse (round brackets).\nYou can still read items with an index.\nTuples are great when the order and items must stay fixed.\n\nCoordinates and function results are common tuple uses.",
                                "example": "coords = (3, 4)\nprint(coords[0])   # 3\nprint(len(coords)) # 2\nx, y = coords      # unpack into two variables\nprint(x, y)",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a tuple called point with the values 5 and 9, then print the first value (index 0).",
                                "starter_code": "# Create a tuple\n\n# Print the first value\n",
                                "check": lambda code: "point" in code and "(" in code and "print(" in code and "0]" in code,
                                "hint": "Type: point = (5, 9)  then  print(point[0])",
                                "success_msg": "Tuples hold fixed values. point[0] reads the first item without changing it.",
                            },
                            {
                                "type": "concept",
                                "title": "Sets hold unique values",
                                "content": "A set stores unique values with no repeats.\nUse {curly braces}.\nDuplicates are removed automatically.\n'value in set' tells you quickly if a value is present.\nSets don't keep a reliable order, so don't use indexes.",
                                "example": "tags = {'python', 'data', 'python'}\nprint(tags)          # {'data', 'python'}\nprint('python' in tags)  # True\nprint('java' in tags)    # False",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a set called colors with 'red', 'green', 'red', then print whether 'green' is in it.",
                                "starter_code": "# Create a set (duplicates allowed to write)\n\n# Check membership and print\n",
                                "check": lambda code: "colors" in code and "{" in code and "print(" in code and "green" in code and "in " in code,
                                "hint": "Make colors = {'red', 'green', 'red'}, then print('green' in colors)",
                                "success_msg": "Sets drop duplicates automatically, so your set has just two colors and 'in' finds 'green'.",
                            },
                            {
                                "type": "review",
                                "question": "Which statement is true about a set?",
                                "options": ["It can hold duplicates", "It keeps items in order", "It stores only unique values", "Items are accessed by index"],
                                "answer": "It stores only unique values",
                            },
                        ],
                        "final_project": {
                            "title": "Unique Visitor Tracker",
                            "description": "Use a set to track unique visitors of the day and a tuple to store a single row of data.",
                            "scenario": "A small shop wants to know how many unique visitors came today. Use a set to hold visitor IDs (duplicates shouldn't double-count!). Then store one day's stats in a tuple and print a clear report.",
                            "start_hints": [
                                "Start by putting a few visitor IDs into a set, including at least one repeat, and print how many unique IDs there are with len().",
                                "Store the day's summary (e.g. visitors and total bookings) in a single tuple.",
                                "Print a labeled report that shows the count of unique visitors and the tuple you stored.",
                            ],
                            "starter_snippet": "visitors = {'a1', 'b2', 'a1', 'c3'}\n\n# Step 1: count unique visitors\nprint(len(visitors))",
                            "steps": [
                                "1. Create a set of visitor IDs that includes at least one repeat",
                                "2. Print how many unique visitors there are using len()",
                                "3. Create a tuple holding one day row, e.g. (date, unique_count)",
                                "4. Print 'green' is in the set using 'in' and print the tuple",
                                "Expected: the unique count, then a membership check, then the tuple",
                            ],
                            "starter_code": "# Build your Unique Visitor Tracker\nvisitors = {'a1', 'b2', 'a1', 'c3'}\n\n# Unique count\n\n# Tuple for one day row\n\n# Membership check + print tuple\n",
                            "check": lambda code: (
                                True, "Great job! You used a set to count unique visitors and a tuple to hold a fixed row."
                            ) if ("{" in code and "len(" in code and "(" in code and "in " in code and "print(" in code) else (
                                False, "Use a set with {}, len() to count uniques, 'in' for membership, and a tuple with ()."
                            ),
                        },
                    },
                    {
                        "title": "Nested loops and data",
                        "unit": "Collections",
                        "topic": "Working with rows",
                        "summary": "A loop inside another loop lets you explore tables and grids. When you combine a for loop over rows with a for loop over columns, you can print or process every cell.",
                        "example": "grid = [[1, 2], [3, 4]]\nfor row in grid:\n    for cell in row:\n        print(cell)",
                        "challenge": "Loop through a 2D list and print each number on the same line, then move to the next row.",
                        "why_it_matters": "Real-world data is often arranged in rows and columns, like spreadsheets and tables. Nested loops are how you walk through every cell of that data.",
                        "key_takeaways": "\u2022 A list inside a list makes a grid (2D data)\n\u2022 An outer loop goes through each row\n\u2022 An inner loop goes through each item in that row\n\u2022 Nested loops are perfect for tables and matrices",
                        "review_question": "In a nested loop over a grid, what does the inner loop iterate over?",
                        "review_answer": "The inner loop iterates over each item inside the current row.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Lists inside lists",
                                "content": "A 'list of lists' is a grid.\nThe outer list holds rows.\nEach row is itself a list of cells.\nYou reach a cell with [row][col], two indexes.\nThis is exactly how spreadsheets and tables are stored.",
                                "example": "grid = [\n    ['a', 'b'],\n    ['c', 'd'],\n]\nprint(grid[0][1])   # 'b'\nprint(grid[1][0])   # 'c'",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a list called grid containing two inner lists, and print the first item of the second row.",
                                "starter_code": "grid = [\n    [1, 2],\n    [3, 4],\n]\n\n# Print row 1, column 0\n",
                                "check": lambda code: "print(" in code and "grid" in code and "[1][0]" in code,
                                "hint": "Rows start at 0, so the second row is grid[1] and its first item is grid[1][0]",
                                "success_msg": "grid[1][0] reaches row 1 (the second row), column 0 (the first cell).",
                            },
                            {
                                "type": "concept",
                                "title": "Looping through every cell",
                                "content": "To touch every cell, use two loops.\nThe OUTER loop picks each row.\nThe INNER loop walks through the cells of that row.\nEach iteration of the inner loop handles one cell.\nYou can print them or build new data.",
                                "example": "grid = [[1, 2], [3, 4]]\nfor row in grid:\n    for cell in row:\n        print(cell)\n# prints 1 2 3 4 each on its own line",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use a nested loop to print each number of the grid on the same line (no newline between cells).",
                                "starter_code": "grid = [[1, 2], [3, 4]]\n\n# Nested loop: print each cell with end=' '\n",
                                "check": lambda code: "for " in code and "for " in code and "print(" in code and "end=" in code,
                                "hint": "Outer: for row in grid:. Inner: for cell in row:. Print with print(cell, end=' ')",
                                "success_msg": "The inner loop prints each cell; end=' ' keeps them on one line, and the outer loop walks row by row.",
                            },
                            {
                                "type": "review",
                                "question": "When walking through a grid with nested loops, which loop handles the columns inside a row?",
                                "options": ["The outer loop", "The inner loop", "A while loop", "Neither loop"],
                                "answer": "The inner loop",
                            },
                        ],
                        "final_project": {
                            "title": "Grid Report",
                            "description": "Use nested loops to print a small grid neatly, then total all the numbers in it.",
                            "scenario": "A teacher has a 2D list of students' quiz scores. Write a program that prints each row of scores and then prints the total of all scores using a nested loop.",
                            "start_hints": [
                                "Start with the grid already given and a nested loop that prints each cell followed by a space.",
                                "After the row loop, print a blank line so each row starts on a fresh line.",
                                "Reuse a nested loop to add every cell into a total, then print it.",
                            ],
                            "starter_snippet": "scores = [\n    [8, 9, 7],\n    [6, 10, 9],\n]\n\n# Step 1: print the grid with nested loops\nfor row in scores:\n    for cell in row:\n        print(cell, end=' ')\n    print()",
                            "steps": [
                                "1. Print each row of the grid on its own line using a nested loop and end=' '",
                                "2. Add a blank print() after each row so lines separate",
                                "3. Use another nested loop to add every cell into a total variable",
                                "4. Print the total of all scores",
                                "Expected: the full grid printed row by row, then the total",
                            ],
                            "starter_code": "# Build your Grid Report\nscores = [\n    [8, 9, 7],\n    [6, 10, 9],\n]\n\n# Print the whole grid neatly\n\n# Total all scores with a nested loop\n",
                            "check": lambda code: (
                                True, "Great job! You used nested loops to print the grid and total every score."
                            ) if ("for " in code and "for " in code and "print(" in code and "+=" in code and "end=" in code) else (
                                False, "Use a nested loop to print with end=' ', and a second nested loop with total += cell."
                            ),
                        },
                    },
                    {
                        "title": "String formatting with f-strings",
                        "unit": "Working with text",
                        "topic": "f-strings",
                        "summary": "f-strings let you embed variable values directly inside text with {} curly braces. They are the modern, clean way to build messages in Python \u2014 far better than messy + concatenation.",
                        "example": "name = 'Ada'\nage = 36\nprint(f'{name} is {age} years old')",
                        "challenge": "Use an f-string to build a sentence that includes a variable.",
                        "why_it_matters": "Real programs spend a LOT of time building readable output for users, logs, and reports. f-strings are the tool professionals reach for first, and they automatically convert numbers to text.",
                        "key_takeaways": "\u2022 f-strings start with f\" and embed values with {expression}\n\u2022 Fixing formatting bugs with f-strings beats string + concatenation\n\u2022 You can call functions inside {} like {len(name)}\n\u2022 Use {{ and }} if you need literal braces",
                        "review_question": "What does the f stand for in f-strings?",
                        "review_answer": "It stands for 'formatted' \u2014 the string is a formatted literal.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Embedding values in text",
                                "content": "Before f-strings, people joined text with +:\nprint('Hi ' + name + '!')  # clunky\n\nWith an f-string:\nprint(f'Hi {name}!')      # clean\n\nPut an f before the quote, then wrap any expression in {}.\nPython evaluates it and inserts the result as text.",
                                "example": "name = 'Ada'\nage = 36\nprint(f'{name} is {age} years old')\n\n# You can even run code inside braces:\nprint(f'{name.upper()} will be {age + 1} next year')",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create variables city = 'Paris' and years = 5, then use one f-string to print 'I studied in Paris for 5 years'.",
                                "starter_code": "city = 'Paris'\nyears = 5\n\n# Build your f-string below\n",
                                "check": lambda code: "f'" in code or 'f"' in code,
                                "hint": "Try: print(f'I studied in {city} for {years} years')",
                                "success_msg": "Clean and clear \u2014 exactly how pros write output.",
                            },
                            {
                                "type": "fill",
                                "instruction": "Complete the f-strings by replacing each ___ with the right expression so the output matches the goal.",
                                "template": "item = 'phone'\nprice = 599\nprint(f'___: $___')\n",
                                "expected_output": "phone: $599",
                                "goal_hint": "The first blank should print the item name, the second should print the price. Use {expression} placeholders.",
                                "check": lambda code: "{item}" in code and "{price}" in code,
                                "success_msg": "Perfect! Your f-string embeds both variables cleanly.",
                                "hint": "Fill the blanks with {item} and {price}.",
                            },
                            {
                                "type": "debug",
                                "instruction": "This code crashes with a TypeError. Rewrite it using an f-string so it prints 'Ada is 36 years old'.",
                                "broken_code": "name = 'Ada'\nage = 36\nprint('Ada is ' + age + ' years old')\n",
                                "goal_hint": "You can't add a string and a number with +. Switch to an f-string: print(f'...')",
                                "bug_notes": "age is an int. 'Ada is ' + age raises TypeError because str + int isn't allowed. An f-string converts it automatically.",
                                "check": lambda code: "f'" in code or 'f"' in code,
                                "success_msg": "Fixed! The f-string auto-converts the number to text.",
                                "hint": "Replace the concatenation with an f-string and embed {name} and {age}.",
                            },
                            {
                                "type": "review",
                                "question": "Which line is a valid f-string?",
                                "options": ["f'{name} lives in {city}'", "f'name lives in city'", "f(name + city)", "format.f'{name}'"],
                                "answer": "f'{name} lives in {city}'",
                            },
                        ],
                        "final_project": {
                            "title": "Receipt Formatter",
                            "description": "Build a tiny receipt that uses f-strings to print a neat store-style summary.",
                            "scenario": "A small shop wants a clean receipt line. Given a product, its price, and a tax rate, print one formatted line like a real register would.",
                            "start_hints": [
                                "Start simple: print(f'{product}') and confirm it shows the product name.",
                                "Add the price next: print(f'{product}: ${price}') — you'll see the raw number $39.99.",
                                "Finish with the tax: format it with {tax:.2f} so it always shows two decimals.",
                            ],
                            "starter_snippet": "product = 'Charging Cable'\nprice = 39.99\ntax = price * 0.07\n\n# Step 1: product only\nprint(f'{product}')",
                            "steps": [
                                "1. Print just the product name with an f-string",
                                "2. Print 'product: $price' on one line",
                                "3. Print 'Total with tax: $X.XX' using {tax:.2f} formatting",
                                "Expected output should look like: Charging Cable: $39.99 / Total with tax: $2.80",
                            ],
                            "starter_code": "# Build your Receipt Formatter\nproduct = 'Charging Cable'\nprice = 39.99\ntax = price * 0.07\n\n# Step 1: product only\n\n# Step 2: product and price\n\n# Step 3: total with tax, formatted to 2 decimals\n",
                            "check": lambda code: (
                                True, "Nice work! Your f-string receipt prints a clean, readable total."
                            ) if ("f'" in code or 'f"' in code) and (".2f" in code) else (
                                False, "Use an f-string everywhere and format the tax with {tax:.2f}."
                            ),
                        },
                    },
                    {
                        "title": "String slicing and indexing",
                        "unit": "Working with text",
                        "topic": "Slicing",
                        "summary": "Strings are sequences. You can grab one character with word[i], a span with word[start:end], and even reverse with word[::-1]. Negative indices count from the end.",
                        "example": "word = \"python\"\nprint(word[0])     # p\nprint(word[1:4])   # yth\nprint(word[::-1])  # nohtyp",
                        "challenge": "Slice the first three letters and reverse a word.",
                        "why_it_matters": "Slicing is how you parse IDs, trim prefixes, and extract fields without splitting. It's daily work with text data.",
                        "key_takeaways": "\u2022 word[0] is the first character, word[-1] the last\n\u2022 word[start:end] up to but not including end\n\u2022 word[start:end:step] \u2014 step -1 reverses\n\u2022 Strings are immutable: slicing returns a new string",
                        "review_question": "What does \"python\"[1:4] return?",
                        "review_answer": "\"yth\" \u2014 characters at indices 1, 2, 3.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Indexing single characters",
                                "content": "A string is a sequence of characters, indexed from 0.\nNegative indices count from the end: -1 is last.\nOut-of-range index raises IndexError.",
                                "example": "word = \"python\"\nprint(word[0])   # p\nprint(word[2])   # t\nprint(word[-1])  # n\nprint(len(word)) # 6, so last index is 5",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create word = 'python' and print word[0] and word[-1] on two lines.",
                                "starter_code": "word = 'python'\n\n# Print first and last character\n",
                                "check": lambda code: "word" in code and "word[0]" in code and "word[-1]" in code and code.count("print(") >= 2,
                                "hint": "Use print(word[0]) and print(word[-1]).",
                                "success_msg": "Indexing \u2014 you reached both ends of the string!",
                            },
                            {
                                "type": "concept",
                                "title": "Slices: start:end:step",
                                "content": "A slice copies a span: word[start:end] includes start but excludes end.\nOmit start or end to mean beginning/end.\nstep controls stride: ::-1 reverses.\nword[1:4] is 1,2,3. word[:3] is first three . word[::2] is every other.",
                                "example": "word = \"python\"\nprint(word[1:4])   # yth\nprint(word[:3])    # pyt\nprint(word[:: -1])  # nohtyp\nprint(word[::2])   # pto",
                            },
                            {
                                "type": "practice",
                                "instruction": "With word = 'stressed', print word[0:3] (first three), word[-3:] (last three), and word[::-1] (reversed).",
                                "starter_code": "word = 'stressed'\n\n# Print slices: first three, last three, reversed\n",
                                "check": lambda code: "word" in code and "print(" in code and ("[0:3]" in code or "[:3]" in code) and "::-1" in code,
                                "hint": "Three prints: word[0:3], word[-3:], word[::-1].",
                                "success_msg": "Slicing success \u2014 you grabbed spans and reversed the word!",
                            },
                            {
                                "type": "review",
                                "question": "What does \"python\"[1:4] return?",
                                "options": ["yth", "pyt", "py", "hon"],
                                "answer": "yth",
                            },
                        ],
                        "final_project": {
                            "title": "Word Slicer",
                            "description": "Use slicing to extract and transform parts of a sentence.",
                            "scenario": "Your chatbot needs to echo a user's sentence in three forms: the first word, the last 5 characters, and the whole sentence reversed. Use slicing on a single sentence variable.",
                            "start_hints": [
                                "Start with sentence = 'Hello, Python world' and print(sentence) to see it.",
                                "First word: sentence[:5] or split \u2014 use slicing; last five is sentence[-5:].",
                                "Reverse with sentence[::-1] and print each result on a labeled line.",
                            ],
                            "starter_snippet": "sentence = 'Hello, Python world'\n\n# Step 2: first word via slice\nprint(sentence[:5])",
                            "steps": [
                                "1. Create sentence = 'Hello, Python world'",
                                "2. Print first word via slice (e.g. [:5])",
                                "3. Print last 5 characters with [-5:]",
                                "4. Print the whole sentence reversed with [::-1]",
                                "Expected: three labeled lines showing slices and reversal",
                            ],
                            "starter_code": "# Build your Word Slicer\nsentence = 'Hello, Python world'\n\n# First word\n\n# Last 5 characters\n\n# Reversed sentence\n",
                            "check": lambda code: (
                                True, "Great slicing \u2014 you cut spans and reversed text!"
                            ) if ("[" in code and ":" in code and "::-1" in code and "print(" in code) else (
                                False, "Use slices like [:5] and [-5:] plus [::-1] to reverse, printing each."
                            ),
                        },
                    },
                    {
                        "title": "Dictionary methods",
                        "unit": "Collections",
                        "topic": "Dictionary tools",
                        "summary": "Dictionaries store more than just direct lookup. .keys(), .values(), .items() let you loop, and .get(key, default) avoids KeyErrors when a label is missing.",
                        "example": "info = {'name': 'Ada', 'age': 36}\nprint(info.keys())\nfor k, v in info.items():\n    print(k, v)\nprint(info.get('email', 'unknown'))",
                        "challenge": "Loop over .items() to print every key and value.",
                        "why_it_matters": "Real data is dictionaries of varying shapes. Methods let you summarize, iterate, and handle missing fields gracefully.",
                        "key_takeaways": "\u2022 .keys(), .values(), .items() return views you can loop over\n\u2022 .get(key, default) returns default if missing instead of crashing\n\u2022 for k, v in dict.items() is the idiomatic loop\n\u2022 dict['key'] still raises KeyError if absent",
                        "review_question": "Which method gives key-value pairs for looping?",
                        "review_answer": ".items() returns (key, value) pairs for for k, v in dict.items().",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Views: keys, values, items",
                                "content": ".keys() \u2192 all labels.\n.values() \u2192 all values.\n.items() \u2192 pairs (key, value) as tuples.\nAll three are 'views' you can loop over or turn into a list.",
                                "example": "info = {'name': 'Ada', 'age': 36}\nprint(list(info.keys()))    # ['name', 'age']\nprint(list(info.values()))  # ['Ada', 36]\nfor k, v in info.items():\n    print(k + \":\", v)",
                            },
                            {
                                "type": "practice",
                                "instruction": "With info = {'name':'Ada','age':36,'city':'London'}, loop over info.items() and print each 'key: value' line.",
                                "starter_code": "info = {'name': 'Ada', 'age': 36, 'city': 'London'}\n\n# Loop over items and print\n",
                                "check": lambda code: "info.items()" in code and "for " in code and "print(" in code,
                                "hint": "Use for k, v in info.items(): then print(f'{k}: {v}') or print(k, v).",
                                "success_msg": "You iterated key-value pairs \u2014 the go-to dictionary loop!",
                            },
                            {
                                "type": "concept",
                                "title": "Safe access with .get()",
                                "content": "dict['missing'] raises KeyError and crashes.\n.get('missing', default) returns default instead.\nDefault often \"\" or 0 for counting.\nAlso handy for counting: counts[w] = counts.get(w, 0) + 1",
                                "example": "info = {'name': 'Ada'}\nprint(info.get('age', 'unknown'))  # unknown\ncounts = {}\ncounts['a'] = counts.get('a', 0) + 1\nprint(counts)",
                            },
                            {
                                "type": "practice",
                                "instruction": "Print info.get('email', 'no email') for info that lacks 'email', then count words in 'the cat and the cat' with get() inside a loop.",
                                "starter_code": "info = {'name': 'Ada'}\nprint(info.get('email', 'no email'))\n\ntext = 'the cat and the cat'\ncounts = {}\n# Loop words and count with get\n",
                                "check": lambda code: ".get(" in code and "for " in code and "print(" in code,
                                "hint": "For each w in text.split(): counts[w] = counts.get(w, 0) + 1, then print(counts).",
                                "success_msg": ".get() kept it safe and made counting a one-liner!",
                            },
                            {
                                "type": "review",
                                "question": "Which method gives key-value pairs for looping?",
                                "options": [".keys()", ".values()", ".items()", ".get()"],
                                "answer": ".items()",
                            },
                        ],
                        "final_project": {
                            "title": "Inventory Counter",
                            "description": "Use dictionary methods to summarize stock and find the busiest item.",
                            "scenario": "A shop tracks stock counts: {'apple': 12, 'bread': 7, 'milk': 15}. Loop with .items() to print each, use .values() and sum() for total, and find the item with the most stock.",
                            "start_hints": [
                                "Loop with for name, count in stock.items(): print(name, count) to show inventory.",
                                "Total = sum(stock.values()) \u2014 values() gives the numbers.",
                                "Most = max(stock, key=lambda k: stock[k]) then print(stock.get(most, 0)).",
                            ],
                            "starter_snippet": "stock = {'apple': 12, 'bread': 7, 'milk': 15}\n\n# Step 2: show inventory\nfor name, count in stock.items():\n    print(name, count)",
                            "steps": [
                                "1. Create stock dict with at least three items",
                                "2. Loop over stock.items() and print each 'name count'",
                                "3. Print total stock with sum(stock.values())",
                                "4. Find and print the item with the max count using max() and a key",
                                "Expected: item lines, total, and busiest item",
                            ],
                            "starter_code": "# Build your Inventory Counter\nstock = {'apple': 12, 'bread': 7, 'milk': 15}\n\n# Loop and print items\n\n# Total with sum(values())\n\n# Busiest item with max()\n",
                            "check": lambda code: (
                                True, "Great! You used keys/values/items and get/max to summarize the inventory."
                            ) if (".items()" in code and ".values()" in code and "sum(" in code and "max(" in code and "print(" in code) else (
                                False, "Use .items() to loop, sum(stock.values()) for total, and max() with a key for the busiest item."
                            ),
                        },
                    },
                    {
                        "title": "Enumerate and zip",
                        "unit": "Pythonic patterns",
                        "topic": "Smart iteration",
                        "summary": "Python gives you smarter loops: enumerate() gives you (index, value) without counting manually, and zip() pairs two lists so you can walk them together.",
                        "example": "names = ['Ada','Bob']\nfor i, name in enumerate(names):\n    print(i, name)\nscores = [90,85]\nfor name, score in zip(names, scores):\n    print(name, score)",
                        "challenge": "Pair names and scores with zip and number them with enumerate.",
                        "why_it_matters": "Manual counters like i = i+1 are fragile. enumerate and zip are the professional, readable way to walk multiple sequences at once.",
                        "key_takeaways": "\u2022 enumerate(seq) \u2192 (index, value) pairs\n\u2022 zip(a,b) \u2192 pairs from a and b, stops at shorter\n\u2022 Both are lazy iterables \u2014 loop over them directly\n\u2022 Avoid index bookkeeping like range(len(seq)) when you can",
                        "review_question": "What does enumerate(['a','b']) produce?",
                        "review_answer": "(0, 'a'), (1, 'b') \u2014 index plus value.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Number your loops",
                                "content": "Instead of\n i = 0\n for item in seq:\n     print(i, item)\n     i += 1\nuse\n for i, item in enumerate(seq):\n     print(i, item)\nstart= lets you begin at 1: enumerate(seq, start=1).",
                                "example": "colors = ['red','green','blue']\nfor i, color in enumerate(colors):\n    print(f'{i}: {color}')\n# enumerate(colors, start=1) begins at 1",
                            },
                            {
                                "type": "practice",
                                "instruction": "With fruits = ['apple','banana','cherry'], use enumerate to print '0 apple', '1 banana', '2 cherry' (index value).",
                                "starter_code": "fruits = ['apple', 'banana', 'cherry']\n\n# Enumerate and print\n",
                                "check": lambda code: "enumerate(" in code and "for " in code and "print(" in code,
                                "hint": "Use for i, fruit in enumerate(fruits): then print(i, fruit).",
                                "success_msg": "enumerate gave you index+value without manual counting!",
                            },
                            {
                                "type": "concept",
                                "title": "Zip two lists together",
                                "content": "zip() walks two lists in lockstep.\nzip(names, scores) yields (name, score) tuples.\nIt stops at the shorter list \u2014 handy but be aware.",
                                "example": "names = ['Ada','Bob']\nscores = [92, 85]\nfor name, score in zip(names, scores):\n    print(name + ': ' + str(score))",
                            },
                            {
                                "type": "practice",
                                "instruction": "With names = ['Ada','Bob'] and scores = [92,85], use zip to print 'Ada: 92' and 'Bob: 85', one per line.",
                                "starter_code": "names = ['Ada', 'Bob']\nscores = [92, 85]\n\n# Zip and print\n",
                                "check": lambda code: "zip(" in code and "for " in code and "print(" in code,
                                "hint": "Loop for name, score in zip(names, scores): then print(f'{name}: {score}').",
                                "success_msg": "zip paired the lists \u2014 clean parallel iteration!",
                            },
                            {
                                "type": "review",
                                "question": "What does enumerate(['a','b']) produce?",
                                "options": ["0, 1, 2", "'a', 'b'", "(0, 'a'), (1, 'b')", "Pairs from two lists"],
                                "answer": "(0, 'a'), (1, 'b')",
                            },
                        ],
                        "final_project": {
                            "title": "Leaderboard Builder",
                            "description": "Combine two lists (players and scores) with zip and rank them with enumerate.",
                            "scenario": "You're building a game leaderboard. Given names and scores as separate lists, zip them, sort by score descending, then use enumerate(start=1) to print ranked lines like '1. Ada: 92'.",
                            "start_hints": [
                                "Zip the lists: pairs = list(zip(names, scores)) and print it to see (name, score) tuples.",
                                "Sort by score: sorted(pairs, key=lambda p: p[1], reverse=True).",
                                "Enumerate the sorted list starting at 1 and print(f'{rank}. {name}: {score}').",
                            ],
                            "starter_snippet": "names = ['Ada', 'Bob', 'Carol']\nscores = [92, 85, 98]\n\n# Step 3: zip\npairs = list(zip(names, scores))\nprint(pairs)",
                            "steps": [
                                "1. Zip names and scores into (name, score) pairs",
                                "2. Sort pairs by score descending with sorted(key=..., reverse=True)",
                                "3. Enumerate the sorted list starting at 1",
                                "4. Print 'rank. name: score' for each",
                                "Expected: ranked leaderboard lines",
                            ],
                            "starter_code": "# Build your Leaderboard Builder\nnames = ['Ada', 'Bob', 'Carol']\nscores = [92, 85, 98]\n\n# Zip into pairs\n\n# Sort by score descending\n\n# Enumerate and print ranking\n",
                            "check": lambda code: (
                                True, "Leaderboard ready \u2014 you zipped, sorted, and enumerated like a pro!"
                            ) if ("zip(" in code and "enumerate(" in code and "sorted(" in code and "print(" in code) else (
                                False, "Use zip(names, scores), sorted(..., key=..., reverse=True), and enumerate(..., start=1)."
                            ),
                        },
                    },
                ],
                "Advanced": [
                    {
                        "title": "Standard library modules",
                        "unit": "Libraries and tools",
                        "topic": "Real Python tooling",
                        "summary": "Python's standard library gives you modules for math, JSON, randomness, and dates. These are pre-written tools you can import and use immediately.",
                        "example": "import math\nprint(math.sqrt(16))\n\nimport random\nprint(random.randint(1, 6))",
                        "challenge": "Import one standard library module and use one function from it.",
                        "why_it_matters": "Standard library modules save you time. The Zen of Python says: do not reinvent the wheel \u2014 use what Python provides.",
                        "key_takeaways": "\u2022 import brings in built-in modules\n\u2022 math has functions like sqrt(), floor(), ceil()\n\u2022 random has choice(), randint() for randomness\n\u2022 The standard library is huge \u2014 explore docs.python.org",
                        "review_question": "What is the purpose of the standard library?",
                        "review_answer": "It provides built-in modules that solve common programming problems.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Python's toolbox",
                                "content": "Python comes with a standard library \u2014 hundreds of pre-built modules you can import.\nimport brings a module into your code so you can use its tools.\nThis saves you from reinventing the wheel.",
                                "example": "import math\nprint(math.sqrt(16))  # 4.0\nprint(math.pi)        # 3.14159...\n\nimport random\nprint(random.randint(1, 6))  # Random number 1-6",
                            },
                            {
                                "type": "practice",
                                "instruction": "Import the math module and use math.sqrt() to print the square root of 25.",
                                "starter_code": "# Import the math module\nimport math\n\n# Print the square root of 25\n",
                                "check": lambda code: "import math" in code and "sqrt(" in code and "print(" in code,
                                "hint": "Use print(math.sqrt(25))",
                                "success_msg": "Great! math.sqrt() calculates square roots instantly.",
                            },
                            {
                                "type": "concept",
                                "title": "The random module",
                                "content": "random gives you tools for randomness: rolling dice, shuffling lists, picking winners.\nrandom.randint(a, b) returns a random integer between a and b (inclusive).\nrandom.choice(list) picks one item randomly from a list.",
                                "example": "import random\nprint(random.randint(1, 6))       # Random 1-6\nprint(random.choice(['a', 'b', 'c']))  # Random letter",
                            },
                            {
                                "type": "practice",
                                "instruction": "Import random and use random.randint() to simulate rolling a die (1-6). Print the result.",
                                "starter_code": "# Import random and roll a die\nimport random\n\nresult = random.randint(1, 6)\nprint(f'You rolled: {result}')",
                                "check": lambda code: "import random" in code and "randint(" in code and "print(" in code,
                                "hint": "Use random.randint(1, 6) to get a number between 1 and 6",
                                "success_msg": "Nice! random.randint() makes simulations and games possible.",
                            },
                            {
                                "type": "review",
                                "question": "What is the purpose of the standard library?",
                                "options": [
                                    "Built-in modules that solve common problems",
                                    "Third-party packages you install separately",
                                    "A code editor for writing Python",
                                    "A database for storing data",
                                ],
                                "answer": "Built-in modules that solve common problems",
                            },
                        ],
                        "final_project": {
                            "title": "Dice Rolling Simulator",
                            "description": "Build a dice game that uses the random module to roll multiple dice and analyze the results.",
                            "scenario": "Your game-night group is tired of losing dice under the couch. They want a digital roller: press run, get 5 die values, "
                                         "plus the total and average for scoring. Use Python's random module so no two rolls are ever the same.",
                            "start_hints": [
                                "Start tiny: import random, then print(random.randint(1, 6)) to confirm a single roll works.",
                                "Turn it into a function \u2014 def roll_dice(n): return a list of n rolls using a loop or a list comprehension.",
                                "Store rolls = roll_dice(5), loop and print each value, then print(sum(rolls)) for the total and sum(rolls) / len(rolls) for the average.",
                            ],
                            "starter_snippet": "import random\n\n# Step 3: roll one die first\nprint(random.randint(1, 6))",
                            "steps": [
                                "1. Import the random module",
                                "2. Create a function roll_dice(n) that returns a list of n random numbers (1-6)",
                                "3. Roll 5 dice and store the results",
                                "4. Print each die value",
                                "5. Calculate and print the sum and average of all rolls",
                                "Expected: 5 random die values with their sum and average",
                            ],
                            "starter_code": "# Build your Dice Rolling Simulator\nimport random\n\ndef roll_dice(n):\n    return [random.randint(1, 6) for i in range(n)]\n\n# Roll 5 dice\n\n# Print each value\n\n# Calculate sum and average\n",
                            "check": lambda code: (
                                True, "Great! You imported a module and used it to build a working program."
                            ) if ("import " in code and "def " in code and "print(" in code) else (
                                False, "Import a module, define a function, and print results."
                            ),
                        },
                    },
                    {
                        "title": "Classes and objects",
                        "unit": "Object-oriented design",
                        "topic": "Object-oriented programming",
                        "summary": "Classes help you model real-world ideas in a structured way. A class is a blueprint, and objects are instances created from that blueprint.",
                        "example": "class Book:\n    def __init__(self, title, author):\n        self.title = title\n        self.author = author\n\n    def summary(self):\n        return f'{self.title} by {self.author}'\n\nbook = Book('Python Basics', 'Guido')\nprint(book.summary())",
                        "challenge": "Create a class that stores a movie title and release year.",
                        "why_it_matters": "Classes are the foundation of object-oriented programming. They help you organize complex programs into logical, reusable pieces.",
                        "key_takeaways": "\u2022 class is a blueprint for creating objects\n\u2022 __init__ is the constructor that runs when you create an object\n\u2022 self refers to each individual object's data\n\u2022 Methods are functions that belong to a class",
                        "review_question": "What does a class define?",
                        "review_answer": "A class defines a blueprint for creating objects.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Classes are blueprints",
                                "content": "A class is a blueprint for creating objects. It defines what data (attributes) and behavior (methods) objects will have.\nThink of a class like a cookie cutter \u2014 it shapes each cookie (object) the same way.",
                                "example": "class Dog:\n    def __init__(self, name):\n        self.name = name\n\nbuddy = Dog('Buddy')\nprint(buddy.name)  # Buddy",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a class called Cat with an __init__ method that takes a name parameter and stores it in self.name.",
                                "starter_code": "# Define your Cat class\nclass Cat:\n    def __init__(self, name):\n        # Store the name in self\n        pass\n\n# Test it\nmy_cat = Cat('Whiskers')\nprint(my_cat.name)",
                                "check": lambda code: "class " in code and "self" in code and "__init__" in code,
                                "hint": "Use self.name = name inside __init__",
                                "success_msg": "Classes define blueprints. __init__ runs when you create a new object.",
                            },
                            {
                                "type": "concept",
                                "title": "Methods add behavior",
                                "content": "Methods are functions that belong to a class. They describe what objects can DO.\nUse self to access each object's own data from inside a method.",
                                "example": "class Dog:\n    def __init__(self, name):\n        self.name = name\n\n    def bark(self):\n        return f'{self.name} says Woof!'\n\nrex = Dog('Rex')\nprint(rex.bark())  # Rex says Woof!",
                            },
                            {
                                "type": "practice",
                                "instruction": "Add a method called meow() to your Cat class that returns '{name} says Meow!'.",
                                "starter_code": "class Cat:\n    def __init__(self, name):\n        self.name = name\n\n    # Add your meow method\n\nmy_cat = Cat('Whiskers')\nprint(my_cat.meow())",
                                "check": lambda code: "def meow(" in code and "return" in code and "self.name" in code,
                                "hint": "def meow(self): return f'{self.name} says Meow!'",
                                "success_msg": "Perfect! Methods let objects perform actions using their own data.",
                            },
                            {
                                "type": "review",
                                "question": "What does a class define?",
                                "options": [
                                    "A blueprint for creating objects",
                                    "A variable that stores data",
                                    "A loop that repeats code",
                                    "A file that saves data",
                                ],
                                "answer": "A blueprint for creating objects",
                            },
                        ],
                        "final_project": {
                            "title": "Library Manager",
                            "description": "Build a Book class and a Library class that manages a collection of books.",
                            "scenario": "Your school's book club wants to know who has what. They need a Library that holds Book objects and can list its contents. "
                                         "You'll finish the Book blueprint that's provided, then build the Library that collects books and prints them.",
                            "start_hints": [
                                "The Book class is provided \u2014 make one book and print(book.info()) to confirm the blueprint works.",
                                "Give Library an __init__ with self.books = [], then add an add_book(book) method that does self.books.append(book).",
                                "Add list_books() that loops over self.books and prints each book.info(). Then create the library, add 3 books, and call list_books().",
                            ],
                            "starter_snippet": "class Book:\n    def __init__(self, title, author):\n        self.title = title\n        self.author = author\n        self.is_available = True\n\n    def info(self):\n        return f'{self.title} by {self.author}'\n\n# Step 3: try creating one book first\nbook = Book('Python Basics', 'Guido')\nprint(book.info())",
                            "steps": [
                                "1. Create a Book class with title, author, and is_available attributes",
                                "2. Add a method info() that returns 'Title by Author'",
                                "3. Create a Library class with an empty books list",
                                "4. Add add_book(book) and list_books() methods to Library",
                                "5. Create 3 books and add them to the library, then list them",
                                "Expected: A list of 3 books displayed with their info",
                            ],
                            "starter_code": "# Build your Library Manager\nclass Book:\n    def __init__(self, title, author):\n        self.title = title\n        self.author = author\n        self.is_available = True\n\n    def info(self):\n        return f'{self.title} by {self.author}'\n\n# Create a Library class\n\n# Create 3 books and add them to the library\n",
                            "check": lambda code: (
                                True, "Perfect! You used classes to model a real-world system."
                            ) if ("class " in code and "self" in code and code.count("class ") >= 2) else (
                                False, "Create at least 2 classes (Book and Library) with self."
                            ),
                        },
                    },
                    {
                        "title": "File handling",
                        "unit": "Data and storage",
                        "topic": "Reading and writing",
                        "summary": "Python can read from and write to files using the built-in open() function. Using the with statement ensures files are properly closed after use.",
                        "example": "with open('notes.txt', 'w') as file:\n    file.write('Hello, World!')\n\nwith open('notes.txt', 'r') as file:\n    content = file.read()\n    print(content)",
                        "challenge": "Create a small file and write one sentence into it.",
                        "why_it_matters": "File handling lets your program save data that persists after it closes. This is how apps remember your settings, notes, and progress.",
                        "key_takeaways": "\u2022 open() connects to a file; 'w' writes, 'r' reads\n\u2022 Use 'with' to automatically close the file\n\u2022 write() saves text, read() retrieves it\n\u2022 Files persist after your program stops running",
                        "review_question": "What built-in function opens a file?",
                        "review_answer": "open() opens a file for reading or writing.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Files remember data",
                                "content": "Python can read from and write to files using the built-in open() function.\nWith 'w' mode you write data. With 'r' mode you read it back.\nAlways use the 'with' statement \u2014 it automatically closes the file when done.",
                                "example": "# Write to a file\nwith open('notes.txt', 'w') as file:\n    file.write('Hello, World!')\n\n# Read it back\nwith open('notes.txt', 'r') as file:\n    content = file.read()\n    print(content)  # Hello, World!",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write your name to a file called 'myname.txt' using open() with write mode.",
                                "starter_code": "# Write to a file\nwith open('myname.txt', 'w') as f:\n    # Write your name\n    pass",
                                "check": lambda code: "open(" in code and "write(" in code,
                                "hint": "Use f.write('Your Name') inside the with block",
                                "success_msg": "Great! File write mode ('w') creates or overwrites a file.",
                            },
                            {
                                "type": "concept",
                                "title": "Reading files back",
                                "content": "read() returns the entire file contents as a string.\nreadline() reads one line at a time.\nreadlines() returns a list of all lines.\nFiles persist after your program stops running.",
                                "example": "# Write multiple lines\nwith open('data.txt', 'w') as f:\n    f.write('Line 1\\n')\n    f.write('Line 2\\n')\n    f.write('Line 3\\n')\n\n# Read it all back\nwith open('data.txt', 'r') as f:\n    print(f.read())",
                            },
                            {
                                "type": "practice",
                                "instruction": "Read the file 'myname.txt' back and print its contents. (Create it first if needed.)",
                                "starter_code": "# Write a file first\nwith open('myname.txt', 'w') as f:\n    f.write('My Name')\n\n# Now read it back and print\n",
                                "check": lambda code: "open(" in code and "read" in code and "print(" in code,
                                "hint": "Use open('myname.txt', 'r') with read() and print the result",
                                "success_msg": "Excellent! File I/O lets your program save data that persists after it closes.",
                            },
                            {
                                "type": "review",
                                "question": "What built-in function opens a file?",
                                "options": ["open()", "file()", "read()", "load()"],
                                "answer": "open()",
                            },
                        ],
                        "final_project": {
                            "title": "Daily Journal",
                            "description": "Build a journal app that writes entries to a file and reads them back.",
                            "scenario": "You're starting a learning journal to remember what you work on each day. The catch: it has to survive after you close the program. "
                                         "Save your first few entries to a real file, then read them back to prove they're still there.",
                            "start_hints": [
                                "Write just one entry first: use open('journal.txt', 'w') inside a with block and f.write('Day 1: ...').",
                                "Add two more write() calls for Day 2 and Day 3, one per line (put a '\\n' at the end of each).",
                                "Read it back: with open('journal.txt', 'r') as f: content = f.read(), then print(content) and count lines with len(content.splitlines()).",
                            ],
                            "starter_snippet": "# Step 3: write a single entry first\nwith open('journal.txt', 'w') as f:\n    f.write('Day 1: Started learning Python\\n')",
                            "steps": [
                                "1. Write 3 journal entries to 'journal.txt', one per line",
                                "2. Each entry should include a label like 'Day 1:'",
                                "3. Read the file back and print all entries",
                                "4. Count and print the total number of lines",
                                "5. Add one more entry and verify the file was updated",
                                "Expected: 4 journal entries printed to the console with a line count",
                            ],
                            "starter_code": "# Build your Daily Journal\n\n# Write 3 entries\nwith open('journal.txt', 'w') as f:\n    f.write('Day 1: Started learning Python\\n')\n    # Add Day 2 and Day 3\n\n# Read and print all entries\n\n# Count total lines\n",
                            "check": lambda code: (
                                True, "Excellent! You used file I/O to create a persistent journal."
                            ) if ("open(" in code and "write" in code and "read" in code) else (
                                False, "Use open() with both write and read operations."
                            ),
                        },
                    },
                    {
                        "title": "Exception handling",
                        "unit": "Robust code",
                        "topic": "Handling errors gracefully",
                        "summary": "Errors happen, but good programs don't crash. try and except let you attempt risky code and respond gracefully if it fails, so your program keeps running.",
                        "example": "try:\n    num = int('abc')\nexcept ValueError:\n    print('That is not a number')",
                        "challenge": "Wrap a risky conversion in try/except and print a friendly message on error.",
                        "why_it_matters": "Real programs face bad input, missing files, and broken connections. Handling errors instead of crashing is what separates scripts from robust applications.",
                        "key_takeaways": "\u2022 try: marks the code you want to attempt\n\u2022 except: catches an error and runs fallback code\n\u2022 You can catch specific error types like ValueError\n\u2022 A program that handles errors keeps running instead of crashing",
                        "review_question": "Which keyword starts the block that handles an error?",
                        "review_answer": "except. It catches the error raised in the matching try block.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Why programs crash",
                                "content": "An 'exception' is an error that stops your program.\nExamples: converting bad text to a number, opening a missing file, dividing by zero.\nWithout handling, the program stops and prints a traceback.\nWith try/except, you decide what happens instead.",
                                "example": "# This crashes:\n# number = int('hello')\n\n# This is safe:\ntry:\n    number = int('hello')\nexcept ValueError:\n    print('That is not a number')",
                            },
                            {
                                "type": "practice",
                                "instruction": "Wrap int('abc') in a try/except. In the except block, print 'Cannot convert'.",
                                "starter_code": "# Convert 'abc' to an int safely\n\n# In except, print 'Cannot convert'\n",
                                "check": lambda code: "try:" in code and "except" in code and "int(" in code and "print(" in code,
                                "hint": "Write 'try:' then on an indented line 'number = int('abc')', then 'except ValueError:' and print a message",
                                "success_msg": "Your try/except catches the error and runs friendly code instead of crashing.",
                            },
                            {
                                "type": "concept",
                                "title": "Making programs robust",
                                "content": "You can catch specific errors (ValueError, FileNotFoundError, ZeroDivisionError).\nCode after the try/except still runs, even when an error occurs inside try.\nThis keeps the whole program alive for the user.\nYou can also put the fallback in the except block only.",
                                "example": "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')\n\nprint('The program is still running')",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use try/except to safely divide by two numbers, catching ZeroDivisionError and printing 'Cannot divide by zero'.",
                                "starter_code": "# Try dividing 10 by 0\n# Catch ZeroDivisionError\n",
                                "check": lambda code: "try:" in code and "except" in code and ("/ " in code or "/0" in code or "division" in code or "ZeroDivisionError" in code) and "print(" in code,
                                "hint": "Inside try: put result = 10 / 0. Under 'except ZeroDivisionError:' print a message",
                                "success_msg": "You caught ZeroDivisionError and let the program carry on safely.",
                            },
                            {
                                "type": "review",
                                "question": "What happens when an exception is raised inside a try block?",
                                "options": ["The program always crashes", "The matching except block runs", "The error is ignored silently", "The try block loops forever"],
                                "answer": "The matching except block runs",
                            },
                        ],
                        "final_project": {
                            "title": "Safe Calculator",
                            "description": "Build a tiny calculator that never crashes: it catches errors from bad input and from dividing by zero.",
                            "scenario": "A classroom app lets students type a calculation, but users make mistakes. Wrap the risky steps in try/except so a bad number prints a kind message and division by zero never crashes, then show a friendly result.",
                            "start_hints": [
                                "Start with one risky line such as number = int('12') inside a try and catch ValueError.",
                                "Add a division inside another try that catches ZeroDivisionError.",
                                "Print the result only when everything worked, and a friendly message otherwise.",
                            ],
                            "starter_snippet": "# Step 1: convert safely\nvalue = '12'\ntry:\n    number = int(value)\nexcept ValueError:\n    print('Not a number')",
                            "steps": [
                                "1. Convert a string value to an int inside a try, catching ValueError",
                                "2. Divide 100 by another value inside a try, catching ZeroDivisionError",
                                "3. Print the result when the math succeeded",
                                "4. Print a friendly message in each except instead of crashing",
                                "Expected: either the result or a clear message, never a traceback",
                            ],
                            "starter_code": "# Build your Safe Calculator\nvalue = '12'\ndivisor = 0\n\n# Step 1: convert safely with try/except\n\n# Step 2: divide safely\n\n# Print result or message\n",
                            "check": lambda code: (
                                True, "Great job! Your Safe Calculator catches errors instead of crashing."
                            ) if ("try:" in code and "except" in code and code.count("except") >= 1 and "print(" in code) else (
                                False, "Use try/except around risky input conversion and division, with print() in each except."
                            ),
                        },
                    },
                    {
                        "title": "JSON files",
                        "unit": "Data and storage",
                        "topic": "Structured file data",
                        "summary": "JSON is a simple text format for storing structured data that Python reads with the json module. It's how programs save and share lists and dictionaries.",
                        "example": "import json\ndata = {'name': 'Ada', 'age': 36}\nwith open('data.json', 'w') as f:\n    json.dump(data, f)\nwith open('data.json') as f:\n    loaded = json.load(f)\nprint(loaded)",
                        "challenge": "Save a dictionary to a JSON file, then load it back and print it.",
                        "why_it_matters": "JSON is the standard for saving structured data and for talking to web services. Learning it means you can save real program state and share data between programs.",
                        "key_takeaways": "\u2022 import json brings in the JSON tools\n\u2022 json.dump(data, file) saves data to a file\n\u2022 json.load(file) reads data back\n\u2022 JSON holds lists and dictionaries cleanly",
                        "review_question": "Which function saves a Python dictionary to a JSON file?",
                        "review_answer": "json.dump(data, f) writes the data to the open file f.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Why JSON exists",
                                "content": "Plain files only store text.\nJSON adds structure: it stores lists and dictionaries as readable text.\nPython turns those back into real lists and dictionaries.\nJSON is the common language between many programs.",
                                "example": "import json\n\ndata = {'color': 'blue', 'size': 10}\n# That dictionary can be saved and reloaded with JSON.",
                            },
                            {
                                "type": "practice",
                                "instruction": "Import json and use json.dump to save the dictionary {'name': 'Ada'} to a file called person.json.",
                                "starter_code": "import json\n\nperson = {'name': 'Ada'}\n\n# Save person to person.json\n",
                                "check": lambda code: "import json" in code and "json.dump(" in code and "open(" in code and "person" in code,
                                "hint": "with open('person.json', 'w') as f: json.dump(person, f)",
                                "success_msg": "json.dump() saved your dictionary to person.json.",
                            },
                            {
                                "type": "concept",
                                "title": "Loading data back",
                                "content": "json.load(file) reads a JSON file and returns a real list or dictionary.\nUse 'r' read mode with a with block.\nThe loaded object works like any normal dictionary.\nNow your program has real structured data again.",
                                "example": "import json\nwith open('person.json') as f:\n    person = json.load(f)\nprint(person['name'])   # Ada",
                            },
                            {
                                "type": "practice",
                                "instruction": "Load person.json back with json.load and print just the 'name' value.",
                                "starter_code": "import json\n\n# Load from person.json\n\n# Print the name\n",
                                "check": lambda code: "json.load(" in code and "open(" in code and "print(" in code,
                                "hint": "with open('person.json') as f: person = json.load(f). Then print(person['name'])",
                                "success_msg": "json.load() brought the data back as a real dictionary, and you read its value.",
                            },
                            {
                                "type": "review",
                                "question": "Which two functions write and read JSON files in Python?",
                                "options": ["json.write() / json.read()", "json.dump() / json.load()", "json.save() / json.open()", "json.put() / json.get()"],
                                "answer": "json.dump() / json.load()",
                            },
                        ],
                        "final_project": {
                            "title": "Favorites Saver",
                            "description": "Save a list of favorite items to a JSON file, then load it back and print them with a count.",
                            "scenario": "You're building a small app that remembers a user's favorites even after it closes. Save a list of favorites to a JSON file, load them back, print each one, and show how many there are.",
                            "start_hints": [
                                "Save the favorites list first: with open('favorites.json', 'w') as f: json.dump(favorites, f).",
                                "Load it back with json.load into a new variable.",
                                "Loop over the loaded list to print each item, then print len() of it.",
                            ],
                            "starter_snippet": "import json\nfavorites = ['Python', 'Data', 'Games']\n\n# Step 1: save the list to favorites.json\nwith open('favorites.json', 'w') as f:\n    json.dump(favorites, f)",
                            "steps": [
                                "1. Import json and create a list of three favorite items",
                                "2. Save the list to favorites.json with json.dump",
                                "3. Load it back with json.load",
                                "4. Loop and print each favorite, then print the total count",
                                "Expected: each favorite printed, then a total count",
                            ],
                            "starter_code": "# Build your Favorites Saver\nimport json\nfavorites = ['Python', 'Data', 'Games']\n\n# Save the list\n\n# Load it back\n\n# Print each item and the count\n",
                            "check": lambda code: (
                                True, "Great job! You saved and reloaded data with JSON."
                            ) if ("import json" in code and "json.dump(" in code and "json.load(" in code and "for " in code and "print(" in code) else (
                                False, "Use import json, json.dump() to save, json.load() to load, and a for loop to print."
                            ),
                        },
                    },
                    {
                        "title": "List comprehensions",
                        "unit": "Pythonic patterns",
                        "topic": "Concise loops",
                        "summary": "A list comprehension builds a new list in one compact line. It's a Pythonic shortcut for the common pattern of creating and filling a list with a for loop.",
                        "example": "squares = [n * n for n in range(5)]\nprint(squares)  # [0, 1, 4, 9, 16]",
                        "challenge": "Build a new list that squares each number in a range, in one line.",
                        "why_it_matters": "List comprehensions are everywhere in real Python. They're shorter, faster, and read clearly once you know the pattern.",
                        "key_takeaways": "\u2022 [expression for item in sequence] builds a list\n\u2022 The expression runs for each item\n\u2022 You can add 'if' to filter items\n\u2022 It replaces a short for-loop that fills a list",
                        "review_question": "What does [n * 2 for n in range(3)] produce?",
                        "review_answer": "It produces the list [0, 2, 4].",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "The comprehension pattern",
                                "content": "A list comprehension builds a list from an expression.\nThe grammar: [expression for item in sequence].\nFor each item, the expression is evaluated and added.\nIt's a compact replacement for a for-loop that appends.",
                                "example": "# Long way:\nresult = []\nfor n in range(4):\n    result.append(n * 2)\n\n# One line:\nsquares = [n * 2 for n in range(4)]\nprint(squares)  # [0, 2, 4, 6]",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use a list comprehension to create a list called squares containing n * n for each n in range(5).",
                                "starter_code": "# Build squares with a list comprehension\n",
                                "check": lambda code: "[" in code and "for " in code and "squares" in code and "*" in code,
                                "hint": "Type: squares = [n * n for n in range(5)]",
                                "success_msg": "One line built the whole list of squares: [0, 1, 4, 9, 16].",
                            },
                            {
                                "type": "concept",
                                "title": "Filtering with if",
                                "content": "Add 'if' to only keep some items.\nThe grammar: [expression for item in sequence if condition].\nItems that fail the condition are skipped.\nThis replaces a for-loop with an if inside.",
                                "example": "nums = [1, 2, 3, 4, 5, 6]\nevens = [n for n in nums if n % 2 == 0]\nprint(evens)  # [2, 4, 6]",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use a list comprehension with an if to keep only even numbers from the list nums = [1, 2, 3, 4], storing them in evens.",
                                "starter_code": "nums = [1, 2, 3, 4]\n\n# evens = [ ... if n % 2 == 0]\n",
                                "check": lambda code: "for " in code and "if " in code and "evens" in code and "% 2" in code,
                                "hint": "Type: evens = [n for n in nums if n % 2 == 0]",
                                "success_msg": "The if inside the comprehension kept only the even numbers: [2, 4].",
                            },
                            {
                                "type": "review",
                                "question": "In [x * 3 for x in vals if x > 0], what does the 'if' do?",
                                "options": ["Stops the whole loop", "Keeps only items where x > 0", "Multiplies by if", "Is invalid syntax"],
                                "answer": "Keeps only items where x > 0",
                            },
                        ],
                        "final_project": {
                            "title": "Data Transformer",
                            "description": "Build new lists from a source list using comprehensions, including a filtered and a doubled version.",
                            "scenario": "You have a list of daily temperatures and need to report a doubled 'adjusted' list and a list of only the warm days (above a threshold). Use comprehensions so the transformations are one clean line each.",
                            "start_hints": [
                                "Start with one comprehension that doubles the list: adjusted = [t * 2 for t in temps].",
                                "Add a second comprehension with an if that keeps only temps above 20.",
                                "Print both new lists so you can see the results.",
                            ],
                            "starter_snippet": "temps = [18, 25, 20, 32, 15]\n\n# Step 1: doubled values\nadjusted = [t * 2 for t in temps]\nprint(adjusted)",
                            "steps": [
                                "1. Create a source list of temperatures",
                                "2. Use a comprehension to make adjusted, doubling each temperature",
                                "3. Use a comprehension with an if to make warm, keeping only values above 20",
                                "4. Print both new lists",
                                "Expected: the doubled list and the filtered warm list",
                            ],
                            "starter_code": "# Build your Data Transformer\ntemps = [18, 25, 20, 32, 15]\n\n# adjusted = doubled values\n\n# warm = only above 20\n\n# Print both lists\n",
                            "check": lambda code: (
                                True, "Great job! You used list comprehensions to transform and filter data."
                            ) if ("[" in code and "for " in code and code.count("for ") >= 2 and "print(" in code) else (
                                False, "Use two list comprehensions with for ... in ..., add an if to one, and print both."
                            ),
                        },
                    },
                    {
                        "title": "GUIs with tkinter",
                        "unit": "GUI apps",
                        "topic": "Building windows",
                        "summary": "tkinter comes with Python and lets you build windows with text, buttons, and more. You create a main window, add widgets to it, and run an event loop that keeps it alive.",
                        "example": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title('My First App')\n\nlabel = tk.Label(root, text='Hello, GUI!')\nlabel.pack()\n\nroot.mainloop()",
                        "challenge": "Create a window with a title and one label.",
                        "why_it_matters": "GUIs let non-programmers use what you build. Even a tiny window is a big step from a script toward a real desktop app.",
                        "key_takeaways": "\u2022 import tkinter as tk brings in the GUI toolkit\n\u2022 tk.Tk() creates the main window\n\u2022 tk.Label shows text; .pack() places it in the window\n\u2022 root.mainloop() keeps the window open and handles events",
                        "review_question": "Which method must you call at the end to keep a tkinter window open and handle clicks?",
                        "review_answer": "root.mainloop(). It starts the event loop that keeps the window alive.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Your first window",
                                "content": "tkinter is Python's built-in GUI toolkit.\nimport tkinter as tk makes its tools available.\nroot = tk.Tk() creates the main window.\nroot.title('...') sets the text at the window's top.\nroot.mainloop() starts the event loop \u2014 the window stays open until you close it.\n\nTip: in this app your window appears for about 1.5 seconds, then closes automatically so the sandbox can finish.",
                                "example": "import tkinter as tk\nroot = tk.Tk()\nroot.title('My App')\nroot.mainloop()",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create a Tk window, give it the title 'My App', and call mainloop() to run it.",
                                "starter_code": "import tkinter as tk\n\n# Create the main window\n\n# Set the title\n\n# Keep the window open\n",
                                "check": lambda code: "tkinter" in code and "tk.Tk(" in code and "title(" in code and "mainloop" in code,
                                "hint": "Type: root = tk.Tk()  then  root.title('My App')  then  root.mainloop()",
                                "success_msg": "Your window opened! tk.Tk() created it and mainloop() kept it on screen until it closed.",
                            },
                            {
                                "type": "concept",
                                "title": "Labels show text",
                                "content": "A Label is a piece of text you put on a window.\nwidget = tk.Label(root, text='...') builds one.\npack() places it in the window and resizes the window to fit.\nYou can change the text later with label.config(text='...').",
                                "example": "import tkinter as tk\nroot = tk.Tk()\nwelcome = tk.Label(root, text='Welcome to Python')\nwelcome.pack()\nroot.mainloop()",
                            },
                            {
                                "type": "practice",
                                "instruction": "Add a Label with the text 'Welcome to Python' to your window and pack() it.",
                                "starter_code": "import tkinter as tk\nroot = tk.Tk()\nroot.title('My App')\n\n# Create a label and pack it\n\n\nroot.mainloop()\n",
                                "check": lambda code: "Label" in code and "text=" in code and "pack(" in code and "tk.Tk(" in code,
                                "hint": "Type: welcome = tk.Label(root, text='Welcome to Python') then welcome.pack()",
                                "success_msg": "Your label showed up in the window. text= sets what it says and pack() placed it.",
                            },
                            {
                                "type": "review",
                                "question": "What does root.mainloop() do?",
                                "options": ["Closes the window", "Starts the event loop that keeps the window open", "Deletes a label", "Adds a new button"],
                                "answer": "Starts the event loop that keeps the window open",
                            },
                        ],
                        "final_project": {
                            "title": "My First Window",
                            "description": "Build a small welcome window with a title and two labels.",
                            "scenario": "Your app is getting a first screen. Create a window titled 'Python Coach' that shows two labels: an app title and a welcome message.",
                            "start_hints": [
                                "Create the root window first: root = tk.Tk(), then give it a title with root.title('Python Coach').",
                                "Make two labels with tk.Label and different text \u2014 one for the app title, one for the welcome message.",
                                "pack() each label so they appear, then call root.mainloop().",
                            ],
                            "starter_snippet": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title('Python Coach')",
                            "steps": [
                                "1. Create the root window with tk.Tk()",
                                "2. Set the window title",
                                "3. Add a label for the app title",
                                "4. Add a label for a welcome message",
                                "5. pack() both labels and call mainloop()",
                                "Expected: a window with a title and two lines of text",
                            ],
                            "starter_code": "# Build your My First Window app\nimport tkinter as tk\n\nroot = tk.Tk()\nroot.title('Python Coach')\n\n# App title label\n\n# Welcome message label\n\n\nroot.mainloop()\n",
                            "check": lambda code: (
                                True, "Awesome! You built a real GUI window with text labels."
                            ) if ("tkinter" in code and "tk.Tk(" in code and "Label" in code and code.count("Label") >= 2 and "pack(" in code and "mainloop" in code) else (
                                False, "Create a Tk window, add two Labels, pack() them, and call mainloop()."
                            ),
                        },
                    },
                    {
                        "title": "Buttons and events",
                        "unit": "GUI apps",
                        "topic": "Responding to clicks",
                        "summary": "Buttons let users make things happen. You give a button a command function, and tkinter runs that function every time the button is clicked.",
                        "example": "import tkinter as tk\n\ndef say_hi():\n    print('Hello!')\n\nroot = tk.Tk()\nbtn = tk.Button(root, text='Click me', command=say_hi)\nbtn.pack()\nroot.mainloop()",
                        "challenge": "Add a button that prints a message when clicked.",
                        "why_it_matters": "Events are how GUI apps interact with users. Every click, keypress, and menu choice runs a small function you write.",
                        "key_takeaways": "\u2022 tk.Button(root, text=..., command=func) creates a clickable button\n\u2022 command= takes the function name with NO parentheses\n\u2022 The button's function runs each time the button is clicked\n\u2022 label.config(text=...) updates text already on screen",
                        "review_question": "How do you pass a function to a Button's command option?",
                        "review_answer": "Use the function name without parentheses: command=my_function.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Making a button",
                                "content": "A Button is a clickable area on your window.\ntk.Button(root, text='Go', command=run) creates one.\ntext= is what the button says.\ncommand= is the function that runs when clicked.\nLike labels, a button needs pack() to appear.",
                                "example": "import tkinter as tk\n\ndef go():\n    print('Clicked!')\n\nroot = tk.Tk()\nbtn = tk.Button(root, text='Go', command=go)\nbtn.pack()\nroot.mainloop()",
                            },
                            {
                                "type": "practice",
                                "instruction": "Add a button that says 'Click me' and runs a function called on_click that prints 'Hello!'.",
                                "starter_code": "import tkinter as tk\n\n# Define on_click that prints 'Hello!'\n\n\nroot = tk.Tk()\n# Create the button with command=on_click\n\n# Pack it\n\n\nroot.mainloop()\n",
                                "check": lambda code: "Button" in code and "command=" in code and "def " in code and "print(" in code and "pack(" in code,
                                "hint": "Write: def on_click(): print('Hello!')  then  btn = tk.Button(root, text='Click me', command=on_click)  and  btn.pack()",
                                "success_msg": "Your button is wired up! Clicking it runs on_click and prints 'Hello!'.",
                            },
                            {
                                "type": "concept",
                                "title": "Updating what's on screen",
                                "content": "Buttons get more useful when they change other widgets.\nlabel.config(text='new text') swaps a label's text.\nThis is how you give feedback without printing to the console.\nIn the window, clicking a button changes what the user sees.",
                                "example": "import tkinter as tk\n\ndef change():\n    label.config(text='Changed!')\n\nroot = tk.Tk()\nlabel = tk.Label(root, text='Before')\nlabel.pack()\nbtn = tk.Button(root, text='Change', command=change)\nbtn.pack()\nroot.mainloop()",
                            },
                            {
                                "type": "practice",
                                "instruction": "Change the label's text to 'It works!' when the button is clicked, using config(text=...).",
                                "starter_code": "import tkinter as tk\n\nroot = tk.Tk()\nlabel = tk.Label(root, text='Before')\nlabel.pack()\n\ndef on_click():\n    # Update the label text\n    pass\n\nbtn = tk.Button(root, text='Click', command=on_click)\nbtn.pack()\nroot.mainloop()\n",
                                "check": lambda code: "config(" in code and "text=" in code and "on_click" in code and "def " in code,
                                "hint": "Inside on_click write: label.config(text='It works!')",
                                "success_msg": "Now the button updates the label on screen \u2014 that's an event changing the UI.",
                            },
                            {
                                "type": "review",
                                "question": "When you create a button with command=my_func, when does my_func run?",
                                "options": ["When the program starts", "Every time the button is clicked", "When the window closes", "Never"],
                                "answer": "Every time the button is clicked",
                            },
                        ],
                        "final_project": {
                            "title": "Click Counter",
                            "description": "Build a button that counts how many times it's been clicked and shows the count in a label.",
                            "scenario": "A small fan page wants a counter: every click raises a number on screen. Use a variable for the count, a label to show it, and a button whose command updates both.",
                            "start_hints": [
                                "Start with a count variable set to 0 before you create the widgets.",
                                "Show it in a label, then write a function that adds 1 to count and calls label.config(text=str(count)).",
                                "Wire the button to that function with command= and pack() everything.",
                            ],
                            "starter_snippet": "import tkinter as tk\n\nroot = tk.Tk()\ncount = 0\nlabel = tk.Label(root, text='0')\nlabel.pack()",
                            "steps": [
                                "1. Create a root window",
                                "2. Make a count variable starting at 0",
                                "3. Show the count in a label",
                                "4. Write a function that increases count and updates the label with config()",
                                "5. Add a button that runs the function when clicked",
                                "Expected: clicking the button raises the number shown",
                            ],
                            "starter_code": "# Build your Click Counter\nimport tkinter as tk\n\nroot = tk.Tk()\ncount = 0\nlabel = tk.Label(root, text=str(count))\nlabel.pack()\n\n# Function that adds 1 and updates the label\n\n\n# Button that calls the function when clicked\n\n\nroot.mainloop()\n",
                            "check": lambda code: (
                                True, "Excellent! The button and its command function make a working counter."
                            ) if ("tkinter" in code and "Button" in code and "command=" in code and "def " in code and "config(" in code and "label" in code.lower()) else (
                                False, "Add a Button with command= wired to a function that adds 1 and updates the label with config()."
                            ),
                        },
                    },
                    {
                        "title": "Entry widgets and forms",
                        "unit": "GUI apps",
                        "topic": "Getting user input",
                        "summary": "A tkinter Entry lets the user type text. You read what they typed with .get(), convert it with int() or float(), and use it in your program.",
                        "example": "import tkinter as tk\n\ndef greet():\n    name = entry.get()\n    label.config(text='Hello, ' + name + '!')\n\nroot = tk.Tk()\nlabel = tk.Label(root, text='What is your name?')\nlabel.pack()\nentry = tk.Entry(root)\nentry.pack()\nbtn = tk.Button(root, text='Go', command=greet)\nbtn.pack()\nroot.mainloop()",
                        "challenge": "Read text from an Entry, convert it, and show a result.",
                        "why_it_matters": "Forms are how apps take real input from users. Converting what they type with int() or float() keeps your math safe.",
                        "key_takeaways": "\u2022 tk.Entry(root) creates a text box the user can type in\n\u2022 entry.get() returns what the user typed as a string\n\u2022 Convert typed numbers with int() or float() before doing math\n\u2022 Show results with label.config(text=...) so the answer appears on screen",
                        "review_question": "What does entry.get() return?",
                        "review_answer": "The text the user typed, as a string.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Typing into a form",
                                "content": "An Entry is a one-line text box.\ntk.Entry(root) creates it and pack() places it.\nentry.get() gives you whatever the user typed, as a string.\nCombine it with a button so the form reacts.",
                                "example": "import tkinter as tk\nroot = tk.Tk()\nentry = tk.Entry(root)\nentry.pack()\nroot.mainloop()",
                            },
                            {
                                "type": "practice",
                                "instruction": "Create an Entry, and in a button command function read it with entry.get() and print it.",
                                "starter_code": "import tkinter as tk\n\ndef show():\n    # Read the entry and print it\n    pass\n\nroot = tk.Tk()\n# Create the Entry and pack it\n\n\n# Button that calls show\n\n\nroot.mainloop()\n",
                                "check": lambda code: "Entry" in code and "get()" in code and "print(" in code and "Button" in code and "command=" in code,
                                "hint": "Inside show() write: value = entry.get() then print(value). Create the box with entry = tk.Entry(root) and pack it.",
                                "success_msg": "entry.get() grabbed what the user typed as a string, and your button printed it.",
                            },
                            {
                                "type": "concept",
                                "title": "Numbers from text",
                                "content": "Everything from an Entry is text.\nTo do math you must convert: int(text) or float(text).\nint('42') becomes the number 42.\nfloat('4.5') handles decimals.\nConvert once, then do the math safely.",
                                "example": "value = entry.get()   # e.g. '42'\nnumber = int(value)    # 42\ndoubled = number * 2\nprint(doubled)",
                            },
                            {
                                "type": "practice",
                                "instruction": "Read the entry, convert it to an int, multiply it by 2, and update the label to show the doubled value.",
                                "starter_code": "import tkinter as tk\n\ndef double_it():\n    # Read, convert, multiply\n    pass\n\nroot = tk.Tk()\nlabel = tk.Label(root, text='Type a number')\nlabel.pack()\nentry = tk.Entry(root)\nentry.pack()\nbtn = tk.Button(root, text='Double', command=double_it)\nbtn.pack()\nroot.mainloop()\n",
                                "check": lambda code: "get()" in code and ("int(" in code or "float(" in code) and "config(" in code and "label" in code.lower() and ("* 2" in code or "*2" in code),
                                "hint": "Inside double_it(): num = int(entry.get()), doubled = num * 2, label.config(text=str(doubled))",
                                "success_msg": "You read text, converted it to a number, did the math, and showed the answer in the window.",
                            },
                            {
                                "type": "review",
                                "question": "Why do you call int() on the value from entry.get()?",
                                "options": ["To make it a letter", "Because get() returns a string and math needs a number", "To open the window", "To clear the entry"],
                                "answer": "Because get() returns a string and math needs a number",
                            },
                        ],
                        "final_project": {
                            "title": "Tip Calculator",
                            "description": "Build a tiny form that reads an amount, calculates a 15% tip, and shows the result in a label.",
                            "scenario": "A restaurant wants a quick tip calculator. The user types a bill amount into an Entry, clicks a button, and the window shows the 15% tip. Convert the entry text and use float math.",
                            "start_hints": [
                                "Start with the Entry and a button wired to a function called calc_tip.",
                                "Inside calc_tip, read the value with float(entry.get()) and multiply by 0.15.",
                                "Show the answer with label.config(text='Tip: $' + str(tip)) and pack everything.",
                            ],
                            "starter_snippet": "import tkinter as tk\n\nroot = tk.Tk()\nentry = tk.Entry(root)\nentry.pack()",
                            "steps": [
                                "1. Create an Entry for the bill amount",
                                "2. Add a label to show the result",
                                "3. Write calc_tip() that reads the entry, converts with float(), and multiplies by 0.15",
                                "4. Update the label with config(text=...) to show the tip",
                                "5. Add a button with command=calc_tip",
                                "Expected: typing an amount and clicking the button shows the 15% tip",
                            ],
                            "starter_code": "# Build your Tip Calculator\nimport tkinter as tk\n\nroot = tk.Tk()\n\n# Entry for the bill amount\n\n\n# Label to show the result\n\n\ndef calc_tip():\n    # Read, convert, multiply by 0.15, show it\n    pass\n\n# Button that runs calc_tip\n\n\nroot.mainloop()\n",
                            "check": lambda code: (
                                True, "Great! Your form reads real input, does the math, and shows the result on screen."
                            ) if ("tkinter" in code and "Entry" in code and "get()" in code and "float(" in code and "0.15" in code and "config(" in code and "Button" in code and "command=" in code) else (
                                False, "Make an Entry, read it with get(), convert with float(), multiply by 0.15, and show it with config()."
                            ),
                        },
                    },
                    {
                        "title": "Loading real data",
                        "unit": "Real-world data",
                        "topic": "JSON datasets",
                        "summary": "Real programs don't invent their data - they read it from files. The app bundles us_states.json with all 50 US states (capitals, statehood years, regions) and json.load() turns that file into a Python list of dictionaries you can loop over.",
                        "example": "import json\nwith open('us_states.json') as f:\n    states = json.load(f)\nprint(len(states), 'states ready')",
                        "challenge": "Load a real JSON dataset and extract facts from it.",
                        "why_it_matters": "Analyzing real data - like all 50 US states - turns your code from toy examples into something genuinely useful. json.load() is the same tool data scientists use to bring datasets into Python.",
                        "key_takeaways": "\u2022 JSON stores structured data in files as a list of {curly brace} records\n\u2022 json.load(file) turns a JSON file into a Python list or dict\n\u2022 Use a with open(...) block so the file closes itself\n\u2022 Each state is a dictionary - access fields like state['capital']",
                        "review_question": "What does json.load(file) give you back?",
                        "review_answer": "A Python list or dictionary built from the JSON file.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Datasets arrive as JSON files",
                                "content": "Real data usually lives in files, not inside your code.\nJSON stores data as text: a list of {curly brace} records.\nThe app bundles three real datasets you can open by name:\n  us_states.json - 50 states with capitals and years\n  elements.json - 20 chemical elements\n  planets.json - the eight planets\nAll three live in the project's data/ folder.",
                                "example": "import json\n\nwith open('us_states.json') as f:\n    states = json.load(f)\n\nprint(len(states))           # 50\nprint(states[0]['capital'])  # Montgomery",
                            },
                            {
                                "type": "practice",
                                "instruction": "Load us_states.json with json.load() and print how many states are in the file.",
                                "starter_code": "import json\n\nwith open('us_states.json') as f:\n    states = json.load(f)\n\n# Print how many states are in the list\n",
                                "check": lambda code: "json" in code and "load(" in code and "open(" in code and "us_states" in code and "print(" in code,
                                "hint": "Print len(states) - states is the list that json.load() returned.",
                                "success_msg": "json.load() turned the file into a list of 50 dictionary records - real data, ready to use.",
                            },
                            {
                                "type": "concept",
                                "title": "One record per state",
                                "content": "Each state is its own dictionary inside the list.\nFields: 'name', 'abbr', 'capital', 'statehood_year', 'region'.\nLoop over the list and print state['name'] and state['capital'].\nThis is how a file of data becomes information.",
                                "example": "import json\n\nwith open('us_states.json') as f:\n    states = json.load(f)\n\nfor state in states:\n    print(state['name'], '-', state['capital'])",
                            },
                            {
                                "type": "practice",
                                "instruction": "Load us_states.json, then use a for loop to print each state's name and its capital, one per line.",
                                "starter_code": "import json\n\nwith open('us_states.json') as f:\n    states = json.load(f)\n\n# Loop and print name and capital for each state\n",
                                "check": lambda code: "json" in code and "load(" in code and "open(" in code and "us_states" in code and "for " in code and "capital" in code and "print(" in code,
                                "hint": "for state in states: then print(state['name'], state['capital']).",
                                "success_msg": "Your loop walked all 50 records and printed the name and capital of each state.",
                            },
                            {
                                "type": "review",
                                "question": "What does json.load(file) give you back?",
                                "options": ["A string of the whole file", "A Python list or dictionary built from the JSON", "A brand-new file", "An error"],
                                "answer": "A Python list or dictionary built from the JSON",
                            },
                        ],
                        "final_project": {
                            "title": "State Census Report",
                            "description": "Load all 50 states and print a report of how many states are in each census region.",
                            "scenario": "Your class is studying how the USA grew. Load us_states.json, count how many states belong to each region (South, Midwest, Northeast, West), and print a line for each region with its total.",
                            "start_hints": [
                                "Load us_states.json with json.load() and store the list.",
                                "Keep a dictionary of counts that starts each region at 0.",
                                "Loop over the states, add 1 to the count for state['region'], then print each region and its total.",
                            ],
                            "starter_snippet": "import json\n\nwith open('us_states.json') as f:\n    states = json.load(f)",
                            "steps": [
                                "1. Import json and load us_states.json",
                                "2. Build a dictionary to hold the region counts",
                                "3. Loop over the states and bump the count for each state's region",
                                "4. Print every region and its total",
                                "Expected: the four regions (South, Midwest, Northeast, West) with totals that sum to 50",
                            ],
                            "starter_code": "# Build your State Census Report\nimport json\n\nwith open('us_states.json') as f:\n    states = json.load(f)\n\n# Dictionary to count states per region\n\n\n# Loop and count each state's region\n\n\n# Print the final report\n",
                            "check": lambda code: (
                                True, "Great! Your census counts every state into its region and the totals sum to 50."
                            ) if ("json" in code and "open(" in code and "load(" in code and "us_states" in code and "region" in code and "for " in code and "print(" in code and ("{" in code or "count" in code)) else (
                                False, "Load us_states.json, count each state['region'] in a dictionary, and print the totals."
                            ),
                        },
                    },
                    {
                        "title": "Filtering and ranking data",
                        "unit": "Real-world data",
                        "topic": "Sorting and selecting",
                        "summary": "Sorted data is easier to read. sorted(data, key=lambda item: item['field']) orders a list of dictionaries by one field, and a for loop or comprehension can pick out just the records that match a condition.",
                        "example": "import json\nwith open('elements.json') as f:\n    data = json.load(f)\nranked = sorted(data, key=lambda e: e['atomic_mass'])\nprint([e['name'] for e in ranked[-3:]])",
                        "challenge": "Rank the elements by mass and filter the dataset down to just the metals.",
                        "why_it_matters": "Every dashboard and report sorts or filters data. This is where your code stops just reading data and starts answering questions about it.",
                        "key_takeaways": "\u2022 sorted(data, key=lambda item: item['field']) orders by one field\n\u2022 key= tells sorted() which field to rank by\n\u2022 Add reverse=True for largest first\n\u2022 A comprehension or if can filter data to matching records",
                        "review_question": "How do you order a list of dictionaries by one field, like atomic_mass?",
                        "review_answer": "sorted(data, key=lambda item: item['field']).",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Sort by one field",
                                "content": "sorted() returns a new list in order.\nkey=lambda item: item['field'] says which field to rank by.\nWithout key=, sorted() would try to compare whole dictionaries.\nreverse=True flips it so the biggest value comes first.",
                                "example": "import json\n\nwith open('elements.json') as f:\n    data = json.load(f)\n\nranked = sorted(data, key=lambda e: e['atomic_mass'], reverse=True)\nfor e in ranked[:3]:\n    print(e['name'], e['atomic_mass'])",
                            },
                            {
                                "type": "practice",
                                "instruction": "Load elements.json and print the names of the three elements with the largest atomic mass, using sorted() with a key= so it orders by that field.",
                                "starter_code": "import json\n\nwith open('elements.json') as f:\n    data = json.load(f)\n\n# Sort by atomic mass, then print the names of the top three\n",
                                "check": lambda code: "json" in code and "load(" in code and "open(" in code and "elements" in code and "sorted(" in code and "atomic_mass" in code and "print(" in code,
                                "hint": "ranked = sorted(data, key=lambda e: e['atomic_mass'], reverse=True), then loop ranked[:3] and print e['name'].",
                                "success_msg": "sorted() ranked all 20 elements by mass and you printed the three heaviest from the real dataset.",
                            },
                            {
                                "type": "concept",
                                "title": "Filter with a condition",
                                "content": "Pick out matching records with a condition.\nA list comprehension keeps only what matches:\n  [item for item in data if condition(item)]\nA for loop plus an if works too.\n'element' in e['category'] matches 'alkali metal' and 'noble gas' alike.",
                                "example": "import json\n\nwith open('elements.json') as f:\n    data = json.load(f)\n\nmetals = [e for e in data if 'metal' in e['category']]\nfor e in metals:\n    print(e['name'])",
                            },
                            {
                                "type": "practice",
                                "instruction": "Load elements.json and print the name of every element whose category contains the word 'metal', one name per line (use a for loop or a list comprehension).",
                                "starter_code": "import json\n\nwith open('elements.json') as f:\n    data = json.load(f)\n\n# Print the name of each element whose category contains 'metal'\n",
                                "check": lambda code: "json" in code and "load(" in code and "open(" in code and "elements" in code and "metal" in code and "print(" in code and ("for " in code or "[" in code),
                                "hint": "Filter with: [e for e in data if 'metal' in e['category']], then loop and print(e['name']).",
                                "success_msg": "Your filter kept only the records whose category contains 'metal', so you see the metals and nothing else.",
                            },
                            {
                                "type": "review",
                                "question": "How do you order a list of dictionaries by one field, like atomic_mass?",
                                "options": ["sorted() isn't for dictionaries", "sorted(data) works automatically", "sorted(data, key=lambda item: item['field'])", "You must write your own sort loop every time"],
                                "answer": "sorted(data, key=lambda item: item['field'])",
                            },
                        ],
                        "final_project": {
                            "title": "Lightest and Heaviest",
                            "description": "Load the elements and print the lightest and heaviest element, each with its atomic mass.",
                            "scenario": "A chemistry poster needs the bookends of the periodic table. Load elements.json, find the element with the smallest atomic_mass and the one with the largest, and print both names with their masses.",
                            "start_hints": [
                                "Load elements.json with json.load() into a list called data.",
                                "Use min(data, key=lambda e: e['atomic_mass']) for the lightest.",
                                "Use max(data, key=lambda e: e['atomic_mass']) for the heaviest, then print both with print().",
                            ],
                            "starter_snippet": "import json\n\nwith open('elements.json') as f:\n    data = json.load(f)",
                            "steps": [
                                "1. Import json and load elements.json",
                                "2. Find the lightest element with min() and a key= for atomic_mass",
                                "3. Find the heaviest element with max() and a key= for atomic_mass",
                                "4. Print each element's name and atomic_mass",
                                "Expected: Hydrogen (1.008) is lightest, Calcium (40.078) is heaviest of the 20",
                            ],
                            "starter_code": "# Build your Lightest and Heaviest report\nimport json\n\nwith open('elements.json') as f:\n    data = json.load(f)\n\n# Find the lightest element\n\n\n# Find the heaviest element\n\n\n# Print both with their names and masses\n",
                            "check": lambda code: (
                                True, "Nice! min() and max() with a key answered both questions from the real dataset."
                            ) if ("json" in code and "open(" in code and "load(" in code and "elements" in code and "atomic_mass" in code and "print(" in code and ("min(" in code or "max(" in code or "sorted(" in code)) else (
                                False, "Load elements.json, use min() and max() with a key= for atomic_mass, and print the results."
                            ),
                        },
                    },
                    {
                        "title": "Summarizing data",
                        "unit": "Real-world data",
                        "topic": "Reports from datasets",
                        "summary": "Summaries turn a whole dataset into a few numbers. min(), max(), and an average (sum / count) answer questions like 'biggest', 'smallest', and 'on average' across a field.",
                        "example": "import json\nwith open('planets.json') as f:\n    data = json.load(f)\nbig = max(data, key=lambda p: p['diameter_km'])\nprint(big['name'], big['diameter_km'])",
                        "challenge": "Answer questions about the planets with max(), min(), and averages.",
                        "why_it_matters": "Real reports rarely list every row. A single average or maximum turns a spreadsheet into a conclusion someone can act on.",
                        "key_takeaways": "\u2022 max(data, key=...) and min(data, key=...) return the record, not just the number\n\u2022 Build a list of one field, then summarize it\n\u2022 Average = sum(values) / len(values)\n\u2022 round(value, 2) keeps the answer tidy",
                        "review_question": "What does max(data, key=lambda p: p['diameter_km']) return?",
                        "review_answer": "The whole planet dictionary with the largest diameter_km.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Pull the biggest record",
                                "content": "max() with no key returns the biggest *number*.\nAdd key=lambda item: item['field'] and max() returns the whole *record*.\nThat record carries the name and the value together.\nmin() does the same for the smallest.",
                                "example": "import json\n\nwith open('planets.json') as f:\n    data = json.load(f)\n\nbiggest = max(data, key=lambda p: p['diameter_km'])\nprint(biggest['name'], biggest['diameter_km'], 'km')",
                            },
                            {
                                "type": "practice",
                                "instruction": "Load planets.json and print the name of the planet with the largest diameter (use max() with a key).",
                                "starter_code": "import json\n\nwith open('planets.json') as f:\n    data = json.load(f)\n\n# Find the planet with the biggest diameter_km and print its name\n",
                                "check": lambda code: "json" in code and "load(" in code and "open(" in code and "planets" in code and "max(" in code and "diameter" in code and "print(" in code,
                                "hint": "biggest = max(data, key=lambda p: p['diameter_km']), then print(biggest['name']).",
                                "success_msg": "max() with a key returned the whole Jupiter record - the largest planet in the dataset.",
                            },
                            {
                                "type": "concept",
                                "title": "Average a column",
                                "content": "An average is total divided by count.\nlist comprehensions gather one field: [p['distance_au'] for p in data].\nsum(values) adds the list, len(values) counts it.\nAverage = sum(values) / len(values).\nround(avg, 2) trims the answer to two decimals.",
                                "example": "import json\n\nwith open('planets.json') as f:\n    data = json.load(f)\n\ndistances = [p['distance_au'] for p in data]\navg = sum(distances) / len(distances)\nprint(round(avg, 2), 'AU')",
                            },
                            {
                                "type": "practice",
                                "instruction": "Load planets.json and print the average distance from the Sun (the distance_au field), rounded to two decimals.",
                                "starter_code": "import json\n\nwith open('planets.json') as f:\n    data = json.load(f)\n\n# Average distance_au across all planets, rounded to 2 decimals\n",
                                "check": lambda code: "json" in code and "load(" in code and "open(" in code and "planets" in code and "distance_au" in code and "round(" in code and "print(" in code and ("sum(" in code or "for " in code),
                                "hint": "avg = sum([p['distance_au'] for p in data]) / len(data), then print(round(avg, 2)).",
                                "success_msg": "Your one-line summary computed the average distance of all eight planets from the Sun.",
                            },
                            {
                                "type": "review",
                                "question": "What does max(data, key=lambda p: p['diameter_km']) return?",
                                "options": ["Just the largest number", "The whole record (dictionary) with the largest diameter_km", "A new sorted list", "An error"],
                                "answer": "The whole record (dictionary) with the largest diameter_km",
                            },
                        ],
                        "final_project": {
                            "title": "Solar System Report",
                            "description": "Load the planets and print the biggest planet, the average diameter, and the planet with the most moons.",
                            "scenario": "An astronomy club wants a one-page summary. Load planets.json, then print (1) the name of the planet with the largest diameter_km, (2) the average diameter_km of all eight planets, and (3) the name of the planet with the most moons.",
                            "start_hints": [
                                "Load planets.json with json.load() into a list called data.",
                                "Use max(data, key=lambda p: p['diameter_km']) for the biggest planet's name.",
                                "Average the diameter_km column with sum() and len(), round() it, and use max() on the moons field for the last line.",
                            ],
                            "starter_snippet": "import json\n\nwith open('planets.json') as f:\n    data = json.load(f)",
                            "steps": [
                                "1. Import json and load planets.json",
                                "2. Print the name of the biggest planet (max with a key for diameter_km)",
                                "3. Print the average diameter_km rounded to two decimals",
                                "4. Print the name of the planet with the most moons (max with a key for moons)",
                                "Expected: Jupiter, an average diameter, and Saturn",
                            ],
                            "starter_code": "# Build your Solar System Report\nimport json\n\nwith open('planets.json') as f:\n    data = json.load(f)\n\n# 1) Biggest planet by diameter\n\n\n# 2) Average diameter, rounded\n\n\n# 3) Planet with the most moons\n",
                            "check": lambda code: (
                                True, "Great! Your report answered all three questions straight from planets.json."
                            ) if ("json" in code and "open(" in code and "load(" in code and "planets" in code and "diameter" in code and "moons" in code and "print(" in code and ("max(" in code or "sorted(" in code) and ("sum(" in code or "/" in code)) else (
                                False, "Load planets.json, then summarize diameter_km and moons with max(), sum(), and len()."
                            ),
                        },
                    },
                    {
                        "title": "Regular expressions",
                        "unit": "Text power tools",
                        "topic": "Regular expressions",
                        "summary": "Regex lets you search and extract text by pattern instead of by exact match. It's how you find every email in a document, validate phone numbers, or pull dates out of messy text. Scary at first, essential for real work.",
                        "example": "import re\n\ntext = 'Call 555-1234 today'\nm = re.search(r'\\d{3}-\\d{4}', text)\nprint(m.group())  # 555-1234",
                        "challenge": "Use re.findall() to pull every email address out of a string.",
                        "why_it_matters": "Almost every real codebase handles messy text: logs, user input, imports, APIs. Regex is the tool professionals use to tame it, and it shows up in interviews, data cleaning, and web scraping.",
                        "key_takeaways": "\u2022 re.findall(pattern, text) returns every match as a list\n\u2022 \\d matches a digit, \\w matches a letter/digit\n\u2022 {n} repeats the previous token exactly n times\n\u2022 r'...' raw strings avoid escaped backslashes",
                        "review_question": "What does \\d+ match?",
                        "review_answer": "One or more consecutive digits.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Patterns instead of exact text",
                                "content": "Regex is a mini-language for describing patterns.\n\n\\d = a digit\n\\w = a letter or digit\n+  = one or more of the previous\n{n} = exactly n of the previous\n[abc] = one of a, b, c\n\nre.search(pattern, text) finds the first match.\nre.findall(pattern, text) returns all matches.",
                                "example": "import re\n\ntext = \"Order 42 then 7, done.\"\nprint(re.findall(r'\\d+', text))   # ['42', '7']\n\nm = re.search(r'\\d+', text)\nprint(m.group())                   # 42",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use re.findall() with a pattern matching one or more digits to print all the numbers in the text.",
                                "starter_code": "import re\n\ntext = \"Version 2.0 released on 5 September\"\n\n# Find all numbers (digits)\n",
                                "check": lambda code: "re.findall" in code and "\\d" in code and "print(" in code,
                                "hint": "Use re.findall(r'\\d+', text) and print the result.",
                                "success_msg": "Nice! findall + \\d+ found every number in one line.",
                            },
                            {
                                "type": "fill",
                                "instruction": "Fill in the blanks to extract every email address from the text. Emails look like name@site.com.",
"template": "import re\n\ntext = 'reach me at ada@cog.com or bob@py.org'\nemail_pattern = r'___@___.___'\nprint(re.findall(email_pattern, ___))\n",
                                "expected_output": "['ada@cog.com', 'bob@py.org']",
                                "goal_hint": "The pattern uses \\w+ for the name, site, and ending. Then the last blank is the text to search in.",
                                "check": lambda code: "\\w+@\\w+.\\w+" in code or "\\w+@\\w+\\.\\w+" in code,
                                "success_msg": "You built a working email-extraction pattern!",
                                "hint": "Blanks: word characters before, after @, and at the end; the last blank is text.",
                            },
                            {
                                "type": "debug",
                                "instruction": "This regex is meant to find the word 'hi', but it returns []. The pattern is the culprit \u2014 fix it and print the matches.",
                                "broken_code": "import re\n\ntext = 'find the word hi in here'\npattern = '\\bhi\\b'\nprint(re.findall(pattern, text))\n",
                                "goal_hint": "Without the r prefix Python reads \\b as the backspace character, not a word boundary, so it matches nothing. Make it raw: r'\\bhi\\b'.",
                                "bug_notes": "In a regular string, '\\b' becomes the invisible backspace control character. re.findall then looks for backspace around 'hi' and comes up empty. A raw string preserves \\b as the word-boundary pattern.",
                                "check": lambda code: "r'\\bhi\\b'" in code and "re.findall" in code and "print(" in code,
                                "success_msg": "Fixed! The raw string turned \\b into a real word boundary and the matches appeared.",
                                "hint": "Add an r before the pattern's opening quote so \\b isn't eaten.",
                            },
                            {
                                "type": "review",
                                "question": "What is r'\\d{3}'?",
                                "options": ["A raw string matching three digits", "A string of 3 backslashes", "An error", "The number 3"],
                                "answer": "A raw string matching three digits",
                            },
                        ],
                        "final_project": {
                            "title": "Log Analyzer",
                            "description": "Build a tool that pulls every timestamp and number out of a messy log line using regex.",
                            "scenario": "A server log line contains mixed text. Write code that extracts all six timestamps (HH:MM) and all four numbers so a monitoring tool can read them.",
                            "start_hints": [
                                "First extract the times: the pattern r'\\d{2}:\\d{2}' finds HH:MM.",
                                "Next extract all numbers anywhere in the line with r'\\d+'.",
                                "Print both lists. The times should be 6 items; the numbers 4 items.",
                            ],
                            "starter_snippet": "import re\n\nlog = '08:15 start rewrite count=12 in ms=30 end 09:02 saved files=4 ms=55'\n\ntimes = re.findall(...)\nprint(times)",
                            "steps": [
                                "1. Find all HH:MM timestamps with re.findall(r'\\d{2}:\\d{2}', log)",
                                "2. Find all numbers (plain digits) elsewhere with re.findall(r'\\d+', log)",
                                "3. Print the times list and the numbers list",
                                "Expected: six times and four numbers printed",
                            ],
                            "starter_code": "# Build your Log Analyzer\nimport re\n\nlog = '08:15 start rewrite count=12 in ms=30 end 09:02 saved files=4 ms=55'\n\n# 1) Find every timestamp (HH:MM)\n\n\n# 2) Find every number in the log\n\n\n# 3) Print both lists\n",
                            "check": lambda code: (
                                True, "Excellent! You extracted structured data from messy text with regex."
                            ) if ("re" in code and "findall" in code and "\\d" in code and "print(" in code) else (
                                False, "Use re.findall with a \\d pattern for times and another for numbers, then print both lists."
                            ),
                        },
                    },
                    {
                        "title": "Testing your code with assert",
                        "unit": "Professional practice",
                        "topic": "Testing and assertions",
                        "summary": "assert lets you check that your code does what you expect, and it's the building block of every real test suite. Writing tests before or alongside your code catches bugs early and makes you a professional-grade developer.",
                        "example": "def double(n):\n    return n * 2\n\nassert double(4) == 8\nassert type(double(3)) == int\nprint('All tests passed')",
                        "challenge": "Write an assert that checks a function's output.",
                        "why_it_matters": "Hiring managers love testers. Testing is how you make code you can trust, refactor without breaking things, and prove to the world (and interviewers) that your code works.",
                        "key_takeaways": "\u2022 assert condition raises AssertionError if the condition is False\n\u2022 assert func(x) == expected is the simplest test\n\u2022 Multiple asserts catch different expectations\n\u2022 If no AssertionError, all your checks passed",
                        "review_question": "What happens when assert 2 + 2 == 5 runs?",
                        "review_answer": "It raises an AssertionError because the condition is False.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "assert checks your assumptions",
                                "content": "assert condition\n\nIf the condition evaluates to True, nothing happens.\nIf it's False, Python raises:\nAssertionError\n\nThis makes assert perfect for tiny tests:\nassert double(4) == 8   # silent = good\nassert area(3, 4) == 12\n\nA script that finishes without an error = all asserts passed.",
                                "example": "def area(w, h):\n    return w * h\n\nassert area(3, 4) == 12\nassert area(0, 5) == 0\nprint('All tests passed.')",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write an assert that checks is_even(10) returns True. Your code should pass silently and end by printing 'All tests passed'.",
                                "starter_code": "def is_even(n):\n    return n % 2 == 0\n\n# Write your assert below\n",
                                "check": lambda code: "assert" in code and "is_even" in code and "print(" in code,
                                "hint": "Try: assert is_even(10) == True, then print('All tests passed')",
                                "success_msg": "Correct! A passing assert runs silently \u2014 that's a good thing.",
                            },
                            {
                                "type": "debug",
                                "instruction": "The function total() is buggy and the assert catches it. Fix the function so the assert passes and the script prints 'All tests passed'.",
                                "broken_code": "def total(prices):\n    t = 0\n    for p in prices:\n        t - p\n    return t\n\nassert total([10, 15, 5]) == 30\nprint('All tests passed')\n",
                                "goal_hint": "The loop subtracts instead of adding: t - p should be t += p. Look for the '=' that's missing.",
                                "bug_notes": "t - p computes a value and throws it away. To change t you must assign with +=.",
                                "check": lambda code: "+=" in code and "assert" in code,
                                "success_msg": "Fixed! The assert was right \u2014 the bug was in the += logic.",
                                "hint": "Change t - p to t += p.",
                            },
                            {
                                "type": "practice",
                                "instruction": "Add a second assert to also check that total([]) equals 0 (an empty list should sum to zero).",
                                "starter_code": "def total(prices):\n    t = 0\n    for p in prices:\n        t += p\n    return t\n\n# Add the two asserts below\n",
                                "check": lambda code: "assert total([10, 15, 5]) == 30" in code and "assert total([]) == 0" in code,
                                "hint": "Write assert total([10, 15, 5]) == 30 and assert total([]) == 0, then a print.",
                                "success_msg": "Two tests, both passing. This is exactly how pro test suites start.",
                            },
                            {
                                "type": "review",
                                "question": "A script with no errors means all asserts...",
                                "options": ["Passed", "Failed silently", "Were ignored", "Ran twice"],
                                "answer": "Passed",
                            },
                        ],
                        "final_project": {
                            "title": "Subtle Bug Hunt",
                            "description": "A correctly-signed divide function has a tricky edge case. Write asserts that expose it, then fix the function.",
                            "scenario": "A teammate swears divide(a, b) is perfect, but a math edge case proves them wrong. Write asserts for normal cases AND the edge case, then fix the function.",
                            "start_hints": [
                                "Write the obvious asserts first: divide(10, 2) == 5 and divide(9, 3) == 3.",
                                "Now think about 0. What happens on divide(1, 0)? Trying to divide by zero raises an exception.",
                                "The fix: check for b == 0 and return what makes sense (like 0, or 'cannot divide by zero').",
                            ],
                            "starter_snippet": "def divide(a, b):\n    return a / b\n\n# Write your asserts, then fix the function",
                            "steps": [
                                "1. Write asserts for divide(10, 2) and divide(9, 3)",
                                "2. Add an assert that divide(1, 0) returns 0 (or check you handle it)",
                                "3. Fix divide() so dividing by zero returns 0 instead of crashing",
                                "4. Print 'All tests passed' once every assert holds",
                            ],
                            "starter_code": "# Build your Subtle Bug Hunt\ndef divide(a, b):\n    return a / b\n\n# 1) Normal-case asserts\n\n# 2) Edge-case assert (divide by zero)\n\n# 3) Fix divide() to handle b == 0\n# 4) print('All tests passed')\n",
                            "check": lambda code: (
                                True, "Outstanding! You wrote tests, found the edge case, and fixed it \u2014 real professional debugging."
                            ) if ("assert" in code and "divide" in code and ("== 0" in code or "!= 0" in code or "return 0" in code) and "print(" in code) else (
                                False, "Write asserts for normal cases, assert something about divide-by-zero, then make divide() handle b == 0 and print confirmation."
                            ),
                        },
                    },
                    {
                        "title": "Recursion and algorithm thinking",
                        "unit": "Algorithm design",
                        "topic": "Recursion",
                        "summary": "A recursive function is one that calls itself to solve a smaller version of the same problem. It's how pros crack tough problems like directory trees, permutations, and sorting. This is classic interview material and pure Python power.",
                        "example": "def countdown(n):\n    if n <= 0:\n        print('Done')\n        return\n    print(n)\n    countdown(n - 1)\n\ncountdown(3)",
                        "challenge": "Write a recursive function that sums numbers from 1 to n.",
                        "why_it_matters": "Recursion appears in real tools (searching filesystems, parsing trees, AI search) and in most technical interviews. Once the pattern \u2018base case + recurse\u2019 clicks, hard problems get easy.",
                        "key_takeaways": "\u2022 Every recursive function needs a base case (a stop condition)\n\u2022 Each call must move toward the base case\n\u2022 A factorial: fib, sum, and tree problems are classic recursive patterns\n\u2022 No base case = infinite recursion and RecursionError",
                        "review_question": "What stops a recursive function from looping forever?",
                        "review_answer": "A base case \u2014 a condition where the function returns without calling itself.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "The base case and the recursive call",
                                "content": "A recursive function has two parts:\n\n1. A base case that stops the recursion (no self-call).\n2. A recursive call on a smaller input.\n\ndef countdown(n):\n    if n <= 0:      # base case\n        print('Done')\n        return\n    print(n)\n    countdown(n - 1)  # moving smaller",
                                "example": "def sum_to(n):\n    if n <= 1:      # base case\n        return n\n    return n + sum_to(n - 1)   # recursive call\n\nprint(sum_to(5))   # 15",
                            },
                            {
                                "type": "fill",
                                "instruction": "Fill in the blanks to make sum_to(n) work. It should sum 1 + 2 + ... + n.",
                                "template": "def sum_to(n):\n    if n <= ___:    # base case\n        return ___    # sums up to n == 1\n    return n + sum_to(___ - 1)   # recurse smaller\n\nprint(sum_to(5))\n",
                                "expected_output": "15",
                                "goal_hint": "The base case stops at n <= 1 (returning n). The recursive call uses n - 1.",
                                "check": lambda code: "def sum_to" in code and "sum_to(___" not in code and "___" not in code,
                                "success_msg": "Correct! Base case + smaller recursive call = recursion.",
                                "hint": "Blanks: the base case compares n to 1, returns n, and recurses with n - 1.",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write a recursive factorial() function: factorial(n) returns n * factorial(n-1), and factorial(1) is 1. Print factorial(5), which should be 120.",
                                "starter_code": "def factorial(n):\n    # base case\n\n    # recursive call\n    \nprint(factorial(5))\n",
                                "check": lambda code: "factorial(" in code and "if" in code and "return" in code and "factorial(n" in code and "print(factorial(5))" in code,
                                "hint": "if n <= 1: return 1, then return n * factorial(n - 1)",
                                "success_msg": "Beautiful work \u2014 that is textbook recursion in a function.",
                            },
                            {
                                "type": "debug",
                                "instruction": "This recursion never stops and crashes with a RecursionError. Find the missing base case and fix it so reverse('abc') prints 'cba'.",
                                "broken_code": "def reverse(s):\n    return reverse(s[1:]) + s[0]\n\nprint(reverse('abc'))\n",
                                "goal_hint": "There is no base case! When the string is empty it should return '' so the calls stop.",
                                "bug_notes": "reverse() always calls itself no matter what. Add a stop: if the string is empty (or has length 1) return it directly.",
                                "check": lambda code: ("if " in code) and ("len(s)" in code or "not s" in code or "== 1" in code or "<= 1" in code),
                                "success_msg": "Fixed! The missing base case was the whole bug \u2014 and it's the classic recursion mistake.",
                                "hint": "Add: if len(s) < 2: return s before the recursive call.",
                            },
                            {
                                "type": "review",
                                "question": "What error do you get if a recursive function has no base case?",
                                "options": ["RecursionError", "TypeError", "SyntaxError", "NameError"],
                                "answer": "RecursionError",
                            },
                        ],
                        "final_project": {
                            "title": "Directory-size Calculator",
                            "description": "Model a nested folder tree as nested lists and use recursion to total up every file size.",
                            "scenario": "You're writing a cleanup tool. Folders contain files and subfolders. Recursion is the natural way to walk the whole tree and add every size.",
                            "start_hints": [
                                "A folder can be represented like [size_or_file, [subfolder], ...]. Start by summing only the direct sizes to see the structure.",
                                "The real trick: for each item, if it's a list, recursively call total_size on it.",
                                "Add a base case: a plain number (a file) returns itself.",
                            ],
                            "starter_snippet": "def total_size(node):\n    if isinstance(node, int):   # a file\n        return node\n    # folder: sum each child\n    total = 0\n    for child in node:\n        total += total_size(child)\n    return total\n\nfolder = [100, 50, [200, [25, 25]], 10]\nprint(total_size(folder))",
                            "steps": [
                                "1. Fill in the base case for a plain file (an int)",
                                "2. Loop over each child and add its recursive total",
                                "3. Print total_size(folder), which should sum to 410",
                                "Expected: 410",
                            ],
                            "starter_code": "# Build your Directory-size Calculator\ndef total_size(node):\n    if isinstance(node, int):   # a file\n        return node\n    # folder: loop children and recurse\n    total = 0\n    \n\n\nfolder = [100, 50, [200, [25, 25]], 10]\nprint(total_size(folder))\n",
                            "check": lambda code: (
                                True, "Masterful! You used recursion to walk a nested tree \u2014 a genuinely professional skill."
                            ) if ("def total_size" in code and "return" in code and "total_size(" in code and "print(total_size(folder))" in code) else (
                                False, "Keep the base case for ints, loop over children, call total_size(child) for each, and use total += to accumulate."
                            ),
                        },
                    },
                    {
                        "title": "Decorators",
                        "unit": "Functional tools",
                        "topic": "Decorators",
                        "summary": "Decorators are functions that wrap other functions to add behavior \u2014 logging, timing, or access control \u2014 without changing the original code. They use the @name syntax.",
                        "example": "def my_decorator(func):\n    def wrapper():\n        print('Before')\n        func()\n        print('After')\n    return wrapper\n\n@my_decorator\ndef greet():\n    print('Hello')\ngreet()",
                        "challenge": "Write a decorator that prints 'Before' and 'After' around a function.",
                        "why_it_matters": "Decorators are everywhere in Python web frameworks, testing, and logging. Understanding them unlocks readable, reusable cross-cutting behavior.",
                        "key_takeaways": "\u2022 A decorator is a function that takes a function and returns a wrapper\n\u2022 The wrapper calls the original inside\n\u2022 @decorator is shorthand for func = decorator(func)\n\u2022 Use *args, **kwargs to wrap any signature",
                        "review_question": "What does @my_decorator above greet do?",
                        "review_answer": "It replaces greet with my_decorator(greet) \u2014 greet becomes the wrapper.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Functions wrapping functions",
                                "content": "In Python, functions are objects you can pass around.\nA decorator takes a function and returns a new function (the wrapper) that adds behavior.\nThe wrapper calls the original at the right moment and can add code before and after.",
                                "example": "def my_decorator(func):\n    def wrapper():\n        print('Before')\n        result = func()\n        print('After')\n        return result\n    return wrapper\n\ndef greet():\n    print('Hello')\ngreet = my_decorator(greet)\ngreet()  # Before / Hello / After",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write a decorator called my_decorator that wraps a no-arg function, printing 'Before' and 'After' around it. Test it on greet().",
                                "starter_code": "def my_decorator(func):\n    def wrapper():\n        # Before, call, After\n        pass\n    return wrapper\n\ndef greet():\n    print('Hello')\n\n# Decorate manually: greet = my_decorator(greet)\n# Then call greet()\n",
                                "check": lambda code: "def my_decorator" in code and "def wrapper" in code and "return wrapper" in code and "func()" in code,
                                "hint": "Inside wrapper: print('Before'), func(), print('After'). Return wrapper at the end of decorator.",
                                "success_msg": "You built a wrapping function \u2014 the core of every decorator!",
                            },
                            {
                                "type": "concept",
                                "title": "The @ shorthand and *args",
                                "content": "@name is just syntax sugar: @my_decorator\\ndef greet(): ... means greet = my_decorator(greet).\nTo handle any arguments, define wrapper(*args, **kwargs) and call func(*args, **kwargs).",
                                "example": "def my_decorator(func):\n    def wrapper(*args, **kwargs):\n        print('Before')\n        result = func(*args, **kwargs)\n        print('After')\n        return result\n    return wrapper\n\n@my_decorator\ndef add(a, b):\n    return a + b\nprint(add(2, 3))",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use @my_decorator syntax to decorate add(a, b) that returns a+b, handling *args, **kwargs in wrapper. Then print add(2,3).",
                                "starter_code": "def my_decorator(func):\n    def wrapper(*args, **kwargs):\n        print('Before')\n        result = func(*args, **kwargs)\n        print('After')\n        return result\n    return wrapper\n\n@my_decorator\ndef add(a, b):\n    return a + b\n\nprint(add(2, 3))\n",
                                "check": lambda code: "@my_decorator" in code and "def add" in code and "*args" in code and "print(" in code,
                                "hint": "Put @my_decorator on the line directly above def add. Wrapper must use *args, **kwargs.",
                                "success_msg": "@ syntax and *args \u2014 your decorator now works for any function!",
                            },
                            {
                                "type": "review",
                                "question": "What does @my_decorator above greet do?",
                                "options": ["Calls greet immediately", "Replaces greet with my_decorator(greet)", "Deletes greet", "Makes greet twice as fast"],
                                "answer": "Replaces greet with my_decorator(greet)",
                            },
                        ],
                        "final_project": {
                            "title": "Timer Decorator",
                            "description": "Build a decorator that counts calls and reports timing for any function.",
                            "scenario": "Your team wants observability: every important function should report how many times it was called and how long it took. Write a decorator that wraps any function and prints that info.",
                            "start_hints": [
                                "Write the decorator shell: def my_decorator(func): def wrapper(*args, **kwargs): ... return wrapper.",
                                "Inside wrapper increment a nonlocal counter (use wrapper.calls) or an outer variable, then call result = func(*args, **kwargs).",
                                "Print f'Call {n}: result {result}' before returning result, then apply @my_decorator to a test function.",
                            ],
                            "starter_snippet": "def my_decorator(func):\n    count = 0\n    def wrapper(*args, **kwargs):\n        nonlocal count\n        count += 1\n        result = func(*args, **kwargs)\n        print(f'Call {count}: {result}')\n        return result\n    return wrapper\n\n@my_decorator\ndef add(a, b):\n    return a + b\nprint(add(2,3))\nprint(add(10,20))",
                            "steps": [
                                "1. Write my_decorator(func) returning wrapper(*args, **kwargs)",
                                "2. Wrapper tracks count and prints 'Call n: result'",
                                "3. Apply @my_decorator to a function like add(a,b)",
                                "4. Call the decorated function twice and see the counting",
                                "Expected: two calls printed with incrementing count and results",
                            ],
                            "starter_code": "# Build your Timer Decorator\ndef my_decorator(func):\n    count = 0\n    def wrapper(*args, **kwargs):\n        nonlocal count\n        # increment, call, print, return\n        pass\n    return wrapper\n\n@my_decorator\ndef add(a, b):\n    return a + b\n\nprint(add(2,3))\nprint(add(10,20))\n",
                            "check": lambda code: (
                                True, "Excellent! You wrote a stateful decorator that wraps any function."
                            ) if ("def my_decorator" in code and "def wrapper" in code and "@my_decorator" in code and "*args" in code and "print(" in code) else (
                                False, "Define my_decorator with wrapper(*args, **kwargs), use @my_decorator, and print the call count."
                            ),
                        },
                    },
                    {
                        "title": "Generators",
                        "unit": "Pythonic patterns",
                        "topic": "Generators",
                        "summary": "A generator is a function that pauses and resumes with yield. It produces values lazily, one at a time, using almost no memory \u2014 perfect for huge sequences and streams.",
                        "example": "def count_up(n):\n    for i in range(n):\n        yield i\n\nfor value in count_up(3):\n    print(value)  # 0, 1, 2",
                        "challenge": "Write a generator that yields squares of numbers.",
                        "why_it_matters": "Generators power streaming data, large file reads, and infinite sequences. They are a favorite interview topic and a Python superpower for efficiency.",
                        "key_takeaways": "\u2022 yield pauses the function and returns a value; next() resumes it\n\u2022 A generator object is lazy \u2014 it makes values on demand\n\u2022 for loop consumes a generator automatically\n\u2022 yield from delegates to another generator",
                        "review_question": "What keyword makes a function a generator?",
                        "review_answer": "yield \u2014 using yield instead of return makes the function return a generator object.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "yield pauses, not ends",
                                "content": "return ends a function. yield pauses it and hands a value to the caller.\nThe next call (or the next iteration of a for loop) resumes right after the yield.\nThe function's local variables are preserved between yields.",
                                "example": "def count_up(n):\n    i = 0\n    while i < n:\n        yield i\n        i += 1\n\ng = count_up(3)\nprint(next(g))  # 0\nprint(next(g))  # 1\nfor v in count_up(3):\n    print(v)",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write a generator count_up(n) that yields i for i in range(n). Then loop over count_up(3) and print each value.",
                                "starter_code": "def count_up(n):\n    for i in range(n):\n        # yield i\n        pass\n\nfor v in count_up(3):\n    print(v)\n",
                                "check": lambda code: "def count_up" in code and "yield" in code and "for " in code and "print(" in code,
                                "hint": "Inside count_up, loop for i in range(n): then yield i on an indented line.",
                                "success_msg": "Your generator yielded values lazily and the loop consumed them!",
                            },
                            {
                                "type": "concept",
                                "title": "Generator expressions and filtering",
                                "content": "Just like list comprehensions, you can write (expr for item in seq if cond) \u2014 that's a generator expression, using parentheses. It doesn't build a list; it yields one by one.\nYou can also yield many values from a helper with yield from.",
                                "example": "squares = (x*x for x in range(5))\nprint(next(squares))  # 0\nprint(list(squares))  # [1, 4, 9, 16]\n\ndef squares_gen(n):\n    yield from (i*i for i in range(n))",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write a generator squares(n) that yields i*i for i in range(n). Then print list(squares(4)) which should be [0,1,4,9].",
                                "starter_code": "def squares(n):\n    for i in range(n):\n        # yield i*i\n        pass\n\nprint(list(squares(4)))\n",
                                "check": lambda code: "def squares" in code and "yield" in code and "list(squares" in code and "print(" in code,
                                "hint": "Inside squares, for i in range(n): yield i*i.",
                                "success_msg": "Squares generator \u2014 lazy and memory-light!",
                            },
                            {
                                "type": "review",
                                "question": "What keyword makes a function a generator?",
                                "options": ["return", "yield", "generate", "async"],
                                "answer": "yield",
                            },
                        ],
                        "final_project": {
                            "title": "Countdown Generator",
                            "description": "Build a generator that counts down from n to 1 and optionally chains to another generator.",
                            "scenario": "A launch sequence needs a countdown that can be reused and composed. Build a countdown(n) generator that yields n, n-1, ..., 1, then demonstrate it by printing the sequence and composing it with another generator via yield from.",
                            "start_hints": [
                                "Define def countdown(n): while n > 0: yield n; n -= 1. Loop and print to test.",
                                "Add a second generator that greets after: def launch(seq): yield from seq; yield 'Liftoff!'",
                                "Print list(countdown(5)) and list(launch(countdown(3))).",
                            ],
                            "starter_snippet": "def countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nprint(list(countdown(5)))",
                            "steps": [
                                "1. Write countdown(n) that yields n down to 1",
                                "2. Print list(countdown(5)) to verify [5,4,3,2,1]",
                                "3. Write a second generator that yields from countdown and then 'Liftoff!'",
                                "4. Print the composed generator",
                                "Expected: countdown list and liftoff message",
                            ],
                            "starter_code": "# Build your Countdown Generator\ndef countdown(n):\n    # yield down to 1\n    pass\n\nprint(list(countdown(5)))\n\n# Second generator with yield from\n\n",
                            "check": lambda code: (
                                True, "Great! You used yield and yield from to compose lazy sequences."
                            ) if ("def countdown" in code and "yield" in code and "list(countdown" in code and "print(" in code) else (
                                False, "Define countdown with yield, print list(countdown(5)), optionally use yield from for composition."
                            ),
                        },
                    },
                    {
                        "title": "Working with APIs",
                        "unit": "Real-world data",
                        "topic": "Web and APIs",
                        "summary": "APIs send data as JSON strings over the web. You parse them with json.loads() (string) vs json.load() (file), then navigate nested dictionaries and lists exactly like the bundled datasets \u2014 but now the data came from a service.",
                        "example": "import json\napi_response = '{\"users\": [{\"name\": \"Ada\", \"score\": 92}]}'\ndata = json.loads(api_response)\nprint(data['users'][0]['name'])",
                        "challenge": "Parse a JSON API response string and print a nested field.",
                        "why_it_matters": "Almost every modern app talks to an API \u2014 weather, maps, social, payments. Parsing JSON responses is the first step to using live web data.",
                        "key_takeaways": "\u2022 json.loads(s) parses a JSON string; json.load(file) parses a file\n\u2022 API responses are nested: dicts inside lists inside dicts\n\u2022 Access with data['key'][0]['field'] chains lookups\n\u2022 Real APIs need error handling for missing keys \u2014 .get() helps",
                        "review_question": "What does json.loads() do?",
                        "review_answer": "It parses a JSON string into a Python dictionary or list.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "JSON strings from the web",
                                "content": "A file stores JSON on disk; an API sends JSON as a string over the network.\njson.load(file) handles files.\njson.loads(string) handles strings (the s is for string).\nBoth give back the same Python objects: lists and dicts.",
                                "example": "import json\napi_response = '{\"users\": [{\"name\": \"Ada\"}]}'\ndata = json.loads(api_response)\nprint(data['users'][0]['name'])  # Ada\n# File version:\n# with open('data.json') as f: data = json.load(f)",
                            },
                            {
                                "type": "practice",
                                "instruction": "Parse api_response = '{\"status\": \"ok\", \"count\": 3}' with json.loads and print the 'status' field.",
                                "starter_code": "import json\napi_response = '{\"status\": \"ok\", \"count\": 3}'\n\n# Parse and print status\n",
                                "check": lambda code: "json.loads(" in code and "api_response" in code and "print(" in code and "status" in code,
                                "hint": "Use data = json.loads(api_response) then print(data['status']).",
                                "success_msg": "json.loads turned the API string into a dict you could read!",
                            },
                            {
                                "type": "concept",
                                "title": "Navigating nested API data",
                                "content": "API data nests: a dict holds a list of dicts, each with fields.\nChain lookups: data['users'][0]['name'] \u2014 dict \u2192 list \u2192 dict \u2192 field.\nUse .get() or try/except if keys might be missing.\nList comprehensions are perfect to pull one field from every record.",
                                "example": "import json\napi_response = '{\"users\": [{\"name\":\"Ada\",\"score\":92},{\"name\":\"Bob\",\"score\":85}]}'\ndata = json.loads(api_response)\nfor user in data['users']:\n    print(user['name'], user['score'])\n# Comprehension: [u['name'] for u in data['users']]",
                            },
                            {
                                "type": "practice",
                                "instruction": "Parse the users API string with two users, then loop over data['users'] and print each user's name.",
                                "starter_code": "import json\napi_response = '{\"users\": [{\"name\": \"Ada\", \"score\": 92}, {\"name\": \"Bob\", \"score\": 85}]}'\n\ndata = json.loads(api_response)\n\n# Loop and print each name\n",
                                "check": lambda code: "json.loads(" in code and "data['users']" in code and "for " in code and "print(" in code,
                                "hint": "After parsing, for user in data['users']: print(user['name']).",
                                "success_msg": "You walked the nested list and extracted each name!",
                            },
                            {
                                "type": "review",
                                "question": "What does json.loads() do?",
                                "options": ["Parses a JSON string into Python objects", "Saves Python data to a file", "Sorts a list", "Creates a web server"],
                                "answer": "Parses a JSON string into Python objects",
                            },
                        ],
                        "final_project": {
                            "title": "API Data Explorer",
                            "description": "Parse a mock API response, filter active users, and rank them by score.",
                            "scenario": "Your dashboard receives this API string: users with name, score, and active flag. Parse it, keep only active users, sort by score descending, and print a ranked report.",
                            "start_hints": [
                                "Parse with data = json.loads(api_response) and print len(data['users']) to confirm.",
                                "Filter: active = [u for u in data['users'] if u['active']] \u2014 keeps only True.",
                                "Sort active with sorted(..., key=lambda u: u['score'], reverse=True), then loop and print f\\\"{u['name']}: {u['score']}\\\".",
                            ],
                            "starter_snippet": "import json\napi_response = '{\"users\": [{\"name\":\"Ada\",\"score\":92,\"active\":true},{\"name\":\"Bob\",\"score\":85,\"active\":false},{\"name\":\"Carol\",\"score\":98,\"active\":true}]}'\n\ndata = json.loads(api_response)\nprint(len(data['users']))",
                            "steps": [
                                "1. Parse api_response with json.loads",
                                "2. Filter to only active users",
                                "3. Sort active users by score descending",
                                "4. Print each active user's name and score in ranked order",
                                "Expected: Carol: 98 and Ada: 92 (Bob is inactive, filtered out)",
                            ],
                            "starter_code": "# Build your API Data Explorer\nimport json\napi_response = '{\"users\": [{\"name\":\"Ada\",\"score\":92,\"active\":true},{\"name\":\"Bob\",\"score\":85,\"active\":false},{\"name\":\"Carol\",\"score\":98,\"active\":true}]}'\n\ndata = json.loads(api_response)\n\n# Filter active users\n\n# Sort by score descending\n\n# Print ranked active users\n",
                            "check": lambda code: (
                                True, "You parsed, filtered, and ranked live-like API data \u2014 real web skills!"
                            ) if ("json.loads(" in code and "active" in code and "sorted(" in code and "print(" in code) else (
                                False, "Use json.loads, filter with if u['active'], sorted(..., key=..., reverse=True), and print."
                            ),
                        },
                    },
                    {
                        "title": "Type Hints, Context Managers & Async",
                        "unit": "High-level Python",
                        "topic": "Professional Python",
                        "summary": "High-level Python leans on three tools: type hints document what a function expects, context managers (with) handle cleanup, and async lets you wait without blocking. Together they make real apps readable and safe.",
                        "example": "def add(a: int, b: int) -> int:\n    return a + b\n\nwith open('demo.txt', 'w') as f:\n    f.write('hi')\n\nimport asyncio\nasync def hi():\n    await asyncio.sleep(0.1)\n    return 'hi'\nprint(add(2,3))\nprint(asyncio.run(hi()))",
                        "challenge": "Add type hints to a function, use with to handle a file, and run an async function.",
                        "why_it_matters": "Type hints catch bugs early in editors, with guarantees files close even on errors, and async powers web servers and data fetching without freezing your app.",
                        "key_takeaways": "\u2022 def fn(x: int) -> int: documents types (checked by mypy, not enforced at runtime)\n\u2022 with open(...) as f: auto-closes the file\n\u2022 async def + await pauses without blocking; run with asyncio.run()\n\u2022 Use -> to hint return type, : to hint param type",
                        "review_question": "What does '-> int' mean after a function header?",
                        "review_answer": "It is a type hint saying the function should return an int.",
                        "steps": [
                            {
                                "type": "concept",
                                "title": "Type hints are labels (checked by tools)",
                                "content": "Type hints don't change how Python runs, they document:\n  def greet(name: str) -> str:\n      return f'Hi {name}'\n  name: str means name should be text, -> str means returns text.\nTools like mypy and your editor use them to warn before you run. Python itself won't error if you pass a number.",
                                "example": "def add(a: int, b: int) -> int:\n    return a + b\nprint(add(2,3))  # 5\n# add('a','b') would still run but mypy would warn",
                            },
                            {
                                "type": "practice",
                                "instruction": "Add type hints: make add(a: int, b: int) -> int that returns a+b, then print(add(5,3)) and print(add(2,7)).",
                                "starter_code": "# Add type hints to add\ndef add(a, b):\n    return a + b\n\nprint(add(5,3))\n",
                                "check": lambda code: "def add(" in code and "-> int" in code and "a: int" in code and "b: int" in code and "print(" in code,
                                "hint": "Write: def add(a: int, b: int) -> int:  then return a + b",
                                "success_msg": "Type hints added - editors can now warn if you misuse add()!",
                            },
                            {
                                "type": "concept",
                                "title": "Context managers - with guarantees cleanup",
                                "content": "with opens and closes for you:\n  with open('demo.txt','w') as f:\n      f.write('hi')\n# file closed here, even if write crashed\nIt's why you write with open(...) as f: instead of f = open(...). Same idea works for locks, network, and custom classes with __enter__/__exit__.",
                                "example": "with open('demo.txt','w') as f:\n    f.write('hello')\nwith open('demo.txt','r') as f:\n    print(f.read())  # hello",
                            },
                            {
                                "type": "practice",
                                "instruction": "Use with to write 'hello async' to demo.txt then with to read it back and print the content.",
                                "starter_code": "# Write with 'with', then read back\n",
                                "check": lambda code: code.count("with open(") >= 2 and "demo.txt" in code and "write(" in code and "read(" in code and "print(" in code,
                                "hint": "with open('demo.txt','w') as f: f.write('hello async') then with open('demo.txt','r') as f: print(f.read())",
                                "success_msg": "with handled open/close - no manual close needed!",
                            },
                            {
                                "type": "concept",
                                "title": "Async - wait without blocking",
                                "content": "async def makes a function pausable.\nawait pauses that function while other work runs.\n\nimport asyncio\nasync def fetch():\n    await asyncio.sleep(0.1)  # pretend network wait\n    return 'data'\n# run it: asyncio.run(fetch())\nWithout async, sleep would freeze the whole app.",
                                "example": "import asyncio\nasync def hi():\n    await asyncio.sleep(0.05)\n    return 'hi'\nprint(asyncio.run(hi()))  # hi",
                            },
                            {
                                "type": "practice",
                                "instruction": "Write async def greet() that awaits asyncio.sleep(0.1) and returns 'hello async', then print(asyncio.run(greet())).",
                                "starter_code": "import asyncio\n\n# async def greet():\n#   await asyncio.sleep(0.1)\n#   return 'hello async'\n\n# print(asyncio.run(greet()))\n",
                                "check": lambda code: "async def greet" in code and "await asyncio.sleep" in code and "asyncio.run(" in code and "print(" in code,
                                "hint": "async def greet(): await asyncio.sleep(0.1); return 'hello async' then print(asyncio.run(greet()))",
                                "success_msg": "Async paused and resumed - you wrote your first non-blocking function!",
                            },
                            {
                                "type": "debug",
                                "instruction": "This async code forgot await and would not pause. Fix it so it truly waits 0.1s before returning.",
                                "broken_code": "import asyncio\nasync def greet():\n    asyncio.sleep(0.1)\n    return 'hello'\nprint(asyncio.run(greet()))\n",
                                "goal_hint": "Add await before asyncio.sleep(0.1) so the pause actually happens.",
                                "bug_notes": "Without await the coroutine is created but never awaited - the sleep never runs.",
                                "check": lambda code: "await asyncio.sleep" in code and "async def greet" in code,
                                "success_msg": "await added - the sleep now actually pauses!",
                                "hint": "Change asyncio.sleep(0.1) to await asyncio.sleep(0.1)",
                            },
                            {
                                "type": "review",
                                "question": "What does '-> int' mean after a function header?",
                                "options": ["Return type hint: should return int", "Makes it run faster", "Creates an int variable", "No meaning"],
                                "answer": "Return type hint: should return int",
                            },
                        ],
                        "final_project": {
                            "title": "Async File Typer",
                            "description": "Combine all three: a typed function that writes with 'with' inside an async workflow.",
                            "scenario": "A log tool must write a typed message to a file safely, then async-wait as if flushing to a server, then read it back - all with proper hints and with blocks.",
                            "start_hints": [
                                "Write def save(msg: str) -> None: with open('out.txt','w') as f: f.write(msg) - note msg: str and -> None.",
                                "Write async def process(msg: str) -> str: save(msg); await asyncio.sleep(0.05); with open('out.txt','r') as f: return f.read()",
                                "Run print(asyncio.run(process('hello async'))) - you should see hello async via file round-trip.",
                            ],
                            "starter_snippet": "import asyncio\n\ndef save(msg: str) -> None:\n    with open('out.txt','w') as f:\n        f.write(msg)\n",
                            "steps": [
                                "1. Define save(msg: str) -> None using with open('out.txt','w') as f: f.write(msg)",
                                "2. Define async def process(msg: str) -> str that calls save(msg), awaits asyncio.sleep(0.05), then with open('out.txt','r') as f: return f.read()",
                                "3. Print asyncio.run(process('hello async')) - expect 'hello async'",
                                "Expected: hello async printed after file write/read via async",
                            ],
                            "starter_code": "# Build your Async File Typer\nimport asyncio\n\ndef save(msg: str) -> None:\n    # with open('out.txt','w') as f: f.write(msg)\n    pass\n\nasync def process(msg: str) -> str:\n    # save(msg); await sleep; with read and return\n    pass\n\n# print(asyncio.run(process('hello async')))\n",
                            "check": lambda code: (
                                True, "High-level done! Type hints documented, with handled files, async awaited cleanly."
                            ) if ("def save(" in code and "-> None" in code and "with open(" in code and "async def process" in code and "await asyncio.sleep" in code and "asyncio.run(" in code) else (
                                False, "Need save(msg: str) -> None with with open, async process(msg: str) -> str with await and asyncio.run."
                            ),
                        },
                    },
                ],
            }

    # -------------------------------------------------------------
    # Learning-intensive expansion: every lesson now has multiple
    # guided steps (concept -> practice -> debug/fill -> integration)
    # -------------------------------------------------------------
    # Two extra steps are inserted before the final review of each
    # lesson so the path is: Concept, Practice, Concept, Practice,
    # Debug/Fix, Integration Practice, Review (+ Final Project).
    # This makes the curriculum more intensive without touching the
    # original 5-step content.
    def _intensive_debug_for(title):
        low = (title or "").lower()
        if "built-in" in low:
            return {
                "type": "debug",
                "instruction": "This code tries to use len() but has a typo. Fix it so it prints the length of name.",
                "broken_code": "name = 'Ada'\nprint(lenght(name))\n",
                "goal_hint": "The function is len(), not lenght(). Fix the spelling and keep the print.",
                "bug_notes": "NameError: name 'lenght' is not defined. One letter breaks the call.",
                "check": lambda code: "len(" in code and "lenght" not in code and "print(" in code,
                "success_msg": "Fixed! len() now counts correctly and the name prints.",
                "hint": "Change lenght to len.",
            }
        if "keyword" in low and "python" in low:
            return {
                "type": "debug",
                "instruction": "Fix the missing colon so this for loop runs and prints each item.",
                "broken_code": "for item in ['one', 'two', 'three']\n    print(item)\n",
                "goal_hint": "A for line must end with a colon.",
                "bug_notes": "SyntaxError: missing ':' after the for header. for...: is required.",
                "check": lambda code: "for " in code and "print(" in code and code.count(":") >= 1,
                "success_msg": "Fixed! The for loop now has its colon and iterates.",
                "hint": "Add ':' at the end of the for line.",
            }
        if "string" in low and "method" in low:
            return {
                "type": "debug",
                "instruction": "This string code tries to make uppercase but forgets (). Fix it.",
                "broken_code": "word = 'python'\nprint(word.upper)\n",
                "goal_hint": "Methods need (): word.upper() returns a new string, word.upper without () does not.",
                "bug_notes": "Printing the method itself, not calling it, gives <built-in method>.",
                "check": lambda code: ".upper(" in code and "print(" in code,
                "success_msg": "Called! .upper() now returns PYTHON.",
                "hint": "Add () after .upper",
            }
        if "variable" in low:
            return {
                "type": "debug",
                "instruction": "This math code forgets to store the result. Fix it so total is 10 then printed.",
                "broken_code": "price = 10\ncount = 3\nprice * count\nprint(total)\n",
                "goal_hint": "Create total = price * count before printing. Without assignment, total is undefined.",
                "bug_notes": "NameError: name 'total' is not defined because it was never assigned.",
                "check": lambda code: "total" in code and "=" in code and "print(" in code and "*" in code,
                "success_msg": "Now total holds the product and prints.",
                "hint": "Use total = price * count",
            }
        if "condition" in low:
            return {
                "type": "debug",
                "instruction": "Fix the equality check so adults are detected. Single = is assignment, not comparison.",
                "broken_code": "age = 20\nif age = 18:\n    print('Adult')\n",
                "goal_hint": "Use == for comparison, = for assignment. if age == 18: or >= 18.",
                "bug_notes": "SyntaxError: invalid syntax. if needs a comparison, not an assignment.",
                "check": lambda code: "if " in code and "==" in code and "print(" in code,
                "success_msg": "Comparison fixed! == checks equality.",
                "hint": "Change = to == or use >=",
            }
        if "reading" in low or "fixing" in low:
            return {
                "type": "fill",
                "instruction": "Complete the blanks so the script prints the fixed greeting correctly.",
                "template": "greeting = ___\nprint(___)\n",
                "expected_output": "Hello",
                "goal_hint": "Fill greeting with 'Hello' and print that same variable.",
                "check": lambda code: "greeting" in code and "'Hello'" in code and "print(" in code and "___" not in code,
                "success_msg": "You filled the variable and printed it consistently!",
                "hint": "Use greeting = 'Hello' then print(greeting)",
            }
        if "input" in low or "conversion" in low:
            return {
                "type": "debug",
                "instruction": "This conversion forgets int(). Fix it so the math works and prints 50.",
                "broken_code": "value = '42'\nprint(value + 8)\n",
                "goal_hint": "value is text. Convert: int(value) + 8, then print.",
                "bug_notes": "TypeError: can only concatenate str not int. Text needs int() first.",
                "check": lambda code: "int(" in code and "value" in code and "print(" in code and "+ 8" in code,
                "success_msg": "Converted! int(value) made it a real number.",
                "hint": "Use int(value) before adding.",
            }
        if low.strip() == "while loops" or low == "while loops":
            return {
                "type": "debug",
                "instruction": "This while loop never updates n and would run forever. Fix it.",
                "broken_code": "n = 3\nwhile n > 0:\n    print(n)\n",
                "goal_hint": "Add n = n - 1 (or n -= 1) inside the indented block so n moves toward 0.",
                "bug_notes": "Infinite loop: condition never becomes False because n never changes.",
                "check": lambda code: "while" in code and "print(" in code and ("n - 1" in code or "n -= 1" in code or "n =" in code),
                "success_msg": "Loop now decrements and terminates!",
                "hint": "Inside while: n = n - 1",
            }
        if "boolean" in low:
            return {
                "type": "fill",
                "instruction": "Fill the blanks to print False, True, False for a=False and b=True logic.",
                "template": "a = True\nb = False\nprint(a ___ b)\nprint(a ___ b)\nprint(not ___)\n",
                "expected_output": "False\nTrue\nFalse",
                "goal_hint": "First is and, second is or, third is a.",
                "check": lambda code: " and " in code and " or " in code and "not " in code and code.count("print(") >= 3,
                "success_msg": "and/or/not wired correctly!",
                "hint": "Use print(a and b), print(a or b), print(not a)",
            }
        if "lists and ranges" in low:
            return {
                "type": "debug",
                "instruction": "Fix the off-by-one so the second item prints. Lists start at 0.",
                "broken_code": "items = ['first','second','third']\nprint(items[2])\n",
                "goal_hint": "The second item is index 1, not 2.",
                "bug_notes": "Off-by-one: index 2 is the third item.",
                "check": lambda code: "print(" in code and ("[1]" in code or "[1 " in code),
                "success_msg": "Index 1 correctly gives second item!",
                "hint": "Use items[1]",
            }
        if "functions and returns" in low or low == "functions and returns":
            return {
                "type": "debug",
                "instruction": "This function never returns. Fix it so double(5) gives 10.",
                "broken_code": "def double(n):\n    n * 2\nprint(double(5))\n",
                "goal_hint": "Add return: return n * 2 so the caller gets the value.",
                "bug_notes": "Without return the function gives None.",
                "check": lambda code: "def " in code and "return" in code and "* 2" in code,
                "success_msg": "return sends the doubled value back!",
                "hint": "Inside double: return n * 2",
            }
        if low == "dictionaries" or low == "dictionaries ":
            return {
                "type": "debug",
                "instruction": "Fix the key access so the pet name prints. Hint: quotes matter.",
                "broken_code": "pet = {'name':'Max'}\nprint(pet[name])\n",
                "goal_hint": "Keys are strings: pet['name'], not pet[name] which looks for a variable called name.",
                "bug_notes": "NameError: name 'name' is not defined. Keys need quotes.",
                "check": lambda code: "pet['name']" in code or 'pet["name"]' in code,
                "success_msg": "pet['name'] now looks up correctly!",
                "hint": "Use pet['name']",
            }
        if "dictionaries" in low and "methods" not in low:
            return {
                "type": "debug",
                "instruction": "Fix the key access so the pet name prints. Hint: quotes matter.",
                "broken_code": "pet = {'name':'Max'}\nprint(pet[name])\n",
                "goal_hint": "Keys are strings: pet['name'], not pet[name] which looks for a variable called name.",
                "bug_notes": "NameError: name 'name' is not defined. Keys need quotes.",
                "check": lambda code: "pet['name']" in code or 'pet["name"]' in code,
                "success_msg": "pet['name'] now looks up correctly!",
                "hint": "Use pet['name']",
            }
        if "sets and tuples" in low:
            return {
                "type": "debug",
                "instruction": "This set code tries indexing, which sets cannot do. Fix it with a membership check.",
                "broken_code": "colors = {'red','green','red'}\nprint(colors[0])\n",
                "goal_hint": "Use 'in': print('green' in colors) instead of colors[0].",
                "bug_notes": "TypeError: 'set' object is not subscriptable. Sets use 'in', not [index].",
                "check": lambda code: " in " in code and "print(" in code and "colors" in code,
                "success_msg": "'in' checks membership without indexing!",
                "hint": "Try print('green' in colors)",
            }
        if "nested loops" in low:
            return {
                "type": "debug",
                "instruction": "Fix the indentation so the inner loop is inside the outer loop.",
                "broken_code": "grid = [[1,2],[3,4]]\nfor row in grid:\nfor cell in row:\n    print(cell)\n",
                "goal_hint": "Indent the inner for:     for cell in row: should be indented under for row.",
                "bug_notes": "IndentationError logic: inner loop must be inside outer loop block.",
                "check": lambda code: code.count("for ") >= 2 and "print(" in code,
                "success_msg": "Nested loops now walk row then cell!",
                "hint": "Indent inner for by 4 spaces",
            }
        if "f-string" in low or "formatting" in low:
            return {
                "type": "fill",
                "instruction": "Fill the blanks to complete the f-string for item and price.",
                "template": "item = 'phone'\nprice = 599\nprint(f'{___}: ${___}')\n",
                "expected_output": "phone: $599",
                "goal_hint": "Blanks are {item} and {price}.",
                "check": lambda code: "{item}" in code and "{price}" in code,
                "success_msg": "F-string now embeds both variables!",
                "hint": "Use {item} and {price}",
            }
        if "slicing" in low or "indexing" in low:
            return {
                "type": "debug",
                "instruction": "Fix the slice so first three letters print. Right syntax is word[0:3] or word[:3].",
                "broken_code": "word = 'python'\nprint(word[0,3])\n",
                "goal_hint": "Use colon, not comma: word[0:3].",
                "bug_notes": "TypeError: string indices must be integers, not tuple. Comma creates a tuple.",
                "check": lambda code: "[0:3]" in code or "[:3]" in code,
                "success_msg": "Slice with colon copies the span!",
                "hint": "Use word[0:3]",
            }
        if "dictionary methods" in low:
            return {
                "type": "debug",
                "instruction": "This tries dict[missing] which crashes. Fix with .get() and a default.",
                "broken_code": "info = {'name':'Ada'}\nprint(info['email'])\n",
                "goal_hint": "Use info.get('email', 'unknown') so missing keys do not crash.",
                "bug_notes": "KeyError: 'email'. .get() returns default instead.",
                "check": lambda code: ".get(" in code and "email" in code,
                "success_msg": ".get() safely handles missing keys!",
                "hint": "Use info.get('email', 'unknown')",
            }
        if "enumerate" in low and "zip" in low:
            return {
                "type": "debug",
                "instruction": "Fix manual counting by using enumerate instead.",
                "broken_code": "fruits = ['apple','banana']\ni = 0\nfor f in fruits:\n    print(i, f)\n",
                "goal_hint": "The code forgets i += 1. Better: for i, f in enumerate(fruits): print(i, f)",
                "bug_notes": "Bug prints 0 every time because i never increments. enumerate fixes it.",
                "check": lambda code: "enumerate(" in code and "for " in code,
                "success_msg": "enumerate numbers loops cleanly!",
                "hint": "Use enumerate(fruits)",
            }
        if "enumerate" in low or "zip" in low:
            return {
                "type": "debug",
                "instruction": "Fix manual counting by using enumerate instead.",
                "broken_code": "fruits = ['apple','banana']\ni = 0\nfor f in fruits:\n    print(i, f)\n",
                "goal_hint": "The code forgets i += 1. Better: for i, f in enumerate(fruits): print(i, f)",
                "bug_notes": "Bug prints 0 every time because i never increments. enumerate fixes it.",
                "check": lambda code: "enumerate(" in code and "for " in code,
                "success_msg": "enumerate numbers loops cleanly!",
                "hint": "Use enumerate(fruits)",
            }
        if "standard library" in low:
            return {
                "type": "debug",
                "instruction": "Fix the import so math.sqrt works.",
                "broken_code": "print(math.sqrt(16))\n",
                "goal_hint": "Add import math at top.",
                "bug_notes": "NameError: name 'math' is not defined without import.",
                "check": lambda code: "import math" in code and "sqrt(" in code,
                "success_msg": "math imported, sqrt works!",
                "hint": "Add import math",
            }
        if low == "classes and objects":
            return {
                "type": "debug",
                "instruction": "Fix the missing self so the cat stores its name.",
                "broken_code": "class Cat:\n    def __init__(self, name):\n        name = name\n",
                "goal_hint": "Use self.name = name to store per-object data.",
                "bug_notes": "Without self, name is just a local variable lost after __init__.",
                "check": lambda code: "self.name" in code and "class " in code,
                "success_msg": "self.name now keeps the name!",
                "hint": "Use self.name = name",
            }
        if "classes" in low:
            return {
                "type": "debug",
                "instruction": "Fix the missing self so the cat stores its name.",
                "broken_code": "class Cat:\n    def __init__(self, name):\n        name = name\n",
                "goal_hint": "Use self.name = name to store per-object data.",
                "bug_notes": "Without self, name is just a local variable lost after __init__.",
                "check": lambda code: "self.name" in code and "class " in code,
                "success_msg": "self.name now keeps the name!",
                "hint": "Use self.name = name",
            }
        if "file handling" in low:
            return {
                "type": "debug",
                "instruction": "Fix the mode so reading works after writing. Hint: close then open for read.",
                "broken_code": "with open('myname.txt','w') as f:\n    f.write('Ada')\nprint(f.read())\n",
                "goal_hint": "Cannot read from a file opened in w mode. Re-open with open(..., \"r\").",
                "bug_notes": "io.UnsupportedOperation: not readable. w is write-only.",
                "check": lambda code: "open(" in code and "'r'" in code and ".read(" in code,
                "success_msg": "Re-opened for reading!",
                "hint": "Use open('myname.txt','r')",
            }
        if "exception" in low:
            return {
                "type": "fill",
                "instruction": "Fill the except line to catch ValueError and print a friendly message.",
                "template": "try:\n    n = int('abc')\nexcept ___:\n    print('not a number')\n",
                "expected_output": "not a number",
                "goal_hint": "except ValueError:",
                "check": lambda code: "except ValueError" in code and "print(" in code,
                "success_msg": "ValueError caught gracefully!",
                "hint": "Use except ValueError:",
            }
        if "json files" in low:
            return {
                "type": "debug",
                "instruction": "Fix the JSON save so it writes to the file handle, not just to a string.",
                "broken_code": "import json\nperson={'name':'Ada'}\njson.dump(person)\n",
                "goal_hint": "json.dump needs the file: with open(...) as f: json.dump(person, f)",
                "bug_notes": "TypeError: dump() missing 1 required argument: fp.",
                "check": lambda code: "json.dump(" in code and "open(" in code,
                "success_msg": "json.dump now writes to the file!",
                "hint": "Use json.dump(person, f) inside with open",
            }
        if "json" in low:
            return {
                "type": "debug",
                "instruction": "Fix the JSON save so it writes to the file handle, not just to a string.",
                "broken_code": "import json\nperson={'name':'Ada'}\njson.dump(person)\n",
                "goal_hint": "json.dump needs the file: with open(...) as f: json.dump(person, f)",
                "bug_notes": "TypeError: dump() missing 1 required argument: fp.",
                "check": lambda code: "json.dump(" in code and "open(" in code,
                "success_msg": "json.dump now writes to the file!",
                "hint": "Use json.dump(person, f) inside with open",
            }
        if "comprehension" in low:
            return {
                "type": "fill",
                "instruction": "Fill the comprehension to square numbers 0-4.",
                "template": "squares = [___ for n in ___(5)]\nprint(squares)\n",
                "expected_output": "[0, 1, 4, 9, 16]",
                "goal_hint": "n * n and range",
                "check": lambda code: "for " in code and "*" in code and "range(" in code,
                "success_msg": "Comprehension builds [0,1,4,9,16]!",
                "hint": "Use [n * n for n in range(5)]",
            }
        if low == "guis with tkinter":
            return {
                "type": "debug",
                "instruction": "Fix the missing pack so the label appears.",
                "broken_code": "import tkinter as tk\nroot=tk.Tk()\nlabel=tk.Label(root,text='Hi')\nroot.mainloop()\n",
                "goal_hint": "Every widget needs .pack() to be placed.",
                "bug_notes": "Window stays empty without pack/grid.",
                "check": lambda code: ".pack(" in code and "Label" in code,
                "success_msg": ".pack() places the widget!",
                "hint": "Add label.pack()",
            }
        if low == "buttons and events":
            return {
                "type": "debug",
                "instruction": "Fix the command so the function has no parentheses.",
                "broken_code": "import tkinter as tk\ndef go(): print('Hi')\nroot=tk.Tk()\nbtn=tk.Button(root,text='Go',command=go())\nbtn.pack()\nroot.mainloop()\n",
                "goal_hint": "Use command=go, not go(). Parentheses call it immediately.",
                "bug_notes": "Button runs once at creation if you call go(), and command becomes None.",
                "check": lambda code: "command=go" in code and "command=go()" not in code,
                "success_msg": "command= now references the function!",
                "hint": "Use command=go",
            }
        if "entry widgets" in low:
            return {
                "type": "debug",
                "instruction": "Fix the conversion so math works on Entry text.",
                "broken_code": "import tkinter as tk\nentry=tk.Entry(root)\nvalue=entry.get()\nprint(value*2)\n",
                "goal_hint": "get() returns text. Use int(entry.get()) before math.",
                "bug_notes": "'2'*2 would give '22' as text, not 4 as number.",
                "check": lambda code: "int(" in code and ".get(" in code,
                "success_msg": "int() converts Entry text to number!",
                "hint": "Use int(entry.get())",
            }
        if "entry" in low:
            return {
                "type": "debug",
                "instruction": "Fix the conversion so math works on Entry text.",
                "broken_code": "import tkinter as tk\nentry=tk.Entry(root)\nvalue=entry.get()\nprint(value*2)\n",
                "goal_hint": "get() returns text. Use int(entry.get()) before math.",
                "bug_notes": "'2'*2 would give '22' as text, not 4 as number.",
                "check": lambda code: "int(" in code and ".get(" in code,
                "success_msg": "int() converts Entry text to number!",
                "hint": "Use int(entry.get())",
            }
        if "loading real data" in low:
            return {
                "type": "debug",
                "instruction": "Fix the file name so us_states.json loads.",
                "broken_code": "import json\nwith open('states.json') as f:\n    data=json.load(f)\n",
                "goal_hint": "File is us_states.json, not states.json.",
                "bug_notes": "FileNotFoundError with wrong name.",
                "check": lambda code: "us_states.json" in code and "json.load(" in code,
                "success_msg": "Correct file loads 50 states!",
                "hint": "Use open('us_states.json')",
            }
        if "filtering and ranking" in low:
            return {
                "type": "debug",
                "instruction": "Fix the key so sorting uses atomic_mass.",
                "broken_code": "import json\nwith open('elements.json') as f:\n    data=json.load(f)\nranked=sorted(data, key=lambda e: e['mass'])\n",
                "goal_hint": "Field is 'atomic_mass', not 'mass'.",
                "bug_notes": "KeyError: 'mass'. Exact field name matters.",
                "check": lambda code: "'atomic_mass'" in code and "sorted(" in code,
                "success_msg": "sorted by 'atomic_mass' now!",
                "hint": "Use e['atomic_mass']",
            }
        if "summarizing" in low:
            return {
                "type": "debug",
                "instruction": "Fix max to use a key so the whole record returns.",
                "broken_code": "import json\nwith open('planets.json') as f:\n    data=json.load(f)\nbig=max(data)\n",
                "goal_hint": "Use max(data, key=lambda p: p[\"diameter_km\"])",
                "bug_notes": "Without key, max tries to compare dicts directly and errors.",
                "check": lambda code: "max(" in code and "key=" in code and "diameter" in code,
                "success_msg": "max with key returns the biggest planet!",
                "hint": "Add key=lambda p: p[\"diameter_km\"]",
            }
        if "regular expression" in low:
            return {
                "type": "debug",
                "instruction": "Fix the pattern so \\d is not eaten. Need raw string.",
                "broken_code": "import re\ntext='a1 b22'\nprint(re.findall('\\d+', text))\n",
                "goal_hint": "Use r'\\d+' not '\\d+'.",
                "bug_notes": "Without r, Python sees \\d as escape, not regex digit.",
                "check": lambda code: "r'\\d+" in code or 'r"\\d+' in code,
                "success_msg": "Raw string preserves \\d!",
                "hint": "Use r'\\d+'",
            }
        if "regular" in low:
            return {
                "type": "debug",
                "instruction": "Fix the pattern so \\d is not eaten. Need raw string.",
                "broken_code": "import re\ntext='a1 b22'\nprint(re.findall('\\d+', text))\n",
                "goal_hint": "Use r'\\d+' not '\\d+'.",
                "bug_notes": "Without r, Python sees \\d as escape, not regex digit.",
                "check": lambda code: "r'\\d+" in code or 'r"\\d+' in code,
                "success_msg": "Raw string preserves \\d!",
                "hint": "Use r'\\d+'",
            }
        if "testing" in low:
            return {
                "type": "debug",
                "instruction": "Fix the operator so the cart totals correctly.",
                "broken_code": "def total(prices):\n    t=0\n    for p in prices:\n        t - p\n    return t\nassert total([10,15,5])==30\n",
                "goal_hint": "t - p computes but discards. Use t += p.",
                "bug_notes": "Without +=, t never changes.",
                "check": lambda code: "+= p" in code and "assert" in code,
                "success_msg": "+= now accumulates!",
                "hint": "Use t += p",
            }
        if "recursion" in low:
            return {
                "type": "debug",
                "instruction": "Add the missing base case so recursion stops.",
                "broken_code": "def countdown(n):\n    print(n)\n    countdown(n-1)\ncountdown(3)\n",
                "goal_hint": "Stop when n <= 0: if n <= 0: return",
                "bug_notes": "RecursionError: infinite calls without base case.",
                "check": lambda code: "if " in code and "return" in code and "countdown" in code,
                "success_msg": "Base case stops recursion!",
                "hint": "Add if n <= 0: return",
            }
        if "decorator" in low:
            return {
                "type": "debug",
                "instruction": "Fix the decorator to return the wrapper.",
                "broken_code": "def my_decorator(func):\n    def wrapper():\n        print('Before')\n        func()\n",
                "goal_hint": "Last line must be return wrapper.",
                "bug_notes": "Without return, decorator gives None.",
                "check": lambda code: "return wrapper" in code and "def wrapper" in code,
                "success_msg": "Decorator now returns wrapper!",
                "hint": "Add return wrapper",
            }
        if "generator" in low:
            return {
                "type": "debug",
                "instruction": "Change return to yield so it becomes a generator.",
                "broken_code": "def count_up(n):\n    for i in range(n):\n        return i\n",
                "goal_hint": "Use yield i not return i.",
                "bug_notes": "return ends function; yield pauses and yields lazily.",
                "check": lambda code: "yield" in code and "def count_up" in code,
                "success_msg": "yield makes it a generator!",
                "hint": "Use yield i",
            }
        if "working with apis" in low or low == "working with apis":
            return {
                "type": "debug",
                "instruction": "Fix the parse: API gives a string, need json.loads, not json.load.",
                "broken_code": "import json\napi_response='{\"name\": \"Ada\"}'\ndata=json.load(api_response)\n",
                "goal_hint": "Use json.loads(api_response) for strings.",
                "bug_notes": "json.load expects a file, json.loads expects a string.",
                "check": lambda code: "json.loads(" in code,
                "success_msg": "json.loads parses the string!",
                "hint": "Use json.loads(api_response)",
            }
        if "api" in low:
            return {
                "type": "debug",
                "instruction": "Fix the parse: API gives a string, need json.loads, not json.load.",
                "broken_code": "import json\napi_response='{\"name\": \"Ada\"}'\ndata=json.load(api_response)\n",
                "goal_hint": "Use json.loads(api_response) for strings.",
                "bug_notes": "json.load expects a file, json.loads expects a string.",
                "check": lambda code: "json.loads(" in code,
                "success_msg": "json.loads parses the string!",
                "hint": "Use json.loads(api_response)",
            }
        return {
            "type": "debug",
            "instruction": "Fix the small bug so the code runs and prints.",
            "broken_code": "print('hi'\n",
            "goal_hint": "Missing closing parenthesis.",
            "bug_notes": "SyntaxError: unmatched parenthesis.",
            "check": lambda code: "print(" in code and code.count("(") == code.count(")"),
            "success_msg": "Parens matched, it runs!",
            "hint": "Close with )",
        }

    def _integration_for(title):
        low = (title or "").lower()
        if "built-in" in low:
            return {
                "type": "practice",
                "instruction": "Integration: create a word, then print the word, its length with len(), and its type with type(), each on a new line.",
                "starter_code": "word = 'Python'\n\n# Print word, len, type\n",
                "check": lambda code: code.count("print(") >= 3 and "len(" in code and "type(" in code,
                "success_msg": "Full report with all three built-ins!",
                "hint": "Three prints: print(word), print(len(word)), print(type(word))",
            }
        if "keyword" in low:
            return {
                "type": "practice",
                "instruction": "Integration: use one for loop over range(5) to print each number and its double on one line.",
                "starter_code": "# Loop 0-4 and print n and n*2\n",
                "check": lambda code: "for " in code and "range(" in code and "print(" in code and "*" in code,
                "success_msg": "Looped and combined values!",
                "hint": "for n in range(5): print(n, n*2)",
            }
        if "string" in low and "method" in low:
            return {
                "type": "practice",
                "instruction": "Integration: take sentence = 'hello world', then print uppercase, then print with world->Python via replace, each on its own line.",
                "starter_code": "sentence = 'hello world'\n\n# upper then replace\n",
                "check": lambda code: ".upper(" in code and ".replace(" in code and code.count("print(") >= 2,
                "success_msg": "Chained transforms work!",
                "hint": "print(sentence.upper()) and print(sentence.replace('world','Python'))",
            }
        if "variable" in low:
            return {
                "type": "practice",
                "instruction": "Integration: create a=8, b=6, compute s=a+b, p=a*b, avg=(a+b)/2, print all three.",
                "starter_code": "a = 8\nb = 6\n\n# s, p, avg\n",
                "check": lambda code: "print(" in code and "+" in code and "*" in code and "/" in code,
                "success_msg": "Math with variables done!",
                "hint": "s = a+b; p = a*b; avg = (a+b)/2; print each",
            }
        if "condition" in low:
            return {
                "type": "practice",
                "instruction": "Integration: read score=85, then if/elif/else to print A/B/C/Needs work as in the project.",
                "starter_code": "score = 85\n\n# if score>=90: etc\n",
                "check": lambda code: "if " in code and "elif" in code and "else" in code and "print(" in code,
                "success_msg": "Full decision chain works!",
                "hint": "Use >=90, >=80, >=70, else",
            }
        if "reading" in low or "fixing" in low:
            return {
                "type": "practice",
                "instruction": "Integration: fix and run both a typo and an indent bug in one script.",
                "starter_code": "greeting = 'Hello'\nname = 'Ada'\nfor ch in greeting:\nprint(ch)\n",
                "check": lambda code: "greeting" in code and "for " in code and "print(" in code,
                "success_msg": "Debugged spelling and indentation together!",
                "hint": "Indent print(ch) under for",
            }
        if "input" in low:
            return {
                "type": "practice",
                "instruction": "Integration: simulate input value='19.99', then float it, add 5, print, then str a number and print 'Score: '+str(num).",
                "starter_code": "value = '19.99'\nnum = 7\n\n# float(value)+5 and str(num)\n",
                "check": lambda code: "float(" in code and "str(" in code and code.count("print(") >= 2,
                "success_msg": "Converted both ways!",
                "hint": "float(value) and str(num)",
            }
        if "while" in low:
            return {
                "type": "practice",
                "instruction": "Integration: while countdown from 5 to 1, printing each, then print 'Go!' after the loop.",
                "starter_code": "n = 5\n# while n>0\n",
                "check": lambda code: "while" in code and "print(" in code and ("n - 1" in code or "n -= 1" in code or "n =" in code),
                "success_msg": "Countdown while with post-loop message!",
                "hint": "while n>0: print(n); n-=1 then print('Go!')",
            }
        if "boolean" in low:
            return {
                "type": "practice",
                "instruction": "Integration: with age=19, has_ticket=False, is_vip=True, compute can_enter = (age>=18 and has_ticket) or is_vip and print it.",
                "starter_code": "age=19\nhas_ticket=False\nis_vip=True\n# can_enter\n",
                "check": lambda code: "and" in code and "or" in code and ">=" in code and "print(" in code,
                "success_msg": "Boolean mix works!",
                "hint": "can_enter = (age>=18 and has_ticket) or is_vip",
            }
        if "lists and ranges" in low:
            return {
                "type": "practice",
                "instruction": "Integration: build nums=[1,2,3], then for n in nums: print double each (extra: also show range version).",
                "starter_code": "nums = [1,2,3]\n# loop and print n*2\n",
                "check": lambda code: "for " in code and "print(" in code and "*" in code,
                "success_msg": "List + loop doubles each!",
                "hint": "for n in nums: print(n*2)",
            }
        if "functions and returns" in low:
            return {
                "type": "practice",
                "instruction": "Integration: define greet(name) that returns f'Hi {name}' and define add(a,b) returning sum, then print both calls.",
                "starter_code": "def greet(name):\n    pass\n\n# add function\n",
                "check": lambda code: code.count("def ") >=2 and "return" in code and "print(" in code,
                "success_msg": "Two functions defined and called!",
                "hint": "def greet with return, def add with return a+b",
            }
        if low == "dictionaries":
            return {
                "type": "practice",
                "instruction": "Integration: make student={'name':'Ada','score':92}, print name, add grade='A', print whole dict.",
                "starter_code": "student = {'name':'Ada','score':92}\n# print and add key\n",
                "check": lambda code: "{" in code and "['name']" in code and "=" in code and "print(" in code,
                "success_msg": "Dict built, accessed, expanded!",
                "hint": "print(student['name']); student['grade']='A'",
            }
        if "dictionaries" in low and "methods" not in low:
            return {
                "type": "practice",
                "instruction": "Integration: make student={'name':'Ada','score':92}, print name, add grade='A', print whole dict.",
                "starter_code": "student = {'name':'Ada','score':92}\n# print and add key\n",
                "check": lambda code: "{" in code and "['name']" in code and "=" in code and "print(" in code,
                "success_msg": "Dict built, accessed, expanded!",
                "hint": "print(student['name']); student['grade']='A'",
            }
        if "sets and tuples" in low:
            return {
                "type": "practice",
                "instruction": "Integration: make visitors={'a1','b2','a1'}, print len, check 'b2' in set, make a tuple row and print it.",
                "starter_code": "visitors = {'a1','b2','a1'}\n# len + in + tuple\n",
                "check": lambda code: "len(" in code and " in " in code and "(" in code,
                "success_msg": "Set deduplicates, tuple records row!",
                "hint": "print(len(visitors)), print('b2' in visitors), point=(date, len)",
            }
        if "nested" in low:
            return {
                "type": "practice",
                "instruction": "Integration: grid=[[1,2],[3,4]]; nested loop to sum all cells into total and print it along with grid.",
                "starter_code": "grid = [[1,2],[3,4]]\n# nested sum\n",
                "check": lambda code: code.count("for ")>=2 and "total" in code and "print(" in code,
                "success_msg": "Nested summed all cells!",
                "hint": "total=0; for row in grid: for cell in row: total+=cell",
            }
        if "f-string" in low:
            return {
                "type": "practice",
                "instruction": "Integration: name='Ada', age=36, city='London'; print f'{name} from {city} is {age}' and print len line via f-string.",
                "starter_code": "name='Ada'\nage=36\ncity='London'\n",
                "check": lambda code: ("f'" in code or 'f"' in code) and code.count("print(")>=2,
                "success_msg": "f-strings embed multiple vars!",
                "hint": "print(f'{name} from {city} is {age}')",
            }
        if "slicing" in low:
            return {
                "type": "practice",
                "instruction": "Integration: word='python' print word[1:4], word[-2:], word[::-1] each on new line.",
                "starter_code": "word='python'\n# slices\n",
                "check": lambda code: "[1:4]" in code and "::-1" in code and code.count("print(")>=3,
                "success_msg": "Slices, tail, reverse all done!",
                "hint": "print(word[1:4]), word[-2:], word[::-1]",
            }
        if "dictionary methods" in low:
            return {
                "type": "practice",
                "instruction": "Integration: stock={'apple':12,'bread':7}; .items loop print, sum(values) print, .get(unknown,0) print.",
                "starter_code": "stock={'apple':12,'bread':7}\n# items, sum, get\n",
                "check": lambda code: ".items(" in code and ".values(" in code and ".get(" in code,
                "success_msg": "Dict methods loop, sum, safe get!",
                "hint": "for k,v in stock.items(), sum(stock.values()), stock.get('x',0)",
            }
        if "enumerate" in low and "zip" in low:
            return {
                "type": "practice",
                "instruction": "Integration: names=['Ada','Bob'], scores=[92,85]; zip then enumerate(start=1) print rank lines.",
                "starter_code": "names=['Ada','Bob']\nscores=[92,85]\n# zip + enumerate\n",
                "check": lambda code: "zip(" in code and "enumerate(" in code and "print(" in code,
                "success_msg": "zip+enumerate ranked them!",
                "hint": "for i,(n,s) in enumerate(zip(names,scores), start=1): print(f'{i} {n}: {s}')",
            }
        if "enumerate" in low or "zip" in low:
            return {
                "type": "practice",
                "instruction": "Integration: names=['Ada','Bob'], scores=[92,85]; zip then enumerate(start=1) print rank lines.",
                "starter_code": "names=['Ada','Bob']\nscores=[92,85]\n# zip + enumerate\n",
                "check": lambda code: "zip(" in code and "enumerate(" in code and "print(" in code,
                "success_msg": "zip+enumerate ranked them!",
                "hint": "for i,(n,s) in enumerate(zip(names,scores), start=1): print(f'{i} {n}: {s}')",
            }
        if "standard library" in low:
            return {
                "type": "practice",
                "instruction": "Integration: import math and random, print math.sqrt(25), print random.randint(1,6), print math.pi rounded.",
                "starter_code": "import math\n# random too\n",
                "check": lambda code: "import " in code and "math." in code and "random" in code,
                "success_msg": "Math + random together!",
                "hint": "import math, random; sqrt, randint, pi",
            }
        if low == "classes and objects":
            return {
                "type": "practice",
                "instruction": "Integration: extend Cat with meow returning f'{self.name} says Meow', make two cats and print both meows.",
                "starter_code": "class Cat:\n    def __init__(self,name): self.name=name\n# meow\n",
                "check": lambda code: "class Cat" in code and "def meow" in code and "self.name" in code,
                "success_msg": "Class with method and instances!",
                "hint": "def meow(self): return f'{self.name} says Meow!'",
            }
        if "classes" in low:
            return {
                "type": "practice",
                "instruction": "Integration: extend Cat with meow returning f'{self.name} says Meow', make two cats and print both meows.",
                "starter_code": "class Cat:\n    def __init__(self,name): self.name=name\n# meow\n",
                "check": lambda code: "class Cat" in code and "def meow" in code and "self.name" in code,
                "success_msg": "Class with method and instances!",
                "hint": "def meow(self): return f'{self.name} says Meow!'",
            }
        if "file handling" in low:
            return {
                "type": "practice",
                "instruction": "Integration: write 'hi\\nbye' to demo.txt, read it back, print content and line count.",
                "starter_code": "# write then read demo.txt\n",
                "check": lambda code: "open(" in code and "write" in code and "read" in code and "print(" in code,
                "success_msg": "File persisted and reloaded!",
                "hint": "with open('demo.txt','w') as f: write; with open(...,'r') as f: read",
            }
        if "file" in low:
            return {
                "type": "practice",
                "instruction": "Integration: write 'hi\\nbye' to demo.txt, read it back, print content and line count.",
                "starter_code": "# write then read demo.txt\n",
                "check": lambda code: "open(" in code and "write" in code and "read" in code and "print(" in code,
                "success_msg": "File persisted and reloaded!",
                "hint": "with open('demo.txt','w') as f: write; with open(...,'r') as f: read",
            }
        if "exception" in low:
            return {
                "type": "practice",
                "instruction": "Integration: two tries: int('abc') ValueError and 10/0 ZeroDivisionError, each with its except and print.",
                "starter_code": "# two try/except blocks\n",
                "check": lambda code: code.count("try:")>=2 and code.count("except")>=2,
                "success_msg": "Both errors caught!",
                "hint": "try: int('abc') except ValueError; try: 10/0 except ZeroDivisionError",
            }
        if "json files" in low:
            return {
                "type": "practice",
                "instruction": "Integration: save {'x':1,'y':[1,2]} to data.json with dump, load back, print dict['y'] length.",
                "starter_code": "import json\n# dump then load\n",
                "check": lambda code: "json.dump(" in code and "json.load(" in code and "open(" in code,
                "success_msg": "JSON round-trip works!",
                "hint": "with open(...,'w') dump, with open(...,'r') load",
            }
        if "json" in low:
            return {
                "type": "practice",
                "instruction": "Integration: save {'x':1,'y':[1,2]} to data.json with dump, load back, print dict['y'] length.",
                "starter_code": "import json\n# dump then load\n",
                "check": lambda code: "json.dump(" in code and "json.load(" in code and "open(" in code,
                "success_msg": "JSON round-trip works!",
                "hint": "with open(...,'w') dump, with open(...,'r') load",
            }
        if "comprehension" in low:
            return {
                "type": "practice",
                "instruction": "Integration: nums=[1,2,3,4,5]; evens=[n for n in nums if n%2==0]; squares=[n*n for n in nums]; print both.",
                "starter_code": "nums=[1,2,3,4,5]\n# comprehensions\n",
                "check": lambda code: code.count("for ")>=2 and "if " in code and "print(" in code,
                "success_msg": "Filtered and transformed via comprehensions!",
                "hint": "[n for n in nums if n%2==0] and [n*n for n in nums]",
            }
        if low == "guis with tkinter":
            return {
                "type": "practice",
                "instruction": "Integration: window with title 'App', two labels different texts, both packed, mainloop.",
                "starter_code": "import tkinter as tk\nroot=tk.Tk()\n# 2 labels\n",
                "check": lambda code: code.count("Label")>=2 and ".pack(" in code and "mainloop" in code,
                "success_msg": "Window with two labels!",
                "hint": "tk.Label(root,text=...) twice, pack each",
            }
        if low == "buttons and events":
            return {
                "type": "practice",
                "instruction": "Integration: label '0', button that increments global count via config, packed, mainloop.",
                "starter_code": "import tkinter as tk\nroot=tk.Tk()\ncount=0\n# label+button\n",
                "check": lambda code: "Button" in code and "command=" in code and "config(" in code,
                "success_msg": "Button updates label!",
                "hint": "def inc(): global count; count+=1; label.config(text=str(count))",
            }
        if "entry widgets" in low:
            return {
                "type": "practice",
                "instruction": "Integration: entry+button where button reads int(entry.get()), adds 10, shows via label.config.",
                "starter_code": "import tkinter as tk\ndef show(): pass\nroot=tk.Tk()\n# entry\n",
                "check": lambda code: "Entry" in code and ".get(" in code and "int(" in code and "config(" in code,
                "success_msg": "Entry -> int -> display!",
                "hint": "value=int(entry.get()); label.config(text=str(value+10))",
            }
        if "entry" in low:
            return {
                "type": "practice",
                "instruction": "Integration: entry+button where button reads int(entry.get()), adds 10, shows via label.config.",
                "starter_code": "import tkinter as tk\ndef show(): pass\nroot=tk.Tk()\n# entry\n",
                "check": lambda code: "Entry" in code and ".get(" in code and "int(" in code and "config(" in code,
                "success_msg": "Entry -> int -> display!",
                "hint": "value=int(entry.get()); label.config(text=str(value+10))",
            }
        if "loading real data" in low:
            return {
                "type": "practice",
                "instruction": "Integration: load us_states.json, then loop and print name where region == 'West'.",
                "starter_code": "import json\nwith open('us_states.json') as f:\n    states=json.load(f)\n# west filter\n",
                "check": lambda code: "us_states.json" in code and "for " in code and "West" in code,
                "success_msg": "Filtered real West states!",
                "hint": "for s in states: if s['region']=='West': print(s['name'])",
            }
        if "filtering and ranking" in low:
            return {
                "type": "practice",
                "instruction": "Integration: load elements.json, print noble gases via 'noble gas' in category, and also sorted by atomic_mass top 2.",
                "starter_code": "import json\nwith open('elements.json') as f:\n    data=json.load(f)\n# filter+sort\n",
                "check": lambda code: "noble gas" in code and "sorted(" in code and "atomic_mass" in code,
                "success_msg": "Filtered gases and ranked by mass!",
                "hint": "filter noble gas, sorted by atomic_mass",
            }
        if "summarizing" in low:
            return {
                "type": "practice",
                "instruction": "Integration: load planets.json, print max moons name, min diameter name, avg distance rounded.",
                "starter_code": "import json\nwith open('planets.json') as f:\n    data=json.load(f)\n# max/min/avg\n",
                "check": lambda code: "max(" in code and "min(" in code and "sum(" in code and "round(" in code,
                "success_msg": "Max/min/avg summarized!",
                "hint": "max key moons, min key diameter, sum/len avg distance",
            }
        if "regular expression" in low:
            return {
                "type": "practice",
                "instruction": "Integration: text='Call 555-1234 and 555-9999', find all \\d{3}-\\d{4} via findall and print count.",
                "starter_code": "import re\ntext='Call 555-1234 and 555-9999'\n# findall\n",
                "check": lambda code: "re.findall" in code and "\\d" in code and "print(" in code,
                "success_msg": "Regex extracts phones!",
                "hint": "re.findall(r'\\d{3}-\\d{4}', text)",
            }
        if "regular" in low:
            return {
                "type": "practice",
                "instruction": "Integration: text='Call 555-1234 and 555-9999', find all \\d{3}-\\d{4} via findall and print count.",
                "starter_code": "import re\ntext='Call 555-1234 and 555-9999'\n# findall\n",
                "check": lambda code: "re.findall" in code and "\\d" in code and "print(" in code,
                "success_msg": "Regex extracts phones!",
                "hint": "re.findall(r'\\d{3}-\\d{4}', text)",
            }
        if "testing" in low:
            return {
                "type": "practice",
                "instruction": "Integration: def double(n): return n*2; assert double(2)==4; assert double(-1)==-2; print('All tests passed')",
                "starter_code": "def double(n):\n    return n*2\n# asserts\n",
                "check": lambda code: "assert" in code and code.count("assert")>=2 and "print(" in code,
                "success_msg": "Asserts verify doubles!",
                "hint": "assert double(2)==4; assert double(-1)==-2",
            }
        if "recursion" in low:
            return {
                "type": "practice",
                "instruction": "Integration: write factorial recursive and sum_to recursive, print factorial(4)=24 and sum_to(4)=10.",
                "starter_code": "def factorial(n):\n    pass\n# sum_to\n",
                "check": lambda code: code.count("def ")>=2 and "return" in code and "factorial" in code,
                "success_msg": "Two recursions work!",
                "hint": "factorial base n<=1 return 1 else n*fact(n-1)",
            }
        if "decorator" in low:
            return {
                "type": "practice",
                "instruction": "Integration: decorator that times: wrapper records count, calls func, prints f'Call {count}', return wrapper; test on add.",
                "starter_code": "def deco(func):\n    def w(*a,**k): pass\n    return w\n",
                "check": lambda code: "def deco" in code and "def w" in code and "return w" in code,
                "success_msg": "Stateful decorator counts!",
                "hint": "nonlocal count; count+=1; result=func(*a,**k); print",
            }
        if "generator" in low:
            return {
                "type": "practice",
                "instruction": "Integration: gen squares(n): yield i*i; print list(squares(5)); also yield from chain.",
                "starter_code": "def squares(n):\n    for i in range(n):\n        yield i*i\n# print\n",
                "check": lambda code: "def squares" in code and "yield" in code and "list(" in code,
                "success_msg": "Generator yields squares!",
                "hint": "yield i*i, print(list(squares(5)))",
            }
        if "working with apis" in low:
            return {
                "type": "practice",
                "instruction": "Integration: api_response with 3 users, loads, filter active, sorted by score desc, print each name:score.",
                "starter_code": "import json\napi_response='{\"users\":[{\"name\":\"Ada\",\"score\":92,\"active\":true}]}'\n# parse+filter+sort\n",
                "check": lambda code: "json.loads(" in code and "active" in code and "sorted(" in code,
                "success_msg": "API parse/filter/sort done!",
                "hint": "data=json.loads(...); [u for u in data['users'] if u['active']]; sorted(key=score)",
            }
        if "api" in low:
            return {
                "type": "practice",
                "instruction": "Integration: api_response with 3 users, loads, filter active, sorted by score desc, print each name:score.",
                "starter_code": "import json\napi_response='{\"users\":[{\"name\":\"Ada\",\"score\":92,\"active\":true}]}'\n# parse+filter+sort\n",
                "check": lambda code: "json.loads(" in code and "active" in code and "sorted(" in code,
                "success_msg": "API parse/filter/sort done!",
                "hint": "data=json.loads(...); [u for u in data['users'] if u['active']]; sorted(key=score)",
            }
        return {
            "type": "practice",
            "instruction": "Integration: combine the key ideas of this lesson into one short program that uses print() and the lesson's main tool.",
            "starter_code": "# Combine lesson ideas\n",
            "check": lambda code: "print(" in code and len(code.split()) > 5,
            "success_msg": "Integrated the lesson ideas!",
            "hint": "Use print() with the lesson's signature construct.",
        }

    for level, lessons in list(sets.items()):
        for lesson in lessons:
            steps = lesson.get("steps", [])
            review_idx = None
            for idx_i, s in enumerate(steps):
                if s.get("type") == "review":
                    review_idx = idx_i
            if review_idx is None:
                review_idx = len(steps)
            title = lesson.get("title", "")
            dbg = _intensive_debug_for(title)
            integ = _integration_for(title)
            steps.insert(review_idx, dbg)
            steps.insert(review_idx + 1, integ)

    return sets

