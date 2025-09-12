#include <iostream>
#include "TXLib.h"
#include <math.h>

int main ()
{
    while(!GetAsyncKeyState(VK_ESCAPE))
    {
        ///   ПЕРЕМЕННЫЕ (И НЕ ОЧЕНЬ)   ///
        cout << "Введите число вершин:";
        int a;
        cin >> a;
        cout << "Введите максимальную длину перескока:";
        int b;
        cin >> b;
        cout << "Введите два числа - расстояние от точки к которой идёт построение до следа:";
        int m1;
        cin >> m1;
        cout << "Введите два числа - расстояние от следа до старой точки:";
        int m2;
        cin >> m2;
        double Tau = 6.283184;
        int vertex_coord[100][2] = {0};
        int vertex_color[100][3] = {0};
        int x = rand() % 1000;
        int y = rand() % 1000;
        int now_vertex;
        int previous_vertex;

        ///   ПОДГОТОВКА ОКНА И ИНСТРУМЕНТОВ РИСОВАНИЯ   ///
        txCreateWindow(1000, 1000);
        txSetColor(RGB (0, 255, 0), 3);
        txCircle(x, y, 1);
        cout << "a:" << a << "\n" << "b:" << b << "\n" << "m1:" << m1 << "\n" << "m2:" << m2 << "\n";

        ///   ПОДГОТОВКА ТОЧЕК ///
        if(a != 1)
        {
            for(int i = 0; i < a; i++)
            {
                vertex_coord[i][0] = int(cos(Tau * i / a) * 375 + 500);
                vertex_coord[i][1] = int(sin(Tau * i / a) * 375 + 500);
                if(i/a <= 1/6)
                {
                    vertex_color[i][0] = 255;
                    vertex_color[i][1] = 6*i/a*255;
                    vertex_color[i][2] = 0;
                }
                else
                {
                    if(i/a <= 2/6)
                    {
                        vertex_color[i][0] = 255*(1 - (i/a-1/6)*6);
                        vertex_color[i][1] = 255;
                        vertex_color[i][2] = 0;
                    }
                    else
                    {
                        if(i/a <= 3/6)
                        {
                            vertex_color[i][0] = 0;
                            vertex_color[i][1] = 255;
                            vertex_color[i][2] = (i/a-2/6)*6*255;
                        }
                        else
                        {
                            if(i/a <= 4/6)
                            {
                                vertex_color[i][0] = 0;
                                vertex_color[i][1] = 255*(1 - (i/a-3/6)*6);
                                vertex_color[i][2] = 255;
                            }
                            else
                            {
                                if(i/a <= 5/6)
                                {
                                    vertex_color[i][0] = (i/a-4/6)*6*255;
                                    vertex_color[i][1] = 0;
                                    vertex_color[i][2] = 255;
                                }
                                else
                                {
                                    vertex_color[i][0] = 255;
                                    vertex_color[i][1] = 0;
                                    vertex_color[i][2] = 255*(1 - (i/a-5/6)*6);
                                }
                            }
                        }
                    }
                }
            }
        }
        else
        {
            vertex_coord[0][0] = 500;
            vertex_coord[0][1] = 500;
        }

        for(int i = 0; i < a; i++)
        {
            txSetPixel (x, y, RGB(vertex_color[i][0], vertex_color[i][1], vertex_color[i][2]));
        }

        ///   БЕСКОНЕЧНЫЙ ЦИКЛ РИСОВАНИЯ   ///
        now_vertex = rand()%a;
        x = (vertex_coord[now_vertex][0] * m2 + x * m1)/(m1 + m2);
        y = (vertex_coord[now_vertex][1] * m2 + y * m1)/(m1 + m2);
        previous_vertex = now_vertex;
        txSetPixel (x, y, RGB(vertex_color[now_vertex][0], vertex_color[now_vertex][1], vertex_color[now_vertex][2]));
        while(!GetAsyncKeyState(VK_ESCAPE))
        {
            now_vertex = (rand()%(2*b+1) - 1 + previous_vertex + a) % a;
            x = (vertex_coord[now_vertex][0] * m2 + x * m1)/(m1 + m2);
            y = (vertex_coord[now_vertex][1] * m2 + y * m1)/(m1 + m2);
            previous_vertex = now_vertex;
            txSetPixel (x, y, RGB(vertex_color[now_vertex][0], vertex_color[now_vertex][1], vertex_color[now_vertex][2]));
        }
    }
}
