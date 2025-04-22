import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Impact IA", layout="centered")

st.markdown("""<style>.card {
        background-color: #5DA28D;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #b2dfc1;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Estimez l'impact écologique de votre utilisation de l'IA")

st.markdown("""
Bienvenue dans ce calculateur vert 🌱 ! Découvrez combien d'énergie, d'eau et d'émissions de CO2e génère votre usage quotidien des IA, et adoptez un usage plus responsable 💚.
""")

# Données d'estimation par requête (en Wh, gCO2e, Litre d'eau)
data = {
    "GPT-3.5": {"conso": 0.35, "co2": 0.2, "eau": 0.6},
    "GPT-4": {"conso": 2.9, "co2": 1.4, "eau": 3.8},
    "Midjourney": {"conso": 6.0, "co2": 3.0, "eau": 5.0},
    "DALL·E": {"conso": 2.5, "co2": 1.2, "eau": 2.5},
    "Copilot": {"conso": 0.5, "co2": 0.25, "eau": 0.8},
    "Gemini": {"conso": 2.0, "co2": 1.0, "eau": 2.0},
    "Mistral": {"conso": 0.3, "co2": 0.15, "eau": 0.2},
    "Claude": {"conso": 1.5, "co2": 0.7, "eau": 1.2},
    "Golem AI": {"conso": 0.05, "co2": 0.01, "eau": 0.05},
    "DeepSeek": {"conso": 0.7, "co2": 0.4, "eau": 0.9},
    "BLOOM": {"conso": 1.0, "co2": 0.5, "eau": 0.3}
}
model = st.selectbox("🤖 Quel modèle d'IA utilisez-vous principalement ?", list(data.keys()))
requests_per_day = st.slider("📅 Combien de requêtes envoyez-vous par jour ?", 1, 200, 10)

# Calculs
conso_totale_j = requests_per_day * data[model]["conso"]
co2_totale_j = requests_per_day * data[model]["co2"]
eau_totale_j = requests_per_day * data[model]["eau"]

conso_semaine = conso_totale_j * 7
conso_mois = conso_totale_j * 30
co2_semaine = co2_totale_j * 7
co2_mois = co2_totale_j * 30
eau_semaine = eau_totale_j * 7
eau_mois = eau_totale_j * 30

st.markdown("""
<div class='highlight-box'>
    <p class='big-font'>📊 Résultats estimés :</p>
    <ul>
        <li><strong>Par jour :</strong> {0:.2f} Wh — {1:.2f} gCO₂e — {2:.2f} L d'eau</li>
        <li><strong>Par semaine :</strong> {3:.2f} Wh — {4:.2f} gCO₂e — {5:.2f} L d'eau</li>
        <li><strong>Par mois :</strong> {6:.2f} Wh — {7:.2f} gCO₂e — {8:.2f} L d'eau</li>
    </ul>
</div>
""".format(conso_totale_j, co2_totale_j, eau_totale_j,
           conso_semaine, co2_semaine, eau_semaine,
           conso_mois, co2_mois, eau_mois), unsafe_allow_html=True)

# Graphique avec Plotly style nature
labels = ["Jour", "Semaine", "Mois"]
conso_values = [conso_totale_j, conso_semaine, conso_mois]
co2_values = [co2_totale_j, co2_semaine, co2_mois]
eau_values = [eau_totale_j, eau_semaine, eau_mois]

fig = go.Figure()
fig.add_trace(go.Bar(x=labels, y=conso_values, name='Consommation (Wh)', marker_color='#6DBF67'))
fig.add_trace(go.Bar(x=labels, y=co2_values, name='CO2 (g)', marker_color='#A1D99B'))
fig.add_trace(go.Bar(x=labels, y=eau_values, name="Eau (L)", marker_color="#7FDBFF"))

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
6. 💧 **Pensez à l'eau** : L'entraînement et l'utilisation des IA consomment aussi de l'eau, souvent invisible mais bien réelle.
7. 🧠 **Adoptez un usage raisonné** : L’IA est puissante, mais chaque prompt a un coût pour la planète 🌍.
""")


# Liste triée des modèles les plus écologiques
sorted_models = sorted(data.items(), key=lambda x: (x[1]['conso'], x[1]['co2'], x[1]['eau']))

st.subheader("🌿 Classements des modèles d'IA les plus écologiques")
for model_name, values in sorted_models:
    st.markdown(f"""
    <div class='card'>
        <strong>{model_name}</strong><br>
        ⚡ {values['conso']} Wh — 🌫️ {values['co2']} g CO₂e — 💧 {values['eau']} L
    </div>
    """, unsafe_allow_html=True)
