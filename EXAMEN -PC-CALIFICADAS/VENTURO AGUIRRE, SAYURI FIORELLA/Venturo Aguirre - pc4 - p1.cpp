#include <iostream>
#include <fstream>
using namespace std;
 
struct Nodo{
	int num;
	Nodo *punt;
};

int main(){
	int N, numero;
	Nodo *var[N];
	do{
		cout << "Ingrese cantidad de datos: "; cin >> N;
	}while(!(N > 0 && N <= 50));
	for(int i = 0; i < N; i++){
		var[i] = new(Nodo);
		do{
			cout << "Ingrese #: "; cin >> numero;
		}while(!(numero > 9 && numero <= 99));
		var[i]->num = numero;
		var[i]->punt = NULL;
	}
	// Enlazamos;
	for(int i = 0; i < N-1; i++){
		for(int j = i+1; j < N; j++){
			var[i]->punt = var[j];
		}
	}
	
	for(int i = 0; i < N; i++){
		cout << var[i]->num << "\t" << var[i]->punt << "\n";
	}
	// Invertimos;
	
}
