import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Votre consomation IA", layout="centered")


st.title("🌍 Estimez l'impact écologique de votre utilisation de l'IA")

st.markdown("""
Bienvenue dans ce calculateur vert 🌱 ! Découvrez combien d'énergie et d'émissions de CO2e génère votre usage quotidien des IA, et adoptez un usage plus responsable 💚.
""")

# Données d'estimation par requête (en Wh et gCO2e)
data = {
    "GPT-3.5": {"conso": 0.35, "co2": 0.2},
    "GPT-4": {"conso": 2.9, "co2": 1.4},
    "Midjourney": {"conso": 6.0, "co2": 3.0},
    "DALL·E": {"conso": 2.5, "co2": 1.2},
    "Copilot": {"conso": 0.5, "co2": 0.25},
    "Gemini": {"conso": 2.0, "co2": 1.0},
    "Mistral": {"conso": 0.3, "co2": 0.15},
    "Claude": {"conso": 1.5, "co2": 0.7},
}

model = st.selectbox("🤖 Quel modèle d'IA utilisez-vous principalement ?", list(data.keys()))
requests_per_day = st.slider("📅 Combien de requêtes envoyez-vous par jour ?", 1, 1000, 10)

# Calculs
conso_totale_j = requests_per_day * data[model]["conso"]
co2_totale_j = requests_per_day * data[model]["co2"]

conso_semaine = conso_totale_j * 7
conso_mois = conso_totale_j * 30
co2_semaine = co2_totale_j * 7
co2_mois = co2_totale_j * 30

st.markdown("""
<div class='highlight-box'>
    <p class='big-font'>📊 Résultats estimés :</p>
    <ul>
        <li><strong>Par jour :</strong> {0:.2f} Wh — {1:.2f} gCO₂e</li>
        <li><strong>Par semaine :</strong> {2:.2f} Wh — {3:.2f} gCO₂e</li>
        <li><strong>Par mois :</strong> {4:.2f} Wh — {5:.2f} gCO₂e</li>
    </ul>
</div>
""".format(conso_totale_j, co2_totale_j, conso_semaine, co2_semaine, conso_mois, co2_mois), unsafe_allow_html=True)

# Graphique avec Plotly style nature
labels = ["Jour", "Semaine", "Mois"]
conso_values = [conso_totale_j, conso_semaine, conso_mois]
co2_values = [co2_totale_j, co2_semaine, co2_mois]

fig = go.Figure()
fig.add_trace(go.Bar(x=labels, y=conso_values, name='Consommation (Wh)', marker_color='#6DBF67'))
fig.add_trace(go.Bar(x=labels, y=co2_values, name='CO2 (g)', marker_color='#A1D99B'))

fig.update_layout(
    barmode='group',
    title='🌿 Impact estimé selon votre utilisation',
    xaxis_title='Période',
    yaxis_title='Valeurs',
    legend_title='Mesures',
    template='plotly',
    margin=dict(l=40, r=40, t=40, b=40)
)

st.plotly_chart(fig)

st.subheader("💡 Conseils pour réduire votre impact écologique")
st.markdown("""
1. 🌱 **Choisissez les modèles légers** : Optez pour GPT-3.5, Mistral ou Claude Instant pour des tâches simples.
2. 📉 **Réduisez la fréquence** : Rassemblez vos questions plutôt que d'interroger l'IA plusieurs fois.
3. 🖼️ **Moins d'images générées** : Préférez des réponses textuelles plutôt que des visuels (Midjourney/DALL·E).
4. 🔁 **Évitez les requêtes inutiles** : Relisez et regroupez avant d’envoyer !
5. 💻 **Modèles locaux éco-friendly** : Pour certaines tâches, tournez-vous vers des modèles en local comme Mistral.
6. 🧠 **Adoptez un usage raisonné** : L’IA est puissante, mais chaque prompt a un coût pour la planète 🌍.
""")