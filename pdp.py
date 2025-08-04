

cookies = {
    'cookieyes-consent': 'consentid:Y0hzWVlmcmFxNE9uNWJJZVk0T241S0NFTUNKa1NhVEo,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
    '_gid': 'GA1.2.8147850.1753697235',
    '_gcl_au': '1.1.1737589649.1753697235',
    'CMSPreferredCulture': 'en-CA',
    'CMSCsrfCookie': 'W8EKgiEb9v6wv4gp5UqUNvD19iNHDb8R+ymRvJyw',
    'ASP.NET_SessionId': 'qxwin2mscu4k4a3kbp4xyj13',
    'CMSCurrentTheme': 'BB_Product_Listing',
    'language': 'en',
    'location': '5',
    'bbregion_language': 'lang=en&prov=Washington',
    'favorites': '',
    'default_store': '',
    'default_store_data': '',
    'VisitorStatus': '11064821345',
    'CMSUserPage': '{"TimeStamp":"2025-07-28T06:25:19.0373628-04:00","LastPageDocumentID":43848,"LastPageNodeID":23487,"Identifier":"a758274d-2ca5-4c0f-9832-b410f870ae69"}',
    'CMSLandingPageLoaded': 'true',
    '_ga': 'GA1.1.1798724763.1753691173',
    '_ga_C3MZ3X6NZ6': 'GS2.1.s1753697213$o3$g1$t1753698323$j60$l0$h0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.bulkbarn.ca/ecomm/product_search.html',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'cookieyes-consent=consentid:Y0hzWVlmcmFxNE9uNWJJZVk0T241S0NFTUNKa1NhVEo,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _gid=GA1.2.8147850.1753697235; _gcl_au=1.1.1737589649.1753697235; CMSPreferredCulture=en-CA; CMSCsrfCookie=W8EKgiEb9v6wv4gp5UqUNvD19iNHDb8R+ymRvJyw; ASP.NET_SessionId=qxwin2mscu4k4a3kbp4xyj13; CMSCurrentTheme=BB_Product_Listing; language=en; location=5; bbregion_language=lang=en&prov=Washington; favorites=; default_store=; default_store_data=; VisitorStatus=11064821345; CMSUserPage={"TimeStamp":"2025-07-28T06:25:19.0373628-04:00","LastPageDocumentID":43848,"LastPageNodeID":23487,"Identifier":"a758274d-2ca5-4c0f-9832-b410f870ae69"}; CMSLandingPageLoaded=true; _ga=GA1.1.1798724763.1753691173; _ga_C3MZ3X6NZ6=GS2.1.s1753697213$o3$g1$t1753698323$j60$l0$h0',
}


import requests
from parsel import Selector


response = requests.get(
    'https://www.bulkbarn.ca/en/Products/All/Mixed-Nuts-with-Peanuts-Roasted-and-Salted-129',
    cookies=cookies,
    headers=headers,
    verify=False,
)

# print(response.text)

sel = Selector(text=response.text)
# name = sel.xpath('/html/body/form/div[4]/div[3]/section/section/section[2]/div[1]/h2/text()').get('N/A')
name = sel.xpath('/html/body/form/div[4]/div[3]/section/section/section[2]/div/div[1]/h2/text()').get('N/A')
nf = sel.xpath('/html/body/form/div[4]/div[3]/section/section/section[2]/div/div[2]/div[2]/div[2]/div/p[2]/text()').get('N/A')
# nf = sel.xpath('/html/body/form/div[4]/div[3]/section/section/section[2]/div[2]/div[3]/div[2]/div/p[2]/text()').get('N/A')
print(name)
print(nf)
print(response.status_code)
print('\n')





