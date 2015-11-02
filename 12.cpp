#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream myfile ("11.txt");
	string line;
	int **input = new int*[20];
	for(int i = 0; i < 20; ++i) {
	    input[i] = new int[20];
	}
  	if(myfile.is_open()){
  		int j = 0;
  		while ( std::getline (myfile, line) )
	    {
	    	for(int i = 0; i < 20; i++){
	    		input[j][i] = stoi(line.substr(i*3,2));
	    		//cout << input[j][i] << endl;
	    	}
	    	j++;
	    }
    	myfile.close();
  	}
  	int largestProductUD = 0;
  	//Up/Down
  	for(int x = 0; x < 20; x++){
  		for(int y = 3; y < 20; y++){
  			int currProduct = 1;
  			for(int i = 0; i < 4; i++){
  				currProduct *= input[x][y-i];
  			}
  			if(currProduct > largestProductUD){
  				largestProductUD = currProduct;
  			}
  		}
  	}
  	int largestProductLR = 0;
  	//Left/Right
  	for(int x = 3; x < 20; x++){
  		for(int y = 0; y < 20; y++){
  			int currProduct = 1;
  			for(int i = 0; i < 4; i++){
  				currProduct *= input[x-i][y];
  			}
  			if(currProduct > largestProductLR){
  				largestProductLR = currProduct;
  			}
  		}
  	}
  	int largestProductDia = 0;
  	//Diagonal 
  	for(int x = 3; x < 20; x++){
  		for(int y = 3; y < 20; y++){
  			int currProduct = 1;
  			for(int i = 0; i < 4; i++){
  				currProduct *= input[x-i][y-i];
  			}
  			if(currProduct > largestProductDia){
  				largestProductDia = currProduct;
  			}
  		}
  	}
  	//Diagonal 
  	for(int x = 0; x < 17; x++){
  		for(int y = 3; y < 20; y++){
  			int currProduct = 1;
  			for(int i = 0; i < 4; i++){
  				currProduct *= input[x+i][y-i];
  			}
  			if(currProduct > largestProductDia){
  				largestProductDia = currProduct;
  			}
  		}
  	}
  	//Output
  	cout << largestProductUD << endl;
  	cout << largestProductLR << endl;
  	cout << largestProductDia << endl; 	
}