using System;

namespace Average
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double firstNum, secondNum;
            double result;

            Console.WriteLine("Среднее арифметическое двух чисел.\nВведите первое число:");
            firstNum = double.Parse(Console.ReadLine());

            Console.WriteLine("Введите второе число:");
            secondNum = double.Parse(Console.ReadLine());

            result = (firstNum + secondNum) / 2;
            Console.WriteLine("Среднее арифметическое двух чисел: " + result + "\n");
        }
    }
}
