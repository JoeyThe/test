import requests
from bs4 import BeautifulSoup
import shutil

if __name__ == "__main__":
    r = requests.get('https://unsplash.com/s/photos/bird')
    soup = BeautifulSoup(r.content, 'html.parser')   
    # myImgs = soup.select('div img')
    imgDiv = soup.find('div', {'data-test':'search-photos-route'})
    headerS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # print(myImgs)
    myImgs = imgDiv.find_all('img')
    for img in myImgs:
        print(img, end='\n\n')
        break
    

    # for img in myImgs:
    #     if img.get('srcset') is not None:
    #         print(img.get('srcset')[0], end='\n\n')
    #         lnk = img.get('data-src')
    #         testImg = requests.get('https://64.media.tumblr.com/ab6b4ff998564bdae6d6efdad3b63f1e/43ff84174c794235-9d/s540x810/6b6f78756c2a029ed1adda5ca234894043c325bf.jpg', stream=True, headers=headerS)
    #         # testImg = requests.get(lnk, stream=True, headers=headers)
    #         print(lnk)
    #         print(testImg.status_code)
    #         if testImg.status_code == 200:
    #             print('Request successful')
    #             with open('C:\\Users\\josep\\Documents\\venv\\git\\test\\RandomImageGen\\Images\\image.jpg', 'wb') as f:
    #                 testImg.raw.decode_content = True
    #                 shutil.copyfileobj(testImg.raw, f)    
    #                 # f = open('C:\\Users\\josep\\Documents\\venv\\git\\test\\RandomImageGen\\Images\\image.jpg', 'wb')
    #                 # f.write(requests.get(lnk).content)
    #                 # f.close()
    #         else:
    #             print("FORBIDDEN")
    #         break
# <img class="wmx100 mx-auto my8 h-auto d-block" width="139" height="114" src="https://cdn.sstatic.net/Img/teams/teams-illo-free-sidebar-promo.svg?v=47faa659a05e" alt="">