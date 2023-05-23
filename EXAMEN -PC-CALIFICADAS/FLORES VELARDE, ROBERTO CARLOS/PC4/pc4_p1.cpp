#include <iostream>
using namespace std;
struct Nodo {
    int x;
    Nodo *punt;
};

void Crea_NodoR(Nodo *&p, int x) {
    if (p == NULL) {
        p = new (Nodo);
        p->x = x;
        p->punt = NULL;
    } else {
        if (p->x != x) {
            Crea_NodoR(p->punt, x);
        }
    }
}
void Datos(Nodo *&p) {
    int x, i, n;
    p = NULL;
    do {
        cout << "Ingrese el # de nodos:";
        cin >> n;
    } while (!(n > 0 && n <= 50));
    for (i = 1; i <= n; i++) {
        cout << "Nodo #" << i << endl;
        cout << "Ingrese numero de dos cifras:";
        cin >> x;
        Crea_NodoR(p, x);
    }
}
void RecorreR(Nodo *p) {
    if (p != NULL) {
        cout << p->x << "\n";
        RecorreR(p->punt);
    }
}
void invertir(Nodo *p, Nodo *q, Nodo *&x) {
    if (q->punt->punt != NULL) {
        invertir(p, q->punt, x);
    } else {
        x = q->punt;
        x->punt = q;
        q->punt = NULL;
        invertir(p, p, x->punt);
    }
}
int main() {
    Nodo *Lista, *y = new (Nodo), *q = Lista;
    Datos(Lista);
    RecorreR(Lista);
    invertir(Lista, q, y);
    RecorreR(y);
    cout << Lista->punt->x;
    return 0;
}