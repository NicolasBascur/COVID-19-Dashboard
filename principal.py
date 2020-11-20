from json import dumps
import altair as alt
import base64
import numpy as np
import pandas as pd
import streamlit as st
import texto

SAMPLE_SIZE=500
MIN_CASES_TH = 10
MIN_DAYS_r0_ESTIMATE = 14
MIN_DATA_CHILE = '2020-03-26' #Fecha Inicial    MIN_DATA_BRAZIL
COMUNA_E = 'Arica' #Ciudad Estandar
REGION_E = 'Arica y Parinacota' #Region estandar
DEFAULT_PARAMS = {
    'fator_subr': 5.0,
    'gamma_inv_dist': (7.0, 14.0, 0.95, 'lognorm'),
    'alpha_inv_dist': (4.0, 7.0, 0.95, 'lognorm'),
    'r0_dist': (2.5, 6.0, 0.95, 'lognorm'),
}   # Parametros estandar modelo SEIR - BAYES.

def write():
    st.markdown("## Modelo Epidemiológico (SEIR-Bayes)")
    st.sidebar.markdown(texto.PARAMETER_SELECTION)
    w_granularity = st.sidebar.selectbox('Unidad',
                                         options=['reg', 'com'],  #state, city -- region, comuna
                                         index=1,
                                         format_func=global_format_func)

    source = 'ms' if w_granularity == 'reg' else 'wcota'
    cases_df = data.load_cases(w_granularity, source)
    population_df = data.load_population(w_granularity)

    DEFAULT_PLACE = (COMUNA_E if w_granularity == 'com' else
                     REGION_E)

    options_place = make_place_options(cases_df, population_df)
    w_place = st.sidebar.selectbox('Município',
                                   options=options_place,
                                   index=options_place.get_loc(DEFAULT_PLACE),
                                   format_func=global_format_func)

    options_date = make_date_options(cases_df, w_place)
    w_date = st.sidebar.selectbox('Data inicial',
                                  options=options_date,
                                  index=len(options_date)-1)
    NEIR0 = make_NEIR0(cases_df, population_df, w_place, w_date)
    
    # Estimar R0
    st.markdown(texto.r0_ESTIMATION_TITLE)
    should_estimate_r0 = st.checkbox(
            'Estimar R0 a partir de dados históricos',
            value=True)
    if should_estimate_r0:
        r0_samples, used_brazil = estimate_r0(cases_df,
                                              w_place,
                                              SAMPLE_SIZE, 
                                              MIN_DAYS_r0_ESTIMATE, 
                                              w_date)
        if used_brazil:
            st.write(texto.r0_NOT_ENOUGH_DATA(w_place, w_date))
                                     
        _place = 'Brasil' if used_brazil else w_place
        st.markdown(texto.r0_ESTIMATION(_place, w_date))

        st.altair_chart(plot_r0(r0_samples, w_date, 
                                _place, MIN_DAYS_r0_ESTIMATE))
        r0_dist = r0_samples[:, -1]
        st.markdown(f'*O $R_{{0}}$ estimado está entre '
                    f'${np.quantile(r0_dist, 0.01):.03}$ e ${np.quantile(r0_dist, 0.99):.03}$*')
        st.markdown(texto.r0_CITATION)
    else:
        r0_dist = make_r0_widgets()
        st.markdown(texto.r0_ESTIMATION_DONT)

    # Predicción de infectados
    w_params = make_param_widgets(NEIR0)
    model = SEIRBayes(**w_params, r0_dist=r0_dist)
    model_output = model.sample(SAMPLE_SIZE)
    ei_df = make_EI_df(model, model_output, SAMPLE_SIZE)
    st.markdown(texto.MODEL_INTRO)
    w_scale = st.selectbox('Escala do eixo Y',
                           ['log', 'linear'],
                           index=1)
    fig = plot_EI(model_output, w_scale, w_date)
    st.altair_chart(fig)
    download_placeholder = st.empty()
    if download_placeholder.button('Preparar dados para download em CSV'):
        href = make_download_href(ei_df, w_params, r0_dist, should_estimate_r0)
        st.markdown(href, unsafe_allow_html=True)
        download_placeholder.empty()

    # Parámetros de simulación
    dists = [w_params['alpha_inv_dist'],
             w_params['gamma_inv_dist'],
             r0_dist]
    SEIR0 = model._params['init_conditions']
    params_intro_txt, seir0_dict, other_params_txt = texto.make_SIMULATION_PARAMS(SEIR0, dists,
                                             should_estimate_r0)
    st.markdown(params_intro_txt)
    st.write(pd.DataFrame(seir0_dict).set_index("Compartimento"))
    st.markdown(other_params_txt)

    # Configuración de simulación
    st.markdown(texto.SIMULATION_CONFIG)
    # Fuentes de datos
    st.markdown(texto.DATA_SOURCES)


if __name__ == '__main__':
    write()
