#include <iostream>
#include "conio.h"
#include <stdlib.h>
using namespace std;

typedef struct nodo_s{
	int dato;
	struct nodo_s *siguiente;
}nodo_t;
typedef nodo_t *ptrNodo;
typedef nodo_t *ptrPila;
void push(ptrPila *pila, int x){
	ptrNodo nd;
	nd=(ptrNodo)malloc(sizeof(nodo_t));
	if (nd != NULL){
		nd->dato=x;
		nd->siguiente=*pila;
		*pila=nd;
	}
}

struct nodo{
	int dato;
	struct nodo *sgte;
};
struct cola{
	nodo *ultimo;
	nodo *primero;
};

void enqueue(struct cola &q, int valor){
	struct nodo *aux =new(struct nodo);
	aux->dato=valor;
	aux->sgte=NULL;
	if( q.ultimo==NULL){
		q.ultimo=aux;
	}
	else{
		(q.primero)->sgte=aux;
	}
	q.primero=aux;
}

int denqueue( struct cola &q){
	int num;
	struct nodo *aux;
	aux=q.ultimo;
	num=aux->dato;
	q.ultimo=(q.ultimo)->sgte;
	delete(aux);
	return num;
}

void invertirCola(struct cola c1, ptrNodo np){
	struct nodo *a1;
	a1=c1.ultimo;
	while(c1.ultimo!=NULL){
		a1=c1.ultimo;
		push(&np,a1->dato);
		c1.ultimo=a1->sgte;
		delete(a1);
	}
	c1.ultimo=NULL;
	c1.primero=NULL;
	while (np!=NULL){
		enqueue(c1,np->dato);
		np=np->siguiente;
	}
	a1=c1.ultimo;
	while(a1!=NULL){
		cout<<"dato: "<<a1->dato<<endl;
		a1=a1->sgte;
	}
}

int main(){
	struct cola c1;
	ptrPila pila =NULL;
	c1.ultimo=NULL, c1.primero=NULL;
	enqueue(c1,8);
	enqueue(c1,5);
	enqueue(c1,3);
	invertirCola(c1,pila);
	cout<<"\n\nCola invertida";
	_getch();
}
