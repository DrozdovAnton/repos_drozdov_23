using System;

namespace test
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ConsoleKey consoleKey = new ConsoleKey();
            consoleKey = Console.ReadKey().Key;

            if (consoleKey == ConsoleKey.M)
            {
                Console.WriteLine("Кнопка М");
            }
        }
    }
}
