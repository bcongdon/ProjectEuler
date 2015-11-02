#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	ifstream myfile ("8.txt");
	string line;
	string input;
  	if(myfile.is_open()){
  		while ( std::getline (myfile, line) )
	    {
	    	input += line;
	    }
    	myfile.close();
  	}
  	//cout << input << endl;
  	unsigned long largestProduct = 0;
  	unsigned long currentProduct = 0;
  	for(int i = 0; i < input.length() - 13; i++){
  		currentProduct = 1;
  		for(int j = 0; j < 13; j++){
  			string charAtIndex = input.substr(i+j,1);
  			int intAtIndex = stoi(charAtIndex);
  			currentProduct *= intAtIndex;
  		}
  		if(currentProduct > largestProduct){
  			largestProduct = currentProduct;
  		}
  	}
  	cout << largestProduct << endl;
}