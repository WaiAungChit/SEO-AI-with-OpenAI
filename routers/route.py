from fastapi import APIRouter, HTTPException
import models.model as category
import services.openai_service as openai_services
import services.google_ads_service as google_ads_services
from utilities.utility import generate_blog_topic, generate_content, generate_meta_tags_description, generate_page_title

# endpoint urls
endpoints = {
    "generate-page-title": generate_page_title,
    "generate-meta-tags-description": generate_meta_tags_description,
    "generate-blog-topic": generate_blog_topic,
    "generate-content": generate_content
}

router = APIRouter()

# Generate data post route
@router.post("/generate-data/{endpoint_path}/")
async def generate_data(endpoint_path: str, data: category.WebsiteCategory):
    print({"params": endpoint_path, "website_category": data.website_category})
    if endpoint_path not in endpoints:
        raise HTTPException(status_code=404, detail="Endpoint not found")

    website_category = data.website_category

    # Generate the list of keywords using the generate_keyword_ideas function
    keyword_list = google_ads_services.generate_keyword_ideas(website_category,page_url=None)

    # Get the corresponding prompt function from the endpoints dictionary
    prompt_func = endpoints[endpoint_path]
    prompt = prompt_func(keyword_list)

    
    # Generate content using the OpenAI API and the selected prompt function
    generated_data = openai_services.generate_data(prompt)
    #
    return {"generated_data": generated_data, "endpoint_path": endpoint_path}
