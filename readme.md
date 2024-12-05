# Zakah Calculation Flask App

This Flask application calculates Zakah (an Islamic obligatory charity) based on the user's wealth and the current gold price in their country's currency. The app provides APIs for retrieving supported countries and calculating Zakah.

## Features

- **Supported Countries API**: Retrieve a list of countries and their currencies.
- **Zakah Calculation API**: Calculate Zakah based on the provided wealth and gold price in the selected country's currency.
- **Gold Price API Integration**: Fetch live gold prices using [GoldAPI](https://www.goldapi.io/).

## Endpoints

### 1. `/countries` (GET)
**Description**: Retrieve a list of supported countries and their currencies.

#### Response Example:
```json
[
    {"name": "USA", "currency": "USD"},
    {"name": "UK", "currency": "GBP"},
    {"name": "Saudi Arabia", "currency": "SAR"}
]
```

### 2. `/calculate` (POST)
**Description**: Calculate Zakah based on the provided wealth, gold, and selected country.

#### Request Body:
```json
{
    "country": "USA",
    "money": 10000,
    "gold_grams": 10,
    "silver_grams": 0
}
```

#### Response Example (If Nisab is met):
```json
{
    "total_wealth": 15000,
    "nisab": 7000,
    "zakah_due": 375,
    "currency": "USD"
}
```

#### Response Example (If Nisab is not met):
```json
{
    "total_wealth": 5000,
    "nisab": 7000,
    "zakah_due": 0,
    "currency": "USD",
    "message": "Your wealth does not meet the Nisab threshold."
}
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/zakah-calculator.git
   cd zakah-calculator
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up GoldAPI Key**:
   Replace `API_KEY` in the code with your GoldAPI key.

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Requirements

All dependencies are listed in `requirements.txt`. Use the following command to install them:
```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

