import pandas as pd
import os

# Create a DataFrame for the template
data = {
    "District": ["Kampala", "Wakiso", "Mbarara", "Gulu", "Jinja", "Arua", "Lira", "Fort Portal", "Masaka", "Mbale",
                 "Soroti", "Hoima", "Luwero", "Kabale", "Mubende", "Tororo", "Bushenyi", "Ntungamo", "Kasese", "Mukono",
                 "Iganga", "Masindi", "Rakai", "Kabarole", "Nakasongola", "Kibaale", "Moroto", "Kanungu", "Kapchorwa", "Nebbi"],
    "Financial Institution": ["Bank of Uganda", "Centenary Bank", "PostBank Uganda", "Pride Microfinance", "Opportunity Bank",
                              "Stanbic Bank Uganda", "Finance Trust Bank", "DFCU Bank", "Housing Finance Bank", "Equity Bank Uganda",
                              "BRAC Uganda", "UGAFODE Microfinance", "UMRA", "Pride Microfinance", "Centenary Bank", "PostBank Uganda",
                              "Opportunity Bank", "Stanbic Bank Uganda", "Finance Trust Bank", "DFCU Bank", "Housing Finance Bank",
                              "Equity Bank Uganda", "BRAC Uganda", "UGAFODE Microfinance", "UMRA", "Pride Microfinance", "Centenary Bank",
                              "PostBank Uganda", "Opportunity Bank", "Stanbic Bank Uganda"],
    "Type of Assistance": ["Loans", "Agricultural Loans", "Livestock Financing", "Small Business Loans", "Agricultural Loans",
                           "Livestock Loans", "Agricultural Financing", "Agricultural Credit", "Rural Development Loans", "Agribusiness Loans",
                           "Smallholder Farmer Loans", "Agricultural Loans", "Microcredit", "Small Business Loans", "Agricultural Loans",
                           "Livestock Financing", "Agricultural Loans", "Livestock Loans", "Agricultural Financing", "Agricultural Credit",
                           "Rural Development Loans", "Agribusiness Loans", "Smallholder Farmer Loans", "Agricultural Loans", "Microcredit",
                           "Small Business Loans", "Agricultural Loans", "Livestock Financing", "Agricultural Loans", "Livestock Loans"],
    "Contact Email": ["info@bog.ug", "info@centenarybank.co.ug", "info@postbank.co.ug", "info@pridemicrofinance.co.ug", "info@opportunitybank.co.ug",
                      "info@stanbicbank.co.ug", "info@financetrust.co.ug", "info@dfcubank.co.ug", "info@housingfinance.co.ug", "info@equitybank.co.ug",
                      "info@brac.net", "info@ugafode.co.ug", "info@umra.go.ug", "info@pridemicrofinance.co.ug", "info@centenarybank.co.ug", "info@postbank.co.ug",
                      "info@opportunitybank.co.ug", "info@stanbicbank.co.ug", "info@financetrust.co.ug", "info@dfcubank.co.ug", "info@housingfinance.co.ug",
                      "info@equitybank.co.ug", "info@brac.net", "info@ugafode.co.ug", "info@umra.go.ug", "info@pridemicrofinance.co.ug", "info@centenarybank.co.ug",
                      "info@postbank.co.ug", "info@opportunitybank.co.ug", "info@stanbicbank.co.ug"],
    "Telephone Number": ["+256 414 258 441", "+256 414 251 276", "+256 414 236 789", "+256 414 231 200", "+256 414 320 300",
                         "+256 414 232 004", "+256 414 341 275", "+256 312 300 200", "+256 414 236 120", "+256 414 223 276",
                         "+256 414 232 158", "+256 414 345 568", "+256 414 251 463", "+256 414 231 200", "+256 414 251 276",
                         "+256 414 236 789", "+256 414 320 300", "+256 414 232 004", "+256 414 341 275", "+256 312 300 200",
                         "+256 414 236 120", "+256 414 223 276", "+256 414 232 158", "+256 414 345 568", "+256 414 251 463",
                         "+256 414 231 200", "+256 414 251 276", "+256 414 236 789", "+256 414 320 300", "+256 414 232 004"]
}

df = pd.DataFrame(data)

# Relative path to the desired location
csv_path = "uganda_cattle_farmers_financial_assistance.csv"

# Save to a Google Sheet compatible format (CSV)
try:
    df.to_csv(csv_path, index=False)
    print(f"File saved successfully at {csv_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Verify the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")