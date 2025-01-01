#!/bin/sh

echo "Running Streamlit app"
streamlit run /app/apptrackr/main.py --server.port=$PORT --server.address=0.0.0.0