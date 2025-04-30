## 🧠 Classificador de Score de Crédito com Machine Learning
Este projeto utiliza algoritmos de Machine Learning para prever o score de crédito de clientes com base em informações como profissão, mix de crédito e comportamento de pagamento. O modelo é treinado usando algoritmos como Random Forest e KNN, e pode ser utilizado para prever o score de novos clientes.

## 📁 Arquivos

clientes.csv: Base de dados com clientes existentes, usada para treinar os modelos.

novos_clientes.csv: Base com dados de novos clientes para previsão.

main.py: Script principal contendo todo o processo de pré-processamento, treinamento e previsão.

---

## 🖥️ Requisitos

Antes de começar, você precisa ter instalado:

- [Python](https://www.python.org) 
- [Git](https://git-scm.com/) (opcional, para clonar o repositório)
- [Pandas](https://pandas.pydata.org/) 
- [Scikit-learn](https://scikit-learn.org/stable/)

---

## ⚙️ Como Executar:

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```


Ou baixe o ZIP e extraia.

---

### 2. Instale as dependências

Abra o terminal (PowerShell ou CMD) dentro da pasta do projeto e execute:

```bash
pip install pandas scikit-learn
```
---

Coloque os arquivos clientes.csv e novos_clientes.csv na mesma pasta do script.

---

### 3. Execute o script

```bash
python main.py
```

## 🔍 O que o código faz
Lê os dados dos clientes.

Codifica variáveis categóricas com LabelEncoder.

Separa os dados em treino e teste.

Treina dois modelos: RandomForestClassifier e KNeighborsClassifier.

Compara a acurácia dos modelos.

Aplica o modelo de melhor desempenho a novos dados.

## 📊 Resultados
O código exibe a acurácia dos dois modelos e mostra as previsões feitas para os novos clientes.

## 📄 Licença
Este projeto está sob a licença MIT.

## 🌐 Redes Sociais

- [Instagram](https://www.instagram.com/joaorbrn/)
- [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-vitor-santos-ab582921b/)

---

Feito com 💚 por João Vitor
