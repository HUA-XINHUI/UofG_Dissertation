from django.shortcuts import render
from django.contrib import messages
from .models import Character
from userprofile.models import UserAsset

def home(request):

    user = request.user
    characters = Character.objects.all()
    current_character = user.user_profile.selected_character

    if request.method == "POST":
        action = request.POST.get("action")
        character_id = request.POST.get("character_id")
        character = Character.objects.get(id=character_id)
        current_character = character
        if action == "select":
            user.user_profile.selected_character = character
            messages.success(
                request,
                f"{character.name} selected"
            )
        elif action == "buy":
            if user.user_profile.gold >= character.unlock_price:
                asset, create = user.user_asset.get_or_create(character=character)
                if create :
                    user.user_profile.gold -= character.unlock_price
                    messages.success(
                        request,
                        f"{character.name} unlocked!"
                    )
            else:
                messages.success(
                    request, "Need more Gold!" )
        user.user_profile.save()

    unlocked_characters_id = list(UserAsset.objects.filter(user=user).values_list(
            "character_id",
            flat=True,
        ))
    
    context = {
        "characters" : characters,
        "unlocked_characters_id" : unlocked_characters_id,
        "current_character_id" : current_character.id,
    }

    return render(request, "store/store.html", context)