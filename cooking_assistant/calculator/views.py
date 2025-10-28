from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


DATA = {
    "omlet": {
        "яйца, шт": 2,
        "молоко, л": 0.1,
        "соль, ч.л.": 0.5,
    },
    "pasta": {
        "макароны, г": 0.3,
        "сыр, г": 0.05,
    },
    "buter": {
        "хлеб, ломтик": 1,
        "колбаса, ломтик": 1,
        "сыр, ломтик": 1,
        "помидор, ломтик": 1,
    },
    # можете добавить свои рецепты ;)
}

def home_view(request):
    context = {
        'dishes' : DATA.keys()
    }
    return render(request, 'home.html', context)

def calculator(request: HttpRequest, dish):
    try:
        servings = int(request.GET.get("servings", 1))
    except (ValueError, TypeError):
        servings = 1
    recipe = DATA.get(dish, None)
    if recipe is None:
        return HttpResponse('Такого блюда нет')
    scaled_recipe = {
        ingredients: ammount * servings for ingredients, ammount in recipe.items()
    }
    context = {
        'recipe' : scaled_recipe,
    }
    return render(request, 'index.html', context)


