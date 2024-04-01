using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        List<string> excludeList = new List<string> { "bike", "boat", "car" };
        List<string> sentense = new List<string> { "I love bikes", "I have boat and car", "I no have truck" };

        var result = sentense.Where(sentence =>
            !excludeList.Any(excludedWord => sentence.Contains(excludedWord)));
        
        foreach (var sentence in result)
        {
            Console.WriteLine(sentence);
        }
        Console.ReadLine();
    }
}