#include <iostream>
using namespace std;

struct Nodo{
	int dato;
	Nodo *siguiente;
};

void insertarlista(Nodo *&lista,int n){
	Nodo *nuevo_nodo =new Nodo();
	nuevo_nodo->dato = n;
	
	Nodo *aux1=lista;
	Nodo *aux2;
}

void mostarlista(Nodo *lista){
	Nodo *actual = new Nodo();
	actual=lista;
	while(actual!= NULL){
		cout<<actual->dato<<" -> ";
		actual= actual-> siguiente;
	}

}
int main(){
	int n;
	int a;
	Nodo *lista = NULL;
	Nodo *lista2= NULL;
	cout<<"Ingrese el numero de enteros a ingresar: ";
	cin>>n;
	int v[n];
	for(int i =0;i<n;i++){
		cout<<"Ingrese el dato de dos digitos a la lista: ";
		cin>>a;
		v[i]=a;
		insertarlista(lista,a);	
	}
	mostarlista(lista);
	for(int i=n; i>=0;i--){
		insertarlista(lista2,v[i]);
	}
	mostarlista(lista2);
	
	return 0;
	
}