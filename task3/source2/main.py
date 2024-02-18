from fastapi import FastAPI

app = FastAPI()


@app.get("/fuel-prices")
def get_fuel_prices_data():
    return [
        {
            "id": 1,
            "fuel_prices": [
                {
                    "name": "АИ-95",
                    "price": 100,
                    "currency": "RUB"
                },
                {
                    "name": "АИ-98",
                    "price": 120,
                    "currency": "RUB"
                },
                {
                    "name": "АИ-95+",
                    "price": 110,
                    "currency": "RUB"
                },
            ]
        },
        {
            "id": 4,
            "fuel_prices": [
                {
                    "name": "АИ-95",
                    "price": 200,
                    "currency": "RSD"
                },
                {
                    "name": "АИ-98",
                    "price": 240,
                    "currency": "RSD"
                },
                {
                    "name": "АИ-95+",
                    "price": 220,
                    "currency": "RSD"
                },
            ]
        }
    ]
