# Project for real-time Data Capture
# Summer, 2026
# THIS MILESTONE GETS API DATA OFF WEBSITES USING SOCRATA QUERIES


# run this by: (venv)py milestone2.py

# NOTE:
#   The file app.py is part of this milestone!  It is a script that runs in 
#   a website and shows what might cause each of the exceptions
#   Run it by: (venv)> streamlit run app.py     
#      Stop it by: ctrl-c   (Visual Code)


import requests  # Milestone 2

#Milestone 2 URL
#URL = "https://data.kcmo.org/resource/d4px-6rwg.json"
URL = "https://data.kcmo.org/resource/frqd-pm5w.json"
#URL = "https://data.kcmo.org/api/v3/views/frqd-pm5w/query.json"


def main():
    print("RUNNING MILESTONE 2 - Potholes")
    
    print("Building test project")
    data = fetch_311_data(limit=2)
    print(f"Successfully fetched {len(data)} records:")
    print(data[0])

    
def fetch_311_data(limit=10):
    try:
        response = requests.get(URL, params={"$limit": limit,
                "$order": "open_date_time DESC"}, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("⏳ Request timed out — the API may be slow or down.")
    except requests.exceptions.ConnectionError: 
        print("🔌 Connection Error — Check your internet or check for" 
             " a typo in the main URL domain name!")
    except requests.exceptions.HTTPError as e:
        # Happens when valid URL but invalid column name OR
        #   valid beginning of URL but a file that doesn't exist 
        #   added on at the end
        print(f"❌ HTTP error from the server: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❓ Something else went wrong: {e}")
    return []


main()
