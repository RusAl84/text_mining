from bs4 import BeautifulSoup
import requests


def get_urls(url='https://priem.mirea.ru/guide'):
    page = requests.get(url)
    # if page.status_code == 200:
    #     print(url + " 200")

    soup = BeautifulSoup(page.text, "html.parser")
    insts = []

    blocks = soup.findAll(True, {"class": ["body-wrapper"]})

    print(blocks)

    # urls = []
    # num_inst = 0
    # for block in blocks:
    #     soup_inst = BeautifulSoup(str(block), "html.parser")
    #     inst = soup_inst.find_all("a", {"class": "uk-text-bold"})
    #     if len(inst) > 0:
    #         print(inst[0].text)  # список институтов
    #
    #         if inst[0].text == 'Институт кибербезопасности и цифровых технологий' or inst[
    #             0].text == 'Институт перспективных технологий и индустриального программирования' or inst[
    #             0].text == 'Институт технологий управления':
    #             num_inst += 1
    #             num = 1
    #             for link in soup_inst.find_all('a', href=True):
    #                 # print(link['href'])
    #                 if "javascript:void(0)" not in link['href']:
    #                     # print(link['href'])
    #                     url = []
    #                     url.append(link['href'])
    #                     url.append(str(num_inst) + "_" + str(num) + "-k.xls")
    #                     url.append(inst[0].text)
    #                     num += 1
    #                     # if "mag" not in link['href'] and "4_kurs" not in link['href'] and "3_kurs" not in link['href']:
    #                     urls.append(url)
    #                     # print(url)
    return urls


if __name__ == '__main__':
    get_urls()