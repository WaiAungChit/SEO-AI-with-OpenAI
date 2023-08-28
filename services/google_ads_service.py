from pytrends.request import TrendReq
from google.ads.googleads.client import GoogleAdsClient
import models.model  

def generate_keyword_ideas(website_category):
    pytrends = TrendReq(hl='en-US', tz=420)
    print("Trend",pytrends)
    # Build payload for Google Trends
    pytrends.build_payload([website_category], cat=0, timeframe='now 1-d', geo='TH', gprop='')
    trend = pytrends.related_topics()
    if website_category in trend:
        related_topics = trend[website_category]['top']
        top_related_topics = list(related_topics['topic_title'][:5])
        return top_related_topics

''' client = GoogleAdsClient.load_from_storage("google-ads.yaml")
    keyword_ideas = []
    
    if not (top_related_topics or page_url):
        raise ValueError(
            "At least one of keywords or page URL is required, "
            "but neither was specified."
        )
    
    keyword_plan_idea_service = client.get_service("KeywordPlanIdeaService")
    keyword_competition_level_enum = client.enums.KeywordPlanCompetitionLevelEnum
    keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH_AND_PARTNERS

    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.keyword_plan_network = keyword_plan_network
    
    if not top_related_topics and page_url:
        request.url_seed.url = page_url
    
    if top_related_topics and page_url:
        request.keyword_and_url_seed.url = page_url
        request.keyword_and_url_seed.keywords.extend(top_related_topics)
    keyword_ideas = keyword_plan_idea_service.generate_keyword_ideas(request=request)
    keyword_list = [idea.text for idea in keyword_ideas]
    return keyword_list'''