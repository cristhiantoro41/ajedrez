from django.shortcuts import render

def mi_vista(request):
    # Puedes agregar lógica aquí para procesar la solicitud
    
    # Por ejemplo, definir un contexto con datos para pasar a la plantilla
    contexto = {
        'titulo': 'Mi Vista',
        'mensaje': 'Hola desde mi vista en Django!',
    }

    # Renderiza la plantilla HTML y envía el contexto
    return render(request, 'nombre_de_tu_template.html', contexto)
