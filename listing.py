
cookies = {
    'CMSPreferredCulture': 'en-CA',
    'language': 'en',
    'location': '5',
    'bbregion_language': 'lang=en&prov=Washington',
    'favorites': '',
    'default_store': '',
    'default_store_data': '',
    'CMSCsrfCookie': 'fqfsS1qj1eyUyxAob/B8SntL65x4uf8LukJ+xbpp',
    'ASP.NET_SessionId': 'g5keoe3walmgwtssoipheyug',
    'cookieyes-consent': 'consentid:c2hOSWdsSFpXU2ZXdm5tcnd5OTl4SDRiaE1rNXh4U1Y,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
    '_gid': 'GA1.2.1869007682.1753691173',
    '_gcl_au': '1.1.2052510414.1753691174',
    'CMSLandingPageLoaded': 'true',
    'viewing_category': '386',
    'CMSCurrentTheme': 'BB_Product_Listing',
    '_ga': 'GA1.2.1798724763.1753691173',
    '_gat_gtag_UA_8942209_1': '1',
    'VisitorStatus': '11064821236',
    'CMSUserPage': '{"TimeStamp":"2025-07-28T04:36:23.6088166-04:00","LastPageDocumentID":43606,"LastPageNodeID":23366,"Identifier":"44e37fb2-6b08-407a-9631-3224adf76391"}',
    '_ga_C3MZ3X6NZ6': 'GS2.1.s1753691174$o1$g1$t1753691829$j60$l0$h0',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.bulkbarn.ca/ecomm/product_search.html?H=EN',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'CMSPreferredCulture=en-CA; language=en; location=5; bbregion_language=lang=en&prov=Washington; favorites=; default_store=; default_store_data=; CMSCsrfCookie=fqfsS1qj1eyUyxAob/B8SntL65x4uf8LukJ+xbpp; ASP.NET_SessionId=g5keoe3walmgwtssoipheyug; cookieyes-consent=consentid:c2hOSWdsSFpXU2ZXdm5tcnd5OTl4SDRiaE1rNXh4U1Y,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _gid=GA1.2.1869007682.1753691173; _gcl_au=1.1.2052510414.1753691174; CMSLandingPageLoaded=true; viewing_category=386; CMSCurrentTheme=BB_Product_Listing; _ga=GA1.2.1798724763.1753691173; _gat_gtag_UA_8942209_1=1; VisitorStatus=11064821236; CMSUserPage={"TimeStamp":"2025-07-28T04:36:23.6088166-04:00","LastPageDocumentID":43606,"LastPageNodeID":23366,"Identifier":"44e37fb2-6b08-407a-9631-3224adf76391"}; _ga_C3MZ3X6NZ6=GS2.1.s1753691174$o1$g1$t1753691829$j60$l0$h0',
}
import requests
from curl_cffi import requests
import json
from fix_busted_json import repair_json


response = requests.get(
    'https://www.bulkbarn.ca/ecomm/sale_data.js',
    # cookies=cookies,
    headers=headers,
    verify=False,
)

data = (response.text.replace('saleData(', '').strip()[:-1].strip().replace('\n', '').
        replace('\r', '').replace('\t', '').replace(',]',']').replace(',}', '}'))
# print(data)
fixed_json = json.loads(data)

print(fixed_json)









