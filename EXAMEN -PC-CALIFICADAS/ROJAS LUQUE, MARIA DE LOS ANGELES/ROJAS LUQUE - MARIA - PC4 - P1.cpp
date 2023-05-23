#include <iostream>
#include <fstream>
using namespace std;

/*  */
struct Nodo{
	int numero1;
	Nodo * punt;
};
int main() {
	int M, numero2;
	Nodo * var[M];
	do{
		cout << "Ingrese numero de datos:";
		cin >> M;
	}
	while(!(M > 0 && M <= 50));
	for(int i=0; i<M; i++){
		var[i] = new(Nodo);
		do{
			cout << "Ingrese el numero: ";
			cin >> numero2;
		}
		while(!(numero2 > 9 && numero2 <= 99));
		var[i] -> numero1 = numero2;
		var[i] -> punt = NULL;
	}
	// Enlazamos;
	for(int i=0; i < M-1; i++){
		for(int j = i+1; j < M; j++){
			var[i] -> punt = var[j];
		}
	}
	for(int i=0; i<M; i++){
		cout << var[i] -> numero1 << "\t" << var[i] -> punt << "\n";		
	}	

}
