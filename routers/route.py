from fastapi import APIRouter, HTTPException
import models.model as category
import services.openai_service as openai_services
import services.google_ads_service as google_ads_services
from utilities.utility import generate_blog_topic, generate_content, generate_meta_tags_description, generate_page_title
import firebase_admin
from firebase_admin import credentials, firestore


# Initialize Firebase Admin SDK
cred = credentials.Certificate('cred.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

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
    if endpoint_path not in endpoints:
        raise HTTPException(status_code=404, detail="Endpoint not found")

    website_category = data.website_category
    website_url = data.website_url
    content_type = data.content_type

    # Generate the list of keywords using the generate_keyword_ideas function
    keyword_list = google_ads_services.generate_keyword_ideas(website_category)
    # Get the corresponding prompt function from the endpoints dictionary
    prompt_func = endpoints[endpoint_path]
    prompt = prompt_func(keyword_list)

    
    # Generate content using the OpenAI API and the selected prompt function
    generated_data = openai_services.generate_data(prompt)

    data={
        "website_category": website_category,
        "website_url": website_url,
        "endpoint_path": endpoint_path,
        "generated_data": generated_data,
        "content_type": content_type
    }

    collection_name = "website_data"
    doc_ref = db.collection(collection_name).add(data)

    return {"generated_data": generated_data, "endpoint_path": endpoint_path}
