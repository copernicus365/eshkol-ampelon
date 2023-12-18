global using static System.Console;
using DotNetXtensions;

// See https://aka.ms/new-console-template for more information
WriteLine("Hello, World!");

string text = await File.ReadAllTextAsync("/Users/nikos/repos/eshkol-ampelon/progs/LettersHelper1/data/temp-file.txt");

WriteLine(text);

var text2 = text.Replace('̣', '݂');

WriteLine("Replaced text:");

WriteLine(text2);

"Done".Print();

ReadKey();

