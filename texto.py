INTRODUCTION = '''
Simulador # COVID-19

Ciencia de datos aplicada a la nueva pandemia de coronavirus

---
'''

ABOUT = '''
Este proyecto es un grupo de trabajo de las comunidades científicas y tecnológicas con el fin de crear modelos de pronóstico de infectados por COVID-19 - y otras métricas relacionadas -, para Brasil. El proyecto es público y puede ser utilizado por todos.

Visite [este enlace] (https://github.com/3778/COVID-19) para obtener información detallada e instrucciones sobre cómo contribuir.


'''

PARAMETER_SELECTION='''
# Selección de parámetros
Para simular otros escenarios, cambie un parámetro y presione ** Enter **. El nuevo resultado se calculará y se mostrará automáticamente.
#### Parámetros de UF / Municipio
'''

MODEL_INTRO='''
### Pronóstico de expuestos e infectados
El siguiente gráfico muestra el resultado de la simulación de la evolución de pacientes expuestos e infectados para los parámetros seleccionados. Más información sobre este modelo está disponible [aquí] (https://github.com/3778/COVID-19#seir-bayes).

** (!) Importante **: Los resultados presentados son * preliminares * y se encuentran en fase de validación.


'''

def make_SIMULATION_PARAMS(SEIR0, intervals, should_estimate_r0):
    alpha_inv_inf, alpha_inv_sup, _, _ = intervals[0]
    gamma_inv_inf, gamma_inv_sup, _, _ = intervals[1]

    if not should_estimate_r0:
        r0_inf, r0_sup, _, _ = intervals[2]
        r0_txt = f'- $${r0_inf:.03} < R_{{0}} < {r0_sup:.03}$$'
    else:
        r0_txt = '- $$R_{{0}}$$ se está estimando con datos históricos'

    intro_txt = '''
    ---

    ### Parámetros de simulación
    
    Valores iniciales de los comportamientos:
    '''
    
    seir0_labels = [
        "Susceptible",
        "Expuesto",
        "Infectado",
        "Remoto",
    ]
    seir0_values = list(map(int, SEIR0))
    seir0_dict = {
        "Comportimento": seir0_labels, 
        "Valor inicial": seir0_values,
    }
    
    other_params_txt = f'''
    Otros parámetros:
    - $${alpha_inv_inf:.03} < T_{{incub}} = 1/\\alpha < {alpha_inv_sup:.03}$$
    - $${gamma_inv_inf:.03} < T_{{infec}} = 1/\gamma < {gamma_inv_sup:.03}$$
    {r0_txt}

    Los intervalos $$ T _ {{incub}} $$ y $$ T _ {{infec}} $$ definen el 95% del intervalo de confianza para una distribución LogNormal.
    ''' 
    return intro_txt, seir0_dict, other_params_txt

SIMULATION_CONFIG = '''
---
### Configuración de simulación (menú a la izquierda)

#### Selección de UF / Municipio
Es posible seleccionar una unidad de la federación o municipio para utilizar sus parámetros en las condiciones iniciales de * Población total * (N), * Individuos infecciosos inicialmente * (I0), * Individuos removidos con inmunidad inicialmente * (R0) y * Individuos inicialmente expuestos ( E0) *.

#### Límites superior e inferior de parámetros
Los límites superior e inferior de los parámetros * Periodo infeccioso *, * Tiempo de incubación * y * Número básico de reproducción * también se pueden ajustar. Estos límites definen un intervalo de confianza del 95% de una distribución logarítmica normal para cada parámetro. \ N \ n \ n
'''

DATA_SOURCES = '''
---

### Fuentes de datos

* Casos confirmados por municipio: [Número de casos confirmados de COVID-19 en Brasil] (https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time.csv) (de https: / /github.com/wcota/covid19br)
* Casos confirmados por estado: [Panel de casos de enfermedad por coronavirus 2019 (COVID-19) en Brasil por el Ministerio de Salud] (https://covid.saude.gov.br/)
* Población: estimación del IBGE del 1 de julio de 2019 (disponible en: [IBGE - Estimaciones de población] (https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html ))
'''

r0_ESTIMATION_TITLE = '### Número de reproduccion básico $ R _ {{0}} $'

def r0_ESTIMATION(place, date): return  f'''
El número de reproducción básico $ R_ {0} $ se estima con datos históricos para {place}. El valor utilizado en el modelo SEIR-Bayes es el de {date}, que es el más reciente.

Si desea especificar el valor manualmente, desactive la opción anterior e ingrese los valores deseados.

** (!) Importante **: La estimación es sensible a la calidad de los informes de casos positivos.
'''

r0_ESTIMATION_DONT = '''
Utilice el menú de la izquierda para configurar el parámetro.
'''

r0_CITATION = '''
La metodología utilizada para la estimación se basó en el artículo [* Thompson, R. N., et al. "Inferencia mejorada de números de reproducción variables en el tiempo durante los brotes de enfermedades infecciosas". Epidemics 29 (2019): 100356 *] (https://www.sciencedirect.com/science/article/pii/S1755436519300350). El código de implementación se puede encontrar [aquí] (https://github.com/3778/COVID-19/blob/master/covid19/estimation.py).
'''

def r0_NOT_ENOUGH_DATA(w_place, w_date): return f'''
** {w_place} no tiene suficientes datos sobre la fecha
{w_date} para estimar. Pronto,
se utilizan datos agregados de Brasil **
'''
