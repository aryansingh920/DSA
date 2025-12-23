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

        // Test();
        // await Example();
        TsTData();
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

    static void TsTData()
    {
        // int[] arr1 = new int[10];
        int[] arr1 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        for (int i=0; i < arr1.Length; i++)
        {
            Console.WriteLine(arr1[i]);
        }
    }
}
