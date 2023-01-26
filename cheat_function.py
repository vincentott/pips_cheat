def cheat(question):
    """
    Enter question as string (e.g. "Q1.2P.1")
    to get the correct answer.
    """
    if question == "Q1.2P.1":
        print("==================== Q1.2P.1 ====================")
        print("The question was:")
        print(
            """
            another_array = np.zeros((2, 4, 6))
            
            This python code produces an error that the name ‘np’ is not defined.
            What line of code did I need to import numpy
            before this line or at the beginning of my Python script?
            """
        )
        print("The answer is:")
        print(
            """
            # You have to run the line:
            # import numpy as np
            """
        )

    elif question == "Q1.2P.8":
        print("==================== Q1.2P.8 ====================")
        print("The question was:")
        print(
            """
            Make a 3 dimensional array of 4 by 3 by 5
            with all elements as missing values.
            """
        )
        print("The answer is:")
        print(
            """
            import numpy as np
            
            my_array = np.full((4,3,5), fill_value=np.nan)
            """
        )


    elif question == "Q2.2P.1":
        print("==================== Q2.2P.1 ====================")
        print("The question was:")
        print(
            """
            Create an if statement that prints Go to sleep! if
            (your computer’s system) time is between 01:00 (1am) and 04:00 (4am),
            else if (elif) the time is between 08:00 (8am) and 09:00 (9am)
            it prints Eet je hagelslag!,
            or otherwise (else) it prints Gut gemacht!.
            """
        )
        print("The answer is:")
        print(
            """
            import numpy as np
            import datetime

            # obtain current_time as military time integer (e.g. "17:30" is 1730)
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            current_time = int(str(current_hour) + str(current_minute))

            print("The current time is:", current_time)
            if 100 <= current_time < 400:
                print("Go to sleep!")
            elif 800 <= current_time < 900:
                print("Eet je hagelslag!")
            else:
                print("Gut gemacht!")
            """
        )


    elif question == "Q2.2P.8":
        print("==================== Q2.2P.8 ====================")
        print("The question was:")
        print(
            """
            Write a definition that gives
            the first n prime numbers as a numpy array.
            Use the following structure:
            
            def prime(n):
                '''
                Returns something...
                '''
                # Your code here
                return result
            """
        )
        print("The answer is:")
        print(
            """
            import numpy as np

            def prime(n):
                '''
                Returns something...
                '''
                # Your code here
                output_array = np.array([])
                # define a function that checks whether a number is a prime number
                def isprime(num):
                    output = True
                    for i in range(2, num - 1):
                        if num % i == 0:
                            output = False
                    return output
                
                current_eval = 2
                if n == 0:
                    return output_array
                while len(output_array) < n:
                    if isprime(current_eval) == True:
                        output_array = np.append(output_array, current_eval)
                    current_eval = current_eval + 1
                return output_array
            """
        )
    else:
        print(f"You looked for the solution to question: "
              f"{question}\n"
              f"But there is no solution stored.\n"
              f"Please make sure that you enter a string"
              f"in the following format: "
              f"QX.2P.X\n"
              f"where your replace the Xs with integers.\n"
              f"If you did then either the question has not"
              f"been implemented yet or it does not exist."
              )