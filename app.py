from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Mocked country data with currencies
COUNTRIES = [
    {"name": "USA", "currency": "USD"},
    {"name": "UK", "currency": "GBP"},
    {"name": "Saudi Arabia", "currency": "SAR"}
]

def get_gold_price(currency="USD"):
    """Fetch current gold price in the specified currency."""
    # Replace with your actual API key
    API_KEY = "goldapi-3rc0l5sm47ggbg6-io"
    API_URL = f"https://www.goldapi.io/api/XAU/{currency}"

    headers = {
        "x-access-token": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("price", None)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching gold price: {e}")
        return None

@app.route('/countries', methods=['GET'])
def get_countries():
    """Return the list of supported countries."""
    return jsonify(COUNTRIES)

@app.route('/calculate', methods=['POST'])
def calculate_zakah():
    """Calculate Zakah based on wealth and gold price."""
    data = request.json

    try:
        # Extract data from the request
        country = data.get("country")
        money = float(data.get("money", 0))
        gold_grams = float(data.get("gold_grams", 0))
        silver_grams = float(data.get("silver_grams", 0))

        # Find the selected country's currency
        selected_country = next((c for c in COUNTRIES if c["name"] == country), None)
        if not selected_country:
            return jsonify({"error": "Country not supported."}), 400

        currency = selected_country["currency"]

        # Get current gold price in the country's currency
        gold_price_per_gram = get_gold_price(currency)
        if gold_price_per_gram is None:
            return jsonify({"error": "Unable to fetch gold price."}), 500

        # Calculate the value of gold in money
        gold_value = gold_grams * gold_price_per_gram

        # Calculate Nisab threshold (85 grams of gold equivalent)
        nisab = gold_price_per_gram * 85

        # Total wealth including money and gold
        total_wealth = money + gold_value

        # Calculate Zakah
        if total_wealth >= nisab:
            zakah = total_wealth * 0.025
            return jsonify({
                "total_wealth": total_wealth,
                "nisab": nisab,
                "zakah_due": zakah,
                "currency": currency
            })
        else:
            return jsonify({
                "total_wealth": total_wealth,
                "nisab": nisab,
                "zakah_due": 0,
                "currency": currency,
                "message": "Your wealth does not meet the Nisab threshold."
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
