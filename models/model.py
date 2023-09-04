from pydantic import BaseModel

#Create Model to get website category
class WebsiteCategory(BaseModel):
    website_category: str
    website_url: str
    content_type: str