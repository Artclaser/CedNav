from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile


# Enlever le Groupe 
admin.site.unregister(Group)

#Mélanger les informations de profil dans les informations utilisateur
class ProfileInline(admin.StackedInline):
    model = Profile

#Étendre le modèle utilisateur
class UserAdmin(admin.ModelAdmin):
    model = User
    #Affichez simplement les champs de nom d'utilisateur sur la page d'administration
    fields = ["username"]
    inlines = [ProfileInline]

# Enlever l'utilisateur initial 
admin.site.unregister(User)
# Et on le remet 
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)


