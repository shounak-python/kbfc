from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Company(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Name of Company or College"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Company"


class Foot(models.Model):
    name = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        help_text="Preferred Foot",
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Preferred Foot"


class Profession(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Name of Profession"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Profession"


class Expertise(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text="Attack, Midfield, Defence or Goalkeeping",
        default="Midfield"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Expertise"
    
class FieldPosition(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Field Position"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Field Position"


class Club(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Professional Club Name"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Professional Club Names"


class Player(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Professional Player Name"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Professional Player Names"


class MemberList(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Name of Member"
    )

    image = models.ImageField(upload_to='static/upload/')

    preferred_foot = models.ForeignKey(Foot,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Preferred Foot",
        related_name = "preferred_foot"
    )

    phone = PhoneNumberField(
        blank=False,
        help_text="Phone number with country code"
    )

    pune_address = models.TextField(
        max_length=300,
        blank=False,
        null=False,
        help_text="Pune Address of Member"
    )

    kolhapur_address = models.TextField(
        max_length=300,
        blank=False,
        null=False,
        help_text="Kolhapur Address of Member"
    )

    birthdate = models.DateField(
        blank=False,
        help_text="Birth date of the member"
    )

    area_of_expertise = models.ForeignKey(Expertise,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Attack, Medfield, Defence or Goalkeeping",
        related_name = "area_of_expertise"
    )

    preferred_field_position = models.ForeignKey(FieldPosition,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Preferred field position",
        related_name = "preferred_field_position"
    )

    secondary_field_position = models.ForeignKey(FieldPosition,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Secondary field position",
        related_name = "secondary_field_position"
    )

    profession = models.ForeignKey(Profession,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Profession"
    )

    current_company = models.ForeignKey(Company,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Profession"
    )

    favorite_club = models.ForeignKey(Club,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Favorite Club"
    )

    favorite_player = models.ForeignKey(Player,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Favorite Player"
    )

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = "KBFC Member List"