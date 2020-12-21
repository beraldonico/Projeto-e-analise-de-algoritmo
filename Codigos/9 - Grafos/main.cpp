/*
	Projeto e Análise de Algoritmos - Caminho Mínimo
	Equipe: Eriel Bernardo Albino, Lucas Fernandes Gauer e Nicolas Beraldo
	Data: Junho de 2019
*/

#include <iostream>
#include <iomanip>

#define N 10 // tamanho base das matrizes utilizadas

float min(float um, float dois);
void print(float (*matriz)[N]);
void copiar(float (*origem)[N], float (*destino)[N]);
void defineArcosInuteis(float (*original)[N], float (*final)[N]);

int main(int argc, char const *argv[]){
	if(argc < 2){
		std::cout << "Erro! Execução deve ser <exec> <N>" << std::endl;
		return -1;
	}

	int modo = atoi(argv[1]);
	if(modo < 1 || modo > 2){
		std::cout << "Erro! Segundo argumento deve ser 1 para o problema original ou 2 para o problema proposto" << std::endl;
		return -1;
	}

	float Z = __INT_MAX__; // infinito
	float anterior[N][N], atual[N][N];
	// matriz do problema 1
	float original[N][N] = {
	  //{0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
		{0, 5, Z, 5, 9, Z, Z, Z, Z, Z }, // 0
		{5, 0, 4, 4, 9, 3, Z, Z, Z, Z }, // 1
		{Z, 4, 0, Z, Z, 2, Z, Z, Z, Z }, // 2
		{5, 4, Z, 0, 3, Z, 5, 6, Z, Z }, // 3
		{9, 9, Z, 3, 0, Z, 9, 4, Z, Z }, // 4
		{Z, 3, 2, Z, Z, 0, Z, 7, 1, Z }, // 5
		{Z, Z, Z, 5, 9, Z, 0, 6, Z, 10}, // 6
		{Z, Z, Z, 6, 4, 7, 6, 0, 2, 3 }, // 7
		{Z, Z, Z, Z, Z, 1, Z, 2, 0, Z }, // 8
		{Z, Z, Z, Z, Z, Z, 10,3, Z, 0 }  // 9
	};

	// matrizes no problema 2
	float m_Vel[N][N]={
	  //{A,   B,   C,   D,   E,   F,   G,   H,   I,   J }
		{0,   20,  35,  0,   0,   0,   200, 0,   0,   0 }, //A
		{20,  0,   0,   0,   5,   100, 0,   0,   0,   0 }, //B
		{35,  0,   0,   120, 0,   0,   60,  53,  0,   0 }, //C
		{0,   0,   120, 0,   60,  0,   0,   73,  200, 0 }, //D
		{0,   5,   0,   60,  0,   0,   0,   0,   0,   40}, //E
		{0,   100, 0,   0,   0,   0,   0,   0,   37,  75}, //F
		{200, 0,   60,  0,   0,   0,   0,   15,  0,   0 }, //G
		{0,   0,   53,  73,  0,   0,   15,  0,   10,  0 }, //H
		{0,   0,   0,   200, 0,   37,  0,   10,  0,   90}, //I
		{0,   0,   0,   0,   40,  75,  0,   0,   90,  0 }  //J
	};

	float m_Dist[N][N]={
	  //{A,   B,   C,   D,   E,   F,   G,   H,   I,   J  }
		{0,   60,  20,  0,   0,   0,   90,  0,   0,   0  }, //A
		{60,  0,   0,   0,   10,  40,  0,   0,   0,   0  }, //B
		{20,  0,   0,   300, 0,   0,   95,  113, 0,   0  }, //C
		{0,   0,   300, 0,   20,  0,   0,   62,  100, 0  }, //D
		{0,   10,  0,   20,  0,   0,   0,   0,   0,   15 }, //E
		{0,   40,  0,   0,   0,   0,   0,   0,   69,  150}, //F
		{90,  0,   95,  0,   0,   0,   0,   25,  0,   0  }, //G
		{0,   0,   113, 62,  0,   0,   25,  0,   60,  0  }, //H
		{0,   0,   0,   100, 0,   69,  0,   60,  0,   460}, //I
		{0,   0,   0,   0,   15,  150, 0,   0,   460, 0  }  //J
	};

	// Definição da matriz de custos do problema 2
	if(modo == 2){
		for(int i = 0; i < N; ++i) {
			for(int j = 0; j < N; ++j) {
				if(i == j) 
					original[i][j] = 0;
				else if(m_Vel[i][j] == 0)
					original[i][j] = Z;
				else
					original[i][j] = m_Dist[i][j] / m_Vel[i][j];
			}
		}
	}

	copiar(original, atual);
	print(atual);

	// Algoritmo de Floyd
	for(int k = 0; k < N; ++k){

		copiar(atual, anterior);

		for(int i = 0; i < N; ++i){
			if(i == k) continue;
			if(anterior[i][k] == Z) continue;

			for(int j = 0; j < N; ++j){
				if(j == k) continue;
				if(anterior[k][j] == Z) continue;
				
				atual[i][j] = min(anterior[i][j], anterior[i][k] + anterior[k][j]);

			}
		}
	}

	print(atual);

	defineArcosInuteis(original, atual);

	return 0;
}

float min(float um, float dois){
	if(um < dois) return um;
	else return dois;
}

void print(float (*matriz)[N]){
	std::cout << std::setprecision(2) << std::fixed;
	std::cout << std::endl;
	for(unsigned i = 0; i < N; i++){
		for(unsigned j = 0; j < N; j++){
			if(matriz[i][j] == __INT_MAX__) std::cout << "i\t";
			else std::cout << matriz[i][j] << "\t";
		}
		std::cout << std::endl;
	}
}

void copiar(float (*origem)[N], float (*destino)[N]){
	for(unsigned i = 0; i < N; i++){
		for(unsigned j = 0; j < N; j++){
			destino[i][j] = origem[i][j];
		}
	}
}

void defineArcosInuteis(float (*original)[N], float (*final)[N]){
	/*
		Esta função verifica se existe diferença entre os vértices não infinitos na matriz
		original e a matriz final. Caso exista diferença, o arco foi otimizado e logo não
		é útil.
	*/
	for(unsigned i = 0; i < N; i++){
		for(unsigned j = i + 1; j < N; j++){
			if(original[i][j] == __INT_MAX__) continue;
			if(original[i][j] - final[i][j] != 0){
				std::cout << "O arco entre " << i << " e " << j << " não é utilizado. ";
				std::cout << "(" << (char)(i + 'A') << ", " << (char)(j + 'A') << ")" << std::endl;
			}
		}
	}
}
