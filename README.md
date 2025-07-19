# Cosmos-Mongodb-Compass
# Gestor de Tasques amb FastAPI + Azure Cosmos DB (MongoDB vCore)

Aquesta és una aplicació web senzilla que et permet afegir i eliminar tasques (to-do) mitjançant un frontend HTML + JavaScript i backend amb FastAPI. Les dades es guarden en una base de dades **Azure Cosmos DB for MongoDB (vCore)**.

---

## Funcionalitats

-  Veure totes les tasques
-  Afegir una nova tasca
-  Esborrar una tasca
-  Connexió a Cosmos DB for MongoDB

---

##  Estructura del projecte
```
app/
│
├── main.py # Backend FastAPI
├── templates/
│ └── index.html # Frontend HTML + JS
├── static/ # (opcional) per JS o CSS futurs
├── requirements.txt # Llista de dependències
├── Dockerfile # Per crear la imatge Docker
├── .env # Credencials de MongoDB
```

---

##  Configuració

Crea un fitxer `.env` a l'arrel amb aquest contingut:

```env
MONGO_URI=mongodb+srv://<usuari>:<password>@prova01.mongocluster.cosmos.azure.com/?retrywrites=true&w=majority
```
## Com executar amb Docker
Construir la imatge:

``` docker build -t cosmos-todo . ```

Executar el contenidor:

``` docker run -p 8000:8000 --env-file .env cosmos-todo ```

Obrir en navegador:

http://localhost:8000

## MongoDB Compass 
https://www.mongodb.com/try/download/compass


