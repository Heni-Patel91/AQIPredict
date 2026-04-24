import gradio as gr
import numpy as np
import joblib

# LOAD MODEL
model = joblib.load("aqi_model.pkl")

# ----------------------------
# AQI CATEGORY FUNCTION
# ----------------------------
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good", "Air quality is safe. Normal outdoor activities."
    elif aqi <= 100:
        return "Moderate", "Sensitive people should limit outdoor exposure."
    elif aqi <= 200:
        return "Poor", "Reduce outdoor activity. Wear mask if needed."
    elif aqi <= 300:
        return "Very Poor", "Avoid outdoor activities. Health risk for all."
    else:
        return "Severe", "Emergency conditions. Stay indoors strictly."


# ----------------------------
# PREDICT FUNCTION
# ----------------------------
def predict_aqi(pm25, pm10, no2, co, temperature, humidity, wind_speed):

    input_data = np.array([[pm25, pm10, no2, co, temperature, humidity, wind_speed]])

    pred = float(model.predict(input_data)[0])
    pred = max(0, min(500, pred))

    category, advice = get_aqi_category(pred)

    forecast = []
    for i in range(24):
        variation = np.sin(i / 3) * 5 + np.random.normal(0, 3)
        value = max(0, min(500, pred + variation))
        forecast.append(round(value, 2))

    return round(pred, 2), category, advice, forecast


# ----------------------------
# MODERN UI USING BLOCKS
# ----------------------------
with gr.Blocks() as app:

    gr.Markdown("## Air Quality Prediction System")
    gr.Markdown("Enter pollution and weather values to predict AQI")

    with gr.Row():
        with gr.Column():
            pm25 = gr.Number(value=50, label="PM2.5")
            pm10 = gr.Number(value=80, label="PM10")
            no2 = gr.Number(value=40, label="NO2")
            co = gr.Number(value=1.0, label="CO")

        with gr.Column():
            temperature = gr.Number(value=30, label="Temperature")
            humidity = gr.Number(value=60, label="Humidity")
            wind_speed = gr.Number(value=2, label="Wind Speed")

    predict_btn = gr.Button("Predict AQI")

    gr.Markdown("### Results")

    with gr.Row():
        aqi_output = gr.Number(label="Predicted AQI")
        category_output = gr.Textbox(label="AQI Category")

    advice_output = gr.Textbox(label="Health Advice")

    forecast_output = gr.JSON(label="24-Hour Forecast")

    predict_btn.click(
        fn=predict_aqi,
        inputs=[pm25, pm10, no2, co, temperature, humidity, wind_speed],
        outputs=[aqi_output, category_output, advice_output, forecast_output]
    )

app.launch()