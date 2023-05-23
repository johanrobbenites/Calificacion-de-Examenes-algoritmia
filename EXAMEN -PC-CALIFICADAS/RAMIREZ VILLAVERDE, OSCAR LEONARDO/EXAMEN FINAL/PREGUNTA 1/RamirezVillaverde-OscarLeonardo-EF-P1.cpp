#include <iostream>
#include <fstream>
using namespace std;

struct Nodo{
	char codigo;
	int dato;
	Nodo *siguiente;
};

void insertarlista(Nodo *&lista,int n){
	Nodo *nuevo_nodo = new Nodo();
	Nodo *aux;
	
	nuevo_nodo->dato = n;
	nuevo_nodo->siguiente = NULL;
	
	if(lista == NULL){
		lista = nuevo_nodo;
	}
	else{
		aux = lista;
		while(aux->siguiente != NULL){
			aux = aux->siguiente;
		}
		aux->siguiente = nuevo_nodo;
	}
}

void calcularmayor(Nodo *lista){
	int mayor=0;
	
	while(lista != NULL){
		if((lista->dato)>mayor){
			mayor = lista->dato;
		}
		}
		lista = lista->siguiente;
	}
	cout << "El mayor numero es: " << mayor;
}

int main(){
	
	Nodo *lista=NULL;
	int dato;
	char codigo;
	bool existe;
	ifstream ent, ent2;
	ent.open("ALGORITMIA.txt");
	if(!ent1){
		cout<<"Error al abrir el archivo ...";
	}
	else{
		while(!ent.eof()){
			if(ent>>codigo>>dato){
				insertarlista(lista,dato)
					}
				}
			}
		}
	}
	calcularmayor(lista)
	return 0
}
