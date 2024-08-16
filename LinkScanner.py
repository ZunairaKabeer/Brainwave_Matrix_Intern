import tldextract
import Levenshtein as lv

trusted_domains = ['amazon.com', 'microsoft.com', 'twitter.com']

urls_to_evaluate = [
    'http://amazon.co',
    'http://microsoft.com',
    'https://www.microsoft-security.com',
    'https://twitter.com/home',
    'https://www.twittter.com',  
]

def parse_domain_components(url):
    domain_parts = tldextract.extract(url)
    return domain_parts.subdomain, domain_parts.domain, domain_parts.suffix

def check_domain_spelling(domain, trusted_domains, min_similarity=0.9):
    for trusted_domain in trusted_domains:
        similarity_index = lv.ratio(domain, trusted_domain)
        if similarity_index >= min_similarity:
            return True  
    return False  

def evaluate_url(url, trusted_domains):
    subdomain, domain, suffix = parse_domain_components(url)

    if f"{domain}.{suffix}" in trusted_domains:
        return f"The URL is verified as safe: {url}"

    if check_domain_spelling(domain, trusted_domains):
        return f"Alert: Potential phishing (misspelled domain): {url}"

    return f"The URL is not trusted: {url}"

if __name__ == '__main__':
    for url in urls_to_evaluate:
        print(evaluate_url(url, trusted_domains))
