import streamlit as st

paginas = ['Inicio', 'Experiencia', 'Gráficos']
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)
if pagina_seleccionada == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>BLOG PERSONAL</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.image("diego.jpeg", caption='DIEGO PAREDES', width=300)
    texto = """
    Soy Diego Paredes, soy de Chancay, Lima, y estudio Comunicación Audiovisual. 
    Me gusta mi carrera porque es muy diversa, permite ser creativo y aprender constantemente cosas nuevas. 
    En el futuro, me gustaría ser director y filmmaker para contar historias que conecten con las personas. 
    En mi tiempo libre disfruto jugar fútbol, ver series, escuchar música y crear historias.
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)
 
elif  pagina_seleccionada == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>Curso Pensamiento Computacional💻</h1>", unsafe_allow_html=True)
    texto_2 = """
    El curso de Pensamiento Computacional fue una excelente introducción a la programación con Python. 
    Permitió aprender de forma clara los conceptos básicos y desarrollar el pensamiento lógico para resolver problemas.
    Además aprender a crear una página web es una herramienta muy importante para los comunicadores. 
    Fue una experiencia muy útil y enriquecedora.
    Por último, agradecer al profesor Joseph Crawford y la porfesora Luisa Gomez por todo su apoyo. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Video PC2</h2>", unsafe_allow_html=True)
    texto_x = """
    En este video se presenta la diferencia entre los códigos FOR y WHILE, desarrollada en la PC2. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_x}</div>", unsafe_allow_html=True) 
    st.video("https://www.youtube.com/watch?v=78oTVRMsJCs")
    st.markdown(f"<div style='text-align: center;'><a href='https://www.youtube.com/watch?v=78oTVRMsJCs' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 
else:
    st.markdown("<h1 style='text-align: center;'>Gráficos</h1>", unsafe_allow_html=True)
    graficos = ['Gráfico de barras verticales de comunidades', 'Gráfico de barra vertical de pilotos', 'mapa de comunidades']
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    if grafico_seleccionado == 'Gráfico de barras verticales de comunidades':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Grafico de idiomas y N° de comunidades</div>", unsafe_allow_html=True)
        st.image("grafico1.png", caption='Gráfico de ideomas en las comunidades', width=800)
        pass
    elif grafico_seleccionado == 'Gráfico de barra vertical de pilotos':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Gráfico de pilotos por escuderia</div>", unsafe_allow_html=True)
        st.image("grafico2.png", caption='Gráfico de Pilotos y Escuderia', width=800)
        pass
    elif grafico_seleccionado == 'mapa de comunidades':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Mapa con las localizaciones de cada comunidad</div>", unsafe_allow_html=True)
        import streamlit.components.v1 as components
        with open("mapa.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass