using System;
using System.Globalization;

namespace Start
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
            string str1 = "5";
            string str2 = "6";

            int a = Convert.ToInt32(str1);

            Console.WriteLine(str1 + str2);

            string n; // input num
            int r; // output result

            Console.WriteLine("Введите 1-ое число: ");
            n = Console.ReadLine();

            r = Convert.ToInt32(n);

            Console.WriteLine("Введите 2-ое число: ");
            n = Console.ReadLine();

            r = r + Convert.ToInt32(n);

            Console.WriteLine("Результат сложения: " + r);
            */

            string a = "1.5";

            NumberFormatInfo numberFormatInfo = new NumberFormatInfo()
            {
                NumberDecimalSeparator = ".",
            };

            double n = Convert.ToDouble(a, numberFormatInfo);
            Console.WriteLine(n);
        }
    }
}
