import streamlit as st

def bereken_totale_rente(lening, jaar_rente, looptijd, restschuld):
   
    r = (jaar_rente / 100) / 12  
    n = looptijd  
    
    # Annuïteit berekenen
    A = (lening - restschuld / ((1 + r) ** n)) / ((1 - (1 + r) ** -n) / r)
    
    # Totale rentekosten
    totale_betalingen = A * n + restschuld  
    totale_rente = totale_betalingen - lening  
    
    return A, totale_rente

st.title("Lease Calculator")

# Inputvelden
lening = st.text_input('Lening bedrag (€)', '20000')
restschuld = st.text_input('Restschuld (€)', '7500')
jaar_rente = st.text_input('Jaarlijkse rente (%)', '9.0')
looptijd = st.text_input('Looptijd (maanden)', '36')

# Knop om te berekenen
if st.button('Bereken'):
    try:
        # Omzetten van tekst naar getal
        lening = float(lening)
        restschuld = float(restschuld)
        jaar_rente = float(jaar_rente)
        looptijd = int(looptijd)

        # Berekening uitvoeren
        maandlast, totale_rente = bereken_totale_rente(lening, jaar_rente, looptijd, restschuld)

        st.success(f'Maandelijks bedrag (Aflossing&Rente): €{maandlast:.2f}')
        st.info(f'Totale rentekosten over de looptijd: €{totale_rente:.2f}')

    except ValueError:
        st.error('Voer alstublieft geldige numerieke waarden in.')

