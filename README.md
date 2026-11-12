# cursor-pagination-closure

## Français

Détecter pages manquantes et boucles de curseurs.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m cursor_pagination_closure examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Détecter pages manquantes et boucles de curseurs : calcul déterministe sur entrées structurées, témoins et cas limites explicites.

### Limites

Modèle borné, données fictives, aucun service ou matériel de production validé. Méthodes classiques ; aucune supériorité SOTA générale ni adoption humaine démontrée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Detect missing pages and cursor loops.

Synthetic data; no network access or secret required.

```sh
python -m cursor_pagination_closure examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Detect missing pages and cursor loops: deterministic computation over structured inputs, explicit witnesses and boundary cases.

### Limits

Bounded model and synthetic data; no production service or hardware validated. Classical methods; no general SOTA superiority or human adoption demonstrated.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Detectar páginas ausentes y bucles de cursor.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m cursor_pagination_closure examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Detectar páginas ausentes y bucles de cursor: cálculo determinista con entradas estructuradas, testigos y casos límite explícitos.

### Límites

Modelo acotado y datos ficticios; ningún servicio ni hardware de producción validado. Métodos clásicos; sin superioridad SOTA general ni adopción humana demostrada.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/modelcontextprotocol/python-sdk/issues/3843
- https://github.com/modelcontextprotocol/python-sdk/issues/3792
- https://modelcontextprotocol.io/specification/2025-06-18/basic

## Projets voisins / Neighboring projects / Proyectos vecinos

FR : [jsonrpc-notification-fence](https://github.com/gbesse/jsonrpc-notification-fence) est un autre diagnostic du portefeuille. Ici : Détecter pages manquantes et boucles de curseurs. Comparaison de périmètres seulement, sans affiliation ni benchmark de supériorité.

EN: [jsonrpc-notification-fence](https://github.com/gbesse/jsonrpc-notification-fence) is a different portfolio diagnostic. Here: Detect missing pages and cursor loops. Scope comparison only, no affiliation or superiority benchmark.

ES: [jsonrpc-notification-fence](https://github.com/gbesse/jsonrpc-notification-fence) es otro diagnóstico del portafolio. Aquí: Detectar páginas ausentes y bucles de cursor. Comparación de alcance, sin afiliación ni benchmark de superioridad.
