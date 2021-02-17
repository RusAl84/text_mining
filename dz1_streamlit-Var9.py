# -*- coding: utf-8 -*-
import streamlit as st


def analiz(stroka):
    # блок определения таблицы переходов
    table_perehod = [['A', '1', 'F'],
                     ['A', 'b', 'B'],
                     ['B', 'b', 'C'],
                     ['C', 'a', 'D'],
                     ['D', '1', 'A'],
                     ['E', '1', 'F'],
                     ['F', '1', 'G'],
                     ['F', 'b', 'M'],
                     ['G', 'a', 'H'],
                     ['H', 'a', 'E'],
                     ['K', 'a', 'L'],
                     ['L', 'b', 'M'],
                     ['M', 'a', 'N'],
                     ['N', '1', 'K']]
    nachaln_simv = 'A'  # начальный символ он у Вас скорее всего 'A'
    kol_perehodov = len(table_perehod)
    length = len(stroka)
    n = 0
    ok = True
    neterm = nachaln_simv
    while ok and (n < length):
        i = 0
        sym = stroka[n]
        print(f"{n} - {sym}")
        n += 1
        ok = False
        while True:
            if (table_perehod[i][0] == neterm) and (table_perehod[i][1] == sym):
                ok = True
                neterm = table_perehod[i][2]
            i += 1
            if not ((not ok) and (i < kol_perehodov)):
                break
    # терминальные символы они у Вас скорее всего 'A'  'E' 'K'
    if ((neterm == 'A') or (neterm == "E") or (neterm == 'K')) and ok:
        return "# Данная строка принадлежит языку :sunglasses:"
    else:
        return "# Данная строка не принадлежит языку"


if __name__ == "__main__":
    st.markdown('# Дано регулярное выражение (bba1)\* (11aa)\* (1ba1)\*')
    st.markdown('## Введите строку символов:')
    ex = "none"
    ex = st.text_input('', value='', max_chars=None, key='ex' + str(ex), type='default')
    # print(ex)
    rez = analiz(ex)
    # print(rez)
    st.button('Анализ')
    st.markdown(rez)
