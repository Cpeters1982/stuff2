''' -*- coding: utf-8 -*- MYBOOK MODELS '''


from __future__ import unicode_literals
from django.db import models
from ..login.models import User


# Create your models here.
class QuoteManager(models.Manager):
    def addQuote(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['title']) < 3 and len(postData['content']) < 10:
            results['errors'].append('All fields must be filled out')
            results['status'] = False

        user = User.objects.get(id=postData['user_id'])
        if results['status']:

            try:
                quote = Quote.objects.create(
                    title=postData['title'],
                    content=postData['content'],
                    user_id=user,
                )
                quote.save()
            except:
                results['errors'].append('Error: Quote not created')
                return results

    def addFavorite(self, postData, user_id):
        results = {'status': True, 'errors': []}
        try:
            
            blog = Blog.objects.get(postData['quote_id'])
            user = User.objects.get(id=user_id)
            favorite = quote.favoriteQuotes.add(user)
            quote.save()
        except:
            results['errors'].append('Error: not favorited')

        return results



class Quote(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    user_id = models.ForeignKey('login.User', related_name='quote')
    # favorite = models.ManyToManyField('Quote', related_name='favorite_quotes')
    created_at = models.DateTimeField(auto_now_add=True)
    # edited_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuoteManager()

# class Edit(models.Model):
#     creation_date = models.DateTimeField(auto_now_add=True)
#     editor = models.ForeignKey(User)
#     quote = models.ForeignKey(Quote)
