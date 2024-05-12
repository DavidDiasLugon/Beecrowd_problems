#include <bits/stdc++.h>

using namespace std; 


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

	int numeroMedicoes, intervaloTempo, temperatura;
    int nTeste = 1; 

    cin >> numeroMedicoes >> intervaloTempo;

    while (numeroMedicoes != 0 && intervaloTempo != 0){
        vector<int> vTemperaturas(numeroMedicoes);
			
        for(int i=0; i < numeroMedicoes; i++){
            cin >> temperatura;
            vTemperaturas[i] = temperatura;
        }

        int mediaMaior= -214748;
        int mediaMenor= 214748;
            
        for(int i = 0; i<numeroMedicoes; i++){
            int soma = 0;
            if(numeroMedicoes - 1 -i >= intervaloTempo - 1){
                for(int j=0; j<intervaloTempo; j++){
                    soma += vTemperaturas[i+j];
                }
                
                int media = (soma/intervaloTempo);	
                
                if(media < mediaMenor){
                    mediaMenor = media;
                }
                if(media > mediaMaior){
                    mediaMaior= media;   
                }
            }
        }
        cout << "Teste " << nTeste << "\n";
        cout << mediaMenor << " " << mediaMaior << "\n";
        nTeste++;
        cout << "\n";
        cin >> numeroMedicoes >> intervaloTempo;
    }
    return 0;
}