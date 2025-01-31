import streamlit as st
import requests

# Booking.com API credentials
API_KEY = "your-api-key" 
API_HOST = "your-api-host"

# Fixed exchange rate for USD to PLN (replace with a live API if needed)
USD_TO_PLN = 4.0  # Example exchange rate

# Function to convert USD to PLN
def convert_usd_to_pln(usd_amount):
    return usd_amount * USD_TO_PLN

# Function to get flight prices from Booking.com API
def get_flight_prices(origin, destination, departure_date, adults, kids):
    url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST,
    }
    params = {
        "fromId": f"{origin}.AIRPORT",
        "toId": f"{destination}.AIRPORT",
        "departDate": departure_date.strftime("%Y-%m-%d"),
        "adults": adults,
        "kids": kids,
        "currency": "USD",  # Fetch prices in USD
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        st.error("Failed to fetch flight data. Please check your inputs or try again later.")
        return None

    return response.json()

# Streamlit app
def main():
    st.title("✈️ Flight Price Checker")
    st.write("Enter your travel details below to check flight prices.")

    # User inputs
    origin = st.text_input("Enter origin airport code:").strip().upper()
    destination = st.text_input("Enter destination airport code:").strip().upper()

    col1, col2 = st.columns(2)  # Create two columns to make adults and kids inputs appear on one line
    with col1:
        adults = st.text_input("Enter number of adults:").strip().upper()
    with col2:
        kids = st.text_input("Enter number of kids:").strip().upper()

    departure_date = st.date_input("Select departure date:")

    if st.button("Check Flight Prices"):
        if not origin or not destination:
            st.error("Please enter both origin and destination airport codes.")
        else:
            st.write(f"Fetching flight prices from **{origin}** to **{destination}** on **{departure_date}**...")

            # Fetch flight data
            flight_data = get_flight_prices(origin, destination, departure_date, adults, kids)

            if flight_data and "data" in flight_data and "flightOffers" in flight_data["data"]:
                st.write("### Flight Prices")
                for flight in flight_data["data"]["flightOffers"]:
                    airline = flight["segments"][0]["legs"][0]["carriersData"][0]["name"]
                    price_usd = flight["priceBreakdown"]["total"]
                    price_pln = convert_usd_to_pln(price_usd["units"] + price_usd["nanos"] / 1e9)  # Convert USD to PLN
                    st.write(f"**{airline}**: {price_pln:.2f} PLN")
            else:
                st.error("No flight data found. Please check your inputs or try a different date.")

if __name__ == "__main__":
    main()