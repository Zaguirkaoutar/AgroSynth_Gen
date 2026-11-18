# AgroSynth Gen
**Synthèse de symptômes végétaux par StyleGAN2-ADA**

Projet d'IA générative visuelle pour générer des images synthétiques de feuilles de tomates malades et mesurer leur utilité pour la classification.

## Structure
- `configs/` : paramètres des expériences.
- `data/` : données brutes, intermédiaires, partitions et métadonnées.
- `notebooks/` : exploration et expérimentations.
- `src/` : code Python organisé par responsabilité.
- `scripts/` : points d'entrée pour préparer, entraîner, générer et évaluer.
- `outputs/` : images générées, checkpoints, métriques et figures.
- `reports/` : rapport scientifique et résultats.
- `docs/` : documentation et Data Card.

## Démarrage
1. Créer un environnement virtuel.
2. Installer les dépendances depuis `requirements.txt`.
3. Télécharger PlantVillage et placer les données dans `data/raw/plantvillage/`.
4. Préparer les partitions avec `scripts/prepare_data.py`.
5. Configurer les expériences dans `configs/`.
6. Exécuter les scripts d'entraînement et d'évaluation.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
pip install -r requirements.txt
```

## Expériences
- **A** : StyleGAN2-ADA conditionnel de référence.
- **B** : A + cohérence de classe via un classifieur auxiliaire gelé.
- **C** : B + filtrage par confiance et distance au plus proche voisin.

## Règles expérimentales
- Le générateur et le classifieur auxiliaire utilisent uniquement les données `train`.
- Les seuils de filtrage sont déterminés sur `val`.
- Le jeu `test` reste réservé à l'évaluation finale.
- PlantDoc est externe : évaluation uniquement, sans entraînement ni adaptation.
- Comparer les trois conditions de classification avec le même protocole et au moins trois graines aléatoires.

## Données
Ne pas versionner les images ni les poids volumineux dans Git. Consulter `docs/DATA_CARD_TEMPLATE.md` et respecter les licences des datasets.
