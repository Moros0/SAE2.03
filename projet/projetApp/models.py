from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator, validate_ipv4_address
from django.utils import timezone

# Create your models here.

class Reseau(models.Model):

	id = models.AutoField(		#l'id est créée automatiquement est inchangeable et est unique
		primary_key = True,
		editable = False,
		unique = True,
	)

	nom = models.CharField(max_length= 32, unique=True)

	adresse_ip = models.CharField(max_length=15, validators=[validate_ipv4_address])		#le validator permet de vérifier qu'il s'agit d'une adresse ipv4 valide

	masque = models.CharField(max_length= 15, validators=[validate_ipv4_address])

	def __str__(self):
		return str(self.nom) + " -> " + self.adresse_ip



class Machine(models.Model):

	TYPE = {
		('PC', ('PC - Windows')),
		('Mac', ('Mac - MacOS')),
		('Serveur', ('Serveur')),
		('Switch', ('Switch')),
		('Routeur', ('Routeur')),
	}

	ETAT = {
		('Online', ('Online')),
		('Offline', ('Offline')),
	}

	id = models.AutoField(		#l'id est créée automatiquement est inchangeable et est unique
			primary_key =  True,
			editable = False,
			unique = True)

	nom = models.CharField(
		max_length = 15)
	
	adresse_ip = models.CharField(max_length=15, validators=[validate_ipv4_address], blank=True)

	masque = models.CharField(max_length= 15, validators=[validate_ipv4_address], blank=True)

	reseau_assoc = models.ForeignKey(Reseau, on_delete=models.CASCADE)		#fk qui permet un lien avec un réseau

	personnel_assoc = models.ForeignKey('Personnel', on_delete=models.CASCADE)		#fk qui permet un lien vers un personnel

	maintenance_date = models.DateTimeField(default=timezone.now)		#défini la date de maintenance, par défault la date à l'instant ou la modif est faite

	mach = models.CharField(max_length = 32, choices = TYPE, default = 'PC')

	etat = models.CharField(max_length = 32, choices = ETAT, default = 'Offline')

	def __str__(self):
		return str(self.id) + " -> " + self.nom



class Personnel(models.Model):
	id = models.PositiveIntegerField(		#l'id est saisi manuellement est changeable et est unique
		primary_key = True,
		editable = True,
		validators=[MinValueValidator(1000000000000) , MaxValueValidator(9999999999999)], #ces valeurs répresentent la forme du num de sécurité sociale
		unique = True,
	)

	nom = models.CharField(
		max_length = 30
	)

	prenom = models.CharField(
		max_length = 30
	)

	mail = models.EmailField(blank = True) # permet la creation d'email automatiquement sous la bonne forme


	def __str__(self):
		return str(self.id) + " -> " + self.nom
	
	def save(self, *args, **kwargs):		#fonction permettant de créer automatiquement les emails a partir des noms du personnel
		if not self.mail:
			username = self.nom.lower().replace(" ", "") 	#permet d'enelever les espaces et de mettre les caractères en minuscules
			domain = "it.management.fr"
			self.mail = f"{username}@{domain}"		#créer l'adrese automatiquement grâce aux arg donnés
		super().save(*args, **kwargs)