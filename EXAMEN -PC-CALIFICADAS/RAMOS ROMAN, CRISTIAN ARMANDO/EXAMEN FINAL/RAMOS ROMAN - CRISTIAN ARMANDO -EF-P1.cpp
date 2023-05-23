#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
struct Nodo{
	char sec;
	int numaprobados,numalumnos;
	float promedio;
	Nodo *punt;
};
void crear_nodo(Nodo *&p,char cod[]){
	char sec;
	sec=cod[0];
	int num;
	if(strlen(cod)==3){
		num=(int)(cod[1]-48)*10+(int)(cod[2]-48);
	}
	else{
		num=(int)(cod[1]-48);
	}
	if(p==NULL){
		p=new(Nodo);
		p->sec=sec;
		p->numalumnos=1;
		if(num>=10){
			p->numaprobados=1;			
		}
		else{
			p->numaprobados=0;
		}
		p->promedio=num;
		p->punt=NULL;
	}
	else{
		if(p->sec==sec){
			p->promedio=(p->promedio*p->numalumnos+num)/(p->numalumnos+1);
			p->numalumnos+=1;
			if(num>=10){
				p->numaprobados+=1;
			}
		}
		else{
			crear_nodo(p->punt,cod);
		}
	}
}
void leer_archivo(Nodo *&p){
	p=NULL;
	ifstream entrada;
	entrada.open("ALGORITMIA.TXT");
	if(!entrada){
		cout<<"Error de apertura...";
	}
	else{
		char cod[4];
		while(!entrada.eof()){
			if(entrada>>cod){
				crear_nodo(p,cod);
			}
		}
		entrada.close();
	}
}
void imprimir_mayores(Nodo *p){
	Nodo *act;
	act=p;
	int mayor=0;
	while(act!=NULL){
		if(p->numaprobados>mayor){
			mayor=p->numaprobados;
		}
		act=act->punt;
	}
	cout<<"\n--Secciones con mayor numero de aprobados--\n";
	cout<<"Numero de aprobados: "<<mayor<<endl;
	cout<<"Seccion\tPromedio\n";
	while(p!=NULL){
		if(p->numaprobados==mayor){
			cout<<"  "<<p->sec<<"\t  "<<p->promedio<<endl;
		}
		p=p->punt;
	}
}
int main(){
	Nodo *lista;
	leer_archivo(lista);
	imprimir_mayores(lista);
	return 0;
}

