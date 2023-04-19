using System;

namespace SumMultiplication
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double firstNum, secondNum, thirdNum;
            double result;

            Console.WriteLine("Сумма и произведение трех чисел.\nВведите первое число:");
            firstNum = double.Parse(Console.ReadLine());

            Console.WriteLine("Введите второе число:");
            secondNum = double.Parse(Console.ReadLine());

            Console.WriteLine("Введите третье число:");
            thirdNum = double.Parse(Console.ReadLine());

            result = firstNum + secondNum + thirdNum;
            Console.WriteLine("Сумма трех чисел: " + result);

            result = firstNum * secondNum * thirdNum;
            Console.WriteLine("Произведение трех чисел: " + result + "\n");
        }
    }
}
