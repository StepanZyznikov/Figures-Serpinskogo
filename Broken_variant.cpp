#include <iostream>
#include "TXLib.h"
#include <math.h>

int main ()
{
    while(!GetAsyncKeyState(VK_ESCAPE))
    {
        ///   ПЕРЕМЕННЫЕ (И НЕ ОЧЕНЬ)   ///
        int a;
        double Tau = 6.283184;
        int vertex[100][2] = {0};
        cin >> a;
        int x = rand() % 1000;
        int y = rand() % 1000;
        int now_vertex;

        ///   ПОДГОТОВКА ОКНА И ИНСТРУМЕНТОВ РИСОВАНИЯ   ///
        txCreateWindow(1000, 1000);
        txSetColor (RGB (255, 127, 127), 3);
        txCircle (x, y, 1);
        txSetColor (RGB (255, 0, 0), 1);



        ///   ПОДГОТОВКА ТОЧЕК ///
        if(a != 1)
        {
            for(int i = 0; i < a; i++)
            {
                vertex[i][0] = int(cos(Tau * i / a) * 375 + 500);
                vertex[i][1] = int(sin(Tau * i / a) * 375 + 500);
            }
        }
        else
        {
            vertex[0][0] = 500;
            vertex[0][1] = 500;
        }

        for(int i = 0; i < a; i++)
        {
            txCircle (vertex[i][0], vertex[i][1], 3);
            cout << vertex[i][0] << vertex[i][1] << "\n";
        }

        ///   БЕСКОНЕЧНЫЙ ЦИКЛ РИСОВАНИЯ   ///
        while(!GetAsyncKeyState(VK_ESCAPE))
        {
            now_vertex = rand()%a;
            x = (vertex[now_vertex][0] - x)/2;
            y = (vertex[now_vertex][1] - y)/2;
            txSetPixel (x, y, TX_WHITE);
        }
    }
}
