def generate_meta_tags_description(top_related_topics):
    prompt = f"""Generate Meta Tags Description using Trending Keywords and Semantic Keywords:
    ...
    Your website's meta tags description is crucial for search engine optimization and attracting users to your page.
    ...
    Trending Keywords: {', '.join(top_related_topics)}
    ...
    Use these keywords strategically to create a compelling and relevant meta tags description for that encourages users to visit your website and boosts your search engine ranking.
    """
    return prompt

def generate_page_title(top_related_topics):
    prompt = f"""Generate a Page Title using Trending Keywords and Semantic Keywords:
    ...
    Your page title should be concise, engaging, and accurately represent the content of your page.
    ...
    Trending Keywords: {', '.join(top_related_topics)}
    ...
    Use these keywords strategically to craft a page title that effectively communicates the essence of your content and entices users to visit your page.
    """
    return prompt

def generate_blog_topic(top_related_topics):
    prompt = f"""Generate a Blog Topic using Trending Keywords and Semantic Keywords:
    ...
    Your blog topic should be informative, relevant, and engaging.
    ...
    Trending Keywords: {', '.join(top_related_topics)}
    ...
    Use these keywords strategically to craft a blog topic that effectively addresses your target audience's interests and captures their attention.
    """
    return prompt

def generate_content(top_related_topics):
    prompt = f"""Generate Content using Trending Keywords and Semantic Keywords:
    ...
    Your content should incorporate both trending keywords and semantic keywords to optimize it for search engines and attract more readers.
    ...
    Trending Keywords: {', '.join(top_related_topics)}
    ...
    Write an article, blog post, or any content for that discusses your topic comprehensively and engages your audience throughout the reading experience.
    """
    return prompt

