using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number:");
        int number = Convert.ToInt32(Console.ReadLine());

        long factorial = CalculateFactorial(number);
        string textinput = textFromInput(number);
        Console.WriteLine($"Factorial of {textinput} is: {factorial}");
        Console.ReadLine();
    }

    static long CalculateFactorial(int n)
    {
        if (n == 0)
            return 1;

        long result = 1;
        for (int i = 1; i <= n; i++)
        {
            result *= i;
        }
        return result;
    }

    static string textFromInput(int n)
    {
        if (n > 0) {
            string test = "1";
            for (int i = 1; i <= n; i++)
            {
                if (i > 1) { 
                    test += "*" + i;
                }
            }
            return test;
        }
        else return n.ToString();
        
    }
}