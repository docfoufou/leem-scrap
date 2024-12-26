from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import re

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
data10 = []
data11 = []
data12 = []
data13 = []
data14 = []
data15 = []
data16 = []
data17 = []
data18 = []
data19 = []
data20 = []
li_appellations = ''
final_activites = ''
final_competences_cles = ''
final_metiers = []

for i in range(0, 7):
    # specify the url
    url_page = 'https://www.leem.org/referentiels-metiers?recherche=&famille=All&sous-famille=All&niveau=All&page=' + str(i)

    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(url_page)

    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    # find results within table
    spans = soup.find_all('span', {'class': 'field-content'})
    for span in spans:
        links = span.find_all('a')
        for link in links:

            data1.append(link.text)

            url_metier = 'https://www.leem.org' + link['href']
            page_metier = urllib.request.urlopen(url_metier)
            soup_metier = BeautifulSoup(page_metier, 'html.parser')

            famille = soup_metier.find('div', {'class': 'field--name-field-metier-sfamille'}).find('p').text
            famille = re.split(' / | : ', famille)
            data2.append(famille[0])
            data3.append(famille[1])

            mission = soup_metier.find('div', {'class': 'field--name-field-mission-generale'}).find('p').text
            data4.append(mission)

            if soup_metier.find('div', {'class': 'field--name-field-autres-appellations'}).find('p'):
                autres_appellations = soup_metier.find('div', {'class': 'field--name-field-autres-appellations'}).find('p').text
                autres_appellations = re.sub('•    ', '• ', autres_appellations)
                data5.append(autres_appellations)
            elif soup_metier.find('div', {'class': 'field--name-field-autres-appellations'}).find('ul'):
                autres_appellations = soup_metier.find('div', {'class': 'field--name-field-autres-appellations'}).find('ul').find_all('li')
                for li in autres_appellations:
                    li_appellations = li_appellations + li.text + '\n'
                data5.append(li_appellations)
                li_appellations = ''

            activites = soup_metier.find('div', {'class': 'field--name-field-activites2'})
            activites_children = activites.find_all(['p', 'h3'])
            for child in activites_children[:-1]:
                final_activites = final_activites + child.text + '\n'
            final_activites = final_activites.rstrip('\n')
            data6.append(final_activites)
            final_activites = ''

            competences_cles = soup_metier.find('div', {'class': 'field--name-field-competences-cles'})
            competences_cles_children = competences_cles.find_all(['p', 'h3'])
            for child in competences_cles_children[:-1]:
                final_competences_cles = final_competences_cles + child.text + '\n'
            final_competences_cles = final_competences_cles.rstrip('\n')
            data7.append(final_competences_cles)
            final_competences_cles = ''

            evolution_metier = soup_metier.find('div', {'class': 'field--name-field-evolution-du-metier2'}).find('p').text
            evolution_metier = evolution_metier.rstrip('\n')
            data8.append(evolution_metier)

            profil_recrutement = soup_metier.find('div', {'class': 'field--name-field-profil-de-recrutement'}).find('p').text
            profil_recrutement = profil_recrutement.rstrip('\n')
            data9.append(profil_recrutement)

            formations_parcours = soup_metier.find('div', {'class': 'field--name-field-formations-parcours-rec'}).find('p').text
            formations_parcours = re.sub('•    ', '• ', formations_parcours)
            data10.append(formations_parcours)

            passerelles_metiers = soup_metier.find('div', {'class': 'field--name-field-passerelles-metiers2'}).find_all('p')
            for p in passerelles_metiers:
                metiers = re.sub('//s+', ' ', p.text)
                metiers = re.split('• ', metiers)
                metiers_without = [string for string in metiers if string != '']
                metiers_without = [string for string in metiers_without if string != ' ']
                metiers_without = [string for string in metiers_without if string != 'A court terme : ']
                metiers_without = [string for string in metiers_without if string != 'A plus long terme :'] 
                final_metiers = final_metiers + metiers_without
            i = len(final_metiers)

            if i == 1:
                data11.append(final_metiers[0].rstrip())
                data12.append('')
                data13.append('')
                data14.append('')
                data15.append('')
                data16.append('')
                data17.append('')
                data18.append('')
                data19.append('')
                data20.append('')
            elif i == 2:
                data11.append(final_metiers[0].rstrip())
                data12.append(final_metiers[1].rstrip())
                data13.append('')
                data14.append('')
                data15.append('')
                data16.append('')
                data17.append('')
                data18.append('')
                data19.append('')
                data20.append('')
            elif i == 3:
                data11.append(final_metiers[0].rstrip())
                data12.append(final_metiers[1].rstrip())
                data13.append(final_metiers[2].rstrip())
                data14.append('')
                data15.append('')
                data16.append('')
                data17.append('')
                data18.append('')
                data19.append('')
                data20.append('')
            elif i == 4:
                data11.append(final_metiers[0].rstrip())
                data12.append(final_metiers[1].rstrip())
                data13.append(final_metiers[2].rstrip())
                data14.append(final_metiers[3].rstrip())
                data15.append('')
                data16.append('')
                data17.append('')
                data18.append('')
                data19.append('')
                data20.append('')
            elif i == 5:
                data11.append(final_metiers[0].rstrip())
                data12.append(final_metiers[1].rstrip())
                data13.append(final_metiers[2].rstrip())
                data14.append(final_metiers[3].rstrip())
                data15.append(final_metiers[4].rstrip())
                data16.append('')
                data17.append('')
                data18.append('')
                data19.append('')
                data20.append('')
            elif i == 6:
                data11.append(final_metiers[0].rstrip())
                data12.append(final_metiers[1].rstrip())
                data13.append(final_metiers[2].rstrip())
                data14.append(final_metiers[3].rstrip())
                data15.append(final_metiers[4].rstrip())
                data16.append(final_metiers[5].rstrip())
                data17.append('')
                data18.append('')
                data19.append('')
                data20.append('')
            elif i == 7:
                data11.append(final_metiers[0].rstrip())
                data12.append(final_metiers[1].rstrip())
                data13.append(final_metiers[2].rstrip())
                data14.append(final_metiers[3].rstrip())
                data15.append(final_metiers[4].rstrip())
                data16.append(final_metiers[5].rstrip())
                data17.append(final_metiers[6].rstrip())
                data18.append('')
                data19.append('')
                data20.append('')
            elif i == 8:
                data11.append(final_metiers[0].rstrip())
                data12.append(final_metiers[1].rstrip())
                data13.append(final_metiers[2].rstrip())
                data14.append(final_metiers[3].rstrip())
                data15.append(final_metiers[4].rstrip())
                data16.append(final_metiers[5].rstrip())
                data17.append(final_metiers[6].rstrip())
                data18.append(final_metiers[7].rstrip())
                data19.append('')
                data20.append('')
            elif i == 9:
                data11.append(final_metiers[0].rstrip())
                data12.append(final_metiers[1].rstrip())
                data13.append(final_metiers[2].rstrip())
                data14.append(final_metiers[3].rstrip())
                data15.append(final_metiers[4].rstrip())
                data16.append(final_metiers[5].rstrip())
                data17.append(final_metiers[6].rstrip())
                data18.append(final_metiers[7].rstrip())
                data19.append(final_metiers[8].rstrip())
                data20.append('')
            final_metiers = []

df = pd.DataFrame({'Métier': data1, 'Famille': data2, 'Sous-famille': data3, 'Mission générale': data4, 'Autres appellations': data5, 'Activités': data6, 
                   'Competences clés': data7, 'Evolution du métier': data8, 'Profil de recrutement': data9, 'Formations / Parcours recommandés': data10,
                   'Passerelles métiers 1': data11, 'Passerelles métiers 2': data12, 'Passerelles métiers 3': data13, 'Passerelles métiers 4': data14,
                   'Passerelles métiers 5': data15, 'Passerelles métiers 6': data16, 'Passerelles métiers 7': data17, 'Passerelles métiers 8': data18,
                   'Passerelles métiers 9': data19, 'Passerelles métiers 10': data20})

df.to_excel('leem.xlsx')
