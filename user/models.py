# region				-----External Imports-----
from django.utils import timezone
from django.contrib import auth
from django.db import models
# endregion

# region				-----Internal Imports-----
from . import choices as user_choices
# endregion


class User(auth.models.AbstractBaseUser,
           auth.models.PermissionsMixin):
    # region       -----Information-----
    email = models.EmailField(verbose_name="Почта",
                              unique=True,
                              blank=False,
                              null=False)

    password = models.CharField(verbose_name="Пароль",
                                max_length=255,
                                blank=False,
                                null=False)

    date_joined = models.DateTimeField(verbose_name="Дата создания аккаунта",
                                       default=timezone.now)

    winnings = models.DecimalField(verbose_name="Выигрышь",
                                   decimal_places=2,
                                   max_digits=100,
                                   default=0)
    # endregion

    # region       -----Relation-----

    # endregion

    # region              -----Metas-----
    USERNAME_FIELD = "email"
    # endregion


class SteamProfile(models.Model):
    # region       -----Information-----
    steam_id = models.CharField(verbose_name="ID",
                                max_length=255,
                                unique=True,
                                null=False,
                                blank=False)

    nickname = models.CharField(verbose_name="Nickname",
                                max_length=255,
                                unique=True,
                                null=False,
                                blank=False)

    persona_name = models.CharField(verbose_name="Persona name",
                                    max_length=255,
                                    null=True,
                                    blank=True)

    avatar = models.ImageField(verbose_name="Avatar")
    # endregion

    # region       -----Relation-----
    user = models.OneToOneField(to="user.User", on_delete=models.CASCADE)
    # endregion
