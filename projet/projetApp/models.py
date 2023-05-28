from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator, validate_ipv4_address
from django.utils import timezone

# Create your models here.

class Machine(models.Model):

	TYPE = {
		('PC', ('PC - Windows')),
		('Mac', ('Mac - MacOS')),
		('Serveur', ('Serveur')),
		('Switch', ('Switch')),	
	}

	ETAT = {
		('Online', ('Online')),
		('Offline', ('Offline')),
	}

	id = models.AutoField(
			primary_key =  True,
			editable = False,
			unique = True)

	nom = models.CharField(
		max_length = 15)
	
	adresse_ip = models.CharField(max_length=15, validators=[validate_ipv4_address])

	masque = models.CharField(max_length= 15, validators=[validate_ipv4_address])

	maintenance_date = models.DateTimeField(default=timezone.now)

	mach = models.CharField(max_length = 32, choices = TYPE, default = 'PC')

	etat = models.CharField(max_length = 32, choices = ETAT, default = 'Offline')

	def __str__(self):
		return str(self.id) + " -> " + self.nom

	def get_name(self):
		return str(self.id) + " " + self.nom


class Personnel(models.Model):
	id = models.PositiveIntegerField(
		primary_key = True,
		editable = True,
		validators=[MinValueValidator(1000000000000) , MaxValueValidator(9999999999999)],
		unique = True,
	)

	nom = models.CharField(
		max_length = 30
	)

	prenom = models.CharField(
		max_length = 30
	)

class Reseau(models.Model):

	id = models.AutoField(
		primary_key = True,
		editable = False,
		unique = True,
	)

	nom = models.CharField(max_length= 32, unique=True)

	adresse_ip = models.CharField(max_length=15, validators=[validate_ipv4_address])

	masque = models.CharField(max_length= 15, validators=[validate_ipv4_address])