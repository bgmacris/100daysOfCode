#include <stdio.h>

struct componentes{
	char nom[20];
	int preu;
	int id;
}
i5={"processador i5",500,1},
i7={"processador i7",750,2},
i9={"processador i9",1200,3},

ram8={"memoria ram 8Gb",200,4},
ram16={"memoria ram 16gb",300,5},

ssd256={"memoria ssd 256Gb",200,6},
ssd512={"memoria sdd 512Gb",300,7},
ssd1={"memoria sdd 1T",500,8};

int preu;

void seleccio(component,id){
	switch(component){
		case 1:
			switch(id){
				case 1:
					printf("Ha seleccionat %s amb un preu de %i�\n\n",i5.nom,i5.preu);
					preu += i5.preu;
					break;
				case 2:
					printf("Ha seleccionat %s amb un preu de %i�\n\n",i7.nom,i7.preu);
					preu += i7.preu;
					break;
				case 3:
					printf("Ha seleccionat %s amb un preu de %i�\n\n",i9.nom,i9.preu);
					preu += i9.preu;
					break;
			}
			
		case 2:
			switch(id){
				case 4:
					printf("Ha seleccionat %s amb un preu de %i�\n\n",ram8.nom,ram8.preu);
					preu += ram8.preu;
					break;
				case 5:
					printf("Ha seleccionat %s amb un preu de %i�\n\n",ram16.nom,ram16.preu);
					preu += ram16.preu;
					break;
			}
			
		case 3:
			switch(id){
				case 6:
					printf("Ha seleccionat %s amb un preu de %i�\n\n",ssd256.nom,ssd256.preu);
					preu += ssd256.preu;
					break;
				case 7:
					printf("Ha seleccionat %s amb un preu de %i�\n\n",ssd512.nom,ssd512.preu);
					preu += ssd512.preu;
					break;
				case 8:
					printf("Ha seleccionat %s amb un preu de %i�\n\n",ssd1.nom,ssd1.preu);
					preu += ssd1.preu;
					break;
			}
	}
}

int main(){
	int id, iva;
	
	preu = 0;
	
	printf("Benvingut a Pera!\n\n");
	
	printf("Aquest son els processadors que tenim en stock: \n");
	printf("%s %i� -> ID del producte: %i\n",i5.nom,i5.preu,i5.id);
	printf("%s %i� -> ID del producte: %i\n",i7.nom,i7.preu,i7.id);
	printf("%s %i� -> ID del producte: %i\n\n",i9.nom,i9.preu,i9.id);
	printf("Indica quin processador vols introduint el seu ID: "); scanf("%i", &id);
	seleccio(1,id);
	
	printf("Aquestes son les memories RAM que tenim en stock: \n");
	printf("%s %i� -> ID del producte: %i\n",ram8.nom,ram8.preu,ram8.id);
	printf("%s %i� -> ID del producte: %i\n\n",ram16.nom,ram16.preu,ram16.id);
	printf("Indica quin processador vols introduint el seu ID: "); scanf("%i", &id);
	seleccio(2,id);
	
	printf("Aquests son els discs durs que tenim en stock: \n");
	printf("%s %i� -> ID del producte: %i\n",ssd256.nom,ssd256.preu,ssd256.id);
	printf("%s %i� -> ID del producte: %i\n",ssd512.nom,ssd512.preu,ssd512.id);
	printf("%s %i� -> ID del producte: %i\n\n",ssd1.nom,ssd1.preu,ssd1.id);
	printf("Indica quin processador vols introduint el seu ID: "); scanf("%i", &id);
	seleccio(3,id);
	
	printf("Preu: %i\n", preu);
	iva = (16*preu/100);
	printf("IVA: %i\n\n", iva);
	preu += iva;
	
	printf("El preu final del ordinador amb IVA inclos: %i�\n\n", preu);
	
	system("pause");
	return 0;
}
