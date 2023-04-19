using System;

namespace ConvertRuUsd
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string nRu;
            double r;

            Console.WriteLine("Конвертет валют: RU -> USD.\nВведите сумму в рублях:");
            nRu = Console.ReadLine();

            r = int.Parse(nRu);
            Console.WriteLine("Сумма в рублях: " + r + "\nСумма в долларах: " + r * 0.012247 + "\n");
        }
    }
}
