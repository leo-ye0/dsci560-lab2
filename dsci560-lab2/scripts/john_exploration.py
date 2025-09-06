import pandas as pd
import pdfplumber

def load_pdf(file):
    with pdfplumber.open(path) as pdf:  
        page = pdf.pages[0]
        text = page.extract_text()
        print(f'Loading pdf: {file}\n')
    return text

def get_matchups(text):
    home_v_away = []

    keywords = {'El':'El Savador', 'Savador':'El Savador', 
                'Trinidad':'Trinidad & Tobago', 'Tobago':'Trinidad & Tobago',
                'Costa':'Costa Rica', 'Rica':'Costa Rica'}

    for line in text.split('\n'):
        line = line.split()
        if 'V' in line:
            index = line.index('V')
            left, right = line[index - 1], line[index + 1]
            if left in keywords:
                home = keywords[left]
            else:
                home = left
            if right in keywords:
                away = keywords[right]
            else:
                away = right
            home_v_away.append([home, away])
    
    return home_v_away

def matchups_to_df(matchups_list):
    df = pd.DataFrame(matchups_list, columns=['Home', 'Away'])
    return df

if __name__ == "__main__":
    file = 'concacaf_qualifiers.pdf'
    path = '../data/' + file

    text = load_pdf(file)

    matchups = get_matchups(text)
    df = matchups_to_df(matchups)

    print('Extractring matchups\n')
    print(f'Converting {file} to .csv\n')

    df.to_csv('../data/concacaf_matchups.csv', index=False)

    print('CSV file saved to data folder')    