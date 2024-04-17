from urllib.request import urlopen

url = "https://www.todays-golfer.com/equipment/witb/witb---rory-mcilroy-/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

start_idx = html.find('<h2 class="product-card_title_content"') + \
    len('<h2 class="product-card_title_content"')
end_idx = html.find('</h2>')
driver = html[start_idx:end_idx]
print(driver)
