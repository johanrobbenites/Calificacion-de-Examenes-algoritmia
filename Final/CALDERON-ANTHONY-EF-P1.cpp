#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
struct NodoU{
	int nota;
	NodoU *siguiente;
};
struct NodoV{
	int nota;
	NodoV *siguiente;
};
struct NodoW{
	int nota;
	NodoW *siguiente;
};

void insertarListaU(NodoU *&lista, int n){
	NodoU *nuevo_nodo=new NodoU();
	NodoU * aux;
	nuevo_nodo->nota=n;
	nuevo_nodo->siguiente=NULL;
	
	if(lista==NULL){
		lista=nuevo_nodo;
	}
	else{
		aux=lista;
		while(aux->siguiente !=NULL){
			aux=aux->siguiente;
		}
		aux->siguiente=nuevo_nodo;
	}
}

void insertarListaW(NodoW *&lista, int n){
	NodoW *nuevo_nodo=new NodoW();
	NodoW * aux;
	nuevo_nodo->nota=n;
	nuevo_nodo->siguiente=NULL;
	
	if(lista==NULL){
		lista=nuevo_nodo;
	}
	else{
		aux=lista;
		while(aux->siguiente !=NULL){
			aux=aux->siguiente;
		}
		aux->siguiente=nuevo_nodo;
	}
}
void insertarListaV(NodoV *&lista, int n){
	NodoV *nuevo_nodo=new NodoV();
	NodoV * aux;
	nuevo_nodo->nota=n;
	nuevo_nodo->siguiente=NULL;
	
	if(lista==NULL){
		lista=nuevo_nodo;
	}
	else{
		aux=lista;
		while(aux->siguiente !=NULL){
			aux=aux->siguiente;
		}
		aux->siguiente=nuevo_nodo;
	}
}
void leer_archivo(NodoU *&p,NodoV *&q,NodoW *&r){
	p=NULL,q=NULL,r=NULL;
	ifstream entrada;
	entrada.open("ALGORITMIA.TXT");
	if(!entrada){
		cout<<"Error de apertura de ALUMNOS.TXT\n";
	}
	else{
		char sec;
		int n;
		while(!entrada.eof()){
			entrada>>sec>>n;
			cout<<sec<<" "<<n<<endl;
			if(sec=='U'){
				insertarListaU(p,n);
			}
			else if(sec=='V'){
				insertarListaV(q,n);
			}
			else if(sec=='W'){
				insertarListaW(r,n);
			}

		}
	}
}

void mostrarListaU(NodoU *lista){
	while(lista!=NULL){
		cout<<lista->nota;
		if(lista->siguiente!=NULL){
			cout<<"->";
		}
		else{
			cout<<".";
		}
		lista=lista->siguiente;
	}
}
void mostrarListaV(NodoV *lista){
	while(lista!=NULL){
		cout<<lista->nota;
		if(lista->siguiente!=NULL){
			cout<<"->";
		}
		else{
			cout<<".";
		}
		lista=lista->siguiente;
	}
}
void mostrarListaW(NodoW *lista){
	while(lista!=NULL){
		cout<<lista->nota;
		if(lista->siguiente!=NULL){
			cout<<"->";
		}
		else{
			cout<<".";
		}
		lista=lista->siguiente;
	}
}
int main(){
	NodoU *lista1;
	NodoV *lista2;
	NodoW *lista3;
	leer_archivo(lista1,lista2,lista3);
	cout<<"Seccion U"<<endl;
	mostrarListaU(lista1);
	cout<<" "<<endl;
	cout<<"Seccion V"<<endl;
	mostrarListaV(lista2);
	
	cout<<" "<<endl;
	cout<<"Seccion W"<<endl;
	mostrarListaW(lista3);

	return 0;
}