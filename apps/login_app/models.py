# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.


class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        users = self.filter(email = postData['email'])
        
        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results
    
    def creator(self, postData):
        user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], alias = postData['alias'], email = postData['email'], birthday = postData['birthday'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user
    
    def validate(self, postData):
        results = {'status': True, 'errors': [] }
        if len(postData ['first_name']) < 3:
            results['errors'].append('Your first name is too $hort.')
            results['status'] = False

        if len(postData ['last_name']) < 3:
            results['errors'].append('Your last name is too $hort.')
            results['status'] = False

        if len(postData ['alias']) < 3:
            results['errors'].append('Your alias is too $hort.')
            results['status'] = False

        
        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            results['errors'].append('Email is not valid.')
            results['status'] = False
        
        if postData ['password'] != postData['c_password']:
            results['errors'].append('Your password does not match.')
            results['status'] = False
        
        if len(postData['password']) < 8:
            results['errors'].append('Password needs to be 8 or more characters.')
            results['status'] = False

        if len(postData['birthday']) < 8:
            results['errors'].append('Birthday needs to be 8 characters long.')
            results['status'] = False

        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('User already exists.')
            results['status'] = False
        return results
    
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    birthday = models.CharField(max_length = 8)
    alias = models.CharField(max_length = 255)