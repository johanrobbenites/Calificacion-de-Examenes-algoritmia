#include<iostream>
#include<conio.h>
#include <fstream>
using namespace std;
struct nodo{
	string n;
	nodo *sigue;
};
nodo *h, *p;
int main(){
	h=new nodo;
	p=h;
	string cadena;
	ifstream datos("ALGORITMIA.TXT");
	if(datos.fail()){
		cout<<"ALGORITMIA.TXT no existe"<<endl;
	}else{
		while(!datos.eof()){
			getline(datos,cadena); //con esta funcion tomas la linea(limitada por \n)
			p->n=cadena;
			p->sigue=new nodo;
			p=p->sigue;
			p->sigue=NULL;
		}
	}
	datos.close();
	p=h;
	cout<<"\nLISTA:\n";
	while(p!=NULL){
		cout<<"\n"<<p->n;
		p=p->sigue;
	}
	return 0;
}