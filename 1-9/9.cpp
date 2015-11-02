#include <iostream>
using namespace std;


int main()
{
	int a = 1;
	int b = 1;
	int c = 1;
	for(a=1; a < 1000; a++){
		for(b=1; b < 1000; b++){
			for(c=1; c < 1000; c++){
				if(a+b+c == 1000 && (a*a) + (b*b) == (c*c)){
					cout << a << " " << b << " " << c << " " << endl;
					cout << a*b*c << endl;
					exit(0);
				}
			}
		}
	}
}