from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator, validate_ipv4_address
from django.utils import timezone

# Create your models here.

class Reseau(models.Model):

	id = models.AutoField(
		primary_key = True,
		editable = False,
		unique = True,
	)

	nom = models.CharField(max_length= 32, unique=True)

	adresse_ip = models.CharField(max_length=15, validators=[validate_ipv4_address])

	masque = models.CharField(max_length= 15, validators=[validate_ipv4_address])

	machine_assoc = models.ForeignKey('self', on_delete=models.CASCADE)

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

	id = models.AutoField(
			primary_key =  True,
			editable = False,
			unique = True)

	nom = models.CharField(
		max_length = 15)
	
	adresse_ip = models.CharField(max_length=15, validators=[validate_ipv4_address])

	masque = models.CharField(max_length= 15, validators=[validate_ipv4_address])

	reseau_assoc = models.ForeignKey(Reseau, on_delete=models.CASCADE)

	maintenance_date = models.DateTimeField(default=timezone.now)

	mach = models.CharField(max_length = 32, choices = TYPE, default = 'PC')

	etat = models.CharField(max_length = 32, choices = ETAT, default = 'Offline')

	def __str__(self):
		return str(self.id) + " -> " + self.nom



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

	machine_assoc = models.OneToOneField(Machine, on_delete=models.CASCADE)

	mail = models.EmailField(blank = True) # max_lenght = 46 car le fomat est 'nom@it.management.fr' donc 30 + 16


	def __str__(self):
		return str(self.id) + " -> " + self.nom
	
	def save(self, *args, **kwargs):
		if not self.mail:
			username = self.nom.lower().replace(" ", "") 	#permet d'enelever les espaces et de mettre les caractères en minuscules
			domain = "it.management.fr"
			self.mail = f"{username}@{domain}"		#créer l'adrese automatiquement grâce aux arg donnés
		super().save(*args, **kwargs)