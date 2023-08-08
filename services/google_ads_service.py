'''from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException


client = GoogleAdsClient.load_from_storage("google-ads.yaml")


def get_trending_keywords(website_category):
    # Create a query to get trending keywords for today
    query = (
        "SELECT keyword.text, keyword.search_volume "
        "FROM keyword "
        "JOIN keyword_category ON keyword.id = keyword_category.keyword "
        "JOIN category ON keyword_category.category = category.id "
        "WHERE category.name = @website_category "
        "AND keyword.search_volume >= 1000 "
        "AND keyword.date_range.start_date = CURRENT_DATE "
        "ORDER BY keyword.search_volume ASC "
        "LIMIT 10"
    )

    # Execute the query and retrieve trending keywords
    response = client.service.google_ads.search(query=query, website_category=website_category)
    keywords = [row["keyword"]["text"]["value"] for row in response]
    return keywords


# Get Semantic keywords using Google Ads API
def get_semantic_keywords(website_category):
    # Create a query to get semantic keywords
    query = (
        "SELECT keyword.text "
        "FROM keyword "
        "JOIN keyword_category ON keyword.id = keyword_category.keyword "
        "JOIN category ON keyword_category.category = category.id "
        "WHERE category.name = @website_category "
        "ORDER BY keyword.text ASC "  # Order by keyword text in ascending order
        "LIMIT 10"
    )

    # Execute the query and retrieve semantic keywords
    response = client.service.google_ads.search(query=query, website_category=website_category)
    keywords = [row["keyword"]["text"]["value"] for row in response]
    return keywords
'''