#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
using namespace std;
typedef char Cadena[10];
struct NodoC{
	int nota;
	NodoC *puntjC;
};
struct NodoA{
	char curso;
	NodoC *puntjC;
	NodoA *puntjA;
};
void Crear_NodoC(NodoC *&p, int nota){
	if(p==NULL){
		p=new(NodoC);
		p->nota=nota;
		p->puntjC=NULL;
	}
	else{
		Crear_NodoC(p->puntjC, nota);
	}
}
void Crear_NodoA(NodoA *&p, char curso, int nota){
	if(p==NULL){
		p=new(NodoA);
		p->curso=curso;
		p->puntjA=NULL;
		p->puntjC=NULL;
		Crear_NodoC(p->puntjC, nota);
	}
	else{
		if(p->curso==curso){
			Crear_NodoC(p->puntjC, nota);
		}
		else{
			Crear_NodoA(p->puntjA, curso, nota);
		}
	}
}
void pasarC(NodoC *p){
	if(p!=NULL){
		cout<<p->nota<<endl;
		pasarC(p->puntjC);
	}
}
void pasarA(NodoA *p){
	if(p!=NULL){
		cout<<p->curso<<endl;
		pasarC(p->puntjC);
		pasarA(p->puntjA);
	}
}
NodoA *Lista;
int main(){
	ifstream ent;
	int i,j,n,aux;
	char curso;
	Cadena s1;
	Lista=NULL;
	ent.open("NOTONES.TXT");
	if(!ent){
		cout<<"Error...";
	}
	else{
		
		while(!ent.eof()){
			if(ent>>s1){
				curso=s1[0];
				i=0;
				n=strlen(s1);
				while(i<n){
				if(((s1[i])!='0') and ((s1[i])!='1') and ((s1[i])!='2') and ((s1[i])!='3') and ((s1[i])!='4') and ((s1[i])!='5') and ((s1[i])!='6') and ((s1[i])!='7') and ((s1[i])!='8') and ((s1[i])!='9')){
				j=i;
				aux++;
			while(j<n){
				s1[j]=s1[j+1];
				j++;
			}
			n--;
		}
		else{
			i++;
		}
	}
				int nota=atoi(s1);
				Crear_NodoA(Lista, curso, nota);
			}
		}
		ent.close();
	}
	//Recorriendo la Lista
	pasarA(Lista);
	return 0;
}