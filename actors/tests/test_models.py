from django.test import TestCase
from actors.models import Actor


class ActorModelTest(TestCase):
    # 1. Preparando os dados de teste
    @classmethod
    def setUpClass(cls) -> None:
        cls.actor_data = {
            "first_name": "George",
            "last_name": "Clooney",
        }

        Actor.objects.create(**cls.actor_data)

    # 2. Teste da propriedade `max_length` do campo `first_name`
    def test_first_name_max_length(self):
        max_length = self.actor._meta.get_field("first_name").max_length

        self.assertEqual(max_length, 100)

    # 3. Teste das propriedades `null` e `blank` do campo `date_of_birth`
    def test_date_of_birth_can_be_null_or_blank(self):
        nullable = self.actor._meta.get_field("date_of_birth").null
        blankable = self.actor._meta.get_field("date_of_birth").blank

        self.assertTrue(nullable)
        self.assertTrue(blankable)

    # 4. Teste do método get_full_name da model
    def test_get_full_name(self):
        result = self.actor.get_full_name()
        expected = f"{self.actor.first_name} {self.actor.last_name}"

        self.assertEqual(expected, result)

    # 5. Teste se os campos foram preenchidos corretamente
    def test_actor_fields(self):
        self.assertEqual(self.actor.first_name, self.actor_data["first_name"])
        self.assertEqual(self.actor.last_name, self.actor_data["last_name"])
        self.assertIsNone(self.actor.date_of_birth)
        self.assertIsNone(self.actor.date_of_death)
