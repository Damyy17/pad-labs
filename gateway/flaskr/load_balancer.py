import requests

# load_balancer
CMA_SERVICE_URLS = ["http://cma:3010", "http://cma2:3011", "http://cma3:3012"]
CR_SERVICE_URLS = ["http://cr:4000", "http://cr2:4001", "http://cr3:4002"]

def round_robin(iterable):
    while True:
        for item in iterable:
            yield item

cma_url_generator = round_robin(CMA_SERVICE_URLS)
cr_url_generator = round_robin(CR_SERVICE_URLS)


# re-routing function if microservice fails
MAX_RETRIES = 3  # maximum number of retries before rerouting
def get_healthy_cma_url(url_generator, retries=0):
    try:
        url = next(url_generator)
        response = requests.get(f'{url}/status')
        response.raise_for_status()
        return url
    except requests.exceptions.RequestException as e:
        if retries < MAX_RETRIES:
            # Retry with the next available URL
            return get_healthy_cma_url(url_generator, retries=retries + 1)
        else:
            raise ValueError(f"All retries failed. No healthy server found. Error: {str(e)}")
        
def get_healthy_cr_url(url_generator, retries=0):
    try:
        url = next(url_generator)
        response = requests.get(f'{url}/status')
        response.raise_for_status()
        return url
    except requests.exceptions.RequestException as e:
        if retries < MAX_RETRIES:
            # Retry with the next available URL
            return get_healthy_cr_url(url_generator, retries=retries + 1)
        else:
            raise ValueError(f"All retries failed. No healthy server found. Error: {str(e)}")
