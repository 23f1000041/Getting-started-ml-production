# Iris Flower Classifier API

This API predicts the species of an Iris flower based on its measurements.

## What it predicts
Given 4 measurements of an Iris flower, it returns one of three species:
- 0 = setosa
- 1 = versicolor
- 2 = virginica

## Example request for /predict
```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

## How to run locally
```bash
python train.py
uvicorn main:app --reload
```
Then open http://127.0.0.1:8000
