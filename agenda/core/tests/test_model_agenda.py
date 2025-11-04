from django.test import TestCase
from core.models import Agenda

class AgendaModelTest(TestCase):
    def setUp(self):
        self.agenda = Agenda.objects.create(
            nome_completo="Cassia Figuereido",
            telefone="(19) 99999-8888",
            email="cassia.figuereido@example.com",
            observacao="Cliente importante, prefere contato por e-mail."
        )

    def test_agenda_criada_com_sucesso(self):
        self.assertEqual(self.agenda.nome_completo, "Cassia Figuereido")
        self.assertEqual(self.agenda.telefone, "(19) 99999-8888")
        self.assertEqual(self.agenda.email, "cassia.figuereido@example.com")
        self.assertEqual(self.agenda.observacao, "Cliente importante, prefere contato por e-mail.")

    def test_str_retorna_nome_e_email(self):
        self.assertEqual(str(self.agenda), "Cassia Figuereido - cassia.figuereido@example.com")
