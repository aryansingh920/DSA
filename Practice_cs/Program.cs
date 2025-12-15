using System.Diagnostics;
using System.Runtime.CompilerServices;
using Practice.Algorithms;
using System;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        //     var solver = new TwoSum();
        //     var result = solver.Solve(new[] { 2, 7, 11, 15 }, 9);

        //     Console.WriteLine($"{result[0]}, {result[1]}");

        Test();
        await Example();
    }

    static async Task Example()
    {
        Console.WriteLine("Start");
        await Task.Delay(2000);
        Console.WriteLine("End");
    }




    static void Test()
    {
        int x = 10;
        double y = 3.14;
        bool ok = true;
        string name = "Aryan";
        Console.WriteLine($"{name} {x} {y} {ok}");

    }
}
