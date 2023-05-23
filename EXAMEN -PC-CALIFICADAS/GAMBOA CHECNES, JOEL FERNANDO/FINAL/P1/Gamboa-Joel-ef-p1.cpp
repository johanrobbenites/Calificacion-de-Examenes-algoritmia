#include <iostream>
#include <conio.h>
#include <String.h>
#include <fstream>
using namespace std;

struct nodo{
	char secc1[4], secc2[4], secc3[4], secc4[4];
	nodo* siguiente;
};

nodo *p, *u, *a, *n;
void cargar(){
	char secc1[4], secc2[4], secc3[4], secc4[4];
	ifstream arch;
	arch.open("ALGORITMIA.TXT",ios::in);
	while(!arch.eof()){
		arch>> secc1 >>secc2 >>secc3 >> secc4;
		if(!arch.eof()){
			n= new nodo;
			strcpy(n->secc1,secc1);
			strcpy(n->secc2,secc2);
			strcpy(n->secc3,secc3);
			strcpy(n->secc4,secc4);
			if(p==NULL){
				p=n;
				p->siguiente=NULL;
				u=p;
			}
			else{
				u->siguiente=n;
				n->siguiente=NULL;
				u=n;
			}
		}
	}
	arch.close();
}

void notas(){
	a=p;
	while(a!=NULL){
		cout<<a->secc1 <<" "<<a->secc2<<" "<<a->secc3<<" "<<a->secc4<<endl;
		a=a->siguiente;
	}
}



int main(){
	cargar();
	notas();
	return 0;
}