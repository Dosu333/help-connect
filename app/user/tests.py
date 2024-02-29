from django.test import TestCase
from graphene.test import Client
from .schema import schema
from graphql_jwt.shortcuts import get_token
from mixer.backend.django import mixer 
import json

class UserCreationTestCase(TestCase):
    def setUp(self):
        self.client = Client(schema)

    def test_user_creation(self):
        # Define the GraphQL mutation for creating a user
        mutation = '''
        mutation CreateUser($first_name: String!, $last_name: String!, $email: String!, $password: String!) {
            createUser(first_name: $first_name, email: $email, password: $password) {
                user {
                    id
                    username
                    email
                }
            }
        }
        '''

        # Define variables for the mutation
        variables = {
            'fullname': 'test user',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }

        # Execute the mutation
        executed = self.client.execute(mutation, variable_values=variables)

        # Assert the response
        self.assertIsNone(executed.get('errors'))
        self.assertIsNotNone(executed.get('data'))

        created_user = executed['data']['createUser']['user']
        self.assertEqual(created_user['username'], 'testuser')
        self.assertEqual(created_user['email'], 'testuser@example.com')
