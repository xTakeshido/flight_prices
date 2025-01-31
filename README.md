# Flight Price Checker

## Overview

The Flight Price Checker is a Streamlit-based web application that allows users to check flight prices for a given route and date using the Booking.com API. The application fetches flight data in USD and converts it to PLN using a fixed exchange rate.

## Features

- **Flight Price Search**: Users can enter their origin and destination airport codes, departure date, and the number of adults and kids to check flight prices.
- **Currency Conversion**: The application converts flight prices from USD to PLN using a fixed exchange rate.
- **User-Friendly Interface**: The interface is built using Streamlit, making it easy to use and navigate.

## Requirements

To run this project, you need the following:

- Python 3.7 or higher
- Streamlit
- Requests library
- Booking.com API credentials (API key and host - You can sub for free on RapidApi)

1. **Install dependencies by running**:
    ```bash
    pip install -r requirements.txt
    ```
## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/flight-price-checker.git
   cd flight-price-checker