from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Carrega modelo
model = joblib.load("modelo_no_show.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Ordenação das features (igual ao notebook!)
    features = [[
        data["prior_no_shows"],
        data["reminder_sms"],
        data["reminder_call"],
        data["reminder_email"],
        data["lead_time_days"],
        data["socioeconomic_index"],
        data["distance_km"],
        data["weather_rain"],
        data["public_transport_strike"],
        data["scheduled_duration_min"],
        data["comorbidity_count"],
        data["has_diabetes"],
        data["has_hypertension"],
        data["has_chronic_resp"]
    ]]

    prob = model.predict_proba(features)[0][1]

    return jsonify({
        "no_show_probability": round(float(prob), 3),
        "decision": "alto_risco" if prob > 0.5 else "baixo_risco"
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
