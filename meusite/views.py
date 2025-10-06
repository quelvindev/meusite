from django.shortcuts import render


def index(request):
    # Aqui você pode definir a seção que deseja exibir
    section = request.GET.get('section', 'header')  # Por padrão, mostra a seção 'default'

    search_value = request.GET.get('q','').strip()
    
    context = {
        'section': section,  # Passa a seção para o template
    }
    
    print(f'{context} valor{search_value}')
    return render(request, 'meusite/index.html', context)
