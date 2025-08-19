#!/bin/bash
# Run scraper in background every 3 hours
while true; do
  python scraper.py
  sleep 10800 # 3 hours
done &

# Start the Streamlit dashboard
streamlit run dashboard.py --server.port $PORT
