using IronPython.Runtime;
using System;
using System.Collections;
using static System.Runtime.InteropServices.JavaScript.JSType;

class Program
{
    static void Main()
    {
        int number;
        string symbol;
        System.Boolean boo;
        int input = GetIntegerInput("Enter your size of number : ");
        var nummberlist = new ArrayList();
        var symbollist = new ArrayList();
        string expression = "";
        for (int i = 0; i < input; i++)
        {
            number = GetIntegerInput("Enter a number: ");
            nummberlist.Add(number);
            
            if (i != input - 1)
            {
                symbol = GetSymbol();
                boo = (symbol == "+" || symbol == "-" || symbol == "*" || symbol == "/" || symbol == "%");
                if (boo == true) { symbollist.Add(symbol); }
                else
                {
                    while (boo != true)
                    {
                        symbol = GetSymbol();
                        boo = (symbol == "+" || symbol == "-" || symbol == "*" || symbol == "/" || symbol == "%");
                        if (boo == true) { symbollist.Add(symbol); }
                    }
                }
            }
        }
        for (int i = 0; i < nummberlist.Count; i++)
        {
           if (i != nummberlist.Count - 1) expression = expression + "" + nummberlist[i] + "" + symbollist[i];
            else expression = expression + "" + nummberlist[i];
        }
        Console.WriteLine("your input is: " + expression);
        int result = EvaluateExpression(expression);
        Console.WriteLine("your result is: " + result);
        Console.ReadLine();
    }

    static int EvaluateExpression(string expression)
    {
        return (int)new System.Data.DataTable().Compute(expression, null);
    }

    static int GetIntegerInput(string word)
    {
        int input = 0;
        bool isValidInput = false;

        while (!isValidInput)
        {
            Console.Write(word);
            string userInput = Console.ReadLine();

            try
            {
                input = Convert.ToInt32(userInput);
                isValidInput = true; 
            }
            catch (FormatException)
            {
                Console.WriteLine("Input is not in the correct format. Please enter a valid integer.");
            }
            catch (OverflowException)
            {
                Console.WriteLine("Input is too large or too small to fit in an integer.");
            }
            catch (Exception ex)
            {
                Console.WriteLine("An unexpected error occurred: " + ex.Message);
            }
        }

        return input;
    }

    static string GetSymbol()
    {
        Console.Write("enter symbol :");
        string input = Console.ReadLine();
        bool isValidInput = (input == "+" || input == "-" || input == "*" || input == "/" || input == "%");
        while (!isValidInput)
        {
            Console.Write("error enter symbol again :");
            input = Console.ReadLine();

            
                if (input == "+" || input == "-" || input == "*" || input == "/" || input == "%")
                {
                    isValidInput = true; 
                }
        }

        return input;
    }

}