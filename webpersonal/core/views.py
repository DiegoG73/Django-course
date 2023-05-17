from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/portfolio">Portafolio</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>
"""

# Create your views here.


def home(request):
    return HttpResponse(html_base + """
        <h2>Portada</h2> 
        <p>Esto es la portada</p>
    """)


def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2> 
        <p>Me llamo Diego y soy un desarrollador backend</p>
    """)


def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portafolio</h2>
        <p>hey, bienvenido a mi portafolio, espero que te guste</p>
    """)


def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Estás en la página de contacto, así que, aquí te dejo las formas de contactarme:
        Número de teléfono: +52 55 8936 7891
        Email: hello@diegod.com
        </p>
    """)
