# include <iostream>
# include <conio.h>
using namespace std;

struct nodo
{int dato;
 nodo *sgte;
};

nodo *h;
nodo *p;
int numero;

int main()
{
int i = 0;
int n;
if(i <=50)
	cout << "INTRODUZCA LA CANTIDAD DE NUMEROS: ";
	cin >> n;	
	
cout << "LECTURA DE NUMEROS" << "-> "; cin >> numero;
if(numero < n)
{p -> sgte = new nodo;
h -> dato = numero;
p = h;
}
	
cout << "LECTURA DEL NUMERO" << "-> "; cin >> numero;
while(numero < n)
{p -> sgte = new nodo;

cout << "LECTURA DEL SIGUIENTE NUMERO" << "->" ; cin >> numero;
p = p->sgte;
    } 

return 0;
			
}
