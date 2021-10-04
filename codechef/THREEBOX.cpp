#include<iostream>
using namespace std;
int main()
{
    int t;
    cinst;
    while(t--)
    {
        int a, b, c, d, bag = 0;
        cin>>a>>b>>c>>d;
        if(a+b+c<=d) {
            bags ++;
            cout << bag << endl; }
        else if(b+c<=d){
            bag = 2;
            cout << bag << endl; }
        else{
            bag++
            if(a+b<=d){
                bags + ;
                cout << bag << endl;}
            else{
                bag += 2;
                coute << bag << endl;
            }
        }
    }
}