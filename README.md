# HC Acesso Fácil — Previsão de Absenteísmo

Solução preditiva para identificar a probabilidade de um paciente faltar a uma teleconsulta, utilizando aprendizado de máquina para apoiar tomadas de decisão, otimizar agendas médicas e reduzir desperdício de recursos em contextos hospitalares.

---

## 🧠 Objetivo

O projeto utiliza técnicas de machine learning para analisar fatores relacionados ao absenteísmo em teleconsultas, gerando uma probabilidade prevista de falta e classificando pacientes em **alto** ou **baixo risco**. Essa predição possibilita:

- Melhor organização das agendas médicas
- Ações preventivas baseadas em risco
- Aumento de eficiência operacional
- Redução de gargalos hospitalares

---

## 👥 Integrantes do Grupo

| Nome | RM |
|------|------|
| Gustavo Tavares da Silva | RM562827 |
| Fellipe Costa de Oliveira | RM564673 |
| Felype Ferreira Maschio | RM563009 |

---

## 🧩 Tecnologias e Ferramentas Utilizadas

- Python
- Jupyter Notebook
- Flask
- Pandas
- Numpy
- Scikit-Learn
- Matplotlib
- Seaborn
- Joblib

---

## 📁 Estrutura do Projeto

```
Sprint4_IA/
├─ Sprint4_IA.ipynb
├─ app.py
├─ modelo_no_show.joblib
├─ requirements.txt
├─ datasets/
└─ screenshots/   (opcional — utilizada apenas para documentação)
```

---

## 🚀 Como Executar Localmente (API Flask)

### 🔧 1. Instale as dependências

No diretório raiz do projeto:

```bash
pip install -r requirements.txt
```

### ▶️ 2. Execute a API

```bash
python app.py
```

A aplicação será iniciada em:

```
http://127.0.0.1:5000
```

---

## 📡 Endpoint Disponível

### **POST** `/predict`

Recebe um JSON contendo variáveis do paciente relacionadas a chance de absenteísmo.

Exemplo de requisição:

```json
{
  "prior_no_shows": 2,
  "reminder_sms": 1,
  "reminder_call": 0,
  "reminder_email": 1,
  "lead_time_days": 13,
  "socioeconomic_index": 0.4,
  "distance_km": 7,
  "weather_rain": 1,
  "public_transport_strike": 0,
  "scheduled_duration_min": 25,
  "comorbidity_count": 1,
  "has_diabetes": 0,
  "has_hypertension": 1,
  "has_chronic_resp": 0
}
```

Resposta esperada:

```json
{
  "no_show_probability": 0.63,
  "decision": "alto_risco"
}
```

---

## 📊 Modelos de IA Aplicados

O projeto utiliza duas abordagens:

### ✅ **Aprendizado Supervisionado**

* Modelo de classificação Random Forest
* Cálculo de probabilidade de falta
* Métricas de avaliação

### ✅ **Aprendizado Não Supervisionado**

* K-Means para agrupamento de perfis de pacientes
* Identificação de padrões de comportamento

---

## 💾 Exportação do Modelo

O modelo treinado é salvo com a biblioteca **joblib**, permitindo:

* Reaproveitamento sem retreinamento
* Fácil integração com APIs

Arquivo gerado:

```
modelo_no_show.joblib
```

---

## 💻 Notebook de Treinamento

O arquivo `Sprint4_IA.ipynb` contém:

* Preparação dos dados
* EDA (análise exploratória)
* Treinamento de modelo
* Avaliação
* Clusterização
* Conclusões

---

## 📌 Observações

* Os prints de teste e execução estão incluídos apenas na documentação PDF.
* Deploy externo (Render/Cloud) não faz parte desta entrega.

---

## 🏁 Conclusão

Este projeto demonstra como o aprendizado de máquina pode auxiliar no combate ao absenteísmo em teleconsultas, permitindo priorização de ações preventivas e otimização do atendimento médico.

---

## 🔗 Repositório GitHub

[https://github.com/gustavaress/Sprint-4-IA-2025](https://github.com/gustavaress/Sprint-4-IA-2025)