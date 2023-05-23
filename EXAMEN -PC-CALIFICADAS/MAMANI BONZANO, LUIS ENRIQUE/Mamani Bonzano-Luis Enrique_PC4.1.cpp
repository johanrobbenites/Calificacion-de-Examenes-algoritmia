// contruir una lista enlazada
# include<iostream>
# include<conio.h>
using namespace std;
// declarando la estructuta tipo nodo
struct nodo
{int dato;
nodo *sgte;
};
// variables
nodo *h;  // puntero de cabecera
nodo *p, *q ; // punteros auxiares
int m;
// programa principal
int main()
{h=new nodo;
p=h;
cout<<"Cantidad de elementos de la lista: ";
cin>>m;
for(int i=m/2; i>=1; i--){
	cout<<"Introduce un valor: ";
	cin>>p->dato;
	q=new nodo;
	cout<<"Introduce otro valor: ";
	cin>>q->dato;
	p->sgte=q;
	p=new nodo;
}
cout<<"Introduce otro valor: ";
p->dato=4;
q->sgte=p;
p->sgte=NULL;
// mostrar los elementos de la lista

p=h;
while (p!=NULL)
{cout<<p->dato<<" -> ";
p=p->sgte;
}

return 0;
}
