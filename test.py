"""flow = InstalledAppFlow.from_client_config(
    {'installed': {
        'client_id': '705715906838-insohcqkve5kbih25cloha6s3024jsu1.apps.googleusercontent.com',
        'client_secret': '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',
        'redirect_uris': ["http://localhost:8000","http://localhost:8000/"],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token'
    }},
    scopes=['https://www.googleapis.com/auth/adwords']
)

creds = flow.run_local_server(port=8000)
with open('google-ads.yaml', 'w') as token:
    token.write(creds.to_json())




#GOOGLE ADS CREDENTIALS

#Developer Token : aP1k8UnaA-_RqYo_MT4Icw
#Client ID : 794-214-4382
#client_id: 538109185685-h8nqtlqsec315c5vp2gde4n3v04o1btd.apps.googleusercontent.com
#client_secret: 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

# import google.auth
# from google.auth.transport.requests import Request
# from google.ads.googleads.client import GoogleAdsClient


# # Replace these placeholders with your own values
# CLIENT_ID = "7942144382"
# CLIENT_SECRET = "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"
# DEVELOPER_TOKEN = "aP1k8UnaA-_RqYo_MT4Icw"
# LOGIN_CUSTOMER_ID = "7942144382"  # Typically your Google Ads account number

# def authenticate_with_service_account():
#     # Load credentials from the JSON key file you downloaded
#     credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/adwords"])

#     # Create a Google Ads API client
#     client = GoogleAdsClient(credentials=credentials, developer_token=DEVELOPER_TOKEN)
#     return client

# def main():
#     client = authenticate_with_service_account()

#     keyword_ideas_query = """
#         SELECT keyword_plan_idea.keyword_text
#         FROM keyword_plan_idea
#         WHERE keyword_plan_network = 'GOOGLE_SEARCH'
#         AND language = 'en'
#         AND country = 'US'
#         AND competition > 0.1
#         AND avg_monthly_searches > 100
#         AND keyword_plan_idea.type = 'KEYWORD'
#         LIMIT 10
#     """

#     # Issue the query to retrieve keyword ideas
#     response = client.service.google_ads.search(query=keyword_ideas_query, customer_id=LOGIN_CUSTOMER_ID)

#     for row in response:
#         keyword_text = row.keyword_plan_idea.keyword_text.value
#         print(f"Keyword Idea: {keyword_text}")

# if __name__ == "__main__":
#     main()
